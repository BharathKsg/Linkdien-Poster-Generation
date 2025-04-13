import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from llm import LinkedInPostGenerator

app = FastAPI()
generator = LinkedInPostGenerator()
class PostRequest(BaseModel):
    article_summary: str
    perspectives: list

class PostResponse(BaseModel):
    linkedin_post: str
    confidence_score: int | None

# Endpoint for LinkedIn Post Generation
@app.post("/generate_linkedin_post", response_model=PostResponse)
async def generate_linkedin_post(request: PostRequest):
    result = generator.generate_post(request.article_summary, request.perspectives)
    return PostResponse(
        linkedin_post=result["linkedin_post"],
        confidence_score=result["confidence_score"]
    )