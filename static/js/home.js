const signinBtn = document.querySelector(".signinBtn")

const goToLogin = () => {
    window.location.href="/login"
}

signinBtn.addEventListener('click', goToLogin)
