import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
import json

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
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #1E1E1E;
    border: 1px solid #333;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title Section
# -----------------------------
st.markdown('<div class="title">🎬 MovieMiner</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Convert movie paragraphs into structured AI-powered movie data</div>',
    unsafe_allow_html=True
)

# -----------------------------
# LLM Setup
# -----------------------------
model = ChatMistralAI(model="mistral-small-2506")


# -----------------------------
# Pydantic Schema
# -----------------------------
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)

# -----------------------------
# Prompt Template
# -----------------------------
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the paragraph.

{format_instructions}
"""
    ),
    ("human", "{paragraph}")
])

# -----------------------------
# User Input
# -----------------------------
user_input = st.text_area(
    "📖 Enter Movie Description",
    height=220,
    placeholder="Example: Inception is a 2010 science fiction film directed by Christopher Nolan..."
)

# -----------------------------
# Extract Button
# -----------------------------
if st.button("🚀 Extract Movie Data"):

    if not user_input.strip():
        st.warning("Please enter a movie paragraph.")
    else:
        with st.spinner("Analyzing movie information... 🎥"):

            try:
                final_prompt = prompt.invoke({
                    "paragraph": user_input,
                    "format_instructions": parser.get_format_instructions()
                })

                response = model.invoke(final_prompt)

                movie_data = parser.parse(response.content)

                # -----------------------------
                # Display Results
                # -----------------------------
                st.success("Movie information extracted successfully!")

                st.markdown("## 🎞 Extracted Movie Data")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("🎬 Title", movie_data.title)

                with col2:
                    st.metric(
                        "📅 Release Year",
                        movie_data.release_year if movie_data.release_year else "N/A"
                    )

                st.markdown("### 🎭 Genre")
                st.write(", ".join(movie_data.genre))

                st.markdown("### 🎬 Director")
                st.write(movie_data.director or "N/A")

                st.markdown("### ⭐ Rating")
                st.write(movie_data.rating or "N/A")

                st.markdown("### 👥 Cast")
                for actor in movie_data.cast:
                    st.write(f"- {actor}")

                st.markdown("### 📝 Summary")
                st.info(movie_data.summary)

                # -----------------------------
                # JSON Output
                # -----------------------------
                st.markdown("### 📦 JSON Output")

                json_data = movie_data.model_dump()

                st.json(json_data)

                # Download Button
                st.download_button(
                    label="⬇ Download JSON",
                    data=json.dumps(json_data, indent=4),
                    file_name="movie_data.json",
                    mime="application/json"
                )

            except Exception as e:
                st.error(f"Error: {e}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<center>Built with ❤️ using Streamlit, LangChain & Mistral AI</center>",
    unsafe_allow_html=True
)