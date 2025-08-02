from spell_checker import check_spelling
from input_preprocess import extract_text_from_pdf
from section_checker import check_sections
from weak_language_checker import detect_weak_words
from feedback_generator import generate_feedback
from ats_matcher import extract_keywords, compare_resume_with_jd
import os

# 📄 Input Paths
resume_path = 'resumes/sample_resume.pdf'
jd_path = 'assets/sample_jd.txt'

# Step 1: Extract text from resume PDF
text = extract_text_from_pdf(resume_path)

# Step 2: Run spelling check
spell_errors = check_spelling(text)

# Step 3: Detect missing sections (Education, Projects, Skills, etc.)
section_status = check_sections(text)

# Step 4: Detect weak/repetitive words
weak_words = detect_weak_words(text)

# Step 5: Load job description and extract keywords
if os.path.exists(jd_path):
    with open(jd_path, 'r') as f:
        jd_text = f.read()

    jd_keywords = extract_keywords(jd_text)
    ats_result = compare_resume_with_jd(text, jd_keywords)
else:
    ats_result = None
    print("⚠️ Warning: Job description file not found. Skipping ATS analysis.")

# Step 6: Generate AI-style feedback
final_feedback = generate_feedback(
    spell_errors,
    section_status,
    weak_words,
    ats_result  # ✅ Pass ATS results if available
)

# Step 7: Save feedback to output file
os.makedirs("output", exist_ok=True)
with open('output/feedback.txt', 'w') as f:
    f.write(final_feedback)

print("✅ Full resume feedback (including ATS match) saved to 'output/feedback.txt'")
