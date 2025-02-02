import json
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY, LLM_MODEL
from utils.api_utils import search_restaurants

# from prompts.base_prompt import base_prompt
# from prompts.few_shot_examples import few_shot_examples
import os

llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    api_key=GEMINI_API_KEY,
)


# Define function mapping
AVAILABLE_FUNCTIONS = {"search_restaurants": search_restaurants}

FUNCTION_DESCRIPTIONS = [
    {
        "name": "search_restaurants",
        "description": "Searches for restaurants based on cuisine, price range, location and feature.",
        "parameters": {
            "type": "object",
            "properties": {
                "cuisine": {
                    "type": "string",
                    "description": "The type of food the user wants",
                },
                "price_range": {
                    "type": "string",
                    "enum": ["cheap", "moderate", "expensive"],
                    "description": "The price range for resturant",
                },
                "location": {
                    "type": "string",
                    "description": "The location of resturant",
                },
                "feature": {
                    "type": "string",
                    "description": "Any features that the resturant should have",
                },
                "order_by": {
                    "type": "string",
                    "enum": ["rating", "review_count"],
                    "description": "Order results by rating or review count",
                },
            },
            "required": [],
        },
    }
]


def load_prompt(filename):
    """Loads prompts from file"""
    with open(filename, "r") as file:
        return file.read()


base_prompt = load_prompt("prompts/base_prompt.txt")
few_shot_examples = load_prompt("prompts/few_shot_examples.txt")


def create_prompt(user_input, history):
    """
    Creates the prompt to send to LLM
    """
    formatted_functions = json.dumps(FUNCTION_DESCRIPTIONS)
    prompt = (
        base_prompt.replace("{{functions}}", formatted_functions)
        + few_shot_examples
        + "".join(history)
        + f"\nUser Input: {user_input}\nThought: "
    )
    return prompt


def process_llm_response(response):
    """Processes the llm response"""
    if response.additional_kwargs.get("function_call"):
        function_call = response.additional_kwargs.get("function_call")
        function_name = function_call.get("name")
        function_args = json.loads(function_call.get("arguments", "{}"))
        return {"action": function_name, "action_input": function_args}
    else:
        return {"text": response.content}


def call_llm(prompt, history):
    """
    Call the llm with given prompt and history and handle the function calls
    """
    response = llm.invoke(
        [{"role": "user", "content": prompt}], functions=FUNCTION_DESCRIPTIONS
    )
    llm_response = process_llm_response(response)
    if "action" in llm_response:
        function_name = llm_response["action"]
        function_args = llm_response["action_input"]
        function_to_call = AVAILABLE_FUNCTIONS.get(function_name)
        if function_to_call:
            observation = function_to_call(**function_args)
            history.append(
                f"Action: {function_name}\nAction Input: {function_args}\nObservation: {observation}\n"
            )
            return call_llm(
                prompt
                + f"Action: {function_name}\nAction Input: {function_args}\nObservation: {observation}\n",
                history,
            )
    else:
        return llm_response
