/* ==============================
   SLIDERS DE PROYECTOS
============================== */
document.addEventListener("DOMContentLoaded", () => {
  const sliders = document.querySelectorAll(".slider");

  sliders.forEach(slider => {
    const slides = slider.querySelectorAll(".slide");
    const prev = slider.querySelector(".prev");
    const next = slider.querySelector(".next");
    let current = 0;

    const showSlide = (index) => {
      slides.forEach((s, i) => {
        s.classList.toggle("active", i === index);
      });
    };

    prev.addEventListener("click", () => {
      current = (current - 1 + slides.length) % slides.length;
      showSlide(current);
    });

    next.addEventListener("click", () => {
      current = (current + 1) % slides.length;
      showSlide(current);
    });

    // Opcional: autoplay
    // setInterval(() => {
    //   current = (current + 1) % slides.length;
    //   showSlide(current);
    // }, 5000);
  });
});