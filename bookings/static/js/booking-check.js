// hide info boxes if no booking info object message is present
const messageRef = document.getElementById("booking-info");
const contactRef = document.getElementById("contact-info");
const openTimesRef = document.getElementById("open-times-info");
if (!messageRef.innerText) {
  messageRef.style.visibility = "hidden";
  openTimesRef.style.visibility = "hidden";
  contactRef.style.visibility = "hidden";
}
