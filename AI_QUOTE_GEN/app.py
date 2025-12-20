import requests
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    print("API key not found.")
headers = {"Authorization": f"Bearer {api_key}"}
url="https://router.huggingface.co"
payload={"inputs":"A fantasy landscape, trending on artstation"}
data = requests.post(url, headers=headers, json=payload)
result = data.json()
print(result)
