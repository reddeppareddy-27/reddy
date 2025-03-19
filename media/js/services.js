
 function toggleServices() {
    const services = document.getElementById('services');
    const isVisible = services.style.display === 'block';

    if (isVisible) {
        services.style.display = 'none';
    } else {
        services.style.display = 'block';
        services.scrollIntoView({ behavior: 'smooth' }); // Scroll to the section smoothly
    }
}