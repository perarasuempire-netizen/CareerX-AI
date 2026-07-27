def recommend_careers(skills):

    skills = [skill.lower() for skill in skills]

    careers = []

    # AI / ML
    if "python" in skills and (
        "machine learning" in skills or
        "tensorflow" in skills or
        "pytorch" in skills
    ):
        careers.append("AI/ML Engineer")

    # Backend
    if (
        "python" in skills and
        "flask" in skills
    ) or (
        "java" in skills and
        "mysql" in skills
    ):
        careers.append("Backend Developer")

    # Frontend
    if (
        "html" in skills and
        "css" in skills and
        "javascript" in skills
    ):
        careers.append("Frontend Developer")

    # Full Stack
    if (
        "html" in skills and
        "css" in skills and
        "javascript" in skills and
        ("flask" in skills or "react" in skills)
    ):
        careers.append("Full Stack Developer")

    # Mobile
    if (
        "flutter" in skills or
        "android" in skills or
        "react native" in skills
    ):
        careers.append("Mobile App Developer")

    # Cyber Security
    if (
        "cybersecurity" in skills or
        "ethical hacking" in skills or
        "network security" in skills
    ):
        careers.append("Cyber Security Analyst")

    # Data Science
    if (
        "python" in skills and
        ("pandas" in skills or "numpy" in skills)
    ):
        careers.append("Data Scientist")

    if not careers:
        careers.append("Software Developer")

    return careers