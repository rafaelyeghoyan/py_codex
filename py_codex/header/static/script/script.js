const menuBar = document.getElementById("menu-bars");
const navBar = document.querySelector(".header-content-navbar");


const openMenu = () => {
    if (navBar.classList[1] === "active") {
        navBar.classList.remove("active");
    } else {
        navBar.classList.add("active");
    }
};

menuBar.addEventListener("click", openMenu);
