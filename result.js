const data = JSON.parse(localStorage.getItem("resumeData"));

const skillsList = document.getElementById("skillsList");
const careerList = document.getElementById("careerList");
const atsScore = document.getElementById("atsScore");
const skillGapDiv = document.getElementById("skillGap");
const roadmapDiv = document.getElementById("roadmap");


if (!data) {

    document.body.innerHTML = `
    <div style="text-align:center;margin-top:100px;">
        <h2>No resume data found.</h2>
        <a href="index.html">🏠 Go Back Home</a>
    </div>
    `;

}
else {


    console.log("Resume Data:", data);



    // Save company recommendations

    if (data.companies) {

        localStorage.setItem(
            "companies",
            JSON.stringify(data.companies)
        );

    }



    // Save course recommendations

    if (data.courses) {

        localStorage.setItem(
            "courses",
            JSON.stringify(data.courses)
        );

    }




    // Skills

    if (data.skills && data.skills.length > 0) {

        skillsList.innerHTML = data.skills
        .map(skill =>
            `<li>${skill}</li>`
        )
        .join("");

    }
    else {

        skillsList.innerHTML =
        "<li>No skills detected</li>";

    }







    // Career Recommendation

    if (data.careers && data.careers.length > 0) {

        careerList.innerHTML = data.careers
        .map(career =>
            `<li>${career}</li>`
        )
        .join("");

    }
    else {

        careerList.innerHTML =
        "<li>No career recommendation</li>";

    }







    // ATS Score

    atsScore.innerHTML = `

    <div class="ats-badge">
        ${data.ats_score}/100
    </div>

    `;








    // Skill Gap Analysis

    if (data.skill_gap) {


        skillGapDiv.innerHTML = `

        <div class="gap-card">


            <h3 class="role-title">
            🎯 ${data.skill_gap.target_role}
            </h3>


            <div class="match-score">
            📊 ${data.skill_gap.match_percentage}% Match
            </div>




            <div class="gap-section">

            <h4>✅ Matched Skills</h4>

            <ul class="matched-list">

            ${
            data.skill_gap.matched_skills
            .map(skill =>
                `<li>${skill}</li>`
            )
            .join("")
            }

            </ul>

            </div>





            <div class="gap-section">

            <h4>❌ Missing Skills</h4>

            <ul class="missing-list">

            ${
            data.skill_gap.missing_skills
            .map(skill =>
                `<li>${skill}</li>`
            )
            .join("")
            }

            </ul>

            </div>



        </div>

        `;


    }
    else {


        skillGapDiv.innerHTML =
        "<p>No skill gap analysis available.</p>";


    }










    // Learning Roadmap

    if (data.roadmap && data.roadmap.length > 0) {


        roadmapDiv.innerHTML = `

        <div class="roadmap-card">


        ${
        data.roadmap
        .map(step =>

        `
        <div class="roadmap-step">
            ${step}
        </div>
        `

        )
        .join("")
        }


        </div>

        `;


    }
    else {


        roadmapDiv.innerHTML =
        "<p>No roadmap available.</p>";

    }



}