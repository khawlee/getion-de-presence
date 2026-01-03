const form = document.getElementById("loginForm");
const errorMsg = document.getElementById("errorMsg");

/* Admin temporaire */
const ADMIN_USER = "admin";
const ADMIN_PASS = "1234";

form.onsubmit = function (e) {
  e.preventDefault();

  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;

  if (user === ADMIN_USER && pass === ADMIN_PASS) {
    localStorage.setItem("role", "admin");
    window.location.href = "/admin_dashboard/";  // <-- URL Django
  } else {
    errorMsg.textContent = "Access denied!";
  }
};

// Vérification d'accès
if (localStorage.getItem("role") !== "admin") {
  window.location.href = "/";  // <-- retourne à login
}
