const navSlide = () => {
    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    //Toggle Nav
    hamburger.addEventListener('click',() => {
        nav.classList.toggle('nav-active');

        //Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation){
                link.style.animation='';
            }else{
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`
            }
        }); 
        //hamburger animation
        hamburger.classList.toggle('toggle');           
    });
}

function deletePost(postId){
    fetch("/delete-post", {
        method: "POST",
        body: JSON.stringify({ postId: postId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}

const app = ()=>{
    navSlide();
}
app();
