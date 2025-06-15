```markdown
# Airline Customer Support Agent

This project is an intelligent customer support agent built using the **Qwen-Agent** framework. It is designed to assist users with common airline-related inquiries by leveraging the power of Large Language Models (LLMs) and custom-defined tools.

The agent can understand natural language queries, interact with simulated airline APIs, and provide helpful, conversational responses.

---

## Features

* **Flight Status Checking:** Responds to queries about the real-time status of a flight (e.g., "On Time," "Delayed," "Cancelled").
* **Flight Search:** Searches for available flights based on departure city, destination, and date.
* **Conversational Interface:** Interacts with users through a simple and intuitive command-line interface.
* **Modular Tool System:** Easily extendable with new tools to handle more complex tasks like booking, baggage claims, or loyalty program inquiries.

---

## Project Structure

The project is organized into a modular structure to separate concerns and make it easy to maintain and extend:

```
airline_support_agent/
│
├── .env                # For storing secret API keys
├── main.py             # Main application entry point
├── README.md           # This file
├── requirements.txt    # Project dependencies
│
├── agents/             # Core agent logic and initialization
├── config/             # Application configuration and settings
├── data/               # For storing static files for RAG (e.g., policy PDFs)
├── logs/               # For storing log files
├── tools/              # Custom tools the agent can use (e.g., flight search)
└── utils/              # Shared utilities, such as API clients
```

---

## Setup and Installation

Follow these steps to set up and run the project locally.

### 1. Prerequisites

* Python 3.8 or higher
* Git

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd airline_support_agent
```

### 3. Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

* **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
* **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 4. Install Dependencies

Install all the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

The agent requires an API key to connect to the language model service.

a.  Create a file named `.env` in the root directory of the project.
b.  Open the `.env` file and add your DashScope API key:

    ```env
    # Get your key from [https://bailian.console.alibabacloud.com/](https://bailian.console.alibabacloud.com/)
    DASHSCOPE_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```

---

## How to Run the Agent

Once the setup is complete, you can start the agent by running the `main.py` script from the root directory:

```bash
python main.py
```

The application will initialize, and you can start interacting with the agent in your terminal. To exit the application, type `quit`.

---

## Example Usage

Here are some examples of questions you can ask the agent:

> **You:** What is the status of flight QA123?

> **You:** Can you find me a flight from JFK to LAX for tomorrow?

> **You:** Hi, can you help me?

```
