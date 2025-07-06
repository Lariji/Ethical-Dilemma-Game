from fastapi import FastAPI
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
        results.append(FrameworkResponse(
            framework=framework,
            response=f"This is a placeholder response using {framework} for the dilemma: '{req.dilemma}'"
        ))
    return DilemmaResult(results=results)

