from qwen_agent.agents import Assistant

# Import the LLM configuration from our settings file
from config.settings import llm_cfg

# IMPORTANT: We must import the tool file here so that the @register_tool decorator
# runs and makes the tool available to the agent.
import tools.flight_status_tool

def create_agent():
    """
    Initializes and returns the main airline support agent.
    """
    # Define the system prompt. This tells the LLM how to behave.
    system_prompt = (
        "You are a helpful airline customer support agent. "
        "When asked for a flight status, you must use the 'flight_status_checker' tool."
    )

    # Create a list of the tools the agent is allowed to use.
    # We use the string name we gave the tool in the @register_tool decorator.
    agent_tools = ['flight_status_checker']

    # Initialize the Assistant agent
    agent = Assistant(
        llm=llm_cfg,
        system_message=system_prompt,
        function_list=agent_tools
    )

    return agent