def calculate_ats_score(text, skills):

    score = 0

    text = text.lower()

    # Education
    education_keywords = [
        "b.e", "b.tech", "bachelor",
        "m.e", "m.tech", "degree"
    ]

    if any(keyword in text for keyword in education_keywords):
        score += 20

    # Skills
    score += min(len(skills) * 5, 30)

    # Projects
    if "project" in text or "projects" in text:
        score += 20

    # Experience
    if "experience" in text or "internship" in text:
        score += 15

    # Certifications
    if "certification" in text or "certifications" in text:
        score += 15

    return min(score, 100)