const imageInputRef = document.querySelector("label[for='id_image']");
const imagePromptSpan = document.createElement("span");
imagePromptSpan.classList.add("form-new-line-span");
imagePromptSpan.textContent = "Please provide in square aspect ratio...";
imageInputRef.append(imagePromptSpan);