const addModal = document.getElementById('add-modal');
const addReviewBtn = document.getElementById('add-modal-toggle');

addModal.addEventListener('shown.bs.modal', () => {
  addReviewBtn.focus();
});