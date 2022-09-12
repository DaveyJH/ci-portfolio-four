const benefitsInputRef = document.querySelector("label[for='id_benefits']");
const benefitsPromptSpan = document.createElement("span");
benefitsPromptSpan.classList.add("form-new-line-span");
benefitsPromptSpan.textContent = "Provide a comma separated list...";
benefitsInputRef.append(benefitsPromptSpan);