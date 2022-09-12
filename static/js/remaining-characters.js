const formInputRefs = Array.from(document.querySelectorAll("input, textarea"));
const formElems = formInputRefs.map(
    elem => ({ elem: elem, id: elem.id })
  ).filter(
    ({elem}) => elem.hasAttribute("maxlength")
  );

// add "remaining characters" paragraph below labels
formElems.forEach(({elem, id}) => {
  const max = elem.getAttribute('maxlength');
  const newCharSpan = document.createElement("span");
  newCharSpan.classList.add("remaining-char-span", "form-new-line-span");
  newCharSpan.textContent = ` ${max} characters remaining...`;
  elem.previousElementSibling.append(newCharSpan);
});

/**
 * Update remaining characters text and change colour if needed
 * @param {Element} elem form input with maxlength attribute
 */
const updateRemainingChars = elem => {
  const max = elem.getAttribute('maxlength');
  const remaining = max - elem.value.length;
  const charSpan = Array.from(elem.previousElementSibling.children).find(
    elem => elem.classList.contains("remaining-char-span")
  );
  if (charSpan) charSpan.textContent = ` ${remaining} characters remaining...`;
  charSpan.classList.toggle("bold-red", remaining <= 3 ? true : false);
};

document.addEventListener('input', (e) => {
  formElems.forEach(({elem, id}) => {
    if (e.target.id === id) {
      updateRemainingChars(elem);
    }
  });
});
