from fastapi import FastAPI,HTTPException
from utils import load_prompt
from pydantic import BaseModel
from typing import List

app = FastAPI()

class DilemmaRequest(BaseModel):
    dilemma: str

class FrameworkResponse(BaseModel):
    framework: str
    response: str

class DilemmaResult(BaseModel):
    results: List[FrameworkResponse]

frameworks = ["Utilitarianism","Deontology", "Virtue Ethics"]

@app.post("/evaluate", response_model=DilemmaResult)
def evaluate_dilemma(req: DilemmaRequest):
    results = []
    for framework in frameworks:
        try:
            prompt = load_prompt(framework,req.dilemma)
        except FileNotFoundError as e:
            raise HTTPException(status_code=500,detail = str(e))

        results.append(FrameworkResponse(
            framework=framework,
            response=prompt
        ))
    return DilemmaResult(results=results)

