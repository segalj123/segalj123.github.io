document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.light-card');
    const user_id = 1;  // Temporary user ID for demonstration purposes

    cards.forEach(card => {
        card.querySelector('.like-btn').addEventListener('click', () => handleSwipe(card, 'like'));
        card.querySelector('.dislike-btn').addEventListener('click', () => handleSwipe(card, 'dislike'));
    });

    function handleSwipe(card, action) {
        const light_id = card.getAttribute('data-id');
        fetch('/swipe_action', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id: user_id, light_id: light_id, action: action })
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'success') {
                  card.style.display = 'none';
              }
          });
    }
});
