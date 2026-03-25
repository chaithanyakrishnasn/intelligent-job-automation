import re

KNOWN_SKILLS = [
    "python", "fastapi", "sql", "docker",
    "kubernetes", "machine learning", "ai",
    "backend", "api", "flask", "django"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in KNOWN_SKILLS:
        if re.search(rf"\b{skill}\b", text):
            found_skills.append(skill)

    return found_skills