document.addEventListener('DOMContentLoaded', () => {

    const toggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('nav ul');

    if (toggle) {
        toggle.addEventListener('click', () => {
            navMenu.classList.toggle('open');
        });
    }

});