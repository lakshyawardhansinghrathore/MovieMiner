from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model='mistral-small-2506')


class Movie(BaseModel):
    title: str = Field(description="Official title of the movie")
    release_year: Optional[int] = Field(description="Year of release")
    genre: List[str] = Field(description="Genres of the movie")
    director: Optional[str] = Field(description="Director(s) of the movie")
    cast: List[str] = Field(description="List of main cast actors in the movie")
    rating: Optional[float] = Field(description="General rating of the movie out of 10 (e.g., IMDb rating)")
    summary: str = Field(description="A brief summary or plot synopsis of the movie")


parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an expert movie database assistant.
Given the name of a movie, provide accurate, detailed, and structured information about that movie.
{format_instructions}
"""
    ),
    ("human", "Movie Name: {movie_name}")
])

if __name__ == "__main__":
    movie_name = input("Enter movie name: ")

    final_prompt = prompt.invoke({
        "movie_name": movie_name,
        "format_instructions": parser.get_format_instructions()
    })

    response = model.invoke(final_prompt)
    movie_data = parser.parse(response.content)

    print(movie_data.model_dump_json(indent=4))


