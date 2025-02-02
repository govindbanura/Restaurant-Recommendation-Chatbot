# Restaurant Recommendation Chatbot

This project implements a restaurant recommendation chatbot using Flask, OpenAI's GPT-3.5 Turbo with function calling, and external restaurant APIs (like Yelp or Google Places). The chatbot understands user preferences and provides personalized recommendations.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This chatbot is designed to help users find restaurants based on their specific preferences, including cuisine, price range, location, and other features. It uses natural language understanding, chain-of-thought prompting, and intelligent tool use to effectively interact with external APIs and deliver accurate and personalized recommendations.

## Features

*   **Interactive Chat Interface:** A user-friendly web-based chat interface to interact with the chatbot.
*   **Personalized Recommendations:** Provides restaurant recommendations based on user preferences and requirements.
*   **External API Integration:** Uses external APIs (Yelp or Google Places) to fetch real-time restaurant data.
*   **Function Calling:** Leverages LLM function calling capabilities to trigger external API requests based on user intent.
*   **Chain of Thought Prompting:** Includes chain-of-thought prompting to improve the reasoning ability of the chatbot.
*   **Contextual Awareness:** Maintains conversation history for more relevant multi-turn interactions.
*   **Error Handling:** Handles various API errors and LLM failures to ensure stability.

## Getting Started

### Prerequisites

*   **Python 3.7+**
*   **pip** (Python package installer)
*   **Gemini API Key:** Obtain an API key from [Gemini(https://aistudio.google.com/).
*   **Yelp API Key:** Obtain an API key from [Yelp Developer](https://developer.yelp.com/) (or a Google Places API key if using that).
*   **Virtual Environment (Recommended):** Using a virtual environment is good practice for isolating project dependencies.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd restaurant_chatbot
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  **Create a `.env` file** in the project's root directory.
2.  **Add your API keys** to the `.env` file:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    YELP_API_KEY=your_yelp_api_key # Or GOOGLE_PLACES_API_KEY=your_google_places_api_key
    ```
    **Note:** If using Google Places API, you must update the `api_utils.py` and other required files.

### Running the Application

1.  **Navigate to the project root directory (if you are not already there):**
    ```bash
    cd restaurant_chatbot
    ```

2.  **Run the Flask application:**
    ```bash
    python app.py
    ```

3.  **Access the application** in your web browser at `http://127.0.0.1:5000`.

## Usage

1.  Open your web browser and navigate to the application URL (`http://127.0.0.1:5000`).
2.  Type your queries into the chat input field and click "Send."
3.  The chatbot will process your request and respond with restaurant recommendations.

**Example Queries:**

*   "I'm looking for a cheap pizza place in Greater Noida."
*   "I want a fancy steakhouse for a business dinner in Hyderabad."
*  "Can you find a cafe with good coffee near India Gate?"
* "Can you find an Indian restaurant that is cheap?"

## Project Structure
```
restaurant_chatbot/
    ├── app.py           # Flask application logic
    ├── templates/       # HTML templates
    │   └── index.html
    ├── static/          # CSS, JS, etc. (optional)
    ├── utils/          # Utility functions
    │    ├── llm_utils.py   # LLM interaction, prompt construction
    │    └── api_utils.py  # API calls (Yelp, etc)
    ├── prompts/       # Prompt templates
    │     ├── base_prompt.txt
    │     └── few_shot_examples.txt
    ├── config.py     # Configuration
    └── requirements.txt
```
## Screenshots
![static/images/Screenshot 2025-02-02 161040.png](https://github.com/govindbanura/Restaurant-Recommendation-Chatbot/blob/main/static/images/Screenshot%202025-02-02%20161040.png)



