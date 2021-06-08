const homeBtn = document.querySelector(".homeBtn");


const goToHome = () => {
    window.location.href="/"
}

homeBtn.addEventListener('click', goToHome)

const inputId = document.getElementById("input-username")
const inputPW1 = document.getElementById("input-password1")
const inputPW2 = document.getElementById("input-password2")
const signUpBtn = document.querySelector(".sign_up_btn")

const signUpBox = document.getElementById("sign-up-box")
const divSignInOrUp = document.getElementById("div-sign-in-or-up")
const btnCheckDup = document.getElementById("btn-check-dup")
const helpId = document.getElementById("help-id")
const helpPassword = document.getElementById("help-password")
const helpPassword2 = document.getElementById("help-password2")
const cancelBtn = document.querySelector(".cancel")

const signUpToggle = () => {
    inputId.value = "";
    inputPW1.value = "";
    signUpBox.classList.toggle("is-hidden")
    divSignInOrUp.classList.toggle("is-hidden")
    btnCheckDup.classList.toggle("is-hidden")
    helpId.classList.toggle("is-hidden")
    helpPassword.classList.toggle("is-hidden")
    helpPassword2.classList.toggle("is-hidden")
}

const signIn = document.querySelector(".sign_in");

const signInClick = () => {
    let username = inputId.value
    let password = inputPW1.value

    // if (username == "") {
    //     $("#help-id-login").text("아이디를 입력해주세요.")
    //     $("#input-username").focus()
    //     return;
    // } else {
    //     $("#help-id-login").text("")
    // }

    // if (password == "") {
    //     $("#help-password-login").text("비밀번호를 입력해주세요.")
    //     $("#input-password").focus()
    //     return;
    // } else {
    //     $("#help-password-login").text("")
    // }
    $.ajax({
        type: "POST",
        url: "/sign_in",
        data: {
            username_give: username,
            password_give: password
        },
        success: function (response) {
            if (response['result'] == 'success') {
                $.cookie('mytoken', response['token'], {path: '/'});
                window.location.replace("/")
            } else {
                alert(response['msg'])
            }
        }
    });
}

const signUp = document.querySelector(".sign_up")

const signUpClick = () => {
    let password = inputPW1.value;
    
    if (helpId.classList.contains("is-danger")) {
        alert("아이디를 다시 확인해주세요.")
        return;
    } else if (!helpId.classList.contains("is-success")) {
        alert("아이디 중복확인을 해주세요.")
        return;
    }

    if (password == "") {
        helpPassword.innerText("비밀번호를 입력해주세요.").classList.remove("is-safe").classList.add("is-danger")
        inputPW1.focus()
        return;
    } else if (!is_password(password)) {
        $("#help-password").text("비밀번호의 형식을 확인해주세요. 영문과 숫자 필수 포함, 특수문자(!@#$%^&*) 사용가능 8-20자").removeClass("is-safe").addClass("is-danger")
        $("#input-password").focus()
        return
    } else {
        $("#help-password").text("사용할 수 있는 비밀번호입니다.").removeClass("is-danger").addClass("is-success")
    }
    if (password2 == "") {
        $("#help-password2").text("비밀번호를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        $("#input-password2").focus()
        return;
    } else if (password2 != password) {
        $("#help-password2").text("비밀번호가 일치하지 않습니다.").removeClass("is-safe").addClass("is-danger")
        $("#input-password2").focus()
        return;
    } else {
        $("#help-password2").text("비밀번호가 일치합니다.").removeClass("is-danger").addClass("is-success")
    }
    $.ajax({
        type: "POST",
        url: "/sign_up/save",
        data: {
            username_give: inputId.value,
            password_give: inputPW1.value
        },
        success: function (response) {
            alert("회원가입을 축하드립니다!")
            window.location.replace("/login")
        }
    });

}


signUpBtn.addEventListener('click', signUpToggle)
cancelBtn.addEventListener('click', signUpToggle)
signUp.addEventListener('click', signUpClick)
signIn.addEventListener('click', signInClick)