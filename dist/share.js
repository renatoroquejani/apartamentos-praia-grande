(() => {
  const button = document.querySelector('[data-copy-link]');
  if (!button) return;

  const status = document.querySelector('[data-copy-status]');
  const fallback = document.querySelector('[data-share-url]');
  const url = new URL(window.location.href);
  url.hash = '';
  url.search = '';
  fallback.value = url.href;
  button.hidden = false;

  button.addEventListener('click', async () => {
    button.disabled = true;
    status.textContent = '';
    fallback.hidden = true;
    try {
      await navigator.clipboard.writeText(url.href);
      status.textContent = 'Link copiado!';
    } catch {
      fallback.hidden = false;
      fallback.focus();
      fallback.select();
      status.textContent = 'Selecione e copie o link abaixo.';
    } finally {
      button.disabled = false;
    }
  });
})();
