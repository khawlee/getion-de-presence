const sidebar = document.querySelector(".sidebar");
const toggle = document.getElementById("toggle");
const darkToggle = document.getElementById("darkToggle");
const icon = darkToggle.querySelector("i");
const text = darkToggle.querySelector(".links-name");

toggle.onclick = () => {
  sidebar.classList.toggle("active");
};

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
const addStudentBtn = document.getElementById("addStudentBtn");
const studentForm = document.getElementById("studentForm");

addStudentBtn.onclick = (e) => {
  e.preventDefault();
  studentForm.style.display = "flex";
};
studentForm.onclick = (e) => {
  if (e.target === studentForm) {
    studentForm.style.display = "none";
  }
};