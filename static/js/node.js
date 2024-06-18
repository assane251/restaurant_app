document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('.carousel');
    const slides = document.querySelectorAll('.carousel-slide');
    const navbar = document.getElementById('navbar');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');
    let currentIndex = 0;

    function showSlide(index) {
        const offset = -index * 100;
        carousel.style.transform = `translateX(${offset}%)`;
    }

    prevButton.addEventListener('click', function () {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : slides.length - 1;
        showSlide(currentIndex);
    });

    nextButton.addEventListener('click', function () {
        currentIndex = (currentIndex < slides.length - 1) ? currentIndex + 1 : 0;
        showSlide(currentIndex);
    });

    // Initialize the carousel
    showSlide(currentIndex);
});
document.addEventListener('DOMContentLoaded', function () {
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    navLinks.forEach(link => {
        link.addEventListener('mouseover', function () {
            this.style.transform = 'translateY(-2px)'; // Déplacer vers le haut
        });

        link.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)'; // Revenir à la position normale
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const dropdowns = document.querySelectorAll('.navbar-nav .dropdown');

    dropdowns.forEach(dropdown => {
        const dropdownMenu = dropdown.querySelector('.dropdown-menu');

        dropdown.addEventListener('mouseover', function () {
            dropdownMenu.classList.add('show');
        });

        dropdown.addEventListener('mouseleave', function () {
            dropdownMenu.classList.remove('show');
        });

        dropdownMenu.addEventListener('mouseover', function () {
            this.classList.add('show');
        });

        dropdownMenu.addEventListener('mouseleave', function () {
            this.classList.remove('show');
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const carouselImages = document.querySelectorAll('.carousel-slide');

    carouselImages.forEach(function(image) {
        image.addEventListener('mouseenter', function() {
            // Ajouter la classe pour l'animation de zoom
            this.classList.add('zoomed');
        });

        image.addEventListener('mouseleave', function() {
            // Supprimer la classe pour réinitialiser l'image
            this.classList.remove('zoomed');
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const addToCartForms = document.querySelectorAll('.add-to-cart-form');

    addToCartForms.forEach(form => {
        form.addEventListener('submit', async (event) => {
            event.preventDefault();

            const formData = new FormData(form);
            const url = form.action;

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    body: formData
                });

                if (!response.ok) {
                    throw new Error('Erreur lors de l\'ajout au panier');
                }

                const data = await response.json();
                updateCartCount(data.count);
            } catch (error) {
                console.error('Erreur:', error.message);
            }
        });
    });

    function updateCartCount(count) {
        const cartCountElement = document.getElementById('cart-count');
        if (cartCountElement) {
            cartCountElement.textContent = count;
        }
    }
});
