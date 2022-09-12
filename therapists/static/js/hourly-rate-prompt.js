const hourlyInputRef = document.querySelector("label[for='id_hourly_rate']");
const hourlyPromptSpan = document.createElement("span");
hourlyPromptSpan.classList.add("form-new-line-span");
hourlyPromptSpan.textContent = "Whole numbers only - max: 100...";
hourlyInputRef.append(hourlyPromptSpan);