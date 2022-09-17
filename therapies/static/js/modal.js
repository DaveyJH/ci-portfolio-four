// add modal ------------------------------
const addModal = document.getElementById('add-modal');
const addReviewBtn = document.getElementById('add-modal-toggle');

addModal.addEventListener('shown.bs.modal', () => {
  addReviewBtn.focus();
});

// edit modal -----------------------------
const editModal = document.getElementById('edit-modal');
const editReviewBtn = document.querySelectorAll('[id^=edit-modal-toggle-]');

editModal.addEventListener('shown.bs.modal', (e) => {
  e.relatedTarget.focus();
});

// populate edit form with current content and set action
editReviewBtn.forEach(btn => btn.addEventListener("click", (e) => {
  const editForm = editModal.querySelector("form");
  const therapyId = editForm.dataset.therapy;
  const reviewId = e.target.id.match(/edit-modal-toggle-(\d+)/)[1];
  const reviewBody = e.target.parentElement.parentElement;
  // ? if form html is modified, this will need updating. consider classes
  const review = {
    title: reviewBody.querySelector("h4").innerText,
    content: reviewBody.children[1].innerText,
    rating: reviewBody.querySelectorAll(".fa-solid").length,
    therapist: reviewBody.children[3].children[1].innerText,
  };
  editModal.querySelector("#id_title").value = review.title;
  editModal.querySelector("#id_content").value = review.content;
  editModal.querySelector("#id_rating").value = review.rating;
  const therapistSelect = editModal.querySelector("#id_therapist");
  const therapistOptions = Array.from(therapistSelect.options);
  therapistSelect.value = therapistOptions.find(
    opt => opt.innerText === review.therapist
  ).value;
  editForm.setAttribute(
    "action", `/reviews/edit_review/${therapyId}/${reviewId}/`
  );
}));

// delete modal ---------------------------
const deleteModal = document.getElementById('delete-modal');
const deleteReviewBtn = document.querySelectorAll('[id^=delete-modal-toggle-]');

deleteModal.addEventListener('shown.bs.modal', (e) => {
  e.relatedTarget.focus();
});

// sets the form action to delete the relevant review
deleteReviewBtn.forEach(btn => btn.addEventListener("click", (e) => {
  const deleteForm = deleteModal.querySelector("form");
  const therapyId = deleteForm.dataset.therapy;
  const reviewId = e.target.id.match(/delete-modal-toggle-(\d+)/)[1];
  deleteForm.setAttribute(
    "action", `/reviews/delete_review/${therapyId}/${reviewId}/`
  );
}));
