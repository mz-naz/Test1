from langchain.llms import GoogleGenerativeAI
from mock_catalog import mock_products
import os

# Set your Gemini API key here or via environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")

llm = GoogleGenerativeAI(api_key=GEMINI_API_KEY)

def get_product_info():
    info = "\n".join([
        f"{p['name']}: {p['description']} Price: ${p['price']} Ingredients: {', '.join(p['ingredients'])}" for p in mock_products
    ])
    return info

def generate_chatbot_response(user_message: str) -> str:
    """
    Use Gemini LLM to answer user queries, referencing the product catalog.
    """
    system_prompt = (
        "You are a helpful AI assistant for a cosmetic webstore. "
        "You can answer questions about products, recommend items, and help with general customer support. "
        "Here is the product catalog:\n" + get_product_info()
    )
    prompt = f"{system_prompt}\n\nCustomer: {user_message}\nAI:"
    response = llm(prompt)
    return response