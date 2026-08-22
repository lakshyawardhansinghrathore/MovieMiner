import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
import json
import re

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="MovieMiner 🎬",
    page_icon="🎥",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #FF4B4B;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #B0B0B0;
    margin-bottom: 30px;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background-color: #FF4B4B;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #E03E3E;
    color: white;
}

.badge {
    display: inline-block;
    padding: 4px 12px;
    margin: 4px 4px 4px 0;
    border-radius: 16px;
    background-color: #2D3748;
    color: #E2E8F0;
    font-size: 14px;
    font-weight: 500;
}

.result-card {
    padding: 20px;
    border-radius: 12px;
    background-color: #1A1C23;
    border: 1px solid #2D3748;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title Section
# -----------------------------
st.markdown('<div class="title">🎬 MovieMiner</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Enter any movie name to generate complete structured AI-powered movie data</div>',
    unsafe_allow_html=True
)

# -----------------------------
# LLM Setup & Schema
# -----------------------------
model = ChatMistralAI(model="mistral-small-2506")


class Movie(BaseModel):
    title: str = Field(description="Official title of the movie")
    release_year: Optional[int] = Field(description="Year the movie was released")
    genre: List[str] = Field(description="List of genres for the movie")
    director: Optional[str] = Field(description="Director(s) of the movie")
    cast: List[str] = Field(description="List of top key actors/cast members in the movie")
    rating: Optional[float] = Field(description="General rating out of 10 (e.g., IMDb rating)")
    summary: str = Field(description="A comprehensive yet concise summary of the movie's plot")


parser = PydanticOutputParser(pydantic_object=Movie)

# -----------------------------
# Prompt Template
# -----------------------------
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

# -----------------------------
# User Input
# -----------------------------
movie_name = st.text_input(
    "🎬 Enter Movie Name",
    placeholder="Example: Inception, Interstellar, The Dark Knight, Spirited Away, RRR...",
    help="Type the name of any movie and press Mine Movie Details"
)

# -----------------------------
# Extract Button
# -----------------------------
if st.button("🚀 Mine Movie Details"):

    if not movie_name or not movie_name.strip():
        st.warning("⚠️ Please enter a movie name.")
    else:
        clean_movie_name = movie_name.strip()
        with st.spinner(f"Mining details for '{clean_movie_name}'... 🎥"):

            try:
                final_prompt = prompt.invoke({
                    "movie_name": clean_movie_name,
                    "format_instructions": parser.get_format_instructions()
                })

                response = model.invoke(final_prompt)
                movie_data = parser.parse(response.content)

                # -----------------------------
                # Display Results
                # -----------------------------
                st.success("✨ Movie information retrieved successfully!")

                st.markdown("## 🎞 Movie Details")

                # Metrics Row
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("🎬 Title", movie_data.title)

                with col2:
                    st.metric(
                        "📅 Release Year",
                        str(movie_data.release_year) if movie_data.release_year else "N/A"
                    )

                with col3:
                    st.metric(
                        "⭐ Rating",
                        f"{movie_data.rating}/10" if movie_data.rating else "N/A"
                    )

                # Details Section
                st.markdown("### 🎬 Director")
                st.write(movie_data.director or "N/A")

                st.markdown("### 🎭 Genres")
                if movie_data.genre:
                    badges_html = "".join([f'<span class="badge">{g}</span>' for g in movie_data.genre])
                    st.markdown(badges_html, unsafe_allow_html=True)
                else:
                    st.write("N/A")

                st.markdown("### 👥 Main Cast")
                if movie_data.cast:
                    col_cast1, col_cast2 = st.columns(2)
                    mid = (len(movie_data.cast) + 1) // 2
                    with col_cast1:
                        for actor in movie_data.cast[:mid]:
                            st.markdown(f"• **{actor}**")
                    with col_cast2:
                        for actor in movie_data.cast[mid:]:
                            st.markdown(f"• **{actor}**")
                else:
                    st.write("N/A")

                st.markdown("### 📝 Summary")
                st.info(movie_data.summary)

                # -----------------------------
                # JSON Output
                # -----------------------------
                st.markdown("### 📦 Structured JSON Output")

                json_data = movie_data.model_dump()
                st.json(json_data)

                # Safe file name for download
                sanitized_title = re.sub(r'[^a-zA-Z0-9_\-]', '_', movie_data.title.lower())
                file_name = f"{sanitized_title}_data.json"

                # Download Button
                st.download_button(
                    label="⬇ Download JSON",
                    data=json.dumps(json_data, indent=4),
                    file_name=file_name,
                    mime="application/json"
                )

            except Exception as e:
                st.error(f"Error fetching movie data: {e}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<center>Built with ❤️ using Streamlit, LangChain & Mistral AI</center>",
    unsafe_allow_html=True
)