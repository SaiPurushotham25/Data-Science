import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.base_url = "https://openrouter.ai/api/v1"

client = openai.OpenAI(api_key=openai.api_key, base_url=openai.base_url)

def interpret_with_llm(question: str, chart_data: dict) -> str:
    prompt = f"You are an astrology expert. Based on chart {chart_data}, answer: {question}"

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[
                {"role": "system", "content": "You are an astrology expert."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"LLM error: {str(e)}"
