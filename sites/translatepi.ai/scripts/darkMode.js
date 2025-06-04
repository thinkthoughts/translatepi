function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
  const isDark = document.body.classList.contains('dark-mode');
  localStorage.setItem('translatePiDarkMode', isDark);
}

function addDarkModeButton() {
  const button = document.createElement('button');
  button.textContent = '🌒';
  button.title = 'Toggle Dark Mode';
  button.style.position = 'fixed';
  button.style.top = '1rem';
  button.style.right = '1rem';
  button.style.padding = '0.5rem 0.75rem';
  button.style.fontSize = '1rem';
  button.style.border = 'none';
  button.style.borderRadius = '6px';
  button.style.cursor = 'pointer';
  button.style.zIndex = '999';
  button.style.background = '#444';
  button.style.color = '#fff';
  button.style.boxShadow = '0 2px 6px rgba(0,0,0,0.2)';

  button.addEventListener('click', toggleDarkMode);
  document.body.appendChild(button);
}

// On load
window.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('translatePiDarkMode') === 'true') {
    document.body.classList.add('dark-mode');
  }
  addDarkModeButton();
});
