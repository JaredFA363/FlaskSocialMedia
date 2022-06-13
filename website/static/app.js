const navSlide = () => {
    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    //Toggle Nav
    hamburger.addEventListener('click',() => {
        nav.classList.toggle('nav-active');
    });
    //Animate Links
    navLinks.forEach((link, index) => {
        link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 2}s`;
    });
}

const app = ()=>{
    navSlide();
}
app();
