# 🎬 Movie Information Extractor (LangChain + Streamlit)

A simple yet powerful **Generative AI application** that extracts structured movie information from unstructured text using **LangChain**, **Mistral AI**, and **Pydantic**.

---

## 🚀 Features

* 🔍 Extracts key movie details from paragraphs
* 🤖 Powered by LLM (Mistral via LangChain)
* 📦 Structured output using **Pydantic schema**
* 🖥️ Interactive **Streamlit UI**
* 📄 Displays both:

  * Raw JSON output
  * Structured expandable view

---

## 🧠 How It Works

1. User inputs a paragraph about a movie
2. LLM processes the text using a prompt template
3. Output is generated in **JSON format**
4. Data is:

   * Parsed using Pydantic (core logic)
   * Displayed in UI (Streamlit app)

---

## 🏗️ Project Structure

```
├── core2.py        # Core extraction logic (LangChain + Pydantic)
├── UIcore.py       # Streamlit UI
├── .env            # API keys
└── README.md
```

---

## ⚙️ Tech Stack

* **LangChain**
* **Mistral AI**
* **Pydantic**
* **Streamlit**
* **Python**

---

## 📂 Core Logic

The core file uses:

* `PydanticOutputParser` for structured validation
* A defined `Movie` schema
* LangChain prompt + model pipeline

👉 See implementation: 

---

## 💻 Streamlit UI

The UI allows users to:

* Enter a movie paragraph
* View extracted data in:

  * Raw JSON format
  * Structured interactive format

👉 See UI code: 

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add API key

Create `.env` file:

```
MISTRAL_API_KEY=your_api_key_here
```

### 3. Run Core Script (CLI)

```bash
python core2.py
```

### 4. Run Streamlit App

```bash
streamlit run UIcore.py
```

---

## 📌 Example Input

```
Interstellar is a science fiction film directed by Christopher Nolan...
```

---

## 📌 Example Output

```json
{
  "title": "Interstellar",
  "release_year": 2014,
  "genre": ["science fiction"],
  "director": "Christopher Nolan",
  "cast": ["Matthew McConaughey"],
  "rating": null,
  "summary": "A journey through space to save humanity."
}
```

---

## 🔥 Key Highlights

* Clean separation of **core logic and UI**
* Demonstrates **LLM + structured output parsing**
* Real-world **information extraction use case**
* Beginner-friendly but **project-worthy for portfolio**

---

## 🚀 Future Improvements

* Add support for **multiple entity types (person, company, etc.)**
* Integrate **external APIs (TMDB)** for enrichment
* Add **download/export JSON feature**
* Improve error handling & validation

---

## 👨‍💻 Author

**Savan Patel**
Aspiring AI/ML Engineer | Generative AI Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
