<<<<<<< HEAD
var slideLeft = {
    distance: '40%',
    opacity: null,
    origin: 'right',
    duration: 5000
};
=======
document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('.carousel');
    const slides = document.querySelectorAll('.carousel-slide');
    const navbar = document.getElementById('navbar');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');
    const cartLink = document.getElementById('cart-link');
   
    let currentIndex = 0;
   
>>>>>>> origin/master

var slideUp = {
    origin: 'top',
    duration: 3000,
    // timer: 1000
}

<<<<<<< HEAD
ScrollReveal().reveal('.carousel-content', slideLeft);
ScrollReveal().reveal('#image-carousel', slideUp);
=======
    function showSlide(index) {
        const offset = -index * 100;
        carousel.style.transform = `translateX(${offset}%)`;
      
    }
>>>>>>> origin/master

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


document.addEventListener('DOMContentLoaded', function () {
    if (window.location.pathname.includes('login')) {
      document.getElementById('navbar').classList.add('navbar-custom');
    }
  });
  setTimeout(() => {
    const flashMessages = document.getElementById("flash-messages");
    if (flashMessages) {
      flashMessages.style.display = "none";
    }
  }, 5000);

  document.addEventListener("DOMContentLoaded", (event) => {
    const flashMessages = document.querySelectorAll("#flash-messages li");
    flashMessages.forEach((msg) => {
      const category = msg.getAttribute("data-category");
      const message = msg.getAttribute("data-message");
      const Toast = Swal.mixin({
        toast: true,
        position: "top-end",
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
          toast.addEventListener("mouseenter", Swal.stopTimer);
          toast.addEventListener("mouseleave", Swal.resumeTimer);
        },
      });

      Toast.fire({
        icon: category,
        title: message,
      });
    });
  });

<<<<<<< HEAD
   // Script pour activer la classe 'active' sur le lien cliqué
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function() {
        document.querySelector('.nav-link.active').classList.remove('active');
        this.classList.add('active');
    });
})
=======

  function zoomIn(element) {
    element.style.boxShadow = '0 0 10px rgba(53, 53, 53, 0.8)'; // Shadow effect on hover with dark color
    element.querySelector('img').style.transform = 'scale(1.1)'; // Zoom in image
}

function zoomOut(element) {
    element.style.boxShadow = ''; // Remove shadow on mouse out
    element.querySelector('img').style.transform = ''; // Reset image zoom
}
>>>>>>> origin/master

document.querySelector('#heart').addEventListener('click', function(event) {
    event.preventDefault();
    this.querySelector('.fa-heart').classList.toggle('red');
<<<<<<< HEAD
});
=======
});

 
>>>>>>> origin/master
