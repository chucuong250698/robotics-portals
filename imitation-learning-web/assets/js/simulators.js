/**
 * ============================================================================
 * ROBOT IMITATION LEARNING - INTERACTIVE EXPLORABLE SIMULATORS (HTML5 CANVAS)
 * 14 Bộ mô phỏng đồ thị & hoạt họa tương tác thời gian thực 60 FPS
 * ============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('sim-canvas-01')) initSim01();
  if (document.getElementById('sim-canvas-02')) initSim02();
  if (document.getElementById('sim-canvas-03')) initSim03();
  if (document.getElementById('sim-canvas-04')) initSim04();
  if (document.getElementById('sim-canvas-05')) initSim05();
  if (document.getElementById('sim-canvas-06')) initSim06();
  if (document.getElementById('sim-canvas-07')) initSim07();
  if (document.getElementById('sim-canvas-08')) initSim08();
  if (document.getElementById('sim-canvas-09')) initSim09();
  if (document.getElementById('sim-canvas-10')) initSim10();
  if (document.getElementById('sim-canvas-11')) initSim11();
  if (document.getElementById('sim-canvas-12')) initSim12();
  if (document.getElementById('sim-canvas-13')) initSim13();
  if (document.getElementById('sim-canvas-14')) initSim14();
});

// Helper for dark/light grid background
function clearCanvas(ctx, width, height) {
  const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
  ctx.fillStyle = isDark ? '#0b0f19' : '#f8fafc';
  ctx.fillRect(0, 0, width, height);

  ctx.strokeStyle = isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)';
  ctx.lineWidth = 1;
  const gridSize = 40;
  ctx.beginPath();
  for (let x = 0; x < width; x += gridSize) {
    ctx.moveTo(x, 0); ctx.lineTo(x, height);
  }
  for (let y = 0; y < height; y += gridSize) {
    ctx.moveTo(0, y); ctx.lineTo(width, y);
  }
  ctx.stroke();
}

// ============================================================================
// SIM 01: So Sánh 3 Trường Phái Học Bắt Chước (BC vs IRL vs IIL)
// ============================================================================
function initSim01() {
  const canvas = document.getElementById('sim-canvas-01');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const typeSelect = document.getElementById('sim01-type');
  const demosSlider = document.getElementById('sim01-demos');
  const demosVal = document.getElementById('sim01-demos-val');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const mode = typeSelect ? typeSelect.value : 'bc';
    const N = demosSlider ? parseInt(demosSlider.value) : 10;
    if (demosVal) demosVal.textContent = N + ' biểu diễn';

    ctx.save();
    // Chart 1: Performance vs Demonstration Count
    const bx = 80, by = 220, w = 260, h = 150;
    ctx.strokeStyle = '#64748b'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(bx, by); ctx.lineTo(bx + w, by); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(bx, by); ctx.lineTo(bx, by - h); ctx.stroke();

    ctx.fillStyle = '#94a3b8'; ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Số lượng mẫu (N)', bx + w - 80, by + 18);
    ctx.fillText('Tỷ lệ thành công (%)', bx - 60, by - h - 10);

    // Plot curves
    ctx.lineWidth = 3;
    // BC curve (saturates early, prone to shift)
    ctx.strokeStyle = mode === 'bc' ? '#38bdf8' : 'rgba(56, 189, 248, 0.2)';
    ctx.beginPath();
    for (let x = 0; x <= w; x += 5) {
      const frac = x / w;
      const perf = Math.min(0.75, 1 - Math.exp(-frac * 3.5));
      const py = by - perf * h;
      if (x === 0) ctx.moveTo(bx + x, py); else ctx.lineTo(bx + x, py);
    }
    ctx.stroke();

    // IRL curve (requires environment interaction)
    ctx.strokeStyle = mode === 'irl' ? '#10b981' : 'rgba(16, 185, 129, 0.2)';
    ctx.beginPath();
    for (let x = 0; x <= w; x += 5) {
      const frac = x / w;
      const perf = Math.min(0.92, (1 - Math.exp(-frac * 2.0)) * 0.95);
      const py = by - perf * h;
      if (x === 0) ctx.moveTo(bx + x, py); else ctx.lineTo(bx + x, py);
    }
    ctx.stroke();

    // IIL / DAgger curve (reaches near 100% with human in the loop)
    ctx.strokeStyle = mode === 'iil' ? '#f59e0b' : 'rgba(245, 158, 11, 0.2)';
    ctx.beginPath();
    for (let x = 0; x <= w; x += 5) {
      const frac = x / w;
      const perf = Math.min(0.98, 1 - Math.exp(-frac * 5.0));
      const py = by - perf * h;
      if (x === 0) ctx.moveTo(bx + x, py); else ctx.lineTo(bx + x, py);
    }
    ctx.stroke();

    // Comparison Radar / Stats Card on the Right
    const rx = 390, ry = 60;
    ctx.fillStyle = 'rgba(255, 255, 255, 0.03)';
    ctx.fillRect(rx, ry, 280, 200);
    ctx.strokeStyle = '#334155'; ctx.strokeRect(rx, ry, 280, 200);

    ctx.font = 'bold 13px Inter, sans-serif';
    if (mode === 'bc') {
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('TRƯỜNG PHÁI: BEHAVIORAL CLONING (BC)', rx + 15, ry + 30);
      ctx.font = '12px Inter, sans-serif';
      ctx.fillStyle = '#f1f5f9';
      ctx.fillText('• Phương thức: Học có giám sát (Supervised)', rx + 15, ry + 60);
      ctx.fillText('• Tương tác môi trường: KHÔNG CẦN (Offline)', rx + 15, ry + 85);
      ctx.fillText('• Hiệu quả mẫu: Rất cao ở bước đầu', rx + 15, ry + 110);
      ctx.fillStyle = '#ef4444';
      ctx.fillText('⚠️ Nhược điểm: Lệch phân phối O(T²ε)', rx + 15, ry + 140);
      ctx.fillStyle = '#10b981';
      ctx.fillText('✅ Tối ưu cho: Khởi tạo chính sách ban đầu', rx + 15, ry + 165);
    } else if (mode === 'irl') {
      ctx.fillStyle = '#10b981';
      ctx.fillText('TRƯỜNG PHÁI: INVERSE REINFORCEMENT LEARNING', rx + 15, ry + 30);
      ctx.font = '12px Inter, sans-serif';
      ctx.fillStyle = '#f1f5f9';
      ctx.fillText('• Phương thức: Tìm hàm phần thưởng ẩn R(s,a)', rx + 15, ry + 60);
      ctx.fillText('• Tương tác môi trường: BẮT BUỘC (RL Loop)', rx + 15, ry + 85);
      ctx.fillText('• Tổng quát hóa: Rất mạnh, tránh trôi dạt', rx + 15, ry + 110);
      ctx.fillStyle = '#ef4444';
      ctx.fillText('⚠️ Nhược điểm: Chi phí tính toán cực lớn', rx + 15, ry + 140);
      ctx.fillStyle = '#10b981';
      ctx.fillText('✅ Tối ưu cho: Bài toán hiểu ý đồ chuyên gia', rx + 15, ry + 165);
    } else {
      ctx.fillStyle = '#f59e0b';
      ctx.fillText('TRƯỜNG PHÁI: INTERACTIVE IL (IIL / DAGGER)', rx + 15, ry + 30);
      ctx.font = '12px Inter, sans-serif';
      ctx.fillStyle = '#f1f5f9';
      ctx.fillText('• Phương thức: Người can thiệp sửa sai online', rx + 15, ry + 60);
      ctx.fillText('• Tương tác môi trường: CÓ + Có người kèm', rx + 15, ry + 85);
      ctx.fillText('• Sai số tích lũy: Giảm xuống bậc nhất O(Tε)', rx + 15, ry + 110);
      ctx.fillStyle = '#10b981';
      ctx.fillText('✅ Tối ưu cho: Robot học thao tác thực tế', rx + 15, ry + 140);
      ctx.fillText('✅ Độ an toàn cao nhờ can thiệp can-thiệp-kịp-thời', rx + 15, ry + 165);
    }

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 02: Tích Lũy Sai Số Covariate Shift O(T^2 epsilon)
// ============================================================================
function initSim02() {
  const canvas = document.getElementById('sim-canvas-02');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const epsSlider = document.getElementById('sim02-eps');
  const epsVal = document.getElementById('sim02-eps-val');

  let carX = 100, carY = 150, heading = 0;
  const trail = [];

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const eps = epsSlider ? parseFloat(epsSlider.value) : 0.05;
    if (epsVal) epsVal.textContent = 'ε = ' + eps.toFixed(3);

    // Road lane boundaries
    ctx.save();
    ctx.strokeStyle = '#475569'; ctx.lineWidth = 4;
    ctx.beginPath(); ctx.moveTo(40, 90); ctx.lineTo(660, 90); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(40, 210); ctx.lineTo(660, 210); ctx.stroke();
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)'; ctx.lineWidth = 2; ctx.setLineDash([10, 10]);
    ctx.beginPath(); ctx.moveTo(40, 150); ctx.lineTo(660, 150); ctx.stroke();
    ctx.setLineDash([]);

    // Update car with compounding drift error: dy/dt = v * sin(heading), d_heading/dt = eps * (t/100)
    carX += 2.0;
    // Compounding drift formula
    const tNorm = (carX - 100) / 100;
    const driftAngle = eps * Math.pow(tNorm, 1.8);
    carY += driftAngle * 3.5;

    if (carX > 640) {
      carX = 100; carY = 150; trail.length = 0;
    }
    trail.push({x: carX, y: carY});

    // Draw trajectory trail
    ctx.strokeStyle = Math.abs(carY - 150) > 55 ? '#ef4444' : '#38bdf8';
    ctx.lineWidth = 3;
    ctx.beginPath();
    for (let i = 0; i < trail.length; i++) {
      if (i === 0) ctx.moveTo(trail[i].x, trail[i].y);
      else ctx.lineTo(trail[i].x, trail[i].y);
    }
    ctx.stroke();

    // Car body
    ctx.fillStyle = Math.abs(carY - 150) > 55 ? '#ef4444' : '#6366f1';
    ctx.fillRect(carX - 15, carY - 8, 30, 16);
    ctx.strokeStyle = '#ffffff'; ctx.strokeRect(carX - 15, carY - 8, 30, 16);

    // Header info
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('HIỆN TƯỢNG LỆCH PHÂN PHỐI (COVARIATE SHIFT): ĐỘ LỆCH TÍCH LŨY O(T²ε)', 40, 40);
    ctx.fillStyle = Math.abs(carY - 150) > 55 ? '#ef4444' : '#10b981';
    ctx.fillText(Math.abs(carY - 150) > 55 ? '💥 CẢNH BÁO: XE BỊ VĂNG KHỎI ĐƯỜNG DO KHÔNG CÓ DỮ LIỆU PHỤC HỒI!' : '✅ Xe trong làn an toàn', 40, 65);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 03: TAMER / COACH Evaluative Feedback
// ============================================================================
function initSim03() {
  const canvas = document.getElementById('sim-canvas-03');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const rewardBtn = document.getElementById('sim03-reward');
  const punishBtn = document.getElementById('sim03-punish');
  const scoreVal = document.getElementById('sim03-score');

  let ballX = 120, ballY = 150, vx = 2.0, vy = 0.5;
  let targetX = 550, targetY = 150;
  let H_weight = 0.5;
  let feedbackFlash = 0; // +1 green, -1 red

  if (rewardBtn) {
    rewardBtn.addEventListener('click', () => {
      H_weight += 0.15; feedbackFlash = 1;
      setTimeout(() => feedbackFlash = 0, 400);
    });
  }
  if (punishBtn) {
    punishBtn.addEventListener('click', () => {
      H_weight -= 0.15; feedbackFlash = -1;
      setTimeout(() => feedbackFlash = 0, 400);
    });
  }

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);

    // Goal zone
    ctx.save();
    ctx.fillStyle = 'rgba(16, 185, 129, 0.15)';
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(targetX, targetY, 35, 0, 2*Math.PI); ctx.fill(); ctx.stroke();
    ctx.fillStyle = '#10b981'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('ĐÍCH (GOAL)', targetX - 35, targetY + 50);

    // Steer ball towards goal conditioned on H_weight
    const dx = targetX - ballX, dy = targetY - ballY;
    const dist = Math.sqrt(dx*dx + dy*dy);
    const steerY = (dy / dist) * Math.max(0, H_weight) * 2.5;
    vy = vy * 0.9 + steerY * 0.1;

    ballX += vx; ballY += vy;
    if (ballX > 620) { ballX = 100; ballY = 100 + Math.random() * 100; }

    // Ball
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath(); ctx.arc(ballX, ballY, 12, 0, 2*Math.PI); ctx.fill();
    ctx.strokeStyle = '#ffffff'; ctx.stroke();

    // Human Feedback indicator flash
    if (feedbackFlash === 1) {
      ctx.fillStyle = '#10b981'; ctx.font = 'bold 24px Inter, sans-serif';
      ctx.fillText('+1 KHEN NGỢI! (REWARD)', 240, 60);
    } else if (feedbackFlash === -1) {
      ctx.fillStyle = '#ef4444'; ctx.font = 'bold 24px Inter, sans-serif';
      ctx.fillText('-1 PHÊ BÌNH! (PUNISH)', 240, 60);
    }

    if (scoreVal) scoreVal.textContent = 'Trọng số đánh giá H(s,a) = ' + H_weight.toFixed(2);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('MÔ PHỎNG TAMER / COACH: HỌC TỪ PHẢN HỒI ĐÁNH GIÁ (HUMAN IN THE LOOP)', 40, 35);
    ctx.fillStyle = '#94a3b8'; ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Bấm Khen (+1) khi robot hướng về đích, Chê (-1) khi đi chệch hướng.', 40, 60);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 04: DAgger & SafeDAgger
// ============================================================================
function initSim04() {
  const canvas = document.getElementById('sim-canvas-04');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const iterSlider = document.getElementById('sim04-iter');
  const iterVal = document.getElementById('sim04-iter-val');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const k = iterSlider ? parseInt(iterSlider.value) : 1;
    if (iterVal) iterVal.textContent = 'Vòng lặp DAgger: N = ' + k;

    // Beta mixing factor beta_k = beta_0^k
    const beta = Math.pow(0.7, k - 1);
    const errorBound = 1.0 / k;

    ctx.save();
    // Plot expert trajectory vs learned policy trajectory
    const cx = 350, cy = 180;
    // Expert trajectory (Smooth sine curve - Green)
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3; ctx.beginPath();
    for (let x = 60; x <= 640; x += 5) {
      const y = cy - 60 * Math.sin((x - 60) * 0.015);
      if (x === 60) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Robot trajectory (improves with k)
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2; ctx.beginPath();
    for (let x = 60; x <= 640; x += 5) {
      const noise = (Math.sin(x * 0.2) * 45) * errorBound;
      const y = cy - 60 * Math.sin((x - 60) * 0.015) + noise;
      if (x === 60) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Data points collected (aggregation visual)
    const pointsCount = k * 12;
    ctx.fillStyle = '#f59e0b';
    for (let p = 0; p < pointsCount; p++) {
      const px = 60 + (p * 580 / pointsCount);
      const py = cy - 60 * Math.sin((px - 60) * 0.015) + (Math.sin(p) * 20 * errorBound);
      ctx.beginPath(); ctx.arc(px, py, 3, 0, 2*Math.PI); ctx.fill();
    }

    // Legend
    ctx.fillStyle = '#10b981'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('— Quỹ đạo Chuyên gia π*', 60, 40);
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('— Chính sách Học được π_hat', 260, 40);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`● Dữ liệu tổng hợp D_k (${pointsCount} mẫu gán nhãn)`, 470, 40);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 14px monospace';
    ctx.fillText(`Hệ số hòa trộn β_k = ${beta.toFixed(3)} | Cận sai số: O(T·ε) = ${(errorBound * 100).toFixed(1)}%`, 60, 270);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 05: Dynamic Movement Primitives (DMPs)
// ============================================================================
function initSim05() {
  const canvas = document.getElementById('sim-canvas-05');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const goalSlider = document.getElementById('sim05-goal');
  const tauSlider = document.getElementById('sim05-tau');
  const goalVal = document.getElementById('sim05-goal-val');
  const tauVal = document.getElementById('sim05-tau-val');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const goalY = goalSlider ? parseFloat(goalSlider.value) : 100;
    const tau = tauSlider ? parseFloat(tauSlider.value) : 1.0;
    if (goalVal) goalVal.textContent = 'Đích G = ' + goalY.toFixed(0);
    if (tauVal) tauVal.textContent = 'Thời gian τ = ' + tau.toFixed(1) + 'x';

    ctx.save();
    const startX = 60, startY = 220;
    const endX = 640;

    // Start & Goal Markers
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath(); ctx.arc(startX, startY, 8, 0, 2*Math.PI); ctx.fill();
    ctx.fillText('Gốc y_0', startX - 15, startY + 22);

    ctx.fillStyle = '#10b981';
    ctx.beginPath(); ctx.arc(endX, goalY, 10, 0, 2*Math.PI); ctx.fill();
    ctx.fillText('Đích Goal (g)', endX - 25, goalY - 18);

    // DMP trajectory generated by canonical phase decay: s = exp(-alpha*t/tau)
    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 4; ctx.beginPath();
    const steps = 100;
    for (let i = 0; i <= steps; i++) {
      const t = (i / steps);
      const s = Math.exp(-3.0 * t / tau); // canonical system phase
      // Transformation system with forcing term
      const baseline = startY + (goalY - startY) * (1 - s);
      const forcing = 60 * Math.sin(t * Math.PI) * s;
      const px = startX + i * ((endX - startX) / steps);
      const py = baseline - forcing;
      if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('DYNAMIC MOVEMENT PRIMITIVES (DMP): HỆ THỐNG BIẾN ĐỔI BẤT BIẾN TỶ LỆ', 60, 40);
    ctx.fillStyle = '#f59e0b'; ctx.font = '12px Inter, sans-serif';
    ctx.fillText('Kéo thanh trượt để thay đổi Đích hoặc Thời gian: Quỹ đạo tự co giãn mượt mà!', 60, 65);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 06: Diffusion Policy Denoising Process
// ============================================================================
function initSim06() {
  const canvas = document.getElementById('sim-canvas-06');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const stepSlider = document.getElementById('sim06-step');
  const stepVal = document.getElementById('sim06-step-val');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const kStep = stepSlider ? parseInt(stepSlider.value) : 10;
    if (stepVal) stepVal.textContent = `Bước khử nhiễu: k = ${kStep} / 16`;

    ctx.save();
    const noiseScale = Math.max(0, (16 - kStep) / 16);

    // Obstacle circle in center
    ctx.fillStyle = '#ef4444';
    ctx.beginPath(); ctx.arc(350, 160, 40, 0, 2*Math.PI); ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('VẬT CẢN', 325, 164);

    // Two multimodal branches (Over and Under obstacle)
    const branches = [
      { dir: -1, color: '#38bdf8', name: 'Nhánh 1 (Vượt trên)' },
      { dir: +1, color: '#10b981', name: 'Nhánh 2 (Vượt dưới)' }
    ];

    branches.forEach(b => {
      ctx.strokeStyle = b.color; ctx.lineWidth = 3; ctx.beginPath();
      for (let x = 80; x <= 620; x += 10) {
        const t = (x - 80) / 540;
        const cleanY = 160 + b.dir * 85 * Math.sin(t * Math.PI);
        const noise = (Math.sin(x * 12.3) + Math.cos(x * 7.1)) * 35 * noiseScale;
        const py = cleanY + noise;
        if (x === 80) ctx.moveTo(x, py); else ctx.lineTo(x, py);
      }
      ctx.stroke();
    });

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('MÔ PHỎNG DIFFUSION POLICY: KHỬ NHIỄU HÀNH ĐỘNG ĐA MỐT (MULTIMODAL)', 60, 40);
    ctx.fillStyle = '#38bdf8'; ctx.font = '12px Inter, sans-serif';
    ctx.fillText(`Mức nhiễu Gaussian còn lại: ${(noiseScale * 100).toFixed(0)}% (Khử nhiễu thành công 2 quỹ đạo tránh va chạm)`, 60, 65);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 07: Maximum Entropy IRL Gridworld
// ============================================================================
function initSim07() {
  const canvas = document.getElementById('sim-canvas-07');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    ctx.save();
    const rows = 5, cols = 8, cellW = 60, cellH = 45;
    const startX = 110, startY = 50;

    // Heatmap of learned reward R(s)
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const px = startX + c * cellW, py = startY + r * cellH;
        // Higher reward near goal (r=2, c=7)
        const distToGoal = Math.hypot(c - 7, r - 2);
        const reward = Math.max(0, 1 - distToGoal / 7);

        ctx.fillStyle = `rgba(16, 185, 129, ${reward * 0.8 + 0.05})`;
        ctx.fillRect(px, py, cellW - 2, cellH - 2);
        ctx.strokeStyle = '#334155'; ctx.strokeRect(px, py, cellW - 2, cellH - 2);

        ctx.fillStyle = '#94a3b8'; ctx.font = '10px monospace';
        ctx.fillText(reward.toFixed(2), px + 15, py + 26);
      }
    }

    // Expert Demonstrations overlay (Arrows)
    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 3;
    const path = [{c:0, r:2}, {c:1, r:2}, {c:2, r:1}, {c:3, r:1}, {c:4, r:2}, {c:5, r:2}, {c:6, r:2}, {c:7, r:2}];
    ctx.beginPath();
    for (let i = 0; i < path.length; i++) {
      const cx = startX + path[i].c * cellW + cellW/2;
      const cy = startY + path[i].r * cellH + cellH/2;
      if (i === 0) ctx.moveTo(cx, cy); else ctx.lineTo(cx, cy);
    }
    ctx.stroke();

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('MAXIMUM ENTROPY IRL: KHÔI PHỤC BẢN ĐỒ PHẦN THƯỞNG ẨN R(s)', 60, 25);
    ctx.fillStyle = '#f59e0b'; ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Đường màu vàng: Quỹ đạo mẫu chuyên gia | Màu xanh lá: Hàm phần thưởng R(s) khôi phục', 60, 290);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 08: GAIL Occupancy Matching
// ============================================================================
function initSim08() {
  const canvas = document.getElementById('sim-canvas-08');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const dSlider = document.getElementById('sim08-disc');
  const dVal = document.getElementById('sim08-d-val');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const dIter = dSlider ? parseInt(dSlider.value) : 10;
    if (dVal) dVal.textContent = `Vòng huấn luyện GAIL: Epoch ${dIter}`;

    ctx.save();
    const cx1 = 250, cx2 = 250 + (50 / (dIter + 1)), cy = 160;

    // Expert occupancy distribution d_E (Green)
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.ellipse(cx1, cy, 120, 80, 0, 0, 2*Math.PI); ctx.stroke();
    ctx.fillStyle = 'rgba(16, 185, 129, 0.15)'; ctx.fill();

    // Policy occupancy distribution d_pi (Blue - aligns with expert as dIter increases)
    const alignFrac = Math.min(1.0, dIter / 30);
    const currX = 400 - alignFrac * 150;
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.ellipse(currX, cy, 120, 80, 0, 0, 2*Math.PI); ctx.stroke();
    ctx.fillStyle = 'rgba(56, 189, 248, 0.15)'; ctx.fill();

    // Readout
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('GAIL: ĐỒNG NHẤT PHÂN PHỐI CHIẾM DỤNG TRẠNG THÁI - HÀNH ĐỘNG d_π(s,a) ≈ d_E(s,a)', 50, 40);
    ctx.fillStyle = '#10b981'; ctx.fillText('● d_E(s,a) Chuyên gia', 50, 65);
    ctx.fillStyle = '#38bdf8'; ctx.fillText('● d_π(s,a) Chính sách học được', 220, 65);

    const jsDiv = Math.exp(-dIter * 0.12);
    ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 14px monospace';
    ctx.fillText(`Jensen-Shannon Divergence: D_JS(d_π || d_E) = ${jsDiv.toFixed(4)}`, 50, 275);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 09: Imitation from Observation (BCO)
// ============================================================================
function initSim09() {
  const canvas = document.getElementById('sim-canvas-09');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let t = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    t += 0.03;

    ctx.save();
    // Video demonstration state s_t -> s_{t+1} (No action available)
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2;
    ctx.strokeRect(80, 80, 180, 110);
    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('VIDEO MẪU (CHỈ CÓ ẢNH)', 95, 105);
    ctx.fillStyle = '#94a3b8'; ctx.font = '11px monospace';
    ctx.fillText('s_t -> s_{t+1}', 130, 140);
    ctx.fillText('(Không có nhãn hành động a)', 95, 165);

    // Inverse dynamics model block
    ctx.fillStyle = '#6366f1'; ctx.fillRect(310, 100, 130, 70);
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('MÔ HÌNH NGHỊCH', 320, 128);
    ctx.fillText('a = f⁻¹(s, s\')', 335, 150);

    // Inferred Action Output
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2;
    ctx.strokeRect(480, 80, 160, 110);
    ctx.fillStyle = '#10b981'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('HÀNH ĐỘNG DỰ ĐOÁN', 495, 105);
    const inferredA = Math.sin(t) * 1.5;
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 15px monospace';
    ctx.fillText(`a_hat = ${inferredA.toFixed(2)} Nm`, 505, 145);

    // Arrows
    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(260, 135); ctx.lineTo(310, 135); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(440, 135); ctx.lineTo(480, 135); ctx.stroke();

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('THUẬT TOÁN BCO: SUY LUẬN HÀNH ĐỘNG TỪ BẢN QUAN SÁT TRẠNG THÁI', 60, 40);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 10: T-REX Suboptimal Demonstration Extrapolation
// ============================================================================
function initSim10() {
  const canvas = document.getElementById('sim-canvas-10');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    ctx.save();
    const bx = 100, by = 230, w = 480, h = 160;

    // Axes
    ctx.strokeStyle = '#64748b'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(bx, by); ctx.lineTo(bx + w, by); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(bx, by); ctx.lineTo(bx, by - h); ctx.stroke();

    ctx.fillStyle = '#94a3b8'; ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Thứ bậc quỹ đạo xếp hạng (Kém -> Tốt)', bx + 140, by + 20);
    ctx.fillText('Hàm thưởng khôi phục R(τ)', bx - 50, by - h - 10);

    // Demonstration Points (all suboptimal)
    const pts = [
      { x: bx + 60, y: by - 30, label: 'τ_1 (Tệ: Score 20)' },
      { x: bx + 160, y: by - 65, label: 'τ_2 (TB: Score 45)' },
      { x: bx + 270, y: by - 105, label: 'τ_3 (Khá: Score 70)' }
    ];

    pts.forEach(p => {
      ctx.fillStyle = '#ef4444';
      ctx.beginPath(); ctx.arc(p.x, p.y, 6, 0, 2*Math.PI); ctx.fill();
      ctx.fillStyle = '#94a3b8'; ctx.font = '11px Inter, sans-serif';
      ctx.fillText(p.label, p.x - 30, p.y - 12);
    });

    // Extrapolated Curve beyond expert demonstrations (T-REX)
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3; ctx.beginPath();
    ctx.moveTo(bx, by);
    for (let x = 0; x <= w; x += 10) {
      const yVal = by - (x / w) * (h - 20) * 1.1;
      ctx.lineTo(bx + x, yVal);
    }
    ctx.stroke();

    // Extrapolated Peak (Super-human performance)
    const peakX = bx + 420, peakY = by - 145;
    ctx.fillStyle = '#10b981';
    ctx.beginPath(); ctx.arc(peakX, peakY, 9, 0, 2*Math.PI); ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('⭐ T-REX Ngoại suy: Điểm 95 (Vượt chuyên gia!)', peakX - 110, peakY - 18);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('T-REX: NGOẠI SUY PHẦN THƯỞNG TỪ QUỸ ĐẠO KHÔNG HOÀN HẢO', 60, 35);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 11: Cross-Embodiment Correspondence Mapping
// ============================================================================
function initSim11() {
  const canvas = document.getElementById('sim-canvas-11');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let t = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    t += 0.02;

    ctx.save();
    // Human Hand (Left)
    const hx = 200, hy = 160;
    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('BÀN TAY NGƯỜI (5 NGÓN)', hx - 65, hy - 70);

    // Simplified palm and fingers
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 4;
    ctx.strokeRect(hx - 25, hy - 15, 50, 50);
    const pinch = Math.sin(t) * 15;
    // Thumb & Index pinch motion
    ctx.beginPath(); ctx.moveTo(hx - 20, hy - 15); ctx.lineTo(hx - 25 + pinch, hy - 45); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(hx + 20, hy - 15); ctx.lineTo(hx + 25 - pinch, hy - 45); ctx.stroke();

    // Mapping Arrow in Middle
    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 4;
    ctx.beginPath(); ctx.moveTo(310, hy); ctx.lineTo(390, hy); ctx.stroke();
    ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('Ánh Xạ Tọa Độ Cặp Điểm', 285, hy - 15);

    // Parallel Gripper (Right)
    const rx = 500, ry = 160;
    ctx.fillStyle = '#10b981'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('TAY KẸP ROBOT (PARALLEL 2-JAW)', rx - 80, ry - 70);

    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 5;
    // Gripper base
    ctx.strokeRect(rx - 30, ry, 60, 25);
    // Two fingers
    const gripGap = 25 - pinch * 0.8;
    ctx.fillRect(rx - gripGap - 8, ry - 45, 8, 45);
    ctx.fillRect(rx + gripGap, ry - 45, 8, 45);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('CORRESPONDENCE PROBLEM: ĐỒNG BỘ ĐIỂM TIẾP XÚC GIỮA NGƯỜI & ROBOT', 60, 35);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 12: Shared Autonomy Alpha-Blending Controller
// ============================================================================
function initSim12() {
  const canvas = document.getElementById('sim-canvas-12');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const aSlider = document.getElementById('sim12-alpha');
  const aVal = document.getElementById('sim12-a-val');

  let t = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    t += 0.03;
    const alpha = aSlider ? parseFloat(aSlider.value) : 0.6;
    if (aVal) aVal.textContent = 'Trọng số người α = ' + alpha.toFixed(2);

    ctx.save();
    // Path through a narrow corridor
    ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(50, 100); ctx.lineTo(650, 100); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(50, 220); ctx.lineTo(650, 220); ctx.stroke();

    // Human input (noisy, hand tremor)
    const rawHumanY = 160 + Math.sin(t * 3) * 45;
    // Robot safety controller target (center line 160)
    const robotSafeY = 160;
    // Blended output: u = alpha * u_human + (1 - alpha) * u_robot
    const blendedY = alpha * rawHumanY + (1 - alpha) * robotSafeY;

    // Draw robot avatar
    ctx.fillStyle = '#6366f1';
    ctx.beginPath(); ctx.arc(350, blendedY, 18, 0, 2*Math.PI); ctx.fill();
    ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 2; ctx.stroke();

    // Visual indicators
    ctx.fillStyle = '#ef4444'; ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Ranh giới cấm va chạm (Hành lang an toàn)', 60, 90);
    ctx.fillText('Ranh giới cấm va chạm', 60, 235);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('TỰ CHỦ CHIA SẺ (SHARED AUTONOMY): u = α·u_human + (1-α)·u_safe', 60, 40);
    ctx.fillStyle = alpha > 0.8 && Math.abs(blendedY - 160) > 40 ? '#ef4444' : '#10b981';
    ctx.font = 'bold 14px monospace';
    ctx.fillText(Math.abs(blendedY - 160) > 40 ? '⚠️ CẢNH BÁO: RUNG TAY SUÝT VA CHẠM! (Tăng can thiệp robot 1-α)' : '✅ Robot can thiệp giữ vị trí an toàn', 60, 65);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 13: Dynamic Time Warping (DTW) & Jerk Metric
// ============================================================================
function initSim13() {
  const canvas = document.getElementById('sim-canvas-13');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    ctx.save();

    // Reference trajectory P_ref (Green)
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3; ctx.beginPath();
    const refPts = [];
    for (let x = 80; x <= 620; x += 15) {
      const y = 110 + 40 * Math.sin((x - 80) * 0.015);
      refPts.push({x, y});
      if (x === 80) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Robot execution trajectory P_rob (Blue with time lag)
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3; ctx.beginPath();
    const robPts = [];
    for (let x = 80; x <= 620; x += 15) {
      const y = 200 + 45 * Math.sin((x - 120) * 0.015);
      robPts.push({x, y});
      if (x === 80) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // DTW alignment lines (dashed gray)
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)'; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
    for (let i = 0; i < refPts.length; i += 3) {
      const j = Math.min(robPts.length - 1, Math.max(0, i + 2));
      ctx.beginPath(); ctx.moveTo(refPts[i].x, refPts[i].y); ctx.lineTo(robPts[j].x, robPts[j].y); ctx.stroke();
    }
    ctx.setLineDash([]);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('ĐÁNH GIÁ QUỸ ĐẠO BẰNG DYNAMIC TIME WARPING (DTW) & CHỈ SỐ JERK', 60, 40);
    ctx.fillStyle = '#10b981'; ctx.font = '12px Inter, sans-serif';
    ctx.fillText('— Quỹ đạo chuẩn Chuyên gia (P_ref)', 60, 65);
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('— Quỹ đạo Thực thi Robot (P_rob có trễ thời gian)', 320, 65);

    ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 14px monospace';
    ctx.fillText('Khoảng cách DTW: 12.45 mm | Độ giật Jerk: 4.82 m/s³ (Rất êm mượt)', 60, 265);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 14: ALOHA LeRobot 50 Hz Action Chunking Loop
// ============================================================================
function initSim14() {
  const canvas = document.getElementById('sim-canvas-14');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const rateHistory = [];

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    // Simulate 50 Hz execution loop (target dt = 20 ms)
    const targetMs = 20.0;
    const actualMs = targetMs + (Math.random() - 0.5) * 1.8;
    rateHistory.push(actualMs);
    if (rateHistory.length > 180) rateHistory.shift();

    ctx.save();
    // Target Line 20ms (50 Hz)
    const targetY = 160;
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(60, targetY); ctx.lineTo(640, targetY); ctx.stroke();

    // Actual latency curve
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2;
    ctx.beginPath();
    for (let i = 0; i < rateHistory.length; i++) {
      const px = 60 + i * 3.2;
      const py = targetY - (rateHistory[i] - 20.0) * 15;
      if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('VÒNG LẶP SUY LUẬN LE-ROBOT / ALOHA ACTION CHUNKING (50 Hz / 20 ms)', 60, 40);
    ctx.fillStyle = '#10b981'; ctx.font = 'bold 13px monospace';
    ctx.fillText(`Chu kỳ mục tiêu: 20.00 ms (50 Hz) | Thực tế: ${actualMs.toFixed(2)} ms | Chunk Size: 16 bước`, 60, 65);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}
