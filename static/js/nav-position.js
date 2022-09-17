const navAdjustRef = document.getElementById("nav-adjust-div");
const navToggleBtn = document.getElementById("nav-toggler");
navToggleBtn.addEventListener("click", () => {
  const collapsed = navToggleBtn.classList.contains("collapsed");
  navAdjustRef.classList.toggle(
    "flex-nowrap", collapsed ? true : false);
});