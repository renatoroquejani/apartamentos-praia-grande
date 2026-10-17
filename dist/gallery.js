(() => {
  const dialog = document.querySelector('#photo-viewer');
  if (!dialog || typeof dialog.showModal !== 'function') return;

  const links = [...document.querySelectorAll('[data-photo]')];
  const photo = dialog.querySelector('.viewer-photo');
  const caption = dialog.querySelector('.viewer-caption');
  const counter = dialog.querySelector('.viewer-counter');
  const original = dialog.querySelector('.viewer-original');
  const status = dialog.querySelector('.viewer-status');
  const closeButton = dialog.querySelector('[data-close]');
  let current = 0;
  let opener;
  let touchStart;

  function showPhoto(index) {
    current = (index + links.length) % links.length;
    const link = links[current];
    photo.src = link.href;
    photo.alt = link.querySelector('img').alt;
    caption.textContent = photo.alt;
    counter.textContent = `${current + 1} / ${links.length}`;
    original.href = link.dataset.original || link.href;
    status.textContent = `Foto ${current + 1} de ${links.length}. ${photo.alt}`;
  }

  for (const [index, link] of links.entries()) {
    link.addEventListener('click', event => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      opener = link;
      touchStart = undefined;
      showPhoto(index);
      dialog.showModal();
      document.documentElement.classList.add('viewer-open');
      closeButton.focus();
    });
  }

  closeButton.addEventListener('click', () => dialog.close());
  dialog.querySelector('[data-prev]').addEventListener('click', () => showPhoto(current - 1));
  dialog.querySelector('[data-next]').addEventListener('click', () => showPhoto(current + 1));
  dialog.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      showPhoto(current + (event.key === 'ArrowLeft' ? -1 : 1));
    }
  });
  dialog.addEventListener('click', event => {
    if (event.target === dialog) dialog.close();
  });
  dialog.addEventListener('close', () => {
    document.documentElement.classList.remove('viewer-open');
    opener?.focus({ preventScroll: true });
  });
  photo.addEventListener('error', () => {
    status.textContent = 'Não foi possível carregar a foto. Tente a próxima ou abra a foto original.';
  });
  photo.addEventListener('touchstart', event => {
    touchStart = event.touches.length === 1
      ? { x: event.touches[0].clientX, y: event.touches[0].clientY }
      : undefined;
  }, { passive: true });
  photo.addEventListener('touchend', event => {
    if (!touchStart || !event.changedTouches.length) return;
    const dx = event.changedTouches[0].clientX - touchStart.x;
    const dy = event.changedTouches[0].clientY - touchStart.y;
    touchStart = undefined;
    if (Math.abs(dx) > 55 && Math.abs(dx) > Math.abs(dy) * 1.5) {
      showPhoto(current + (dx < 0 ? 1 : -1));
    }
  }, { passive: true });
  photo.addEventListener('touchcancel', () => { touchStart = undefined; }, { passive: true });
})();
