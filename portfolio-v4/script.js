const header = document.querySelector('.site-header');
const anchors = [...document.querySelectorAll('main section[id]')];
const navLinks = [...document.querySelectorAll('.site-header nav a')];

const setHeaderState = () => {
  header.classList.toggle('scrolled', window.scrollY > 24);
};

const observer = new IntersectionObserver((entries) => {
  const visible = entries
    .filter((entry) => entry.isIntersecting)
    .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
  if (!visible) return;
  navLinks.forEach((link) => {
    link.classList.toggle('active', link.getAttribute('href') === `#${visible.target.id}`);
  });
}, { rootMargin: '-22% 0px -62%', threshold: [0.05, 0.25, 0.5] });

anchors.forEach((section) => observer.observe(section));
setHeaderState();
window.addEventListener('scroll', setHeaderState, { passive: true });
