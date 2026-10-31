from dotenv import load_dotenv
from pathlib import Path
import os
import litellm

load_dotenv(Path("customer_support_agent/.env"))

response = litellm.completion(
    model="groq/openai/gpt-oss-120b",
    messages=[
        {"role": "user", "content": "What is 2 + 3? Answer only with the number."}
    ],
    api_key=os.getenv("GROQ_API_KEY"),
)

print(response.choices[0].message.content)