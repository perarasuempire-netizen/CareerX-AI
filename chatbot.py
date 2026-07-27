def career_chatbot(message, resume_data):


    message = message.lower()


    skills = resume_data.get(
        "skills",
        []
    )


    role = resume_data.get(
        "target_role",
        "Software Developer"
    )


    companies = resume_data.get(
        "companies",
        []
    )


    courses = resume_data.get(
        "courses",
        []
    )


    roadmap = resume_data.get(
        "roadmap",
        []
    )


    missing = resume_data.get(
        "skill_gap",
        {}
    ).get(
        "missing_skills",
        []
    )



    # Career Question

    if "career" in message or "role" in message:

        return f"""

Based on your resume:

Recommended Role:
{role}

Your Skills:
{', '.join(skills)}

You should focus on improving:
{', '.join(missing)}

"""



    # Company Question

    elif "company" in message or "job" in message:


        if companies:

            company_names = [
                c["name"]
                for c in companies
            ]


            return f"""

Recommended companies for you:

{', '.join(company_names)}

Apply for roles matching:
{role}

"""


    # Course Question

    elif "course" in message or "learn" in message:


        if courses:

            course_names = [
                c["course"]
                for c in courses
            ]


            return f"""

Recommended learning:

{', '.join(course_names)}

These will help you close your skill gap.

"""



    # Skill Question

    elif "skill" in message:


        return f"""

Current Skills:

{', '.join(skills)}


Missing Skills:

{', '.join(missing)}

"""


    # Roadmap

    elif "roadmap" in message or "plan" in message:


        return "\n".join(roadmap)



    else:


        return """

I can help you with:

• Career recommendation
• Skill improvement
• Company suggestions
• Learning courses
• Career roadmap

Ask me anything about your career.

"""