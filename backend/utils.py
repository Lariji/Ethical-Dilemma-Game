import os 

PROMPT_DIR = os.path.join(os.path.dirname(__file__), "prompts")

def load_prompt(framework: str, dilemma: str) -> str:
    filename = framework.lower().replace(" ", "_") + ".txt"
    path = os.path.join(PROMPT_DIR, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt for framework '{framework}' not found at {path}")
    
    with open(path, "r", encoding="utf-8") as f:
        template = f.read()

    return template.replace("{dilemma}", dilemma)