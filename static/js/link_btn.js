// ----------회원가입 버튼----------------------
const signupBtn = document.querySelector(".signupBtn");

const goToSignup = () => {
  window.location.href = "/sign_up";
};

signupBtn?.addEventListener("click", goToSignup);

//------------------------------------------------

// ----------식단일기 작성 버튼----------------------
const diaryBtn = document.querySelector('.diaryBtn')

const goToDiary = () => {
  window.location.href = "/write";
};

diaryBtn?.addEventListener("click", goToDiary);
//--------------------------------------------------

// ----------로그인 버튼-------------------------------
const loginBtn = document.querySelector('.loginBtn')

const goToLogin = () => {
  window.location.href = "/login";
};

loginBtn?.addEventListener("click", goToLogin);
//------------------------------------------------------


// ----------로그아웃 버튼-----------------------------
const logoutBtn = document.querySelector(".logoutBtn")

const signout = () => {
  $.removeCookie('mytoken', {path: '/'});
  alert('로그아웃!')
  window.location.href = "/"
}

logoutBtn?.addEventListener('click', signout)
//----------------------------------------------------