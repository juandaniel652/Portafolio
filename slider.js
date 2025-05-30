document.addEventListener('DOMContentLoaded', () => {
  const sliders = document.querySelectorAll('.slider');

  sliders.forEach(slider => {
    let slides = slider.querySelectorAll('.slide');
    let current = 0;

    const showSlide = (index) => {
      slides.forEach((slide, i) => {
        slide.classList.toggle('active', i === index);
      });
    };

    slider.querySelector('.prev').addEventListener('click', () => {
      current = (current - 1 + slides.length) % slides.length;
      showSlide(current);
    });

    slider.querySelector('.next').addEventListener('click', () => {
      current = (current + 1) % slides.length;
      showSlide(current);
    });
  });
});
