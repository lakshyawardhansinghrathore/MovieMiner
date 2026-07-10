# 🎬 MovieMiner

**MovieMiner** is derived from two words:

* **Movie** → Represents films and cinema-related content
* **Miner** → Refers to extracting valuable information from raw data

So, **MovieMiner** means:

> *“An AI-powered tool that mines and extracts structured movie information from unstructured text.”*

🌐 **Live Demo:**

```text id="c8el6r"
https://movieminer-ud6qc38f76463uj5btlyci.streamlit.app/
```

---

# 🚀 About the Project

MovieMiner is an AI-powered movie information extraction application built using **LangChain**, **Mistral AI**, **Pydantic**, and **Streamlit**.

The application takes a paragraph describing a movie and automatically converts it into structured data such as:

* Movie Title
* Release Year
* Genre
* Director
* Cast
* Rating
* Summary

This project demonstrates the power of **LLMs + Structured Output Parsing** for real-world NLP applications.

---

# ✨ Features

* 🎥 Extract movie details from plain English text
* 🤖 AI-powered information extraction using Mistral AI
* 📦 Structured output with Pydantic validation
* 🎨 Interactive Streamlit UI
* 📄 JSON formatted output
* ⬇ Download extracted data as JSON
* ⚡ Fast and lightweight application

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
├── movieminer.py        # Core extraction logic
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

```bash id="yr03df"
streamlit run app.py
```

---

# 🧠 How It Works

1. User enters a movie paragraph
2. LangChain sends the prompt to Mistral AI
3. The LLM extracts movie details
4. Pydantic validates the structured response
5. Streamlit displays the formatted output

---

# 📸 Example

## Input

```text id="t56v8r"
Inception is a 2010 science fiction film directed by Christopher Nolan and starring Leonardo DiCaprio. The movie follows a skilled thief who enters people's dreams to steal secrets.
```

## Output

```json id="g1wqto"
{
  "title": "Inception",
  "release_year": 2010,
  "genre": ["Science Fiction"],
  "director": "Christopher Nolan",
  "cast": ["Leonardo DiCaprio"],
  "rating": null,
  "summary": "A skilled thief enters dreams to steal secrets."
}
```

---

# 🔮 Future Improvements

* 🎭 Multiple movie extraction support
* 🌐 TMDB/IMDb API integration
* 📊 Export to CSV/PDF
* 🎨 Better UI animations
* 🧠 Improved genre classification
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

# 👨‍💻 Author

Developed by [Lakshyawardhan Singh Rathore]
