import os
from dotenv import load_dotenv

# Load environment variables from a .env file
# The load_dotenv() function will search for a .env file in the current directory
# and its parent directories and load them.
print("Attempting to load .env file...")
load_dotenv()
print(".env file loaded (if found).")


# Get the LLM configuration from environment variables
LLM_MODEL = os.getenv("LLM_MODEL")
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")

# --- DIAGNOSTIC PRINT ---
# Let's see what value is actually being loaded for the API key.
# It should print your key. If it prints "None", the .env file was not found or the variable name is wrong.
print(f"Loaded API Key: {DASHSCOPE_API_KEY}")
# ------------------------

# Check if the API key was loaded successfully
if not DASHSCOPE_API_KEY or DASHSCOPE_API_KEY == "YOUR_API_KEY_HERE":
    print("\n--- ERROR ---")
    print("API Key not found or is still the placeholder value.")
    print("Please ensure you have a .env file in the project root directory with your correct DASHSCOPE_API_KEY.")
    print("-------------")
    exit() # Exit the script if the key is not configured


# Create the LLM configuration dictionary
# This structure is what Qwen-Agent expects
llm_cfg = {
    'model': LLM_MODEL,
    'model_server': 'https://dashscope-intl.aliyuncs.com/compatible-mode/v1',
    'api_key': DASHSCOPE_API_KEY,
}
