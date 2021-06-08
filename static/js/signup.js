const homeBtn = document.querySelector(".homeBtn");


const goToHome = () => {
    window.location.href="/"
}

homeBtn.addEventListener('click', goToHome)

const inputId = document.getElementById("input-username")
const inputPW1 = document.getElementById("input-password1")
const inputPW2 = document.getElementById("input-password2")
const inputNick = document.getElementById("input-nickname")
const signUpBtn = document.querySelector(".sign_up_btn")

const signUpBox = document.getElementById("sign-up-box")
const divSignInOrUp = document.getElementById("div-sign-in-or-up")
const btnCheckDup = document.getElementById("btn-check-dup")
const helpId = document.getElementById("help-id")
const helpPassword = document.getElementById("help-password")
const helpPassword2 = document.getElementById("help-password2")

const signUp = document.querySelector(".sign_up")
const checkDup = document.querySelector(".check_dup")

const is_nickname = (asValue) => {
    var regExp = /^(?=.*[a-zA-Z])[-a-zA-Z0-9_.]{2,10}$/;
    return regExp.test(asValue);
}

function checkDupClick() {
    
    let username =inputId.value

    if (username == "") {
        helpId.innerText = "아이디를 입력해주세요."
        helpId.classList.remove("is-safe")
        helpId.classList.add("is-danger")
        inputId.focus()
        return;
    } else {
        if (!is_nickname(username)) {
            helpId.innerText = "아이디의 형식을 확인해주세요. 영문과 숫자, 일부 특수문자(._-) 사용 가능. 2-10자 길이"
            helpId.classList.remove("is-safe")
            helpId.classList.add("is-danger")
            inputId.focus()
            return;
        }
    }
    helpId.classList.add("is-loading")
    $.ajax({
        type: "POST",
        url: "/sign_up/check_dup",
        data: {
            username_give: username
        },
        success: function (response) {

            if (response["exists"]) {
                helpId.innerText = "이미 존재하는 아이디입니다."
                helpId.classList.remove("is-safe")
                helpId.classList.add("is-danger")
                inputId.focus()
            } else {
                helpId.innerText = "사용할 수 있는 아이디입니다."
                helpId.classList.remove("is-danger")
                helpId.classList.add("is-success")
            }
            helpId.classList.remove("is-loading")

        }
    });
}

const signUpClick = () => {
    let username = inputId.value
    let password = inputPW1.value
    let password2 = inputPW2.value
    let nickname = inputNick.value

    const is_password = (asValue) => {
        var regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;
        return regExp.test(asValue);
    }
    // if (helpId.classList.contains("is-danger")) {
    //     alert("아이디를 다시 확인해주세요.")
    //     return;
    // } else if (!helpId.classList.contains("is-success")) {
    //     alert("아이디 중복확인을 해주세요.")
    //     return;
    // }

    // if (password == "") {
    //     helpPassword.innerText("비밀번호를 입력해주세요.").classList.remove("is-safe").classList.add("is-danger")
    //     inputPW1.focus()
    //     return;
    // } else if (!is_password(password)) {
    //     $("#help-password").text("비밀번호의 형식을 확인해주세요. 영문과 숫자 필수 포함, 특수문자(!@#$%^&*) 사용가능 8-20자").removeClass("is-safe").addClass("is-danger")
    //     $("#input-password").focus()
    //     return
    // } else {
    //     $("#help-password").text("사용할 수 있는 비밀번호입니다.").removeClass("is-danger").addClass("is-success")
    // }
    // if (password2 == "") {
    //     $("#help-password2").text("비밀번호를 입력해주세요.").removeClass("is-safe").addClass("is-danger")
    //     $("#input-password2").focus()
    //     return;
    // } else if (password2 != password) {
    //     $("#help-password2").text("비밀번호가 일치하지 않습니다.").removeClass("is-safe").addClass("is-danger")
    //     $("#input-password2").focus()
    //     return;
    // } else {
    //     $("#help-password2").text("비밀번호가 일치합니다.").removeClass("is-danger").addClass("is-success")
    // }
    $.ajax({
        type: "POST",
        url: "/sign_up/save",
        data: {
            username_give: username,
            password_give: password,
            nickname_give: nickname
        },
        success: function (response) {
            alert("회원가입을 축하드립니다!")
            window.location.replace("/login")
        }
    });

}

signUp.addEventListener('click', signUpClick)
checkDup.addEventListener('click', checkDupClick)