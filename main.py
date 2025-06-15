from agents.airline_agent import create_agent

def main():
    """
    The main function to run the airline support agent.
    """
    print("Initializing Airline Support Agent...")
    agent = create_agent()
    print("Agent is ready. Type 'quit' to exit.")
    print("-" * 30)

    messages = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        messages.append({'role': 'user', 'content': user_input})

        # --- CORRECTED HISTORY AND STREAMING LOGIC ---
        print("Agent: ", end="", flush=True)

        # This list will capture all of the agent's responses (text and tool calls)
        agent_responses = []
        printed_length = 0

        for response in agent.run(messages=messages):
            # The generator yields a list of message dicts at each step
            if isinstance(response, list) and response:
                # The final text content for this streaming step
                full_content = ''
                is_final_content = False

                # Find the main text content in the latest response chunk
                for r in response:
                    if r['role'] == 'assistant':
                        full_content = r.get('content', '')
                        is_final_content = True

                # If it's a final text response, handle the printing logic
                if is_final_content:
                    new_text_chunk = full_content[printed_length:]
                    print(new_text_chunk, end="", flush=True)
                    printed_length = len(full_content)

            # Store the agent's response for the history
            agent_responses.extend(response)

        print()  # Final newline

        # Add the full chain of agent responses to the message history
        # This is CRITICAL for the agent to have context of what the tools returned.
        if agent_responses:
            messages.extend(agent_responses)

if __name__ == "__main__":
    main()
