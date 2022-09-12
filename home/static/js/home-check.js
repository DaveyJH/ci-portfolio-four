// hide home info boxes if no home object present
const homeRef = document.getElementById("home-info");
const addressRef = document.getElementById("address-info");
if (!homeRef.innerText) {
  homeRef.style.visibility = "hidden";
  addressRef.style.visibility = "hidden";
}
