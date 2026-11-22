// App Logic: ScrollSpy, Live Search, Track Filters & Reading Progress
document.addEventListener('DOMContentLoaded', () => {
  // 1. Reading Progress Bar
  const progressBar = document.getElementById('reading-progress');
  if (progressBar) {
    window.addEventListener('scroll', () => {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      progressBar.style.width = scrolled + '%';
    });
  }

  // 2. ScrollSpy for Sidebar Navigation
  const sections = document.querySelectorAll('section[id^="sec-"]');
  const navLinks = document.querySelectorAll('.sidebar-link');

  if (sections.length > 0 && navLinks.length > 0) {
    const updateActiveSection = () => {
      let currentSecId = '';
      sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 160 && rect.bottom >= 160) {
          currentSecId = section.getAttribute('id');
        }
      });

      if (!currentSecId && window.scrollY < 200) {
        currentSecId = sections[0].getAttribute('id');
      }

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + currentSecId) {
          link.classList.add('active');
        }
      });
    };

    window.addEventListener('scroll', updateActiveSection);
    updateActiveSection();
  }

  // 3. Live Search on Hub Page
  const searchInput = document.getElementById('matrix-search-input') || document.getElementById('chapter-search');
  const cards = document.querySelectorAll('.matrix-card, .chapter-card');

  if (searchInput && cards.length > 0) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      cards.forEach(card => {
        const text = card.textContent.toLowerCase();
        const tags = (card.getAttribute('data-tags') || '').toLowerCase();
        const match = text.includes(q) || tags.includes(q);
        if (match) {
          card.classList.remove('hidden');
          card.style.display = '';
        } else {
          card.classList.add('hidden');
          card.style.display = 'none';
        }
      });
    });

    // Keyboard shortcut Ctrl + K
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        searchInput.focus();
      }
    });
  }

  // 4. Track Filter Pills
  const pills = document.querySelectorAll('.filter-pill');
  if (pills.length > 0 && cards.length > 0) {
    pills.forEach(pill => {
      pill.addEventListener('click', () => {
        pills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');

        const filter = pill.getAttribute('data-filter') || pill.getAttribute('data-track');
        cards.forEach(card => {
          const cardTrack = card.getAttribute('data-filter') || card.getAttribute('data-track');
          if (filter === 'all' || cardTrack === filter) {
            card.classList.remove('hidden');
            card.style.display = '';
          } else {
            card.classList.add('hidden');
            card.style.display = 'none';
          }
        });

        // Reset search input if filtering
        if (searchInput && searchInput.value) {
          searchInput.value = '';
        }
      });
    });
  }
});
