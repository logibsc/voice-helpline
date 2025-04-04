import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

def generate_response(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text