/**
 * Design and Analysis of Control Systems - Knowledge Web Portal
 * Application Core Logic:
 *  - Dark / Light Theme Toggle & Persistence
 *  - Reading Progress Bar
 *  - Dynamic ScrollSpy with Smooth Highlighting for Sticky Sidebar
 *  - Ultra-Fast Live Search (< 10ms execution, Ctrl+K / Cmd+K shortcut)
 *  - 5-Track Filter Pills (Track 1 to Track 5 + Tất cả)
 *  - Mobile Sidebar Drawer Toggle & Code Block Copy
 *
 * Arthur G.O. Mutambara - Version 20261122
 */

document.addEventListener('DOMContentLoaded', () => {
  // -------------------------------------------------------------------------
  // 1. Dark / Light Theme Manager
  // -------------------------------------------------------------------------
  const themeToggle = document.getElementById('theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

  const initTheme = () => {
    const savedTheme = localStorage.getItem('csd-theme');
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
      localStorage.setItem('csd-theme', newTheme);
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
  // 3. ScrollSpy for Sticky Sidebar Navigation (320px)
  // -------------------------------------------------------------------------
  const sections = document.querySelectorAll('section[id^="sec-"], section[id^="ch-"], div[id^="sec-"], article[id^="sec-"]');
  const navLinks = document.querySelectorAll('.sidebar-link, .nav-item a');

  if (sections.length > 0 && navLinks.length > 0) {
    let spyTicking = false;
    const updateActiveSection = () => {
      let currentSecId = '';
      const scrollPos = window.scrollY || window.pageYOffset;

      sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        // Section active if its top is near navbar offset
        if (rect.top <= 170 && rect.bottom >= 110) {
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

  function normalizeTrack(val) {
    if (!val) return '';
    const clean = val.toLowerCase().replace(/[^a-z0-9]/g, '');
    if (clean.includes('track1') || clean === '1') return 'track1';
    if (clean.includes('track2') || clean === '2') return 'track2';
    if (clean.includes('track3') || clean === '3') return 'track3';
    if (clean.includes('track4') || clean === '4') return 'track4';
    if (clean.includes('track5') || clean === '5') return 'track5';
    return clean;
  }

  function applyFilters() {
    if (!cards.length) return;
    const q = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const activeFilterPill = document.querySelector('.filter-pill.active');
    const rawFilter = activeFilterPill ? (activeFilterPill.getAttribute('data-filter') || activeFilterPill.getAttribute('data-track') || 'all') : 'all';
    const filter = normalizeTrack(rawFilter);

    cards.forEach(card => {
      const text = card.textContent.toLowerCase();
      const tags = (card.getAttribute('data-tags') || '').toLowerCase();
      const rawCardTrack = card.getAttribute('data-track') || card.getAttribute('data-filter') || '';
      const cardTrack = normalizeTrack(rawCardTrack);

      const matchesQuery = !q || text.includes(q) || tags.includes(q);
      const matchesFilter = (filter === 'all' || !filter) || (cardTrack === filter);

      if (matchesQuery && matchesFilter) {
        card.classList.remove('hidden');
        card.style.display = '';
      } else {
        card.classList.add('hidden');
        card.style.display = 'none';
      }
    });
  }

  if (searchInput && cards.length > 0) {
    searchInput.addEventListener('input', applyFilters);

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
  // 5. 5 Filter Pills (Track 1 to Track 5 + Tất cả)
  // -------------------------------------------------------------------------
  const pills = document.querySelectorAll('.filter-pill');
  if (pills.length > 0 && cards.length > 0) {
    pills.forEach(pill => {
      pill.addEventListener('click', () => {
        pills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        applyFilters();
      });
    });
  }

  // -------------------------------------------------------------------------
  // 6. Mobile Sidebar Drawer Toggle
  // -------------------------------------------------------------------------
  const sidebarToggle = document.getElementById('sidebar-toggle');
  const sidebar = document.querySelector('.sidebar') || document.querySelector('.sidebar-container') || document.getElementById('sidebar');
  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      const isOpen = sidebar.classList.contains('open');
      sidebarToggle.setAttribute('aria-expanded', isOpen);
    });
  }

  // -------------------------------------------------------------------------
  // 7. Interactive Code Block Copy Buttons
  // -------------------------------------------------------------------------
  document.querySelectorAll('pre code').forEach((block) => {
    const pre = block.parentElement;
    if (pre && !pre.querySelector('.btn-copy-code')) {
      const copyBtn = document.createElement('button');
      copyBtn.className = 'btn-copy-code';
      copyBtn.setAttribute('type', 'button');
      copyBtn.innerHTML = '📋 Copy';
      copyBtn.style.position = 'absolute';
      copyBtn.style.top = '0.5rem';
      copyBtn.style.right = '0.5rem';
      copyBtn.style.padding = '0.2rem 0.55rem';
      copyBtn.style.fontSize = '0.75rem';
      copyBtn.style.borderRadius = '4px';
      copyBtn.style.border = '1px solid rgba(255,255,255,0.2)';
      copyBtn.style.background = 'rgba(0,0,0,0.5)';
      copyBtn.style.color = '#fff';
      copyBtn.style.cursor = 'pointer';

      pre.style.position = 'relative';
      copyBtn.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(block.innerText);
          copyBtn.innerHTML = '✓ Copied!';
          setTimeout(() => { copyBtn.innerHTML = '📋 Copy'; }, 2000);
        } catch (err) {
          copyBtn.innerHTML = 'Error';
        }
      });
      pre.appendChild(copyBtn);
    }
  });
});
