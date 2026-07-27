# course_recommender.py


course_database = {


"Software Developer":[

{
"platform":"NPTEL",
"course":"Programming in Java",
"skills":["java","oop"],
"website":"https://nptel.ac.in"
},

{
"platform":"Coursera",
"course":"Python for Everybody",
"skills":["python"],
"website":"https://www.coursera.org"
},

{
"platform":"GeeksforGeeks",
"course":"Data Structures and Algorithms",
"skills":["dsa","problem solving"],
"website":"https://www.geeksforgeeks.org"
},

{
"platform":"Udemy",
"course":"Complete Software Development Bootcamp",
"skills":["software development","git"],
"website":"https://www.udemy.com"
},

{
"platform":"GitHub Learning",
"course":"Git and Version Control",
"skills":["git"],
"website":"https://skills.github.com"
}

],




"AI Engineer":[

{
"platform":"Coursera",
"course":"Machine Learning Specialization",
"skills":["machine learning","python"],
"website":"https://www.coursera.org"
},

{
"platform":"DeepLearning.AI",
"course":"Deep Learning Specialization",
"skills":["deep learning","neural networks"],
"website":"https://www.deeplearning.ai"
},

{
"platform":"Kaggle",
"course":"Python and Machine Learning Practice",
"skills":["python","ml"],
"website":"https://www.kaggle.com"
},

{
"platform":"NPTEL",
"course":"Artificial Intelligence Course",
"skills":["ai"],
"website":"https://nptel.ac.in"
}

],





"Data Scientist":[

{
"platform":"Coursera",
"course":"IBM Data Science Professional Certificate",
"skills":["python","data science"],
"website":"https://www.coursera.org"
},

{
"platform":"Kaggle",
"course":"Data Science Projects",
"skills":["machine learning","analytics"],
"website":"https://www.kaggle.com"
},

{
"platform":"edX",
"course":"Data Analytics Fundamentals",
"skills":["statistics","data analysis"],
"website":"https://www.edx.org"
}

],






"Cloud Engineer":[

{
"platform":"AWS Skill Builder",
"course":"AWS Cloud Practitioner",
"skills":["cloud","aws"],
"website":"https://skillbuilder.aws"
},

{
"platform":"Microsoft Learn",
"course":"Azure Fundamentals",
"skills":["azure","cloud"],
"website":"https://learn.microsoft.com"
},

{
"platform":"Google Cloud Skills Boost",
"course":"Cloud Computing Fundamentals",
"skills":["gcp","cloud"],
"website":"https://cloudskillsboost.google"
}

],






"Web Developer":[

{
"platform":"freeCodeCamp",
"course":"Responsive Web Design",
"skills":["html","css","javascript"],
"website":"https://www.freecodecamp.org"
},

{
"platform":"JavaScript.info",
"course":"Modern JavaScript Tutorial",
"skills":["javascript"],
"website":"https://javascript.info"
},

{
"platform":"Udemy",
"course":"Full Stack Web Development",
"skills":["frontend","backend"],
"website":"https://www.udemy.com"
}

]

}




def recommend_courses(target_role, missing_skills=[]):


    recommendations = []


    courses = course_database.get(
        target_role,
        course_database["Software Developer"]
    )



    for course in courses:


        # Check skill matching

        if any(
            skill.lower() in 
            [s.lower() for s in missing_skills]
            for skill in course["skills"]
        ):

            recommendations.append(course)



    # If no skill match, return default courses

    if not recommendations:

        recommendations = courses[:5]


    return recommendations