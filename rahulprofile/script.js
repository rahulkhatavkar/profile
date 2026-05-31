const revealElements = document.querySelectorAll('.reveal');

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.15 }
);

revealElements.forEach((el) => observer.observe(el));

const contactButton = document.querySelector('.button');
if (contactButton) {
  contactButton.addEventListener('click', () => {
    contactButton.textContent = 'Sending a message...';
    setTimeout(() => {
      contactButton.textContent = 'Hire Me';
    }, 1000);
  });
}
