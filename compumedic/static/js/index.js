// Cuando se carga la ventana, ocultar el preloader
window.addEventListener('load', () => {
    const preloader = document.querySelector('.preloader');
    preloader.style.opacity = '0';
    setTimeout(() => {
        preloader.style.display = 'none';
    }, 1000); // Cambia el tiempo según tus necesidades
});