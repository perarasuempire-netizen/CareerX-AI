def get_skill_gap(user_skills, target_role):

    roles = {

        "AI Engineer": [
            "python", "machine learning", "deep learning",
            "tensorflow", "pytorch", "numpy",
            "pandas", "scikit-learn"
        ],

        "Data Scientist": [
            "python", "pandas", "numpy",
            "sql", "machine learning",
            "data analysis", "statistics"
        ],

        "Frontend Developer": [
            "html", "css", "javascript",
            "react", "bootstrap", "tailwind"
        ],

        "Backend Developer": [
            "python", "flask", "django",
            "mysql", "postgresql", "api", "git"
        ],

        "Full Stack Developer": [
            "html", "css", "javascript",
            "react", "python", "flask",
            "mysql", "git"
        ],

        "Mobile App Developer": [
            "flutter", "dart",
            "firebase", "android",
            "react native"
        ],

        "Cyber Security Analyst": [
            "cybersecurity",
            "network security",
            "ethical hacking",
            "cryptography",
            "linux"
        ],

        "Cloud Engineer": [
            "aws", "azure",
            "docker", "kubernetes",
            "linux", "git"
        ],

        "Software Developer": [
            "python", "java",
            "c", "git",
            "sql", "problem solving"
        ]
    }

    role_key = target_role.strip().lower()

    roles_lower = {
        key.lower(): value
        for key, value in roles.items()
    }

    required_skills = roles_lower.get(role_key, [])

    user_skills = [skill.lower() for skill in user_skills]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in user_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(required_skills) > 0:
        match_percentage = round(
            (len(matched_skills) / len(required_skills)) * 100,
            2
        )
    else:
        match_percentage = 0

    print("Target Role:", target_role)
    print("Required Skills:", required_skills)
    print("Matched Skills:", matched_skills)
    print("Missing Skills:", missing_skills)

    return {
        "target_role": target_role,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage
    }