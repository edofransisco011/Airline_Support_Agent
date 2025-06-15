
# Airline Customer Support Agent

An intelligent, extensible customer support agent for airline-related inquiries, built on the **Qwen-Agent** framework. This project leverages Large Language Models (LLMs) and custom tools to deliver conversational support for common airline questions.

The agent understands natural language, interacts with simulated airline APIs, and provides helpful, human-like responses.

---

## Features

- **Flight Status Checking:** Get real-time updates on flight status (e.g., "On Time," "Delayed," "Cancelled").
- **Flight Search:** Find available flights by departure city, destination, and date.
- **Conversational CLI:** Simple, intuitive command-line chat interface.
- **Modular Tool System:** Easily extend or customize the agent to handle bookings, baggage, loyalty programs, and more.

---

## Project Structure

```
airline_support_agent/
│
├── .env                # Secret API keys (not committed)
├── main.py             # Application entry point
├── README.md           # Project overview and instructions
├── requirements.txt    # Python dependencies
│
├── agents/             # Core agent logic and orchestration
├── config/             # App settings and configuration files
├── data/               # Static files (e.g., airline policies for RAG)
├── logs/               # Application logs
├── tools/              # Custom tool plugins (e.g., flight search)
└── utils/              # Shared utilities, API clients, helpers
```

---

## Setup & Installation

### 1. Prerequisites

- Python 3.8+
- Git

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd airline_support_agent
```

### 3. Create a Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
**Windows:**
```bash
python -m venv venv
.env\Scriptsctivate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add Environment Variables

- Create a `.env` file in the project root.
- Add your DashScope API key:
    ```env
    # Get your API key from:
    # https://bailian.console.alibabacloud.com/
    DASHSCOPE_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```

---

## Running the Agent

Start the agent with:

```bash
python main.py
```

The CLI will launch—just type your questions. To exit, type `quit`.

---

## Example Queries

Ask the agent questions like:

```
What is the status of flight QA123?
Find me a flight from JFK to LAX for tomorrow.
Hi, can you help me?
```

---

## Extending the Agent

The modular design makes it easy to add new tools (e.g., for booking, baggage claims, etc.). See the `tools/` directory for examples.

---

## License

MIT License

---

## Contact

edofransisco011@gmail.com
