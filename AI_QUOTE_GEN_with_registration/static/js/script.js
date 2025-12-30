document.addEventListener("DOMContentLoaded", () => {
    const card = document.querySelector(".card");

    // Small interaction effect
    card.addEventListener("mouseenter", () => {
        card.style.transform = "scale(1.02)";
    });

    card.addEventListener("mouseleave", () => {
        card.style.transform = "scale(1)";
    });
});
