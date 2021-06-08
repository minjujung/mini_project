const signinBtn = document.querySelector(".signinBtn");

const goToLogin = () => {
  window.location.href = "/sign_up";
};

signinBtn.addEventListener("click", goToLogin);

const diaryBtn = document.querySelector('.diaryBtn')

const goToDiary = () => {
  window.location.href = "/write";
};

diaryBtn.addEventListener("click", goToDiary);
