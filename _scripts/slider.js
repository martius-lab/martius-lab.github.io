/*
  auto-advancing slider, see _includes/slider.html
*/

{
  const onLoad = () => {
    for (const slider of document.querySelectorAll(".slider")) {
      const track = slider.querySelector(".slider-track");
      const slides = [...track.children];
      const interval = Number(slider.dataset.interval) || 6000;

      // whether there is anything to scroll
      const update = () =>
        slider.toggleAttribute(
          "data-static",
          track.scrollWidth <= track.clientWidth + 1
        );
      update();
      window.addEventListener("resize", update);

      // index of slide closest to current scroll position
      const current = () => {
        const distances = slides.map((slide) =>
          Math.abs(slide.offsetLeft - track.scrollLeft)
        );
        return distances.indexOf(Math.min(...distances));
      };

      const atEnd = () =>
        track.scrollLeft + track.clientWidth >= track.scrollWidth - 1;

      const go = (index) => {
        index = (index + slides.length) % slides.length;
        track.scrollTo({ left: slides[index].offsetLeft });
      };
      const next = () => (atEnd() ? go(0) : go(current() + 1));
      const prev = () =>
        track.scrollLeft <= 1 ? go(slides.length - 1) : go(current() - 1);

      slider.querySelector(".slider-prev").onclick = prev;
      slider.querySelector(".slider-next").onclick = next;

      // advance automatically, pause while hovered
      let paused = false;
      slider.onmouseenter = () => (paused = true);
      slider.onmouseleave = () => (paused = false);
      if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches)
        window.setInterval(
          () => !paused && !slider.hasAttribute("data-static") && next(),
          interval
        );
    }
  };

  // after page loads
  window.addEventListener("load", onLoad);
}
