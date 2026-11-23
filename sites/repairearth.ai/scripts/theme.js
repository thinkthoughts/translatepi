(() => {
  'use strict';
  const root = document.documentElement;
  const button = document.getElementById('theme-toggle');
  if (!button) return;
  function syncButton() {
    const dark = root.dataset.theme === 'dark';
    button.setAttribute('aria-pressed', String(dark));
    button.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    button.textContent = dark ? '☼ Light' : '◐ Dark';
  }
  syncButton();
  button.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('earthrepair-theme', next); } catch (e) { /* optional */ }
    syncButton();
  });
})();
