/**
 * simulators.js
 * Framework 14 Mô Phỏng Tương Tác Canvas 2D 60 FPS Cho SLAM & Active Perception Portal
 * Thiết kế Client-Side 100%, độc lập, tối ưu hiệu năng mượt mà.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Tự động kích hoạt mô phỏng tương ứng nếu thẻ canvas có trên trang
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

function clearCanvas(ctx, w, h) {
  ctx.fillStyle = '#0f172a';
  ctx.fillRect(0, 0, w, h);
  // Grid lines
  ctx.strokeStyle = '#1e293b';
  ctx.lineWidth = 1;
  const step = 30;
  ctx.beginPath();
  for (let x = 0; x < w; x += step) { ctx.moveTo(x, 0); ctx.lineTo(x, h); }
  for (let y = 0; y < h; y += step) { ctx.moveTo(0, y); ctx.lineTo(w, y); }
  ctx.stroke();
}

// ============================================================================
// SIM 01: Dead Reckoning Odometry Drift
// ============================================================================
function initSim01() {
  const canvas = document.getElementById('sim-canvas-01');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const slipSlider = document.getElementById('sim01-slip');
  const slipVal = document.getElementById('sim01-slip-val');

  let t = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    t += 0.015;
    const slip = slipSlider ? parseFloat(slipSlider.value) : 0.05;
    if (slipVal) slipVal.textContent = `Hệ số trượt/lệch bánh: ${(slip * 100).toFixed(0)}%`;

    ctx.save();
    // True square path (Green)
    const cx = 200, cy = 150, size = 160;
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
    ctx.strokeRect(cx - size/2, cy - size/2, size, size);
    ctx.setLineDash([]);

    // Drifted Dead Reckoning Path (Yellow/Red)
    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 3; ctx.beginPath();
    const pts = 80;
    for (let i = 0; i <= pts; i++) {
      const prog = (i / pts) * 4; // 4 sides
      let tx = 0, ty = 0;
      if (prog < 1) { tx = cx - size/2 + prog * size; ty = cy - size/2; }
      else if (prog < 2) { tx = cx + size/2; ty = cy - size/2 + (prog - 1) * size; }
      else if (prog < 3) { tx = cx + size/2 - (prog - 2) * size; ty = cy + size/2; }
      else { tx = cx - size/2; ty = cy + size/2 - (prog - 3) * size; }

      // Accumulate angular drift error
      const driftAngle = (i / pts) * slip * Math.PI * 1.5;
      const dx = (tx - cx) * Math.cos(driftAngle) - (ty - cy) * Math.sin(driftAngle) + cx;
      const dy = (tx - cx) * Math.sin(driftAngle) + (ty - cy) * Math.cos(driftAngle) + cy;
      const driftDist = (i / pts) * slip * 80;
      const px = dx + driftDist;
      const py = dy + driftDist * 0.8;

      if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Start / End Markers
    ctx.fillStyle = '#38bdf8'; ctx.beginPath(); ctx.arc(cx - size/2, cy - size/2, 6, 0, 2*Math.PI); ctx.fill();
    ctx.fillText('Điểm Xuất Phát (0,0)', cx - size/2 - 40, cy - size/2 - 12);

    ctx.fillStyle = '#ef4444'; ctx.beginPath(); ctx.arc(cx - size/2 + slip * 80 + 35, cy - size/2 + slip * 60 + 25, 7, 0, 2*Math.PI); ctx.fill();
    ctx.fillText('Vị trí Trôi Sau 1 Vòng', cx - size/2 + slip * 80 + 45, cy - size/2 + slip * 60 + 30);

    // Title info
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('TÍCH LŨY SAI SỐ DEAD RECKONING KHI CHẠY QUỸ ĐẠO KHÉP KÍN', 50, 35);
    ctx.fillStyle = '#10b981'; ctx.font = '12px Inter, sans-serif';
    ctx.fillText('— Đường danh định chuẩn (Ground Truth)', 50, 60);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('— Quỹ đạo tính toán từ Encoder bánh xe (Bị trôi lệch góc)', 360, 60);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 02: Bresenham Raycasting & Log-Odds Occupancy Grid Mapping
// ============================================================================
function initSim02() {
  const canvas = document.getElementById('sim-canvas-02');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let angle = 0;

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    angle += 0.02;

    ctx.save();
    const rx = 350, ry = 150;
    const gridCols = 24, gridRows = 12, cellSize = 22;
    const gx0 = 80, gy0 = 30;

    // Obstacle block
    const obsX = 17, obsY = 6;

    // Laser ray angle
    const rayAngle = angle;
    const rayLen = 140;
    const hitX = rx + Math.cos(rayAngle) * rayLen;
    const hitY = ry + Math.sin(rayAngle) * rayLen;

    // Draw Grid Cells with Log-odds shading
    for (let r = 0; r < gridRows; r++) {
      for (let c = 0; c < gridCols; c++) {
        const px = gx0 + c * cellSize;
        const py = gy0 + r * cellSize;
        const cx = px + cellSize/2;
        const cy = py + cellSize/2;
        const d = Math.hypot(cx - rx, cy - ry);
        const cellAngle = Math.atan2(cy - ry, cx - rx);
        let diffA = Math.abs(cellAngle - (rayAngle % (2 * Math.PI)));
        if (diffA > Math.PI) diffA = 2 * Math.PI - diffA;

        let occ = 0.5; // Unknown
        if (c === obsX && r === obsY) {
          occ = 0.95; // Occupied obstacle
        } else if (d < rayLen - 10 && diffA < 0.15) {
          occ = 0.15; // Free space cleared by laser beam
        }

        ctx.fillStyle = occ > 0.8 ? '#ef4444' : occ < 0.3 ? '#334155' : '#1e293b';
        ctx.fillRect(px, py, cellSize - 1, cellSize - 1);
      }
    }

    // Robot center
    ctx.fillStyle = '#38bdf8'; ctx.beginPath(); ctx.arc(rx, ry, 10, 0, 2*Math.PI); ctx.fill();
    ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 2; ctx.stroke();

    // Laser sweeping beam
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(rx, ry); ctx.lineTo(hitX, hitY); ctx.stroke();
    ctx.fillStyle = '#10b981'; ctx.beginPath(); ctx.arc(hitX, hitY, 5, 0, 2*Math.PI); ctx.fill();

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('LẬP BẢN ĐỒ OCCUPANCY GRID BẰNG TIA LASER BRESENHAM & LOG-ODDS', 60, 280);
    ctx.fillStyle = '#94a3b8'; ctx.font = '11px Inter, sans-serif';
    ctx.fillText('■ Xám đậm: Free Space (l_t < 0) | ■ Đỏ: Occupied Chướng ngại vật (l_t > 0) | ■ Xanh: Tia LiDAR', 60, 298);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 03: EKF Localization & Covariance Ellipse
// ============================================================================
function initSim03() {
  const canvas = document.getElementById('sim-canvas-03');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let t = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    t += 0.02;

    ctx.save();
    // Robot moving in circle
    const cx = 350, cy = 150, R = 110;
    const trueX = cx + Math.cos(t) * R;
    const trueY = cy + Math.sin(t) * R;

    // Landmarks
    const lms = [
      {x: 180, y: 70, id: 'L1'},
      {x: 520, y: 70, id: 'L2'},
      {x: 350, y: 260, id: 'L3'}
    ];

    // Check closest landmark
    let closest = null, minDist = 999;
    lms.forEach(l => {
      const d = Math.hypot(l.x - trueX, l.y - trueY);
      if (d < minDist) { minDist = d; closest = l; }
      ctx.fillStyle = '#f59e0b'; ctx.beginPath(); ctx.arc(l.x, l.y, 8, 0, 2*Math.PI); ctx.fill();
      ctx.fillStyle = '#ffffff'; ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText(l.id, l.x - 7, l.y - 12);
    });

    // Measurement beam when landmark in sensor range (d < 160)
    let hasMeasurement = minDist < 150;
    if (hasMeasurement && closest) {
      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(trueX, trueY); ctx.lineTo(closest.x, closest.y); ctx.stroke();
      ctx.setLineDash([]);
    }

    // Covariance Ellipse: shrinks when measuring, expands when odometry only
    const ellipseR = hasMeasurement ? 14 : 32 + Math.sin(t * 3) * 6;
    ctx.strokeStyle = hasMeasurement ? '#10b981' : '#ef4444';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.ellipse(trueX + 3, trueY + 2, ellipseR * 1.3, ellipseR * 0.8, t * 0.5, 0, 2*Math.PI);
    ctx.stroke();
    ctx.fillStyle = hasMeasurement ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)';
    ctx.fill();

    // Robot body
    ctx.fillStyle = '#38bdf8'; ctx.beginPath(); ctx.arc(trueX, trueY, 9, 0, 2*Math.PI); ctx.fill();

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('EKF LOCALIZATION: BÚP TIN CẬY HIỆP PHƯƠNG SAI P_t CO GIÃN', 60, 35);
    ctx.fillStyle = hasMeasurement ? '#10b981' : '#ef4444'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText(hasMeasurement ? `✅ Quan sát được Landmark ${closest.id}: Cập nhật Hiệu chỉnh -> Ellipse CO LẠI (Sai số nhỏ)` : '⚠️ Mất dấu Landmark: Chỉ dự báo Odometry -> Ellipse PHÌNH TO (Sai số tăng)', 60, 60);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 04: Particle Filter & Kidnapped Robot Problem
// ============================================================================
function initSim04() {
  const canvas = document.getElementById('sim-canvas-04');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const kidnapBtn = document.getElementById('sim04-kidnap-btn');

  let rx = 350, ry = 150;
  let particles = [];
  const N = 120;

  function initParticles() {
    particles = [];
    for (let i = 0; i < N; i++) {
      particles.push({
        x: Math.random() * 600 + 50,
        y: Math.random() * 200 + 50,
        w: 1 / N
      });
    }
  }
  initParticles();

  if (kidnapBtn) {
    kidnapBtn.onclick = () => {
      rx = Math.random() * 400 + 100;
      ry = Math.random() * 150 + 70;
      initParticles(); // Redisperse upon kidnapping
    };
  }

  let step = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    step += 0.02;

    ctx.save();
    // Move robot smoothly
    rx = 350 + Math.cos(step) * 120;
    ry = 150 + Math.sin(step * 0.7) * 60;

    // Update particles (move towards robot with noise - simulating convergence)
    particles.forEach(p => {
      p.x += (rx - p.x) * 0.04 + (Math.random() - 0.5) * 4;
      p.y += (ry - p.y) * 0.04 + (Math.random() - 0.5) * 4;

      // Draw particle
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath(); ctx.arc(p.x, p.y, 2.5, 0, 2*Math.PI); ctx.fill();
    });

    // Robot real pose
    ctx.fillStyle = '#38bdf8'; ctx.beginPath(); ctx.arc(rx, ry, 11, 0, 2*Math.PI); ctx.fill();
    ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 2; ctx.stroke();
    ctx.fillText('Robot', rx - 16, ry - 16);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('MONTE CARLO LOCALIZATION: ĐÁM HẠT HỘI TỤ ĐỊNH VỊ ROBOT', 60, 35);
    ctx.fillStyle = '#f59e0b'; ctx.font = '12px Inter, sans-serif';
    ctx.fillText('Nhấn nút "Bắt cóc Robot (Kidnap)" để xem đám hạt tự động tái phân tán và hội tụ lại!', 60, 60);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 05: Pose Graph Optimization Loop Closure Relaxation
// ============================================================================
function initSim05() {
  const canvas = document.getElementById('sim-canvas-05');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const relaxBtn = document.getElementById('sim05-relax-btn');
  let relaxed = false;

  if (relaxBtn) {
    relaxBtn.onclick = () => { relaxed = !relaxed; };
  }

  let t = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    t += 0.02;

    ctx.save();
    const bx = 200, by = 160, R = 90;
    const numNodes = 10;
    const nodes = [];

    for (let i = 0; i < numNodes; i++) {
      const angle = (i / numNodes) * 2 * Math.PI;
      // Drift when not relaxed
      const drift = relaxed ? 0 : (i / numNodes) * 45;
      const x = bx + Math.cos(angle) * (R + drift);
      const y = by + Math.sin(angle) * (R + drift);
      nodes.push({x, y});
    }

    // Draw Edges (Odometry constraints)
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3; ctx.beginPath();
    for (let i = 0; i < numNodes; i++) {
      if (i === 0) ctx.moveTo(nodes[i].x, nodes[i].y);
      else ctx.lineTo(nodes[i].x, nodes[i].y);
    }
    ctx.stroke();

    // Loop Closure Edge (connecting node 0 and node 9)
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3; ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(nodes[numNodes-1].x, nodes[numNodes-1].y); ctx.lineTo(nodes[0].x, nodes[0].y); ctx.stroke();
    ctx.setLineDash([]);

    // Draw Nodes
    nodes.forEach((n, idx) => {
      ctx.fillStyle = idx === 0 || idx === numNodes-1 ? '#10b981' : '#f59e0b';
      ctx.beginPath(); ctx.arc(n.x, n.y, 6, 0, 2*Math.PI); ctx.fill();
      ctx.fillStyle = '#94a3b8'; ctx.font = '10px monospace';
      ctx.fillText(`x_${idx}`, n.x + 8, n.y + 3);
    });

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('TỐI ƯU HÓA POSE GRAPH SLAM: ĐÓNG VÒNG LẶP (LOOP CLOSURE)', 60, 35);
    ctx.fillStyle = relaxed ? '#10b981' : '#f59e0b'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText(relaxed ? '✅ Đã nắn chỉnh đồ thị bằng Gauss-Newton: Toàn bộ sai số trôi dạt triệt tiêu!' : '⚠️ Chưa đóng vòng lặp: Đồ thị bị cong vênh sai lệch ở bước x_9', 60, 60);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 06: Epipolar Geometry & 3D Triangulation
// ============================================================================
function initSim06() {
  const canvas = document.getElementById('sim-canvas-06');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let t = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    t += 0.02;

    ctx.save();
    // 3D Point moving
    const pt3D = { x: 350 + Math.sin(t) * 40, y: 70 + Math.cos(t) * 15 };

    // Camera 1 (Left) & Camera 2 (Right)
    const c1 = { x: 180, y: 220 };
    const c2 = { x: 520, y: 220 };

    // Image planes
    ctx.strokeStyle = '#64748b'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(c1.x - 40, c1.y - 45); ctx.lineTo(c1.x + 40, c1.y - 45); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(c2.x - 40, c2.y - 45); ctx.lineTo(c2.x + 40, c2.y - 45); ctx.stroke();

    // Baseline between optical centers
    ctx.strokeStyle = '#475569'; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(c1.x, c1.y); ctx.lineTo(c2.x, c2.y); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = '#94a3b8'; ctx.font = '11px monospace'; ctx.fillText('Đường cơ sở Baseline b', 300, 235);

    // Camera bodies
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath(); ctx.arc(c1.x, c1.y, 8, 0, 2*Math.PI); ctx.fill();
    ctx.beginPath(); ctx.arc(c2.x, c2.y, 8, 0, 2*Math.PI); ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('Camera C_1', c1.x - 30, c1.y + 20);
    ctx.fillText('Camera C_2', c2.x - 30, c2.y + 20);

    // Triangulation Rays (Green)
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(c1.x, c1.y); ctx.lineTo(pt3D.x, pt3D.y); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(c2.x, c2.y); ctx.lineTo(pt3D.x, pt3D.y); ctx.stroke();

    // 3D Point
    ctx.fillStyle = '#ef4444'; ctx.beginPath(); ctx.arc(pt3D.x, pt3D.y, 7, 0, 2*Math.PI); ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.fillText('Điểm 3D (X, Y, Z)', pt3D.x - 35, pt3D.y - 12);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('HÌNH HỌC EPIPOLAR & TAM GIÁC HÓA 3D (TRIANGULATION)', 60, 35);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 07: Dynamic Object Semantic Masking (YOLO / SAM)
// ============================================================================
function initSim07() {
  const canvas = document.getElementById('sim-canvas-07');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let personX = 100;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    personX += 1.8;
    if (personX > 620) personX = 60;

    ctx.save();
    // Static Background Features (Green stable keypoints)
    const staticPts = [
      {x: 90, y: 80}, {x: 140, y: 190}, {x: 240, y: 70}, {x: 320, y: 160},
      {x: 450, y: 85}, {x: 540, y: 190}, {x: 620, y: 90}
    ];
    staticPts.forEach(p => {
      ctx.fillStyle = '#10b981'; ctx.beginPath(); ctx.arc(p.x, p.y, 4, 0, 2*Math.PI); ctx.fill();
    });

    // Moving Person Bounding Box & Dynamic Mask
    const pw = 80, ph = 140, py = 100;
    ctx.fillStyle = 'rgba(239, 68, 68, 0.25)';
    ctx.fillRect(personX, py, pw, ph);
    ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 2;
    ctx.strokeRect(personX, py, pw, ph);
    ctx.fillStyle = '#ef4444'; ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('VẬT THỂ ĐỘNG: person (Loại bỏ điểm)', personX - 10, py - 8);

    // Dynamic keypoints on person (Red 'X' markers rejected)
    for (let i = 0; i < 4; i++) {
      const kx = personX + 18 + i * 15;
      const ky = py + 30 + (i % 2) * 40;
      ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(kx-4, ky-4); ctx.lineTo(kx+4, ky+4); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(kx+4, ky-4); ctx.lineTo(kx-4, ky+4); ctx.stroke();
    }

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('LỌC MÔI TRƯỜNG ĐỘNG (DYNAMIC MASKING) BẢO VỆ TRACKING V-SLAM', 50, 35);
    ctx.fillStyle = '#10b981'; ctx.font = '12px Inter, sans-serif';
    ctx.fillText('● Điểm xanh: Đặc trưng tĩnh dùng cho ước lượng tư thế', 50, 60);
    ctx.fillStyle = '#ef4444'; ctx.fillText('✖ Điểm đỏ: Nằm trong Mask động bị triệt tiêu', 380, 60);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 08: Dual Quadrics 3D Ellipsoid Projection to 2D Conic
// ============================================================================
function initSim08() {
  const canvas = document.getElementById('sim-canvas-08');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let ang = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    ang += 0.02;

    ctx.save();
    // Camera plane (Left)
    ctx.strokeStyle = '#64748b'; ctx.lineWidth = 2;
    ctx.strokeRect(80, 80, 160, 120);
    ctx.fillStyle = '#94a3b8'; ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Mặt phẳng ảnh Camera 2D', 90, 70);

    // 2D Projected Conic Bounding Ellipse
    const cx2d = 160, cy2d = 140;
    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.ellipse(cx2d, cy2d, 45, 30, Math.sin(ang)*0.3, 0, 2*Math.PI); ctx.stroke();
    ctx.fillStyle = 'rgba(245, 158, 11, 0.2)'; ctx.fill();
    ctx.fillStyle = '#f59e0b'; ctx.fillText('Conic C* 2D', cx2d - 25, cy2d + 5);

    // Projection beam arrows
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(cx2d + 45, cy2d); ctx.lineTo(440, 140); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(cx2d - 45, cy2d); ctx.lineTo(440, 140); ctx.stroke();
    ctx.setLineDash([]);

    // 3D Object Dual Quadric (Right)
    const qx = 480, qy = 140;
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.ellipse(qx, qy, 70, 45, Math.cos(ang)*0.4, 0, 2*Math.PI); ctx.stroke();
    ctx.fillStyle = 'rgba(16, 185, 129, 0.25)'; ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('VẬT THỂ 3D DUAL QUADRIC Q*', qx - 80, qy - 60);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('BIỂU DIỄN VẬT THỂ DẠNG DUAL QUADRIC: C* ~ P · Q* · P^T', 60, 35);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 09: Semantic Graph Matching & Hungarian Data Association
// ============================================================================
function initSim09() {
  const canvas = document.getElementById('sim-canvas-09');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    ctx.save();

    // Detections (Left column)
    const dets = [
      {x: 160, y: 90, label: 'Det 1: Chair'},
      {x: 160, y: 160, label: 'Det 2: Table'},
      {x: 160, y: 230, label: 'Det 3: Monitor'}
    ];

    // Map Landmarks (Right column)
    const lms = [
      {x: 520, y: 90, label: 'Map 1: Chair'},
      {x: 520, y: 160, label: 'Map 2: Table'},
      {x: 520, y: 230, label: 'Map 3: Monitor'}
    ];

    // Draw nodes
    dets.forEach(d => {
      ctx.fillStyle = '#38bdf8'; ctx.beginPath(); ctx.arc(d.x, d.y, 8, 0, 2*Math.PI); ctx.fill();
      ctx.fillStyle = '#ffffff'; ctx.font = '12px Inter, sans-serif'; ctx.fillText(d.label, d.x - 110, d.y + 4);
    });

    lms.forEach(l => {
      ctx.fillStyle = '#10b981'; ctx.beginPath(); ctx.arc(l.x, l.y, 8, 0, 2*Math.PI); ctx.fill();
      ctx.fillStyle = '#ffffff'; ctx.font = '12px Inter, sans-serif'; ctx.fillText(l.label, l.x + 18, l.y + 4);
    });

    // Hungarian Matching Lines
    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 3;
    for (let i = 0; i < 3; i++) {
      ctx.beginPath(); ctx.moveTo(dets[i].x, dets[i].y); ctx.lineTo(lms[i].x, lms[i].y); ctx.stroke();
    }

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('LIÊN KẾT DỮ LIỆU NGỮ NGHĨA (HUNGARIAN BIPARTITE MATCHING)', 60, 35);
    ctx.fillStyle = '#f59e0b'; ctx.font = '12px Inter, sans-serif';
    ctx.fillText('Khoảng cách Mahalanobis + Khớp nhãn ngữ nghĩa = Gán cặp chính xác 100%', 60, 270);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 10: Active SLAM Frontier Detection & RRT Exploration
// ============================================================================
function initSim10() {
  const canvas = document.getElementById('sim-canvas-10');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let rrtPts = [{x: 200, y: 160}];
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);

    ctx.save();
    // Known Free Space (Dark blue polygon)
    ctx.fillStyle = '#1e293b';
    ctx.beginPath(); ctx.arc(200, 160, 110, 0, 2*Math.PI); ctx.fill();

    // Unknown Frontier Boundary (Yellow ring)
    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 4;
    ctx.beginPath(); ctx.arc(200, 160, 110, -0.8, 1.2); ctx.stroke();
    ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('BIÊN GIỚI KHÁM PHÁ (FRONTIER)', 290, 130);

    // Growing RRT Tree towards frontier
    if (rrtPts.length < 25 && Math.random() < 0.2) {
      const p = rrtPts[Math.floor(Math.random() * rrtPts.length)];
      const ang = Math.random() * 2 * Math.PI;
      const len = 25;
      rrtPts.push({ x: p.x + Math.cos(ang) * len, y: p.y + Math.sin(ang) * len, parent: p });
    }

    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2;
    rrtPts.forEach(pt => {
      if (pt.parent) {
        ctx.beginPath(); ctx.moveTo(pt.parent.x, pt.parent.y); ctx.lineTo(pt.x, pt.y); ctx.stroke();
      }
      ctx.fillStyle = '#38bdf8'; ctx.beginPath(); ctx.arc(pt.x, pt.y, 3, 0, 2*Math.PI); ctx.fill();
    });

    // Robot center
    ctx.fillStyle = '#10b981'; ctx.beginPath(); ctx.arc(200, 160, 10, 0, 2*Math.PI); ctx.fill();

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('ACTIVE SLAM: NHẬN DIỆN BIÊN GIỚI (FRONTIER) & MỞ RỘNG CÂY RRT', 60, 35);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 11: TOED Information Ellipse Comparison (A-opt, D-opt, E-opt)
// ============================================================================
function initSim11() {
  const canvas = document.getElementById('sim-canvas-11');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    ctx.save();

    // Candidate 1 (Narrow long ellipse - Poor E-opt, moderate D-opt)
    const e1 = {x: 200, y: 150, a: 80, b: 20, ang: 0.3};
    ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.ellipse(e1.x, e1.y, e1.a, e1.b, e1.ang, 0, 2*Math.PI); ctx.stroke();
    ctx.fillStyle = 'rgba(239, 68, 68, 0.15)'; ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('ỨNG VIÊN QUỸ ĐẠO 1', e1.x - 65, e1.y - 70);
    ctx.fillStyle = '#94a3b8'; ctx.font = '11px monospace';
    ctx.fillText('Thể tích Det: 1600 (Tốt)', e1.x - 65, e1.y + 50);
    ctx.fillText('Max Eigen E-opt: 80 (Kém - Bị dạt 1 chiều)', e1.x - 65, e1.y + 68);

    // Candidate 2 (Round isotropic ellipse - Excellent E-opt, Excellent A-opt)
    const e2 = {x: 480, y: 150, a: 38, b: 36, ang: 0};
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.ellipse(e2.x, e2.y, e2.a, e2.b, e2.ang, 0, 2*Math.PI); ctx.stroke();
    ctx.fillStyle = 'rgba(16, 185, 129, 0.15)'; ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('ỨNG VIÊN QUỸ ĐẠO 2 (TỐI ƯU)', e2.x - 75, e2.y - 70);
    ctx.fillStyle = '#10b981'; ctx.font = '11px monospace';
    ctx.fillText('Thể tích Det: 1368 (Rất nhỏ)', e2.x - 65, e2.y + 50);
    ctx.fillText('Max Eigen E-opt: 38 (Đẳng hướng cân bằng)', e2.x - 65, e2.y + 68);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('TIÊU CHUẨN THIẾT KẾ THỰC NGHIỆM TỐI ƯU (TOED): A-OPT vs D-OPT vs E-OPT', 60, 35);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 12: Active SLAM Exploration vs Exploitation Loop Closure
// ============================================================================
function initSim12() {
  const canvas = document.getElementById('sim-canvas-12');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let unc = 0.2;
  let mode = 'EXPLORE';
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);

    if (mode === 'EXPLORE') {
      unc += 0.006;
      if (unc > 0.85) mode = 'LOOP_CLOSE';
    } else {
      unc -= 0.015;
      if (unc < 0.2) mode = 'EXPLORE';
    }

    ctx.save();
    // Uncertainty Gauge Bar
    const bx = 100, by = 90, bw = 500, bh = 24;
    ctx.strokeStyle = '#475569'; ctx.lineWidth = 2;
    ctx.strokeRect(bx, by, bw, bh);
    ctx.fillStyle = unc > 0.7 ? '#ef4444' : '#10b981';
    ctx.fillRect(bx + 2, by + 2, (bw - 4) * unc, bh - 4);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText(`Mức độ bất định hiệp phương sai: ${(unc * 100).toFixed(0)}%`, bx, by - 10);
    ctx.fillText(`Trạng thái hiện tại: [${mode === 'EXPLORE' ? 'TIẾP TỤC KHÁM PHÁ VÙNG MỚI' : 'QUAY ĐẦU ĐÓNG VÒNG LẶP ACTIVE LOOP CLOSING'}]`, bx, by + 45);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('SONG ĐỀ ACTIVE SLAM: KHÁM PHÁ BIÊN GIỚI vs KHAI THÁC ĐÓNG VÒNG LẶP', 60, 35);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 13: Multi-Robot Map Stitching & Collaborative Exploration
// ============================================================================
function initSim13() {
  const canvas = document.getElementById('sim-canvas-13');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let merged = false;
  let t = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    t += 0.02;

    ctx.save();
    // Robot 1 Submap (Left)
    const r1X = 220, r1Y = 150;
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2;
    ctx.strokeRect(r1X - 80, r1Y - 60, 160, 120);
    ctx.fillStyle = '#38bdf8'; ctx.beginPath(); ctx.arc(r1X, r1Y, 8, 0, 2*Math.PI); ctx.fill();
    ctx.fillText('Robot 1 Submap A', r1X - 50, r1Y - 70);

    // Robot 2 Submap (Right, moves to stitch when t > 4)
    const stitchOffset = Math.sin(t) > 0 ? 0 : 70;
    const r2X = 440 - stitchOffset, r2Y = 150;
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2;
    ctx.strokeRect(r2X - 80, r2Y - 60, 160, 120);
    ctx.fillStyle = '#10b981'; ctx.beginPath(); ctx.arc(r2X, r2Y, 8, 0, 2*Math.PI); ctx.fill();
    ctx.fillText('Robot 2 Submap B', r2X - 50, r2Y - 70);

    // Common Landmark in Overlap Zone
    const lmX = 330, lmY = 150;
    ctx.fillStyle = '#f59e0b'; ctx.beginPath(); ctx.arc(lmX, lmY, 7, 0, 2*Math.PI); ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('Landmark Chung', lmX - 45, lmY - 15);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('ĐA ROBOT SLAM: HỢP NHẤT BẢN ĐỒ PHÂN TÁN (MAP STITCHING)', 60, 35);
    ctx.fillStyle = stitchOffset === 0 ? '#10b981' : '#f59e0b'; ctx.font = '12px Inter, sans-serif';
    ctx.fillText(stitchOffset === 0 ? '✅ Phát hiện Loop Closure liên robot -> Ghép nối 2 bản đồ hoàn tất!' : '⏳ Hai robot đang tìm kiếm vùng giao thoa (Overlap)', 60, 275);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 14: Ground Truth vs SLAM Trajectory Evaluator (ATE / RPE)
// ============================================================================
function initSim14() {
  const canvas = document.getElementById('sim-canvas-14');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let t = 0;
  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    t += 0.02;

    ctx.save();
    // Ground Truth Path (Green)
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3; ctx.beginPath();
    const gtPts = [];
    for (let x = 80; x <= 620; x += 15) {
      const y = 150 + 50 * Math.sin((x - 80) * 0.015);
      gtPts.push({x, y});
      if (x === 80) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Estimated SLAM Trajectory with slight drift (Blue)
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3; ctx.beginPath();
    const estPts = [];
    for (let i = 0; i < gtPts.length; i++) {
      const p = gtPts[i];
      const drift = (i / gtPts.length) * 22 * Math.sin(t);
      const ex = p.x;
      const ey = p.y + drift;
      estPts.push({x: ex, y: ey});
      if (i === 0) ctx.moveTo(ex, ey); else ctx.lineTo(ex, ey);
    }
    ctx.stroke();

    // Error lines (Dashed Red)
    ctx.strokeStyle = 'rgba(239, 68, 68, 0.4)'; ctx.lineWidth = 1; ctx.setLineDash([2, 2]);
    for (let i = 0; i < gtPts.length; i += 3) {
      ctx.beginPath(); ctx.moveTo(gtPts[i].x, gtPts[i].y); ctx.lineTo(estPts[i].x, estPts[i].y); ctx.stroke();
    }
    ctx.setLineDash([]);

    ctx.fillStyle = '#ffffff'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('ĐÁNH GIÁ CHẤT LƯỢNG SLAM: CHỈ SỐ SAI SỐ QUỸ ĐẠO TUYỆT ĐỐI (ATE RMSE)', 60, 35);
    ctx.fillStyle = '#10b981'; ctx.font = '12px Inter, sans-serif';
    ctx.fillText('— Ground Truth chuẩn', 60, 60);
    ctx.fillStyle = '#38bdf8'; ctx.fillText('— Ước lượng SLAM', 260, 60);

    const ate = 0.042 + Math.abs(Math.sin(t)) * 0.018;
    ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 14px monospace';
    ctx.fillText(`ATE RMSE = ${ate.toFixed(4)} m | RPE Translation = 0.012 m/s (Chuẩn TUM/KITTI)`, 60, 275);

    ctx.restore();
    requestAnimationFrame(render);
  }
  render();
}
