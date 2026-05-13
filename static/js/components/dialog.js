/*
In order to activate the dialog component: add class "open-dialog" to the activating element
*/

const openDialog = () => {
    const dialogComp = document.querySelector(".overlay");
    dialogComp.style = "display: flex;";
};

const closeDialog = () => {
    const dialogComp = document.querySelector(".overlay");
    dialogComp.style = "display: none;";
};

window.addEventListener("load", () => {
    const openBtn = document.querySelector(".open-dialog");
    openBtn.addEventListener("click", openDialog);

    const closeMark = document.querySelector(".dialog-close");
    const cancelBtn = document.querySelector(".btn-close");
    const actBtn = document.querySelector(".btn-act");
    closeMark.addEventListener("click", closeDialog);
    cancelBtn.addEventListener("click", closeDialog);
    actBtn.addEventListener("click", closeDialog);
});
