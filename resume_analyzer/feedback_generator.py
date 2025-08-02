from weak_language_checker import replacement_suggestions

def generate_feedback(spell_errors, section_status, weak_words, ats_result=None):
    feedback = []

    # 📋 HEADER
    feedback.append("📝 Resume Review")
    feedback.append("────────────────────────────────────────────\n")

    # 📌 Section Analysis
    feedback.append("📌 Section Overview:")
    feedback.append("────────────────────")
    for section, found in section_status.items():
        if found:
            feedback.append(f"✔️ {section.title()} section found")
        else:
            tip = {
                'projects': '→ Consider adding 1–2 relevant academic or personal projects',
                'experience': '→ Include internships, freelance, or volunteering',
                'education': '→ Add your degree, university, and graduation date',
                'skills': '→ Include technical, soft, and domain-specific skills'
            }.get(section, '')
            feedback.append(f"✘ {section.title()} section missing {tip}")

    # 🔍 Spelling Errors
    feedback.append("\n🔍 Spelling Suggestions:")
    feedback.append("────────────────────────")
    if not spell_errors:
        feedback.append("✔️ No spelling mistakes found.")
    else:
        for line, word, suggestion in spell_errors:
            feedback.append(f"• On line {line}, the word **'{word}'** might be a typo. Did you mean **'{suggestion}'**?")

    # 💬 Weak Language
    feedback.append("\n💬 Weak or Generic Words:")
    feedback.append("────────────────────────────")
    if not weak_words:
        feedback.append("✔️ No weak language detected.")
    else:
        for word, count in weak_words.items():
            suggestions = replacement_suggestions.get(word, [])
            better = f"→ Try: {', '.join(suggestions)}" if suggestions else ""
            feedback.append(f"• Used **'{word}'** {count} time(s). {better}")

    # 📌 ATS Keyword Matching
    if ats_result:
        present, missing, score = ats_result
        feedback.append("\n📌 ATS Keyword Match:")
        feedback.append("────────────────────")
        feedback.append(f"🔢 Match Score: {score}%")
        if missing:
            feedback.append(f"❌ Missing Keywords: {', '.join(missing)}")
        if present:
            feedback.append(f"✔️ Found Keywords: {', '.join(present)}")
    else:
        feedback.append("\n📌 ATS Match: Skipped (No JD Provided)")

    # ✅ Suggestions
    feedback.append("\n✅ Recommendations:")
    feedback.append("────────────────────────")
    feedback.append("• Start with a 2–3 line personal summary.")
    feedback.append("• Use action verbs: *developed*, *led*, *designed*, etc.")
    feedback.append("• Quantify achievements where possible.")
    feedback.append("• Keep formatting consistent.")

    # 📄 Final Note
    feedback.append("\n📄 Final Thoughts:")
    feedback.append("────────────────────────")
    feedback.append("You're off to a great start! A few focused edits will make your resume stand out even more. Keep it up! 🚀")

    return "\n".join(feedback)
