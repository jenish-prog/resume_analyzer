def check_sections(text):
    sections = ['education', 'projects', 'skills', 'experience']
    found = {section: (section in text.lower()) for section in sections}
    return found
