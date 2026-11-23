/**
 * Multicopter Design and Control Practice (Prof. Quan Quan, Xunhua Dai, Shuai Wang - Springer)
 * Application Core Logic:
 *  - Dark / Light Theme Toggle & Persistence ('mc-theme')
 *  - Reading Progress Bar (#reading-progress)
 *  - Dynamic ScrollSpy with Highlighting (320px sticky sidebar)
 *  - Live Search (< 10ms execution, Ctrl+K / Cmd+K shortcut)
 *  - 4-Track Filter Pills (Track 1 to Track 4 + Tất cả)
 *  - Code Block Copy Buttons
 */

document.addEventListener('DOMContentLoaded', () => {
  // -------------------------------------------------------------------------
  // 1. Dark / Light Theme Manager
  // -------------------------------------------------------------------------
  const themeToggle = document.getElementById('theme-toggle') || document.getElementById('theme-btn');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

  const initTheme = () => {
    const savedTheme = localStorage.getItem('mc-theme');
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
      localStorage.setItem('mc-theme', newTheme);
      
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

      navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (currentSection && href === `#${currentSection.id}`) {
          link.classList.add('active');
          const parentItem = link.closest('.nav-item');
          if (parentItem) parentItem.classList.add('active');
        } else {
          link.classList.remove('active');
          const parentItem = link.closest('.nav-item');
          if (parentItem) parentItem.classList.remove('active');
        }
      });
    };

    window.addEventListener('scroll', handleScrollSpy, { passive: true });
    handleScrollSpy();
  }

  // -------------------------------------------------------------------------
  // 4. Live Search & 4-Track Filter Pills (For Hub Page)
  // -------------------------------------------------------------------------
  const searchInput = document.getElementById('search-input');
  const filterPills = document.querySelectorAll('.filter-pill');
  const chapterCards = document.querySelectorAll('.chapter-card');

  if (chapterCards.length > 0) {
    let currentFilter = 'all';
    let searchQuery = '';

    const filterCards = () => {
      const query = searchQuery.toLowerCase().trim();
      let visibleCount = 0;

      chapterCards.forEach(card => {
        const track = card.getAttribute('data-track') || '';
        const title = (card.querySelector('.card-title') || {}).textContent || '';
        const desc = (card.querySelector('.card-desc') || {}).textContent || '';
        const tags = Array.from(card.querySelectorAll('.tag-chip')).map(t => t.textContent).join(' ');
        const cardText = `${title} ${desc} ${tags}`.toLowerCase();

        const matchesTrack = currentFilter === 'all' || track === currentFilter;
        const matchesQuery = query === '' || cardText.includes(query);

        if (matchesTrack && matchesQuery) {
          card.style.display = 'flex';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      // No results notice
      let noResultMsg = document.getElementById('no-search-results');
      if (visibleCount === 0) {
        if (!noResultMsg) {
          noResultMsg = document.createElement('div');
          noResultMsg.id = 'no-search-results';
          noResultMsg.className = 'no-results-box';
          noResultMsg.innerHTML = `
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔍</div>
            <h3>Không tìm thấy chương hoặc nội dung phù hợp</h3>
            <p>Thử tìm từ khóa khác như "Bayes", "Kalman", "Particle", "MCL", "FastSLAM", "MDP", "POMDP"...</p>
          `;
          const container = document.querySelector('.matrix-grid');
          if (container) container.appendChild(noResultMsg);
        }
        noResultMsg.style.display = 'block';
      } else if (noResultMsg) {
        noResultMsg.style.display = 'none';
      }
    };

    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value;
        filterCards();
      });

      // Keyboard Shortcut Ctrl+K / Cmd+K
      window.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
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
        currentFilter = pill.getAttribute('data-filter') || 'all';
        filterCards();
      });
    });
  }

  // -------------------------------------------------------------------------
  // 5. Code Block Copy Button Feature
  // -------------------------------------------------------------------------
  document.querySelectorAll('pre').forEach(pre => {
    if (pre.querySelector('.copy-code-btn')) return;

    const copyBtn = document.createElement('button');
    copyBtn.className = 'copy-code-btn';
    copyBtn.textContent = 'Sao chép';
    copyBtn.setAttribute('title', 'Sao chép mã nguồn');
    copyBtn.setAttribute('aria-label', 'Copy code to clipboard');

    copyBtn.addEventListener('click', async () => {
      const code = pre.querySelector('code');
      const textToCopy = code ? code.innerText : pre.innerText;

      try {
        await navigator.clipboard.writeText(textToCopy);
        copyBtn.textContent = '✓ Đã sao chép';
        copyBtn.classList.add('copied');
        setTimeout(() => {
          copyBtn.textContent = 'Sao chép';
          copyBtn.classList.remove('copied');
        }, 2000);
      } catch (err) {
        console.error('Không thể sao chép:', err);
      }
    });

    pre.style.position = 'relative';
    pre.appendChild(copyBtn);
  });
});
