import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the LLM configuration from environment variables
LLM_MODEL = os.getenv("LLM_MODEL")
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")

# Create the LLM configuration dictionary
# This structure is what Qwen-Agent expects
llm_cfg = {
    'model': LLM_MODEL,
    'model_server': 'dashscope',
    'api_key': DASHSCOPE_API_KEY,
}