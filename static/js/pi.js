// Sidebar toggle
const sidebar = document.querySelector(".sidebar");
const toggle = document.getElementById("toggle");

if (sidebar && toggle) {
  toggle.onclick = () => {
    sidebar.classList.toggle("active");
  };
}

// Dark mode toggle
const darkToggle = document.getElementById("darkToggle");

if (darkToggle) {
  const icon = darkToggle.querySelector("i");
  const text = darkToggle.querySelector(".links-name");

  darkToggle.onclick = (e) => {
    e.preventDefault();
    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {
      icon.classList.replace("bx-moon", "bx-sun");
      text.textContent = "Light Mode";
    } else {
      icon.classList.replace("bx-sun", "bx-moon");
      text.textContent = "Dark Mode";
    }
  };
}
