// Selecting form and input elements
const form = document.querySelector("form");
const passwordInput = document.getElementById("password");
const passToggleBtn = document.getElementById("pass-toggle-btn");
const passToggleBtn2 = document.getElementById("pass-toggle-btn2");
const confirmInput = document.getElementById("confirm_password");

// Function to display error messages
const showError = (field, errorText) => {
    field.classList.add("error");
    const errorElement = document.createElement("small");
    errorElement.classList.add("error-text");
    errorElement.innerText = errorText;
    field.closest(".form-group").appendChild(errorElement);
}

// Function to handle form submission
const handleFormData = (e) => {
    e.preventDefault();

    // Retrieving input elements
    const nameInput = document.getElementById("nom");
    const fullnameInput = document.getElementById("prenom");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const confirmInput = document.getElementById("confirm_password");

    // Getting trimmed values from input fields
    const name = nameInput.value.trim();
    const fullname = fullnameInput.value.trim();
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();
    const confirm = confirmInput.value.trim();

    // Regular expression pattern for email validation
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    // Clearing previous error messages
    document.querySelectorAll(".form-group .error").forEach(field => field.classList.remove("error"));
    document.querySelectorAll(".error-text").forEach(errorText => errorText.remove());

    // Performing validation checks
    if (name === "") {
        showError(nameInput, "Veuillez entrer votre nom");
    }
    if (fullname === "") {
        showError(fullnameInput, "Veuillez entrer votre prenom");
    }
    if (!emailPattern.test(email)) {
        showError(emailInput, "Veuillez entrer un email valide");
    }
    if (password === "") {
        showError(passwordInput, "Veuillez entrer votre mot de passe");
    }
    if (confirm !== password) {
        showError(confirmInput, "Les mots de passe ne correspondent pas");
    }

    // Checking for any remaining errors before form submission
    const errorInputs = document.querySelectorAll(".form-group .error");
    if (errorInputs.length > 0) return;

    // Submitting the form
    form.submit();
}

// Toggling password visibility
passToggleBtn.addEventListener('click', () => {
    passToggleBtn.className = passwordInput.type === "password" ? "fa-solid fa-eye-slash" : "fa-solid fa-eye";
    passwordInput.type = passwordInput.type === "password" ? "text" : "password";
});

passToggleBtn2.addEventListener('click', () => {
    passToggleBtn2.className = confirmInput.type === "password" ? "fa-solid fa-eye-slash" : "fa-solid fa-eye";
    confirmInput.type = confirmInput.type === "password" ? "text" : "password";
});


// Handling form submission event
form.addEventListener("submit", handleFormData);