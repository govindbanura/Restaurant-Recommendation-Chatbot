from flask import Flask, render_template, request, jsonify
from utils.llm_utils import create_prompt, call_llm

app = Flask(__name__)
conversation_history = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["msg"]
    prompt = create_prompt(user_input, conversation_history)
    llm_response = call_llm(prompt, conversation_history)

    print(llm_response)

    if "text" in llm_response:
        conversation_history.append(f"Final Answer: {llm_response['text']}\n")
        return llm_response["text"]


if __name__ == "__main__":
    app.run(debug=True)
