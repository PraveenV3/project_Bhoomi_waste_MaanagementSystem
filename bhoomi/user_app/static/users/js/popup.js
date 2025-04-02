function showPopup(popupId) {
    document.getElementById(popupId).style.display = 'flex';
}

function closePopup(popupId) {
    document.getElementById(popupId).style.display = 'none';
}

// Add event listeners to the cards
document.querySelectorAll('.clickable-card').forEach(card => {
    const popupId = card.getAttribute('data-popup-id');
    card.addEventListener('mouseenter', () => showPopup(popupId));
    card.addEventListener('mouseleave', () => closePopup(popupId));
});