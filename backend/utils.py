import os 
import httpx
from typing import List, Dict

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "mistral"
PROMPT_DIR = os.path.join(os.path.dirname(__file__), "prompts")

async def query_model(prompt: str, framework: str, timeout: int =20) -> Dict[str,str]:
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                LM_STUDIO_URL,
                json={
                    "model": MODEL_NAME,
                    "messages": [
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 512
                }
            )
            response.raise_for_status()
            result = response.json()
            content = result['choices'][0]['message']['content'].strip()
            return{framework:content}
    except Exception as e:
        return {framework:f"Error {str(e)}"}
    

def load_prompt(framework: str, dilemma: str) -> str:
    filename = framework.lower().replace(" ", "_") + ".txt"
    path = os.path.join(PROMPT_DIR, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt for framework '{framework}' not found at {path}")
    
    with open(path, "r", encoding="utf-8") as f:
        template = f.read()

    return template.replace("{dilemma}", dilemma)