const form = document.querySelector("form");
const phoneGroup = document.getElementById("phone-group");
const companyGroup = document.getElementById("company-group");
const roleRadios = document.querySelectorAll("input[name='role']");

// Initial state logic
if (companyGroup && phoneGroup) {
    companyGroup.style.display = "none";
}

roleRadios.forEach((radio) => {
    radio.addEventListener("change", () => {
        if (radio.value === "admin" && radio.checked) {
            companyGroup.style.display = "block";
            phoneGroup.style.display = "none";
            document.getElementById("phone").value = "";
        } else if (radio.value === "user" && radio.checked) {
            companyGroup.style.display = "none";
            phoneGroup.style.display = "block";
            document.getElementById("company_name").value = "";
        }
    });
});

// FORM SUBMISSION & VALIDATION
form.addEventListener("submit", function (e) {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;
    const role = document.querySelector("input[name='role']:checked").value;
    const company = document.getElementById("company_name").value;
    const phone = document.getElementById("phone").value;

    // CLIENT-SIDE VALIDATION
    // If validation fails, we stop the event. 
    // If it passes, we do NOT call preventDefault(), letting Django handle the save.

    if (password !== confirmPassword) {
        e.preventDefault();
        alert("Passwords do not match");
        return;
    }

    if (role === "admin" && !company) {
        e.preventDefault();
        alert("Company name is required for Admin accounts");
        return;
    }

    if (role === "user" && !phone) {
        e.preventDefault();
        alert("Phone number is required for Regular Users");
        return;
    }


    console.log("Validation passed! Submitting to Django...");
});