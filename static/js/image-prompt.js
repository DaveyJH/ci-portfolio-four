const imageInputRef = document.querySelector("label[for='id_image']");
const imagePromptPara = document.createElement("p");
imagePromptPara.textContent = "Please provide in square aspect ratio...";
imageInputRef.append(imagePromptPara);