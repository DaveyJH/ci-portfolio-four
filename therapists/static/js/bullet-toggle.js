const editIcon = "fa-pen";
const deleteIcon = "fa-user-large-slash";
const userIcon = "fa-user";
const editListRef = document.querySelector("#edit-therapists-list-toggle");
const deleteListRef = document.querySelector("#delete-therapists-list-toggle");

const toggleBullet = (item, addIcon, removeIcon) => {
  item.querySelector("i").classList.toggle(addIcon, true);
  item.querySelector("i").classList.toggle(removeIcon, false);
};

editListRef.addEventListener("click", () => {
  const editItemRefs = editListRef.nextElementSibling.
    querySelectorAll(".therapist-li");
  editItemRefs.forEach(item => item.querySelector("a").
    addEventListener("mouseenter", () => {
      toggleBullet(item, editIcon, userIcon);
  }));
  editItemRefs.forEach(item => item.querySelector("a").
    addEventListener("mouseleave", () => {
      toggleBullet(item, userIcon, editIcon);
  }));
});

deleteListRef.addEventListener("click", () => {
  const deleteItemRefs = deleteListRef.nextElementSibling.
    querySelectorAll(".therapist-li");
  deleteItemRefs.forEach(item => item.querySelector("a").
    addEventListener("mouseenter", () => {
      toggleBullet(item, deleteIcon, userIcon);
  }));
  deleteItemRefs.forEach(item => item.querySelector("a").
    addEventListener("mouseleave", () => {
      toggleBullet(item, userIcon, deleteIcon);
  }));
});