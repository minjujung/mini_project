const homeBtn = document.querySelector(".homeBtn")

const goToHome = () => {
    window.location.href="/"
}

homeBtn.addEventListener('click', goToHome)