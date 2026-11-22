/**
 * ============================================================================
 * STATE ESTIMATION FOR ROBOTICS - INTERACTIVE KNOWLEDGE WEB APP LOGIC
 * Theme, ScrollSpy, Reading Progress, Matrix Search & Filter, Copy Code
 * ============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initScrollSpyAndProgress();
  initCopyCodeButtons();
  initCurriculumMatrix();
});

// ============================================================================
// THEME SWITCHER (DARK BY DEFAULT FOR ROBOTICS THEME)
// ============================================================================
function initTheme() {
  const toggleBtns = document.querySelectorAll('#theme-toggle, #theme-btn, .btn-theme-toggle');
  
  // Default to light theme for clean readability, or respect saved theme
  const savedTheme = localStorage.getItem('ser-theme') || 'light';
  setTheme(savedTheme);

  toggleBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      setTheme(next);
    });
  });

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('ser-theme', theme);
  }
}

// ============================================================================
// READING PROGRESS BAR & SCROLLSPY
// ============================================================================
function initScrollSpyAndProgress() {
  const progressBar = document.getElementById('reading-progress');
  const navLinks = document.querySelectorAll('.sidebar-links a, #sidebar-nav .nav-item, .sidebar-nav a');
  const sections = document.querySelectorAll('section[id], [id^="sec-"], [id^="sim-"]');

  function updateScrollSpy() {
    // 1. Reading Progress
    const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
    if (progressBar) {
      progressBar.style.width = Math.min(100, Math.max(0, scrolled)) + '%';
    }

    // 2. ScrollSpy Active Highlight
    if (sections.length > 0 && navLinks.length > 0) {
      let currentId = '';
      sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 160) {
          currentId = section.getAttribute('id');
        }
      });

      if (!currentId && sections.length > 0 && winScroll < 300) {
        currentId = sections[0].getAttribute('id');
      }

      if (currentId) {
        navLinks.forEach(link => {
          const href = link.getAttribute('href');
          if (href === '#' + currentId || href.endsWith('#' + currentId)) {
            link.classList.add('active');
            const parent = link.closest('li');
            if (parent) parent.classList.add('active');
          } else {
            link.classList.remove('active');
            const parent = link.closest('li');
            if (parent) parent.classList.remove('active');
          }
        });
      }
    }
  }

  window.addEventListener('scroll', updateScrollSpy, { passive: true });
  updateScrollSpy();
}

// ============================================================================
// CURRICULUM LIVE SEARCH & TRACK FILTER (FOR PORTAL HUB)
// ============================================================================
function initCurriculumMatrix() {
  const searchInput = document.getElementById('matrix-search-input') || document.getElementById('chapter-search');
  const filterPills = document.querySelectorAll('.filter-pill');
  const cards = document.querySelectorAll('.matrix-card, .chapter-card');

  if (!cards || cards.length === 0) return;

  let activeTrack = 'all';
  let searchTerm = '';

  function applyFilters() {
    cards.forEach(card => {
      const cardTrack = card.getAttribute('data-track') || card.getAttribute('data-filter') || '';
      const cardTags = card.getAttribute('data-tags') || '';
      const cardText = ((card.innerText || '') + ' ' + cardTags).toLowerCase();

      const matchesTrack = (activeTrack === 'all' || cardTrack === activeTrack);
      const matchesSearch = searchTerm === '' || cardText.includes(searchTerm);

      if (matchesTrack && matchesSearch) {
        card.classList.remove('hidden');
        card.style.display = 'flex';
      } else {
        card.classList.add('hidden');
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
      activeTrack = pill.getAttribute('data-filter') || pill.getAttribute('data-track') || 'all';
      applyFilters();
    });
  });
}

// ============================================================================
// COPY TO CLIPBOARD HELPER
// ============================================================================
function initCopyCodeButtons() {
  window.copyCode = function(btn) {
    const card = btn.closest('.code-card, pre');
    if (!card) return;
    const codeBlock = card.querySelector('code') || card;
    if (codeBlock) {
      navigator.clipboard.writeText(codeBlock.innerText).then(() => {
        const origText = btn.textContent;
        btn.textContent = '✓ Đã sao chép!';
        btn.style.color = '#34d399';
        setTimeout(() => {
          btn.textContent = origText;
          btn.style.color = '';
        }, 2000);
      });
    }
  };
}
