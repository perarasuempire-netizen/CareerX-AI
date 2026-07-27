const companyContainer =
document.getElementById("companyContainer");


const companyData =
localStorage.getItem("companies");


console.log("Company Data:", companyData);



if(companyData){


    const companies =
    JSON.parse(companyData);



    companies.forEach(company=>{


        companyContainer.innerHTML += `

        <div class="company-card">

            <h2>
            🏢 ${company.name}
            </h2>


            <p>
            📍 ${company.location}
            </p>


            <p>
            💼 ${company.roles.join(", ")}
            </p>


            <a href="${company.website}" target="_blank">
            Official Website 🌐
            </a>

        </div>

        `;


    });


}
else{


    companyContainer.innerHTML = `

    <div class="company-card">

    <h2>
    No Company Data Found
    </h2>

    <p>
    Analyze resume again.
    </p>

    </div>

    `;

}