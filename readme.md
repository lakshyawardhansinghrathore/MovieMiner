# 🎬 MovieMiner

**MovieMiner** is derived from two words:

* **Movie** → Represents films and cinema-related content
* **Miner** → Refers to extracting valuable information from raw data

So, **MovieMiner** means:

> *“An AI-powered tool that mines and generates structured movie information directly from a movie name.”*

🌐 **Live Demo:**

```text id="c8el6r"
https://movieminer-ud6qc38f76463uj5btlyci.streamlit.app/
```

---

# 🚀 About the Project

MovieMiner is an AI-powered movie information generator application built using **LangChain**, **Mistral AI**, **Pydantic**, and **Streamlit**.

Simply type in the name of any movie, and the application instantly mines and generates comprehensive, structured data including:

* 🎬 Movie Title
* 📅 Release Year
* 🎭 Genre(s)
* 🎬 Director(s)
* 👥 Main Cast
* ⭐ Rating (out of 10)
* 📝 Plot Summary

This project demonstrates the power of **LLMs + Structured Output Parsing** for real-world NLP and cinema data applications.

---

# ✨ Features

* 🔍 **Instant Movie Mining**: Just type the movie name to retrieve detailed metadata.
* 🤖 **AI-Powered Knowledge Extraction**: Uses Mistral AI (`mistral-small-2506`) to pull complete movie details.
* 📦 **Strict Schema Validation**: Uses Pydantic & LangChain output parser to guarantee structured data format.
* 🎨 **Modern Streamlit UI**: Dark mode, metric cards, genre badges, and responsive layout.
* 📄 **Structured JSON**: Formatted JSON viewer with 1-click download.
* ⚡ **Fast & Lightweight**: Minimal overhead and rapid response times.

---

# 🛠 Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Mistral AI**
* **Pydantic**
* **python-dotenv**

---

# 📂 Project Structure

```text id="o4r6dr"
MovieMiner/
│
├── app.py               # Streamlit UI
├── movieminer.py        # Core generation logic
├── requirements.txt     # Dependencies
├── .gitignore
└── README.md
```

---

# ⚙ Installation

## 1️⃣ Clone the Repository

```bash id="myj4r8"
git clone https://github.com/lakshyawardhansinghrathore/MovieMiner
cd MovieMiner
```

---

## 2️⃣ Create Virtual Environment

```bash id="jlwmgn"
python -m venv venv
```

Activate virtual environment:

### Windows

```bash id="ehqz6o"
venv\Scripts\activate
```

### Mac/Linux

```bash id="vtxk0g"
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash id="2uktrm"
pip install -r requirements.txt
```

---

## 4️⃣ Add Environment Variables

Create a `.env` file and add your Mistral API key:

```env id="crmd7m"
MISTRAL_API_KEY=your_api_key_here
```

---

# ▶ Running the Application

### Streamlit Web App:
```bash id="yr03df"
streamlit run app.py
```

### CLI / Script Mode:
```bash
python movieminer.py
```

---

# 🧠 How It Works

1. User enters any movie name (e.g. `Inception`, `Interstellar`, `RRR`)
2. LangChain constructs a structured prompt for Mistral AI
3. The LLM generates the factual movie metadata based on world cinema knowledge
4. Pydantic validates and parses the output into a typed schema
5. Streamlit renders metric cards, badges, plot summary, and downloadable JSON

---

# 📸 Example

## Input

```text id="t56v8r"
Inception
```

## Output

```json id="g1wqto"
{
  "title": "Inception",
  "release_year": 2010,
  "genre": [
    "Action",
    "Adventure",
    "Sci-Fi"
  ],
  "director": "Christopher Nolan",
  "cast": [
    "Leonardo DiCaprio",
    "Joseph Gordon-Levitt",
    "Elliot Page",
    "Tom Hardy",
    "Ken Watanabe"
  ],
  "rating": 8.8,
  "summary": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
}
```

---

# 🔮 Future Improvements

* 🎭 Multiple movie comparison support
* 🌐 TMDB/IMDb API live data enrichment & poster fetching
* 📊 Export to CSV/PDF
* 🎨 Streaming responses & poster galleries
* ☁ Deploy with Docker & CI/CD

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve MovieMiner:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---


---

