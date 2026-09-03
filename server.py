import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

# Load Environment Variables
load_dotenv()

# Initialize FastAPI App
app = FastAPI(title="MovieMiner API")

# Setup LLM & Parser
model = ChatMistralAI(model="mistral-small-2506")

class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str] = []
    director: Optional[str] = None
    cast: List[str] = []
    rating: Optional[float] = None
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an expert movie database assistant with extensive knowledge of world cinema.
Given the name of a movie, provide accurate, detailed, and structured information about that movie.
If release year or specific details are provided in the title, use them to identify the exact movie.

{format_instructions}
"""
    ),
    ("human", "Movie Name: {movie_name}")
])

class MovieRequest(BaseModel):
    movie_name: str

@app.post("/api/mine", response_model=Movie)
async def mine_movie(request: MovieRequest):
    if not request.movie_name or not request.movie_name.strip():
        raise HTTPException(status_code=400, detail="Movie name cannot be empty")
    
    clean_movie_name = request.movie_name.strip()
    try:
        final_prompt = prompt.invoke({
            "movie_name": clean_movie_name,
            "format_instructions": parser.get_format_instructions()
        })
        
        response = await model.ainvoke(final_prompt)
        movie_data = parser.parse(response.content)
        return movie_data
    except Exception as e:
        print(f"Error fetching movie data: {e}")
        raise HTTPException(status_code=500, detail="Failed to mine movie details")

# Mount static files and serve index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
