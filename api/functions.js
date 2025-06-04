// functions.js
// TranslatePi.ai — Shared Utility Functions

// DARK MODE TOGGLE
export function initDarkModeToggle() {
  const button = document.createElement('button');
  button.innerText = '🌓';
  button.className = 'dark-toggle';
  button.title = 'Toggle Dark Mode';
  button.onclick = () => {
    document.body.classList.toggle('dark');
    localStorage.setItem('theme', document.body.classList.contains('dark') ? 'dark' : 'light');
  };

  document.body.appendChild(button);

  // Load saved theme
  if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark');
  }
}

// LOAD TRANSLATIONS
export async function loadTranslations(jsonPath = '../api/translations.json') {
  try {
    const res = await fetch(jsonPath);
    if (!res.ok) throw new Error('Failed to load translations');
    const data = await res.json();
    return data.translations || [];
  } catch (error) {
    console.error('Error loading translations:', error);
    return [];
  }
}

// RENDER TRANSLATION TABLE
export function renderTranslations(translations, containerId = 'translation-table') {
  const container = document.getElementById(containerId);
  if (!container || !translations.length) return;

  const table = document.createElement('table');
  table.innerHTML = `
    <thead>
      <tr>
        <th>ID</th>
        <th>Expression</th>
        <th>Meaning</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      ${translations.map(t => `
        <tr>
          <td><code>${t.id}</code></td>
          <td><code>${t.expression}</code></td>
          <td>${t.meaning}</td>
          <td>${t.notes}</td>
        </tr>
      `).join('')}
    </tbody>
  `;

  container.innerHTML = '';
  container.appendChild(table);
}
