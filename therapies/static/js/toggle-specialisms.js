const therapistsDivRef = document.querySelector("#div_id_therapists");
const specialismDivRef = document.querySelector("#div_id_specialism");
const therapistRefs = therapistsDivRef.querySelectorAll(
  "input[type=checkbox]");
const specialismTherapistDivRefs = specialismDivRef.querySelectorAll(
  ".form-check");
// hide specialisms
specialismTherapistDivRefs.forEach(
  elem => elem.classList.add("visually-hidden")
);
// show relevant specialism option when therapist is selected.
therapistRefs.forEach(elem => elem.addEventListener("click", (e) => {
  const value = e.target.value;
  specialismTherapistDivRefs.forEach(div => {
    if (div.querySelector("input").value === value) {
      div.classList.toggle(
        "visually-hidden",
        e.target.checked ? false : true
      );
      // uncheck specialism if therapist is unchecked
      if (div.classList.contains("visually-hidden")) {
        div.querySelector("input").checked = false;
      }
    }
  });
}));