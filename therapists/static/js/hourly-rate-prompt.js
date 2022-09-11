const hourlyInputRef = document.querySelector("label[for='id_hourly_rate']");
const hourlyPromptPara = document.createElement("p");
hourlyPromptPara.textContent = "Whole numbers only - max: 100...";
hourlyInputRef.append(hourlyPromptPara);