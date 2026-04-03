from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    code: str

class Action(BaseModel):
    issues: List[str]
    quality_score: float
    suggestion: str

class Reward(BaseModel):
    score: float