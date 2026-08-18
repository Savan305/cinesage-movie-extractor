from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# ------------------ MODEL ------------------
model = ChatGroq(
    model="llama3-70b-8192",
    temperature=0
)

# ------------------ PROMPT ------------------
prompt = ChatPromptTemplate.from_messages([

    ("system", """You are an expert information extraction system.

STRICT RULES:
- Return ONLY valid JSON.
- Do NOT add explanation.
- Do NOT wrap JSON in ``` or ```json.
"""),

    ("human", """Extract movie details from the paragraph.

Return JSON with:
title, release_year, genre, director, cast, rating, summary

Paragraph:
{paragraph}
""")
])

chain = prompt | model

# ------------------ UI ------------------
st.set_page_config(page_title="Movie Extractor", layout="centered")

st.title("🎬 Movie Information Extractor")

user_input = st.text_area(
    "Enter your paragraph:",
    height=200,
    placeholder="Paste your movie paragraph here..."
)

if st.button("Extract Information"):

    if not user_input.strip():
        st.warning("Please enter a paragraph.")
    else:
        response = chain.invoke({"paragraph": user_input})

        # 🔥 Clean markdown if model still returns ```json
        raw_output = response.content
        clean_output = raw_output.replace("```json", "").replace("```", "").strip()

        # ---------------- RAW VIEW ----------------
        st.subheader("🔹 Raw Model Output")
        st.code(clean_output, language="json")

        # ---------------- STRUCTURED VIEW ----------------
        try:
            parsed_json = json.loads(clean_output)

            st.subheader("🔹 Structured Output")
            st.json(parsed_json)   # 👈 expandable UI like your screenshot

        except Exception:
            st.error("⚠️ Could not parse JSON properly.")