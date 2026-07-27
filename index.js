const upload =
document.getElementById("resumeUpload");

const error =
document.getElementById("errorMsg");

const success =
document.getElementById("successMsg");

upload.addEventListener(
    "change",
    async function () {

        const file = this.files[0];

        if (!file) return;

        const maxSize =
            10 * 1024 * 1024;

        const allowedExtensions = [
            "pdf",
            "docx"
        ];

        const extension =
            file.name
                .split(".")
                .pop()
                .toLowerCase();

        if (
            !allowedExtensions.includes(
                extension
            )
        ) {

            error.textContent =
                "Only PDF and DOCX files are allowed.";

            error.style.display =
                "block";

            success.style.display =
                "none";

            this.value = "";

            return;
        }

        if (file.size > maxSize) {

            error.textContent =
                "File size must be less than 10 MB.";

            error.style.display =
                "block";

            success.style.display =
                "none";

            this.value = "";

            return;
        }

        error.style.display =
            "none";

        success.style.display =
            "none";

        await uploadResume(file);
    }
);
async function uploadResume(file) {

    const formData = new FormData();

    formData.append(
        "resume",
        file
    );

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/upload",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        console.log("Server Response:", data);

        if (response.ok && data.success) {

            success.textContent =
                "✓ Resume uploaded successfully";

            success.style.display = "block";

            error.style.display = "none";

            localStorage.setItem(
                "resumeData",
                JSON.stringify(data)
            );

            setTimeout(() => {

                window.location.href =
                    "result.html";

            }, 1000);

        } else {

            error.textContent =
                data.error || "Upload failed";

            error.style.display = "block";

            success.style.display = "none";
        }

    } catch (err) {

        console.error(err);

        success.style.display = "none";

        error.textContent =
            "❌ Upload failed. Backend server is not running.";

        error.style.display = "block";
    }
}