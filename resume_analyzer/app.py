import streamlit as st
from spell_checker import check_spelling
from input_preprocess import extract_text_from_pdf
from section_checker import check_sections
from weak_language_checker import detect_weak_words
from feedback_generator import generate_feedback
from ats_matcher import extract_keywords, compare_resume_with_jd
import tempfile
import os

st.set_page_config(page_title="📄 Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer with ATS Match")

uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
uploaded_jd = st.file_uploader("Upload Job Description (Optional)", type=["txt"])

# Use a single button block
if st.button("Analyze Resume"):
    if not uploaded_resume:
        st.warning("⚠️ Please upload your resume to start analysis.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_resume:
            tmp_resume.write(uploaded_resume.read())
            resume_path = tmp_resume.name

        # Extract text
        resume_text = extract_text_from_pdf(resume_path)

        # NLP Processing
        spell_errors = check_spelling(resume_text)
        section_status = check_sections(resume_text)
        weak_words = detect_weak_words(resume_text)

        ats_result = None
        if uploaded_jd:
            jd_text = uploaded_jd.read().decode("utf-8")
            jd_keywords = extract_keywords(jd_text)
            ats_result = compare_resume_with_jd(resume_text, jd_keywords)

        # Generate feedback
        feedback = generate_feedback(spell_errors, section_status, weak_words, ats_result)

        # Display
        st.subheader("📝 Feedback Report")
        st.text_area("Result", value=feedback, height=500)

        # Download
        st.download_button("📥 Download Feedback", feedback, file_name="resume_feedback.txt")
