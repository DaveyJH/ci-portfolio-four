const therapistsDivRef = document.querySelector("#div_id_therapists");
const specialistDivRef = document.querySelector("#div_id_specialists");
const therapistRefs = therapistsDivRef.querySelectorAll(
  "input[type=checkbox]");
const specialistTherapistDivRefs = specialistDivRef.querySelectorAll(
  ".form-check");
// hide specialists
specialistTherapistDivRefs.forEach(
  elem => elem.classList.add("visually-hidden")
);
// show relevant specialist option when therapist is selected.
therapistRefs.forEach(elem => elem.addEventListener("click", (e) => {
  const value = e.target.value;
  specialistTherapistDivRefs.forEach(div => {
    if (div.querySelector("input").value === value) {
      div.classList.toggle(
        "visually-hidden",
        e.target.checked ? false : true
      );
      // uncheck specialist if therapist is unchecked
      if (div.classList.contains("visually-hidden")) {
        div.querySelector("input").checked = false;
      }
    }
  });
}));