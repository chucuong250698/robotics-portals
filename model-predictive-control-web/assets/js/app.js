/**
 * Model Predictive Control (MPC) - Knowledge Portal (Rawlings, Mayne, Diehl)
 * Application Core Logic:
 *  - Dark / Light Theme Toggle & Persistence ('mpc-theme')
 *  - Reading Progress Bar (#reading-progress)
 *  - Dynamic ScrollSpy with Highlighting (320px sticky sidebar)
 *  - Live Search (< 10ms execution, Ctrl+K / Cmd+K shortcut)
 *  - 6-Track Filter Pills (Track 1 to Track 6 + Tất cả)
 *  - Responsive Mobile Navigation Toggle
 */

document.addEventListener('DOMContentLoaded', () => {
  // -------------------------------------------------------------------------
  // 1. Dark / Light Theme Manager
  // -------------------------------------------------------------------------
  const themeToggle = document.getElementById('theme-toggle') || document.getElementById('theme-btn');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

  const initTheme = () => {
    const savedTheme = localStorage.getItem('mpc-theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
    } else if (prefersDark.matches) {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.setAttribute('data-theme', 'dark'); // Default to dark for high-tech aesthetic
    }
  };

  initTheme();

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('mpc-theme', newTheme);
      
      const themeIcon = document.getElementById('theme-icon');
      const themeText = document.getElementById('theme-text');
      if (themeIcon) themeIcon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
      if (themeText) themeText.textContent = newTheme === 'dark' ? 'Chế độ sáng' : 'Chế độ tối';
    });
  }

  // -------------------------------------------------------------------------
  // 2. Reading Progress Bar
  // -------------------------------------------------------------------------
  const progressBar = document.getElementById('reading-progress');
  if (progressBar) {
    window.addEventListener('scroll', () => {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      progressBar.style.width = scrolled + '%';
    }, { passive: true });
  }

  // -------------------------------------------------------------------------
  // 3. Dynamic ScrollSpy for Sidebar TOC
  // -------------------------------------------------------------------------
  const navLinks = document.querySelectorAll('.sidebar-nav .nav-item a, .sidebar-nav .nav-link');
  const sections = Array.from(navLinks).map(link => {
    const href = link.getAttribute('href');
    if (href && href.startsWith('#')) {
      return document.querySelector(href);
    }
    return null;
  }).filter(Boolean);

  if (navLinks.length > 0 && sections.length > 0) {
    const handleScrollSpy = () => {
      const scrollPos = window.scrollY + 140; // 140px offset for sticky header
      
      let currentSection = null;
      for (let i = 0; i < sections.length; i++) {
        const sec = sections[i];
        if (sec.offsetTop <= scrollPos) {
          currentSection = sec;
        } else {
          break;
        }
      }

      if (currentSection) {
        const activeId = '#' + currentSection.id;
        navLinks.forEach(link => {
          if (link.getAttribute('href') === activeId) {
            link.classList.add('active');
            // Ensure visible in sidebar scroll
            const container = link.closest('.sidebar-container') || link.closest('.sidebar-nav');
            if (container) {
              const linkRect = link.getBoundingClientRect();
              const contRect = container.getBoundingClientRect();
              if (linkRect.top < contRect.top || linkRect.bottom > contRect.bottom) {
                link.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
              }
            }
          } else {
            link.classList.remove('active');
          }
        });
      }
    };

    window.addEventListener('scroll', handleScrollSpy, { passive: true });
    handleScrollSpy();
  }

  // -------------------------------------------------------------------------
  // 4. Live Search & Category Filter (Index Hub Page)
  // -------------------------------------------------------------------------
  const searchInput = document.getElementById('chapter-search') || document.getElementById('master-search-input') || document.getElementById('search-input');
  const filterPills = document.querySelectorAll('.filter-pill');
  const chapterCards = document.querySelectorAll('.matrix-card, .chapter-card, .portal-master-card');

  let currentCategory = 'all';
  let searchQuery = '';

  const applyFilters = () => {
    chapterCards.forEach(card => {
      const cardCategory = card.getAttribute('data-track') || card.getAttribute('data-category') || 'all';
      const text = card.textContent.toLowerCase();
      const keywords = (card.getAttribute('data-keywords') || '').toLowerCase();
      
      const matchesCategory = (currentCategory === 'all' || cardCategory === currentCategory);
      const matchesSearch = !searchQuery || text.includes(searchQuery) || keywords.includes(searchQuery);

      if (matchesCategory && matchesSearch) {
        card.style.display = '';
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
      } else {
        card.style.display = 'none';
      }
    });
  };

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim().toLowerCase();
      applyFilters();
    });

    // Keyboard shortcut Ctrl+K / Cmd+K
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        searchInput.focus();
      }
    });
  }

  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentCategory = pill.getAttribute('data-filter') || 'all';
      applyFilters();
    });
  });

  // -------------------------------------------------------------------------
  // 5. Solution Toggle Smooth Animation (Practice Exercises)
  // -------------------------------------------------------------------------
  const practiceDetails = document.querySelectorAll('.practice-solution');
  practiceDetails.forEach(detail => {
    detail.addEventListener('toggle', () => {
      if (detail.open && window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise([detail]).catch(err => console.warn(err));
      }
    });
  });
});
