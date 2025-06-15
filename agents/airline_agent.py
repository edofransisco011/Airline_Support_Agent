from qwen_agent.agents import Assistant

# Import the LLM configuration from our settings file
from config.settings import llm_cfg

# IMPORTANT: We must import the tool files here so that their @register_tool decorators
# run and make the tools available to the agent.
import tools.flight_status_tool
import tools.booking_tool

def create_agent():
    """
    Initializes and returns the main airline support agent.
    """
    # Update the system prompt to be more explicit about the agent's process.
    system_prompt = (
        "You are a helpful airline customer support agent. Your process has three steps:\n"
        "1. First, based on the user's query, decide which tool to use ('flight_status_checker' or 'flight_search').\n"
        "2. Second, call the selected tool with the necessary parameters.\n"
        "3. Third, after the tool returns a result, you MUST summarize this result in a friendly, natural language sentence for the user. Do not just stop after the tool call."
    )


    # Add the new tool to the list of tools the agent can use.
    agent_tools = [
        'flight_status_checker',
        'flight_search'
    ]

    # Initialize the Assistant agent
    agent = Assistant(
        llm=llm_cfg,
        system_message=system_prompt,
        function_list=agent_tools
    )

    return agent
