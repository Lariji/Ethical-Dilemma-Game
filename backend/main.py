from fastapi import FastAPI,HTTPException
from utils import load_prompt, query_model
from pydantic import BaseModel
from typing import List,Dict
import asyncio

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
async def evaluate_dilemma(req: DilemmaRequest):
    tasks = []
    for framework in frameworks:
        try:
            prompt = load_prompt(framework,req.dilemma)
        except FileNotFoundError as e:
            raise HTTPException(status_code=500,detail = str(e))
        
        tasks.append(query_model(prompt,framework))

    responses = await asyncio.gather(*tasks)

    results = []
    for item in responses: 
        for framework, response in item.items():
            results.append(FrameworkResponse(framework = framework, response = response))

    return DilemmaResult(results = results)


