/**
 * Foundations of Robotics - Web Knowledge Portal
 * Application Core Logic:
 *  - Dark / Light Theme Toggle & Persistence
 *  - Reading Progress Bar
 *  - Dynamic ScrollSpy with Smooth Highlighting
 *  - Live Search (< 10ms execution, Ctrl+K / Cmd+K shortcut)
 *  - 4-Track Filter Pills (Track 1 to Track 4 + Tất cả)
 *  - Responsive Mobile Navigation Toggle
 */

document.addEventListener('DOMContentLoaded', () => {
  // -------------------------------------------------------------------------
  // 1. Dark / Light Theme Manager
  // -------------------------------------------------------------------------
  const themeToggle = document.getElementById('theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

  const initTheme = () => {
    const savedTheme = localStorage.getItem('for-theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
    } else if (prefersDark.matches) {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.setAttribute('data-theme', 'light');
    }
  };

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('for-theme', newTheme);
    });
  }

  initTheme();

  // -------------------------------------------------------------------------
  // 2. Reading Progress Bar
  // -------------------------------------------------------------------------
  const progressBar = document.getElementById('reading-progress');
  if (progressBar) {
    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
          const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
          const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
          progressBar.style.width = Math.min(100, Math.max(0, scrolled)) + '%';
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  // -------------------------------------------------------------------------
  // 3. ScrollSpy for Sidebar Navigation
  // -------------------------------------------------------------------------
  const sections = document.querySelectorAll('section[id^="sec-"], section[id^="ch-"], div[id^="sec-"]');
  const navLinks = document.querySelectorAll('.sidebar-link');

  if (sections.length > 0 && navLinks.length > 0) {
    let spyTicking = false;
    const updateActiveSection = () => {
      let currentSecId = '';
      const scrollPos = window.scrollY || window.pageYOffset;

      sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        // Section is considered active if top is near header offset (140px)
        if (rect.top <= 160 && rect.bottom >= 120) {
          currentSecId = section.getAttribute('id');
        }
      });

      if (!currentSecId && scrollPos < 200 && sections.length > 0) {
        currentSecId = sections[0].getAttribute('id');
      }

      if (currentSecId) {
        navLinks.forEach(link => {
          const href = link.getAttribute('href');
          if (href === '#' + currentSecId) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
      spyTicking = false;
    };

    window.addEventListener('scroll', () => {
      if (!spyTicking) {
        window.requestAnimationFrame(updateActiveSection);
        spyTicking = true;
      }
    }, { passive: true });

    updateActiveSection();
  }

  // -------------------------------------------------------------------------
  // 4. Ultra-Fast Live Search (< 10ms execution) & Ctrl+K Shortcut
  // -------------------------------------------------------------------------
  const searchInput = document.getElementById('matrix-search-input') || document.getElementById('chapter-search');
  const cards = document.querySelectorAll('.matrix-card, .chapter-card');

  if (searchInput && cards.length > 0) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      const activeFilterPill = document.querySelector('.filter-pill.active');
      const activeFilter = activeFilterPill ? (activeFilterPill.getAttribute('data-filter') || activeFilterPill.getAttribute('data-track')) : 'all';

      cards.forEach(card => {
        const text = card.textContent.toLowerCase();
        const tags = (card.getAttribute('data-tags') || '').toLowerCase();
        const cardTrack = card.getAttribute('data-track') || card.getAttribute('data-filter') || '';

        const matchesQuery = !q || text.includes(q) || tags.includes(q);
        const matchesFilter = !activeFilter || activeFilter === 'all' || cardTrack.toLowerCase() === activeFilter.toLowerCase();

        if (matchesQuery && matchesFilter) {
          card.classList.remove('hidden');
          card.style.display = '';
        } else {
          card.classList.add('hidden');
          card.style.display = 'none';
        }
      });
    });

    // Keyboard shortcut: Ctrl + K / Cmd + K to focus search
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        searchInput.focus();
        searchInput.select();
      }
    });
  }

  // -------------------------------------------------------------------------
  // 5. 4 Filter Pills (Track 1 to Track 4 + Tất cả)
  // -------------------------------------------------------------------------
  const pills = document.querySelectorAll('.filter-pill');
  if (pills.length > 0 && cards.length > 0) {
    pills.forEach(pill => {
      pill.addEventListener('click', () => {
        pills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');

        const filter = pill.getAttribute('data-filter') || pill.getAttribute('data-track') || 'all';
        const q = searchInput ? searchInput.value.toLowerCase().trim() : '';

        cards.forEach(card => {
          const cardTrack = card.getAttribute('data-track') || card.getAttribute('data-filter') || '';
          const text = card.textContent.toLowerCase();
          const tags = (card.getAttribute('data-tags') || '').toLowerCase();

          const matchesFilter = (filter === 'all') || (cardTrack.toLowerCase() === filter.toLowerCase());
          const matchesQuery = !q || text.includes(q) || tags.includes(q);

          if (matchesFilter && matchesQuery) {
            card.classList.remove('hidden');
            card.style.display = '';
          } else {
            card.classList.add('hidden');
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // -------------------------------------------------------------------------
  // 6. Mobile Sidebar Drawer Toggle
  // -------------------------------------------------------------------------
  const sidebarToggle = document.getElementById('sidebar-toggle');
  const sidebar = document.querySelector('.sidebar');
  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      sidebarToggle.setAttribute('aria-expanded', sidebar.classList.contains('open'));
    });
  }
});
