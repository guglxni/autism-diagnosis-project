// theme.js

// Retrieve the stored theme preference from localStorage
const userPreference = localStorage.getItem("theme");
const body = document.body;
const toggleButton = document.getElementById("theme-toggle");

// Apply the user's preference if it exists
if (userPreference) {
    body.setAttribute("data-theme", userPreference);
    toggleButton.textContent =
        userPreference === "dark" ? "Switch to Light Mode" : "Switch to Dark Mode";
}

// Toggle theme on button click
toggleButton.addEventListener("click", function () {
    const currentTheme = body.getAttribute("data-theme") || "light";
    const newTheme = currentTheme === "light" ? "dark" : "light";

    // Set the new theme on the body
    body.setAttribute("data-theme", newTheme);

    // Update the button text
    toggleButton.textContent =
        newTheme === "dark" ? "Switch to Light Mode" : "Switch to Dark Mode";

    // Save the user's preference to localStorage
    localStorage.setItem("theme", newTheme);
});