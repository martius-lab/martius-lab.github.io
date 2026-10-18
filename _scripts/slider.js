/*
  auto-advancing image slider, see _includes/slider.html
*/

{
  const onLoad = () => {
    for (const slider of document.querySelectorAll(".slider")) {
      const track = slider.querySelector(".slider-track");
      const count = track.children.length;
      const interval = Number(slider.dataset.interval) || 6000;

      // current slide index, from scroll position
      const current = () => Math.round(track.scrollLeft / track.clientWidth);
      const go = (index) =>
        track.scrollTo({ left: ((index + count) % count) * track.clientWidth });

      slider.querySelector(".slider-prev").onclick = () => go(current() - 1);
      slider.querySelector(".slider-next").onclick = () => go(current() + 1);

      // advance automatically, pause while hovered
      let paused = false;
      slider.onmouseenter = () => (paused = true);
      slider.onmouseleave = () => (paused = false);
      if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches)
        window.setInterval(() => !paused && go(current() + 1), interval);
    }
  };

  // after page loads
  window.addEventListener("load", onLoad);
}
