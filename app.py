import streamlit as st
from resume_parser import extract_text_from_pdf
from similarity_engine import compute_similarity
import os

st.set_page_config(page_title="Resume Screener", layout="wide")

st.title("📄 AI-Powered Resume Screening & Ranking Model")

jd_text = st.text_area("🔹 Paste Job Description Here", height=250)

uploaded_files = st.file_uploader("📤 Upload Resumes (PDFs)", type="pdf", accept_multiple_files=True)

if st.button("🔍 Screen Resumes") and jd_text and uploaded_files:
    resumes = []
    names = []

    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(text)
        names.append(file.name)

    ranked_scores = compute_similarity(jd_text, resumes, names)

    st.subheader("📊 Top Matches")
    for rank, (name, score) in enumerate(ranked_scores, start=1):
        st.write(f"**#{rank} - {name}** | 🔹 Score: {score:.2f}")
