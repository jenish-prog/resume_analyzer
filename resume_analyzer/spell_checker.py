import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def check_spelling(text):
    matches = tool.check(text)
    errors = []

    for match in matches:
        if match.ruleId.startswith("MORFOLOGIK_RULE") or "Spelling mistake" in match.message:
            line = text[:match.offset].count('\n') + 1
            word = text[match.offset: match.offset + match.errorLength]
            suggestion = match.replacements[0] if match.replacements else "?"
            errors.append((line, word, suggestion))

    return errors
