const signinBtn = document.querySelector(".signinBtn");

const goToLogin = () => {
  window.location.href = "/sign_up";
};

signinBtn.addEventListener("click", goToLogin);
