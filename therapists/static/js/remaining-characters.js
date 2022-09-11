const formInputRefs = Array.from(document.querySelectorAll("input, textarea"));
const formElems = formInputRefs.map(
    elem => ({ elem: elem, id: elem.id })
  ).filter(
    ({elem}) => elem.hasAttribute("maxlength")
  );

// add "remaining characters" paragraph below labels
formElems.forEach(({elem, id}) => {
  const max = elem.getAttribute('maxlength');
  const newCharPara = document.createElement("p");
  newCharPara.classList.add("remaining-char-para");
  newCharPara.textContent = ` ${max} characters remaining...`;
  elem.previousElementSibling.append(newCharPara);
});

/**
 * Update remaining characters text and change colour if needed
 * @param {Element} elem form input with maxlength attribute
 */
const updateRemainingChars = elem => {
  const max = elem.getAttribute('maxlength');
  const remaining = max - elem.value.length;
  const charPara = Array.from(elem.previousElementSibling.children).find(
    elem => elem.classList.contains("remaining-char-para")
  );
  if (charPara) charPara.textContent = ` ${remaining} characters remaining...`;
  charPara.classList.toggle("low-char-remain", remaining <= 3 ? true : false);
};

document.addEventListener('input', (e) => {
  formElems.forEach(({elem, id}) => {
    if (e.target.id === id) {
      updateRemainingChars(elem);
    }
  });
});
