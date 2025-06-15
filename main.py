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

        # --- CORRECTED STREAMING LOGIC ---
        print("Agent: ", end="", flush=True) # Print the prefix once
        
        full_response = ""
        for response in agent.run(messages=messages):
            if isinstance(response, list) and response:
                # Check if the response chunk contains text content
                if 'content' in response[0]:
                    content_chunk = response[0]['content']
                    print(content_chunk, end="", flush=True) # Print only the chunk
                    full_response += content_chunk
        
        print() # Add a final newline after the full response is printed

        # Append the agent's full response to the history for context
        if full_response:
            messages.append({'role': 'assistant', 'content': full_response})

if __name__ == "__main__":
    main()
