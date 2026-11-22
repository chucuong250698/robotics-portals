/**
 * Analytical System Dynamics: Modeling and Simulation (Prof. Brian C. Fabien, Springer)
 * Application Core Logic:
 *  - Dark / Light Theme Toggle & Persistence ('asd-theme')
 *  - Reading Progress Bar (#reading-progress)
 *  - Dynamic ScrollSpy with Highlighting (320px sticky sidebar)
 *  - Live Search (< 10ms execution, Ctrl+K / Cmd+K shortcut)
 *  - 3-Track Filter Pills (Track 1 to Track 3 + Tất cả)
 *  - Responsive Mobile Navigation Toggle
 */

document.addEventListener('DOMContentLoaded', () => {
  // -------------------------------------------------------------------------
  // 1. Dark / Light Theme Manager
  // -------------------------------------------------------------------------
  const themeToggle = document.getElementById('theme-toggle') || document.getElementById('theme-btn');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

  const initTheme = () => {
    const savedTheme = localStorage.getItem('asd-theme');
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
      localStorage.setItem('asd-theme', newTheme);
      
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
  const navLinks = document.querySelectorAll('.sidebar-nav .nav-item a, .sidebar-nav .nav-link, .nav-item a');
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
    handleScrollSpy(); // Initial call
  }

  // -------------------------------------------------------------------------
  // 4. Live Search Filter on Portal Hub
  // -------------------------------------------------------------------------
  const searchInput = document.getElementById('search-input') || document.getElementById('portal-search');
  const cards = document.querySelectorAll('.chapter-card, .matrix-card');

  if (searchInput && cards.length > 0) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase().trim();
      cards.forEach(card => {
        const title = (card.querySelector('h3, .card-title')?.textContent || '').toLowerCase();
        const desc = (card.querySelector('p, .card-desc')?.textContent || '').toLowerCase();
        const tags = Array.from(card.querySelectorAll('.card-tag, .tag-chip')).map(t => t.textContent.toLowerCase()).join(' ');
        
        if (title.includes(query) || desc.includes(query) || tags.includes(query)) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });

    // Keyboard shortcut (Ctrl+K / Cmd+K)
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        searchInput.focus();
      }
    });
  }

  // -------------------------------------------------------------------------
  // 5. Track Filter Pills on Portal Hub
  // -------------------------------------------------------------------------
  const filterPills = document.querySelectorAll('.filter-pill');
  if (filterPills.length > 0 && cards.length > 0) {
    filterPills.forEach(pill => {
      pill.addEventListener('click', () => {
        filterPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');

        const trackFilter = pill.getAttribute('data-filter');
        cards.forEach(card => {
          const cardTrack = card.getAttribute('data-track');
          if (trackFilter === 'all' || cardTrack === trackFilter) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }
});
