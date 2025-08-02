import re
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, top_n=30):
    text = re.sub(r'[^\w\s]', '', text.lower())
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform([text])
    scores = zip(vectorizer.get_feature_names_out(), tfidf.toarray()[0])
    sorted_keywords = sorted(scores, key=lambda x: x[1], reverse=True)
    return [word for word, score in sorted_keywords[:top_n]]

def compare_resume_with_jd(resume_text, jd_keywords):
    resume_words = set(re.sub(r'[^\w\s]', '', resume_text.lower()).split())
    present = [kw for kw in jd_keywords if kw in resume_words]
    missing = [kw for kw in jd_keywords if kw not in resume_words]
    score = round((len(present) / len(jd_keywords)) * 100, 2) if jd_keywords else 0
    return present, missing, score
