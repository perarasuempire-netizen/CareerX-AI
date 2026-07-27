skills_db = [

    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "php",
    "go",
    "ruby",
    "kotlin",
    "swift",

    # Web Development
    "html",
    "css",
    "bootstrap",
    "tailwind",
    "react",
    "angular",
    "vue",
    "nodejs",
    "express",
    "flask",
    "django",

    # Databases
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "oracle",
    "sql",

    # Data Science & AI
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "tensorflow",
    "pytorch",
    "opencv",
    "numpy",
    "pandas",
    "scikit-learn",
    "data analysis",

    # Cloud & DevOps
    "aws",
    "azure",
    "google cloud",
    "docker",
    "kubernetes",
    "jenkins",
    "git",
    "github",
    "linux",

    # Mobile Development
    "android",
    "flutter",
    "react native",
    "firebase",

    # Cyber Security
    "cybersecurity",
    "ethical hacking",
    "network security",
    "penetration testing",
    "cryptography",

    # Networking
    "computer networks",
    "tcp/ip",
    "routing",
    "switching",

    # Software Engineering
    "oop",
    "data structures",
    "algorithms",
    "software testing",
    "agile",
    "scrum",

    # Tools
    "vscode",
    "postman",
    "figma",
    "canva",
    "jira",

    # Soft Skills
    "communication",
    "leadership",
    "teamwork",
    "problem solving",
    "critical thinking",
    "time management"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill.title())

    return found_skills