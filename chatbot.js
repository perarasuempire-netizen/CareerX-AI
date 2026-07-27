function sendMessage() {

    const input = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");

    const message = input.value.trim().toLowerCase();

    if (message === "") return;

    chatBox.innerHTML += `
        <p><strong>You:</strong> ${input.value}</p>
    `;

    let reply = "";

    if (
        message.includes("hi") ||
        message.includes("hello") ||
        message.includes("hii")
    ) {

        reply =
        "👋 Hello! I am CareerX AI. Ask me about careers, skills, roadmaps, or companies.";

    } else if (
        message.includes("career") ||
        message.includes("careers")
    ) {

        reply =
        "🚀 Popular careers: AI Engineer, Software Developer, Data Scientist, Mobile App Developer, Cloud Engineer, Cyber Security Analyst.";

    } else if (
        message.includes("company") ||
        message.includes("companies") ||
        message.includes("apply")
    ) {

        reply =
        "🏢 Top companies: Google, Microsoft, Amazon, Zoho, Infosys, TCS, Wipro, Accenture, Cognizant.";

    } else if (
        message.includes("ai engineer")
    ) {

        reply =
        "🤖 Learn Python → Machine Learning → Deep Learning → TensorFlow → Build AI Projects.";

    } else if (
        message.includes("software developer")
    ) {

        reply =
        "💻 Learn Java, Python, SQL, Git and Data Structures.";

    } else if (
        message.includes("mobile app")
    ) {

        reply =
        "📱 Learn Dart, Flutter, Firebase and build Android applications.";

    } else if (
        message.includes("roadmap")
    ) {

        reply =
        "🗺️ Choose a career role first. Then I can suggest a roadmap.";

    } else if (
        message.includes("skills")
    ) {

        reply =
        "🎯 Popular skills: Python, Java, SQL, Git, Flutter, React, AWS, Machine Learning.";

    } else {

        reply =
        "❓ I didn't understand that. Ask about careers, skills, roadmaps or companies.";
    }

    chatBox.innerHTML += `
        <p><strong>CareerX AI:</strong> ${reply}</p>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    input.value = "";
}