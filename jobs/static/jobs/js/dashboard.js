const dropMenu = (event) => {
    const el = event.target;
    const menu = document.querySelector(".menu");
    const btnPos = el.getBoundingClientRect();
    // No active menus
    if (activeMenuId == null) {
        activeMenuId = el.id;
        menu.style = `display: flex; top: ${btnPos.top - btnPos.height}px; left: ${btnPos.right - btnPos.width}px;`;
        document.getElementById("view-link").href =
            `job-detail.html?job_id=${activeMenuId}&edit=false`;
        document.getElementById("edit-link").href =
            `job-detail.html?job_id=${activeMenuId}&edit=true`;
    }
    // Menu is active elsewhere
    else if (activeMenuId != el.id && activeMenuId != null) {
        activeMenuId = el.id;
        menu.style = `display: flex; top: ${btnPos.top - btnPos.height}px; left: ${btnPos.right - btnPos.width}px;`;
        document.getElementById("view-link").href =
            `job-detail.html?job_id=${activeMenuId}&edit=false`;
        document.getElementById("edit-link").href =
            `job-detail.html?job_id=${activeMenuId}&edit=true`;
    }
    // Dismiss current menu
    else {
        activeMenuId = null;
        menu.style = "display: none;";
    }
};

let activeMenuId = null;
let selectedJobId = null;

window.addEventListener("load", () => {
    // Saves selected job id for deletion
    const deleteButton = document.querySelector("#delete");
    deleteButton.addEventListener("click", () => {
        selectedJobId = activeMenuId;
        console.log(selectedJobId);
    });

    // Calls deleleJob with selectedJobId via dialog
    const dialogDeleteBtn = document.querySelector("#dialog-delete-btn");
    dialogDeleteBtn.addEventListener("click", () => {
        // deleteJob(selectedJobId); needs to be replaced with django delete
        selectedJobId = null;
    });
});

window.addEventListener("click", (event) => {
    const el = event.target;
    const menu = document.querySelector(".menu");
    if (!el.classList.contains("menu-btn-icon")) {
        menu.style = "display: none;";
        activeMenuId = null;
    }
});
