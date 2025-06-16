# Airline Customer Support Agent

An intelligent, extensible customer support agent for airline-related inquiries, built on the **Qwen-Agent** framework. This project leverages Large Language Models (LLMs) and custom tools to deliver conversational support for common airline questions.

The agent understands natural language, interacts with simulated airline APIs, and provides helpful, human-like responses.

---

## 🌟 Key Features

-   **Flight Status Checking:** Get real-time updates on flight status (e.g., "On Time," "Delayed," "Cancelled").
-   **Flight Search:** Find available flights by departure city, destination, and date.
-   **Conversational CLI:** A polished and intuitive command-line chat interface.
-   **Automated Tool Discovery:** The agent automatically discovers and registers new tools, making it highly extensible.

---

## 🚀 How It Works

The agent uses a simple but powerful "Reason and Act" loop. When it receives a user query, it follows a process defined by its system prompt:

1.  **Decide:** The LLM analyzes the query and chooses the most appropriate tool (e.g., `flight_status_checker` or `flight_search`).
2.  **Act:** The agent calls the selected tool with the necessary parameters extracted from the query.
3.  **Summarize:** The tool returns structured data (JSON) from a mock API, and the LLM summarizes this data into a friendly, natural language response for the user.

```
┌──────────────┐   1. Query   ┌──────────────┐   2. Selects Tool   ┌────────────────────────┐
│     User     │─────────────>│  LLM Agent   │────────────────────>│ flight_status_checker  │
└──────────────┘              └───────┬──────┘                     └────────────────────────┘
       ^                              │                              │ 3. Returns "On Time"
       │ 5. Formats &               │                              │
       │    Responds                 │ 4. Summarizes Result         │
       └──────────────────────────────┘                              ↓
                                                            ┌────────────────────────┐
                                                            │      flight_search     │
                                                            └────────────────────────┘
```

---

## 💬 Sample Conversation

Here is an example of the agent in action:

![Agent Demo](httpst://i.imgur.com/example.gif)  **You:** What is the status of flight QA123?

**Agent:** The status of flight QA123 is **On Time**.

---

**You:** Find me a flight from JFK to LAX for tomorrow.

**Agent:** I found a couple of flights for you from JFK to LAX:
* **Flight QA701**: Departs at 09:00, arrives at 12:00. Price: $350.00 USD.
* **Flight QA703**: Departs at 17:00, arrives at 20:00. Price: $420.50 USD.

---

## 🛠️ Setup & Installation

*(The setup instructions remain largely the same, but ensure `requirements.txt` is updated per Step 1)*

... (Keep your existing Setup & Installation section here) ...

---

## 🔌 Extending the Agent

This project is designed for easy extension. Adding a new tool is straightforward:

1.  **Create the Tool File:** Create a new Python file in the `tools/` directory (e.g., `tools/baggage_tracker_tool.py`).
2.  **Define the Tool Class:** Inside the new file, create a class that inherits from `BaseTool` and decorate it with `@register_tool('your_tool_name')`.
3.  **Implement Logic:** Define the `description`, `parameters`, and `call` method. The `call` method contains your tool's logic.
4.  **Run:** That's it! The agent will automatically discover and load your new tool on the next run, thanks to the dynamic tool discovery mechanism.

---

## ✅ Running Tests

The project includes a suite of unit tests to ensure the tools function correctly. To run the tests:

```bash
python -m unittest discover
```

---

## License

MIT License