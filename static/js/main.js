document.addEventListener("DOMContentLoaded", () => {
  const heroText = document.querySelector('.hero-text');
  const hero = document.querySelector('.hero');

  // Fade-in effect on load
  heroText.style.opacity = 0;
  heroText.style.transition = "opacity 1.5s ease-in-out";
  setTimeout(() => {
    heroText.style.opacity = 1;
  }, 300);

  // Parallax effect on scroll
  window.addEventListener("scroll", () => {
    let offset = window.pageYOffset;
    hero.style.backgroundPositionY = offset * 0.5 + "px";
  });
});
