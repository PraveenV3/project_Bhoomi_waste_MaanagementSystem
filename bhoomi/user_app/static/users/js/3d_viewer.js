document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".item");
  let angle = 0;

  // Function to apply wave animation
  function animateWave() {
    items.forEach((item, index) => {
      const offset = Math.sin((angle + index * 15) * (Math.PI / 180)) * 50; // Calculate wave offset
      item.style.transform = `rotateY(calc(var(--index, ${index}) * 15deg)) translateZ(${200 + offset}px)`;
    });
    angle += 2; // Increment angle for continuous animation
    requestAnimationFrame(animateWave); // Loop the animation
  }

  // Start the wave animation
  animateWave();
});