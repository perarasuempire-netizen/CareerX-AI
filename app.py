from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from pdf_parser import extract_pdf_text
from docx_parser import extract_docx_text
from skill_extractor import extract_skills
from recommender import recommend_careers
from ats_score import calculate_ats_score
from skill_gap import get_skill_gap
from roadmap import generate_roadmap
from company_recommender import recommend_companies
from course_recommender import recommend_courses
from chatbot import career_chatbot

app = Flask(__name__)

CORS(app)



# =========================
# Configuration
# =========================

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {
    "pdf",
    "docx"
}


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)




# =========================
# File Validation
# =========================

def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".",1)[1].lower()
        in ALLOWED_EXTENSIONS
    )





# =========================
# Home
# =========================

@app.route("/")
def home():

    return "CareerX AI Backend Running"






# =========================
# Resume Upload API
# =========================

@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return jsonify({
            "error": "No file uploaded"
        }), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({
            "error": "No file selected"
        }), 400

    if not allowed_file(file.filename):
        return jsonify({
            "error": "Only PDF and DOCX files are allowed"
        }), 400

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    # =========================
    # Extract Resume Text
    # =========================

    if filename.lower().endswith(".pdf"):
        extracted_text = extract_pdf_text(filepath)

    elif filename.lower().endswith(".docx"):
        extracted_text = extract_docx_text(filepath)

    else:
        extracted_text = ""

    print("\n===== RESUME TEXT =====")
    print(extracted_text)
    print("=======================\n")

    # =========================
    # Resume Validation
    # =========================

    resume_keywords = [
        "education",
        "skills",
        "experience",
        "projects",
        "internship",
        "objective",
        "certification",
        "technical skills",
        "profile",
        "summary"
    ]

    text_lower = extracted_text.lower()

    matches = 0

    for keyword in resume_keywords:
        if keyword in text_lower:
            matches += 1

    if matches < 2:
        return jsonify({
            "error": "Uploaded file does not appear to be a resume."
        }), 400

    # =========================
    # Skills
    # =========================

    skills = extract_skills(
        extracted_text
    )

    # =========================
    # Career Prediction
    # =========================

    careers = recommend_careers(
        skills
    )

    # =========================
    # ATS Score
    # =========================

    ats_score = calculate_ats_score(
        extracted_text,
        skills
    )

    # =========================
    # Target Role
    # =========================

    if careers:
        target_role = careers[0]
    else:
        target_role = "Software Developer"

    # =========================
    # Skill Gap
    # =========================

    skill_gap = get_skill_gap(
        skills,
        target_role
    )

    # =========================
    # Roadmap
    # =========================

    roadmap = generate_roadmap(
        target_role,
        skill_gap.get(
            "missing_skills",
            []
        )
    )

    # =========================
    # Course Recommendation
    # =========================

    courses = recommend_courses(
        target_role,
        skill_gap.get(
            "missing_skills",
            []
        )
    )

    # =========================
    # Company Recommendation
    # =========================

    companies = recommend_companies(
        skills,
        target_role
    )

    # =========================
    # Debug
    # =========================

    print("Skills:", skills)
    print("Careers:", careers)
    print("Target Role:", target_role)
    print("ATS Score:", ats_score)
    print("Skill Gap:", skill_gap)
    print("Roadmap:", roadmap)
    print("Courses:", courses)
    print("Companies:", companies)

    return jsonify({

        "success": True,

        "filename": filename,

        "resume_text": extracted_text[:500],

        "skills": skills,

        "careers": careers,

        "target_role": target_role,

        "ats_score": ats_score,

        "skill_gap": skill_gap,

        "roadmap": roadmap,

        "courses": courses,

        "companies": companies

    })
    return jsonify({

        "success": True,
        "filename": filename,
        "resume_text": extracted_text[:500],

        "skills": skills,
        "careers": careers,

        "target_role": target_role,

        "ats_score": ats_score,

        "skill_gap": skill_gap,

        "roadmap": roadmap,

        "courses": courses,

        "companies": companies

    })


# =========================
# AI Chatbot API
# =========================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    message = data.get("message", "")

    resume_data = data.get("resume_data", {})

    response = career_chatbot(
        message,
        resume_data
    )

    return jsonify({
        "reply": response
    })


# =========================
# Run Server
# =========================

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )
