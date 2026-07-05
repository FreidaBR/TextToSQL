import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env first
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Check that your .env file exists in the project root."
    )

print("API Key Loaded:", api_key[:10] + "...")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

print("Loaded API Key:", api_key)
def ask_gemini(prompt: str):
    response = model.generate_content(prompt)
    return response.text