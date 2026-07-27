const courseContainer =
document.getElementById("courseContainer");


const courses =
JSON.parse(localStorage.getItem("courses"));



if(courses && courses.length > 0){


courses.forEach(course=>{


const card =
document.createElement("div");


card.className =
"course-card";



card.innerHTML = `


<h2>
🎓 ${course.platform}
</h2>


<h3>
${course.course}
</h3>


<a href="${course.website}"
target="_blank">

Visit Platform 🌐

</a>


`;



courseContainer.appendChild(card);


});


}

else{


courseContainer.innerHTML = `


<div class="course-card">

<h2>
No Course Data Found
</h2>


<p>
Please analyze your resume again.
</p>


</div>


`;


}