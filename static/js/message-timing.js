const messages = document.querySelectorAll(".message");
messages.forEach(message => {
  setTimeout(() => {
    message.classList.add("visually-hidden");
  }, 2500);
});