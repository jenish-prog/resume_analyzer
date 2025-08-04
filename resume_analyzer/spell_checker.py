from textblob import TextBlob

def check_spelling(text):
    blob = TextBlob(text)
    corrected = blob.correct()

    errors = []
    original_words = text.split()
    corrected_words = str(corrected).split()

    for i, (orig, corr) in enumerate(zip(original_words, corrected_words)):
        if orig != corr:
            errors.append((i + 1, orig, corr))

    return errors
