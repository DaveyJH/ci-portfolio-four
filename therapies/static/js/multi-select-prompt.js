const multiChoiceDivRefs = document.querySelectorAll(
  "#div_id_body_area, #div_id_therapists, #div_id_specialists"
);
const multiChoiceLabelRefs = Array.from(multiChoiceDivRefs).map(
  div => div.querySelector("label"));
multiChoiceLabelRefs.forEach(label => {
  const multiPromptSpan = document.createElement("span");
  multiPromptSpan.classList.add("form-new-line-span");
  multiPromptSpan.textContent = "Select as many as required...";
  label.appendChild(multiPromptSpan);
});