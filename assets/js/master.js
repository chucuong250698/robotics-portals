/**
 * MASTER PORTAL GATEWAY JS LOGIC (2026 SOTA)
 * Theme Switcher, Search with Ctrl+K, Track Filters
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMasterSearchAndFilter();
});

function initTheme() {
  const toggleBtn = document.getElementById('theme-toggle');
  const savedTheme = localStorage.getItem('master-portal-theme') || 'light';
  setTheme(savedTheme);

  if (toggleBtn) {
    toggleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      setTheme(next);
    });
  }

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('master-portal-theme', theme);
  }
}

function initMasterSearchAndFilter() {
  const searchInput = document.getElementById('master-search-input');
  const filterPills = document.querySelectorAll('.filter-pill');
  const cards = document.querySelectorAll('.portal-master-card');

  let activeFilter = 'all';
  let searchTerm = '';

  function applyFilters() {
    cards.forEach(card => {
      const cardCategory = card.getAttribute('data-category') || '';
      const cardKeywords = (card.getAttribute('data-keywords') || '').toLowerCase();
      const cardText = (card.innerText || '').toLowerCase();

      const matchesFilter = (activeFilter === 'all' || cardCategory.includes(activeFilter));
      const matchesSearch = searchTerm === '' || cardKeywords.includes(searchTerm) || cardText.includes(searchTerm);

      if (matchesFilter && matchesSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchTerm = e.target.value.trim().toLowerCase();
      applyFilters();
    });

    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        searchInput.focus();
        searchInput.select();
      }
    });
  }

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeFilter = pill.getAttribute('data-filter') || 'all';
      applyFilters();
    });
  });
}
