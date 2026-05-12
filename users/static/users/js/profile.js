
document.addEventListener("DOMContentLoaded", function () {
    const experienceForm = document.querySelector("#experience-section form");
    const descriptionInput = document.getElementById("description");

    if (experienceForm) {
        experienceForm.addEventListener("submit", function (e) {

            const saveBtn = experienceForm.querySelector("button");
            saveBtn.innerText = "Saving...";
            saveBtn.style.opacity = "0.7";
            saveBtn.disabled = true;
        });
    }
});