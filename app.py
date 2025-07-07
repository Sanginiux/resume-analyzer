import streamlit as st
from resume_parser import extract_resume_text

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 Resume Analyzer")
st.subheader("Analyze your resume and match it with job requirements")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    with st.spinner("Analyzing your resume..."):
        resume_text = extract_resume_text(uploaded_file)

    st.success("✅ Resume Uploaded and Analyzed!")
    
    st.subheader("📃 Extracted Resume Content:")
    st.text_area("Text", resume_text, height=300)

    # Placeholder for JD Matching (next step)
    st.subheader("🔍 JD Match (coming next...)")
