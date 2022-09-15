const editIcon = "fa-pen";
const deleteUserIcon = "fa-user-large-slash";
const deleteSpaIcon = "fa-spray-can-sparkles";
const userIcon = "fa-user";
const spaIcon = "fa-spa";
const editListRef = document.querySelector("#edit-list-toggle");
const deleteListRef = document.querySelector("#delete-list-toggle");

const toggleBullet = (item, addIcon, removeIcon) => {
  item.querySelector("i").classList.toggle(addIcon, true);
  item.querySelector("i").classList.toggle(removeIcon, false);
};

editListRef.addEventListener("click", () => {
  const editItemRefs = editListRef.nextElementSibling.
    querySelectorAll("li");
  if (editItemRefs[0].dataset.type !== "question") {
    const type = editItemRefs[0].dataset.type;
    let originIcon = "fa-wrench"; // should never show, easy error identifier
    switch (type) {
      case "spa":
        originIcon = spaIcon;
        break;
      case "user":
        originIcon = userIcon;
        break;
    }
    editItemRefs.forEach(item => item.querySelector("a").
      addEventListener("mouseenter", () => {
        toggleBullet(item, editIcon, originIcon);
    }));
    editItemRefs.forEach(item => item.querySelector("a").
      addEventListener("mouseleave", () => {
        toggleBullet(item, originIcon, editIcon);
    }));
  }
});

deleteListRef.addEventListener("click", () => {
  const deleteItemRefs = deleteListRef.nextElementSibling.
    querySelectorAll("li");
  if (deleteItemRefs[0].dataset.type !== "question") {
    const type = deleteItemRefs[0].dataset.type;
    let originIcon = "fa-eraser"; // should never show, easy error identifier
    let deleteIcon = "fa-skull"; // should never show, easy error identifier
    switch (type) {
      case "spa":
        originIcon = spaIcon;
        deleteIcon = deleteSpaIcon;
        break;
      case "user":
        originIcon = userIcon;
        deleteIcon = deleteUserIcon;
        break;
    }
    deleteItemRefs.forEach(item => item.querySelector("a").
      addEventListener("mouseenter", () => {
        toggleBullet(item, deleteIcon, originIcon);
    }));
    deleteItemRefs.forEach(item => item.querySelector("a").
      addEventListener("mouseleave", () => {
        toggleBullet(item, originIcon, deleteIcon);
    }));
  }
});