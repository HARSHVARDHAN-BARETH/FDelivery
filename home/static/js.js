const hamburger = document.querySelector(".hamburger")
const close = document.querySelector(".nav-list .close")
const menue = document.querySelector(".nav-list ")

hamburger.addEventListener("click", ()=>{
       menue.classList.add("show")
});

close.addEventListener("click", ()=>{
       menue.classList.remove("show")
});

// <!--=============== SignIn Form ===============-->
// const singin = document.querySelector(".header .sing-in")
const signIn = document.querySelector(".header .wrapper");
document.querySelector(".sing-in").onlcick = ()=>{
    signIn.classList.add("active");
};
document.querySelector(".close-form").onlcick = ()=>{
    signIn.classList.remove("active");
};