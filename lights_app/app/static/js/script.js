document.addEventListener('DOMContentLoaded', function () {
    const swiper = new Swiper('.swiper-container', {
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        on: {
            slideChangeTransitionEnd: function () {
                const activeSlide = document.querySelector('.swiper-slide-active');
                const lightId = activeSlide.getAttribute('data-id');
                
                // Send a POST request to add to wishlist
                fetch(`/wishlist/${lightId}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }).then(response => response.json())
                .then(data => {
                    if (data.success) {
                        activeSlide.querySelector('p:last-child').textContent = `Wishlist Count: ${data.wishlist_count}`;
                    }
                });
            }
        }
    });
});
