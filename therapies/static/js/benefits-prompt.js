const benefitsInputRef = document.querySelector("label[for='id_benefits']");
const benefitsPromptPara = document.createElement("p");
benefitsPromptPara.textContent = "Provide a comma separated list...";
benefitsInputRef.append(benefitsPromptPara);