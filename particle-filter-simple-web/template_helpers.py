# -*- coding: utf-8 -*-
"""
Common Template Helper for Particle Filter Made Simple Knowledge Portal
"""

def render_page(ch_info, all_chapters, content_html):
    # Sidebar navigation items
    nav_items_html = []
    for anchor, title in ch_info["sections"]:
        is_sub = len(anchor.split("-")) > 3
        sub_class = " sub-item" if is_sub else ""
        nav_items_html.append(f"""        <div class="nav-item{sub_class}">
          <a href="#{anchor}">
            <span class="nav-text">{title}</span>
          </a>
        </div>""")
    sidebar_nav_html = "\n".join(nav_items_html)

    # Prev / Next links
    prev_html = ""
    if ch_info["prev"]:
        prev_ch = next(c for c in all_chapters if c["id"] == ch_info["prev"])
        prev_html = f"""      <a href="{prev_ch['id']}.html" class="ch-nav-btn ch-nav-prev">
        <span class="ch-nav-label">← BÀI TRƯỚC</span>
        <span class="ch-nav-title">Chương {prev_ch['num']}: {prev_ch['title']}</span>
      </a>"""
    else:
        prev_html = """      <a href="../index.html" class="ch-nav-btn ch-nav-prev">
        <span class="ch-nav-label">← TỔNG QUAN</span>
        <span class="ch-nav-title">Về Trang Chủ Portal Hub</span>
      </a>"""

    next_html = ""
    if ch_info["next"]:
        next_ch = next(c for c in all_chapters if c["id"] == ch_info["next"])
        next_html = f"""      <a href="{next_ch['id']}.html" class="ch-nav-btn ch-nav-next">
        <span class="ch-nav-label">BÀI TIẾP THEO →</span>
        <span class="ch-nav-title">Chương {next_ch['num']}: {next_ch['title']}</span>
      </a>"""
    else:
        next_html = """      <a href="../index.html" class="ch-nav-btn ch-nav-next">
        <span class="ch-nav-label">HOÀN TẤT CHUYÊN KHẢO →</span>
        <span class="ch-nav-title">Về Danh Mục Chuyên Khảo Master Gateway</span>
      </a>"""

    return f"""<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chương {ch_info['num']}: {ch_info['title']} | Particle Filter Made Simple</title>
  <link rel="stylesheet" href="../assets/css/style.css">
  
  <!-- MathJax 3 Strict Zero-Error Configuration -->
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$']],
        displayMath: [['$$', '$$']],
        processEscapes: true
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }}
    }};
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
  <div id="reading-progress"></div>

  <!-- Global Header -->
  <header class="site-header">
    <div class="header-left">
      <nav class="header-breadcrumbs">
        <a href="../index.html" class="breadcrumb-item">🏠 Lộ trình PF</a>
        <span class="breadcrumb-sep">/</span>
        <span class="breadcrumb-item">{ch_info['track']}</span>
        <span class="breadcrumb-sep">/</span>
        <span class="breadcrumb-current">Chương {ch_info['num']}</span>
      </nav>
    </div>
    <div class="header-right">
      <a href="../index.html" class="header-book-ref">📖 Particle Filter Made Simple • Dhayalkar</a>
      <button id="theme-toggle" class="btn btn-outline" style="padding: 0.35rem 0.75rem; font-size: 0.85rem;" title="Chuyển chế độ Sáng / Tối">
        <span id="theme-icon">☀️</span> <span id="theme-text">Chế độ sáng</span>
      </button>
    </div>
  </header>

  <div class="app-layout">
    <!-- 320px Sticky Left Sidebar TOC -->
    <aside class="sidebar-container">
      <div class="sidebar-header">
        <span class="sidebar-title">MỤC LỤC CHƯƠNG {ch_info['num']}</span>
        <span class="sidebar-badge">{len(ch_info['sections'])} MỤC</span>
      </div>
      <nav class="sidebar-nav">
{sidebar_nav_html}
      </nav>
      <div class="sidebar-footer">
        <a href="../index.html" class="sidebar-back-link">← Trở về Hub Dashboard</a>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
      <!-- Chapter Hero Banner -->
      <section class="chapter-hero">
        <div class="hero-badge-row">
          <span class="hero-badge badge-primary">{ch_info['track'].upper()}</span>
          <span class="hero-badge badge-accent">CHƯƠNG {ch_info['num']}</span>
        </div>
        <h1 class="chapter-title">{ch_info['title']}</h1>
        <p class="chapter-subtitle-en">{ch_info['title_en']}</p>
        <p class="chapter-lead">{ch_info['desc']}</p>
        <div class="chapter-meta-row">
          <span>⏱️ Thời gian đọc: ~25 phút</span>
          <span>📐 Mô hình Toán 6 tầng</span>
          <span>🎮 Canvas 2D 60 FPS</span>
          <span>🤖 C++20 / ROS 2 Bridge</span>
        </div>
      </section>

      <!-- Chapter Detailed Content -->
      <div class="chapter-body">
{content_html}
      </div>

      <!-- Navigation Row -->
      <nav class="chapter-nav-row">
{prev_html}
{next_html}
      </nav>

      <!-- Footer -->
      <footer class="site-footer">
        <p>© 2026 Viện Tri Thức Robotics & AI. Chưng cất học thuật từ chuyên khảo <em>Particle Filter Made Simple</em> (Sahil Rajesh Dhayalkar, Arizona State University).</p>
      </footer>
    </main>
  </div>

  <script src="../assets/js/app.js"></script>
  <script src="../assets/js/simulators.js"></script>
</body>
</html>"""
