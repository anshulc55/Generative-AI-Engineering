import os
from dotenv import load_dotenv

load_dotenv()

import sys
import os
print("Python System Info:")
print(f"Version: {sys.version.split()[0]}")
print(f"Executable Path: {sys.executable}")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print(f"OpenAI Key Detected: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")
print(f"Anthropic Key Detected: {'Yes' if os.getenv('ANTHROPIC_API_KEY') else 'No'}")
print(f"Gemini Key Detected: {'Yes' if os.getenv('GEMINI_API_KEY') else 'No'}")   