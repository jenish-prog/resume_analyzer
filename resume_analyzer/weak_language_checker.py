weak_words = [
    'good', 'helped', 'did', 'etc', 'worked', 'responsible for',
    'nice', 'thing', 'stuff', 'some', 'various', 'many', 'several',
    'tasked with', 'hard-working', 'motivated', 'quick learner',
    'team player', 'fast', 'basic', 'tried', 'assisted', 'made',
    'participated', 'contributed', 'handled', 'involved in', 'experience in'
]


replacement_suggestions = {
    'helped': ['collaborated', 'assisted', 'supported'],
    'did': ['executed', 'implemented', 'performed'],
    'worked': ['developed', 'engineered', 'built'],
    'responsible for': ['led', 'owned', 'oversaw'],
    'participated': ['contributed to', 'actively engaged in'],
    'contributed': ['delivered', 'implemented'],
    'made': ['designed', 'created', 'developed'],
    'involved in': ['managed', 'took initiative on'],
    'basic': ['foundational', 'introductory'],
    'thing': ['feature', 'component', 'module'],
    'stuff': ['items', 'tools', 'materials'],
    'nice': ['efficient', 'effective'],
    'fast': ['high-performance', 'rapid'],
    'tried': ['experimented with', 'attempted'],
    'experience in': ['proficient with', 'hands-on experience in'],
    'motivated': ['goal-oriented', 'self-driven'],
    'team player': ['collaborative contributor']
}


# Function to detect weak words and suggest replacements
def detect_weak_words(text):
    text = text.lower()
    word_count = {}

    for weak_word in weak_words:
        if weak_word in text:
            count = text.count(weak_word)
            word_count[weak_word] = count

    return word_count

# Function to generate feedback from weak word detections
def generate_weak_word_feedback(text):
    weak_found = detect_weak_words(text)

    if not weak_found:
        return "✅ No weak or generic words detected."

    feedback = ["=== Weak or Generic Language Feedback ==="]
    for word, count in weak_found.items():
        suggestion = replacement_suggestions.get(word, [])
        suggestion_text = f" → Try: {', '.join(suggestion)}" if suggestion else ""
        feedback.append(f"⚠️ '{word}' used {count} time(s){suggestion_text}.")
    return "\n".join(feedback)

# 🧪 Example usage
if __name__ == "__main__":
    sample_resume_text = """
        I am a hard-working team player who helped with many projects. 
        I was responsible for making a good website and did several tasks.
        I participated in various activities and was involved in nice things.
    """

    feedback = generate_weak_word_feedback(sample_resume_text)
    print(feedback)
