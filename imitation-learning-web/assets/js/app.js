/**
 * ============================================================================
 * ELEMENTS OF ROBOTICS - INTERACTIVE KNOWLEDGE WEB APP LOGIC
 * Theme, ScrollSpy, Reading Progress, Matrix Search & Filter, Copy Code
 * Multi-Page & Portal Hub Support
 * ============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initScrollSpyAndProgress();
  initCopyCodeButtons();
  initCurriculumMatrix();
});

// ============================================================================
// THEME SWITCHER (DARK / LIGHT MODE)
// ============================================================================
function initTheme() {
  const themeBtn = document.getElementById('theme-btn');
  const themeIcon = document.getElementById('theme-icon');
  const themeText = document.getElementById('theme-text');
  
  const savedTheme = localStorage.getItem('eor-theme') || 
                     (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  
  setTheme(savedTheme);

  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      setTheme(next);
    });
  }

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('eor-theme', theme);
    if (themeIcon && themeText) {
      if (theme === 'dark') {
        themeIcon.textContent = '☀️';
        themeText.textContent = 'Chế độ sáng';
      } else {
        themeIcon.textContent = '🌙';
        themeText.textContent = 'Chế độ tối';
      }
    }
  }
}

// ============================================================================
// READING PROGRESS BAR & SCROLLSPY
// ============================================================================
function initScrollSpyAndProgress() {
  const progressBar = document.getElementById('reading-progress');
  const navLinks = document.querySelectorAll('#sidebar-nav .nav-item');
  const sections = document.querySelectorAll('[id^="sec-"], [id^="sim-"], [id^="ch-"], section[id], article[id], h4[id]');

  function updateScrollSpy() {
    // 1. Reading Progress
    const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
    if (progressBar) {
      progressBar.style.width = scrolled + '%';
    }

    // 2. ScrollSpy Active Highlight
    if (sections.length > 0 && navLinks.length > 0) {
      let currentId = '';
      sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 140) {
          currentId = section.getAttribute('id');
        }
      });

      // Default to first section when near top of page
      if (!currentId && sections.length > 0 && winScroll < 300) {
        currentId = sections[0].getAttribute('id');
      }

      if (currentId) {
        navLinks.forEach(item => {
          item.classList.remove('active');
          const link = item.querySelector('a');
          if (link) {
            const href = link.getAttribute('href');
            if (href === '#' + currentId || href.endsWith('#' + currentId)) {
              item.classList.add('active');
            }
          }
        });
      }
    }
  }

  window.addEventListener('scroll', updateScrollSpy, { passive: true });
  // Call once on init to set active state immediately
  updateScrollSpy();
}

// ============================================================================
// CURRICULUM MATRIX LIVE SEARCH & TRACK FILTER (FOR PORTAL HUB)
// ============================================================================
function initCurriculumMatrix() {
  const searchInput = document.getElementById('matrix-search-input');
  const filterPills = document.querySelectorAll('.filter-pill');
  const cards = document.querySelectorAll('.matrix-card');

  if (!cards || cards.length === 0) return;

  let activeTrack = 'all';
  let searchTerm = '';

  function applyFilters() {
    cards.forEach(card => {
      const cardTrack = card.getAttribute('data-track');
      const cardText = (card.innerText || '').toLowerCase();

      const matchesTrack = (activeTrack === 'all' || cardTrack === activeTrack);
      const matchesSearch = searchTerm === '' || cardText.includes(searchTerm);

      if (matchesTrack && matchesSearch) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchTerm = e.target.value.trim().toLowerCase();
      applyFilters();
    });
  }

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeTrack = pill.getAttribute('data-filter') || 'all';
      applyFilters();
    });
  });

  // Smooth pulse for internal links
  cards.forEach(card => {
    card.addEventListener('click', (e) => {
      const targetId = card.getAttribute('href');
      if (targetId && targetId.startsWith('#')) {
        const targetEl = document.querySelector(targetId);
        if (targetEl) {
          e.preventDefault();
          targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
          targetEl.classList.add('highlight-pulse');
          setTimeout(() => targetEl.classList.remove('highlight-pulse'), 2500);
        }
      }
    });
  });
}

// ============================================================================
// COPY TO CLIPBOARD HELPER
// ============================================================================
function initCopyCodeButtons() {
  window.copyCode = function(btn) {
    const card = btn.closest('.code-card');
    if (!card) return;
    const codeBlock = card.querySelector('pre code');
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
