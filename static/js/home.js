const signupBtn = document.querySelector(".signupBtn");

const goToSignup = () => {
  window.location.href = "/sign_up";
};

signupBtn.addEventListener("click", goToSignup);

const diaryBtn = document.querySelector('.diaryBtn')

const goToDiary = () => {
  window.location.href = "/write";
};

diaryBtn.addEventListener("click", goToDiary);


const loginBtn = document.querySelector('.loginBtn')

const goToLogin = () => {
  window.location.href = "/login";
};

loginBtn.addEventListener("click", goToLogin);
