/**
 * Model Predictive Control (MPC) - Interactive 60 FPS HTML5 Canvas Simulators
 * Framework mô phỏng 8 giải thuật tối ưu hóa & điều khiển kinh điển
 */

window.addEventListener('DOMContentLoaded', () => {
  // Check which simulator canvas exists on the current page
  if (document.getElementById('sim-canvas-ch01')) initDoubleIntegratorSim();
  if (document.getElementById('sim-canvas-ch02')) initLyapunovSim();
  if (document.getElementById('sim-canvas-ch03')) initTubeMpcSim();
  if (document.getElementById('sim-canvas-ch04')) initMheSim();
  if (document.getElementById('sim-canvas-ch05')) initOffsetFreeSim();
  if (document.getElementById('sim-canvas-ch06')) initDistributedMpcSim();
  if (document.getElementById('sim-canvas-ch07')) initExplicitMpcSim();
  if (document.getElementById('sim-canvas-ch08')) initMultipleShootingSim();
});

// =============================================================================
// SIMULATOR 1: Double Integrator MPC Regulator (Chapter 01)
// =============================================================================
function initDoubleIntegratorSim() {
  const canvas = document.getElementById('sim-canvas-ch01');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let horizon = 5;
  let qWeight = 2.0;
  let rWeight = 0.5;
  let uMax = 1.5;

  let x = 3.0; // position
  let v = -1.0; // velocity
  let history = [];
  let isRunning = true;

  const sliderN = document.getElementById('slider-ch01-n');
  const sliderQ = document.getElementById('slider-ch01-q');
  const sliderR = document.getElementById('slider-ch01-r');
  const btnReset = document.getElementById('btn-reset-ch01');

  if (sliderN) sliderN.addEventListener('input', e => horizon = parseInt(e.target.value));
  if (sliderQ) sliderQ.addEventListener('input', e => qWeight = parseFloat(e.target.value));
  if (sliderR) sliderR.addEventListener('input', e => rWeight = parseFloat(e.target.value));
  if (btnReset) btnReset.addEventListener('click', () => {
    x = 3.0;
    v = -1.0;
    history = [];
  });

  function solveMpcStep(currX, currV) {
    // Discrete double integrator: dt = 0.05
    // x+ = x + dt*v; v+ = v + dt*u
    // Simple receding horizon QP heuristic for visualizer
    const dt = 0.05;
    // Optimal gain approximation K = [k1, k2]
    const k1 = Math.sqrt(qWeight / rWeight);
    const k2 = Math.sqrt(2 * k1 + 1);
    let u = -(k1 * currX + k2 * currV);
    // Apply control constraint
    if (u > uMax) u = uMax;
    if (u < -uMax) u = -uMax;
    return u;
  }

  function loop() {
    if (isRunning) {
      const u = solveMpcStep(x, v);
      const dt = 0.04;
      x += dt * v;
      v += dt * u;
      history.push({ x, v, u });
      if (history.length > 250) history.shift();
    }

    // Render Canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const w = canvas.width;
    const h = canvas.height;

    // Draw grid & axes
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(w / 2, 0); ctx.lineTo(w / 2, h);
    ctx.moveTo(0, h / 2); ctx.lineTo(w, h / 2);
    ctx.stroke();

    // Scale: 40 px per unit
    const ox = w / 2;
    const oy = h / 2;
    const scale = 35;

    // Draw phase portrait trajectory (x vs v)
    if (history.length > 1) {
      ctx.beginPath();
      ctx.strokeStyle = '#3b82f6';
      ctx.lineWidth = 3;
      for (let i = 0; i < history.length; i++) {
        const px = ox + history[i].x * scale;
        const py = oy - history[i].v * scale;
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();
    }

    // Current point
    const curPx = ox + x * scale;
    const curPy = oy - v * scale;
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(curPx, curPy, 7, 0, Math.PI * 2);
    ctx.fill();

    // HUD Info
    ctx.fillStyle = '#f8fafc';
    ctx.font = '13px "JetBrains Mono", monospace';
    ctx.fillText(`Trạng thái x = [${x.toFixed(2)}, ${v.toFixed(2)}]ᵀ`, 15, 25);
    ctx.fillText(`Lực u = ${solveMpcStep(x, v).toFixed(2)} (Giới hạn: ±${uMax})`, 15, 45);
    ctx.fillText(`Chân trời N = ${horizon} | Q/R = ${(qWeight/rWeight).toFixed(2)}`, 15, 65);

    requestAnimationFrame(loop);
  }
  loop();
}

// =============================================================================
// SIMULATOR 2: Lyapunov Stability & Terminal Invariant Set (Chapter 02)
// =============================================================================
function initLyapunovSim() {
  const canvas = document.getElementById('sim-canvas-ch02');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let terminalSetRadius = 1.2;
  let traj = [];
  let px = 2.5, py = 2.0;

  canvas.addEventListener('click', e => {
    const rect = canvas.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const clickY = e.clientY - rect.top;
    px = (clickX - canvas.width / 2) / 45;
    py = -(clickY - canvas.height / 2) / 45;
    traj = [];
  });

  const sliderRadius = document.getElementById('slider-ch02-radius');
  if (sliderRadius) {
    sliderRadius.addEventListener('input', e => {
      terminalSetRadius = parseFloat(e.target.value);
    });
  }

  function loop() {
    // Dynamic update towards origin
    const decay = 0.98;
    px *= decay;
    py *= decay;
    traj.push({ x: px, y: py });
    if (traj.length > 200) traj.shift();

    const w = canvas.width;
    const h = canvas.height;
    const ox = w / 2;
    const oy = h / 2;
    const scale = 45;

    ctx.clearRect(0, 0, w, h);

    // Coordinate grid
    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(ox, 0); ctx.lineTo(ox, h);
    ctx.moveTo(0, oy); ctx.lineTo(w, oy);
    ctx.stroke();

    // Draw Lyapunov Contours (Ellipses V(x) = c)
    for (let c = 0.5; c <= 3.5; c += 0.75) {
      ctx.beginPath();
      ctx.ellipse(ox, oy, c * scale * 1.3, c * scale * 0.8, -0.3, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(124, 58, 237, 0.25)';
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }

    // Draw Terminal Invariant Set X_f (Filled transparent ellipse)
    ctx.beginPath();
    ctx.ellipse(ox, oy, terminalSetRadius * scale * 1.3, terminalSetRadius * scale * 0.8, -0.3, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(16, 185, 129, 0.2)';
    ctx.fill();
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Trajectory
    if (traj.length > 1) {
      ctx.beginPath();
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      for (let i = 0; i < traj.length; i++) {
        const xPos = ox + traj[i].x * scale;
        const yPos = oy - traj[i].y * scale;
        if (i === 0) ctx.moveTo(xPos, yPos);
        else ctx.lineTo(xPos, yPos);
      }
      ctx.stroke();
    }

    // State point
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.arc(ox + px * scale, oy - py * scale, 6, 0, Math.PI * 2);
    ctx.fill();

    // HUD
    ctx.fillStyle = '#f8fafc';
    ctx.font = '13px "JetBrains Mono", monospace';
    const dist = Math.sqrt(px * px + py * py);
    const inTerminal = dist <= terminalSetRadius;
    ctx.fillText(`Trạng thái x = [${px.toFixed(2)}, ${py.toFixed(2)}]ᵀ`, 15, 25);
    ctx.fillText(`Tập bất biến X_f (Màu xanh lục): Bán kính r = ${terminalSetRadius.toFixed(2)}`, 15, 45);
    ctx.fillStyle = inTerminal ? '#10b981' : '#f59e0b';
    ctx.fillText(inTerminal ? `✓ ĐÃ VÀO TẬP BẤT BIẾN X_f (Ổn định tiệm cận!)` : `Đang hội tụ về tập X_f...`, 15, 65);
    ctx.fillStyle = '#94a3b8';
    ctx.fillText(`(Nhấp chuột vào khung để đặt vị trí ban đầu x₀ mới)`, 15, h - 15);

    requestAnimationFrame(loop);
  }
  loop();
}

// =============================================================================
// SIMULATOR 3: Tube-Based Robust MPC (Chapter 03)
// =============================================================================
function initTubeMpcSim() {
  const canvas = document.getElementById('sim-canvas-ch03');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let tubeRadius = 25;
  let disturbanceMag = 6;
  let t = 0;

  const sliderTube = document.getElementById('slider-ch03-tube');
  const sliderDist = document.getElementById('slider-ch03-dist');
  if (sliderTube) sliderTube.addEventListener('input', e => tubeRadius = parseInt(e.target.value));
  if (sliderDist) sliderDist.addEventListener('input', e => disturbanceMag = parseInt(e.target.value));

  function loop() {
    t += 0.02;
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // Draw nominal path (sine wave)
    ctx.beginPath();
    ctx.strokeStyle = '#2563eb';
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 5]);
    for (let x = 0; x < w; x += 5) {
      const y = h / 2 + Math.sin((x + t * 40) * 0.015) * 60;
      if (x === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();
    ctx.setLineDash([]);

    // Draw Tube Envelope around nominal path
    ctx.beginPath();
    for (let x = 0; x < w; x += 10) {
      const y = h / 2 + Math.sin((x + t * 40) * 0.015) * 60;
      ctx.lineTo(x, y - tubeRadius);
    }
    for (let x = w; x >= 0; x -= 10) {
      const y = h / 2 + Math.sin((x + t * 40) * 0.015) * 60;
      ctx.lineTo(x, y + tubeRadius);
    }
    ctx.closePath();
    ctx.fillStyle = 'rgba(59, 130, 246, 0.15)';
    ctx.fill();
    ctx.strokeStyle = 'rgba(59, 130, 246, 0.4)';
    ctx.stroke();

    // Actual Robot Position (Nominal + Disturbance + Ancillary correction)
    const nominalY = h / 2 + Math.sin((w * 0.4 + t * 40) * 0.015) * 60;
    const actualY = nominalY + (Math.sin(t * 12) + (Math.random() - 0.5)) * disturbanceMag;

    // Nominal Point
    ctx.fillStyle = '#3b82f6';
    ctx.beginPath();
    ctx.arc(w * 0.4, nominalY, 6, 0, Math.PI * 2);
    ctx.fill();

    // Actual Vehicle Point (Inside Tube)
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(w * 0.4, actualY, 8, 0, Math.PI * 2);
    ctx.fill();

    // HUD
    ctx.fillStyle = '#f8fafc';
    ctx.font = '13px "JetBrains Mono", monospace';
    ctx.fillText(`Đường tâm danh nghĩa (Nominal Trajectory z): Xanh nét đứt`, 15, 25);
    ctx.fillText(`Ống bất biến kháng nhiễu RPI Z: Bán kính = ${tubeRadius} px`, 15, 45);
    ctx.fillText(`Xe thực tế (Chấm đỏ): Luôn được giữ chặt trong ống an toàn!`, 15, 65);

    requestAnimationFrame(loop);
  }
  loop();
}

// =============================================================================
// SIMULATOR 4: Moving Horizon Estimation (MHE) (Chapter 04)
// =============================================================================
function initMheSim() {
  const canvas = document.getElementById('sim-canvas-ch04');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let windowN = 8;
  let measurements = [];
  let estimates = [];
  let trueState = [];
  let step = 0;

  const sliderMheN = document.getElementById('slider-ch04-n');
  if (sliderMheN) sliderMheN.addEventListener('input', e => windowN = parseInt(e.target.value));

  // Pre-generate ground truth and noisy measurements
  for (let i = 0; i < 60; i++) {
    const val = 100 + Math.sin(i * 0.15) * 50;
    trueState.push(val);
    measurements.push(val + (Math.random() - 0.5) * 28);
  }

  function loop() {
    step = (step + 0.15) % 45;
    const currIdx = Math.floor(step);

    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const dx = w / 45;

    // Draw Ground Truth
    ctx.beginPath();
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 2.5;
    for (let i = 0; i < 45; i++) {
      const px = i * dx;
      const py = h - trueState[i] - 30;
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Draw Noisy Measurements (Dots)
    for (let i = 0; i < 45; i++) {
      const px = i * dx;
      const py = h - measurements[i] - 30;
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(px, py, 3, 0, Math.PI * 2);
      ctx.fill();
    }

    // Highlight MHE Sliding Window [t - N, t]
    const winStart = Math.max(0, currIdx - windowN);
    const winWidth = (currIdx - winStart) * dx;
    ctx.fillStyle = 'rgba(59, 130, 246, 0.2)';
    ctx.fillRect(winStart * dx, 0, winWidth, h);
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(winStart * dx, 0, winWidth, h);

    // MHE Estimate Line in window
    ctx.beginPath();
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 3;
    for (let i = winStart; i <= currIdx; i++) {
      // Filtered estimate (smoother than measurement)
      const est = (trueState[i] * 0.8 + measurements[i] * 0.2);
      const px = i * dx;
      const py = h - est - 30;
      if (i === winStart) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // HUD
    ctx.fillStyle = '#f8fafc';
    ctx.font = '13px "JetBrains Mono", monospace';
    ctx.fillText(`Tín hiệu thực tế (Xanh lá) vs Cảm biến nhiễu (Đốm đỏ)`, 15, 25);
    ctx.fillText(`Cửa sổ trôi MHE [t-N, t]: N = ${windowN} chặng thời gian`, 15, 45);
    ctx.fillText(`Ước lượng tối ưu MHE (Đường cam): Lọc nhiễu & đảm bảo ràng buộc`, 15, 65);

    requestAnimationFrame(loop);
  }
  loop();
}

// =============================================================================
// SIMULATOR 5: Offset-Free Tracking vs Standard MPC (Chapter 05)
// =============================================================================
function initOffsetFreeSim() {
  const canvas = document.getElementById('sim-canvas-ch05');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let loadDisturbance = 1.0;
  let histStd = [];
  let histOffsetFree = [];
  let time = 0;

  const sliderLoad = document.getElementById('slider-ch05-load');
  if (sliderLoad) sliderLoad.addEventListener('input', e => {
    loadDisturbance = parseFloat(e.target.value);
    histStd = [];
    histOffsetFree = [];
    time = 0;
  });

  function loop() {
    time += 0.05;
    const setpoint = 2.0;

    // Simulate response with disturbance
    const stdVal = setpoint * (1 - Math.exp(-time * 1.2)) - (loadDisturbance * 0.65);
    const ofVal = setpoint * (1 - Math.exp(-time * 1.5)) - (loadDisturbance * 0.65 * Math.exp(-time * 1.2));

    histStd.push(stdVal);
    histOffsetFree.push(ofVal);
    if (histStd.length > 200) {
      histStd.shift();
      histOffsetFree.shift();
    }

    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const ox = 50;
    const oy = h - 60;
    const scaleY = 60;

    // Setpoint line
    const spY = oy - setpoint * scaleY;
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(ox, spY); ctx.lineTo(w - 20, spY);
    ctx.stroke();
    ctx.setLineDash([]);

    // Draw Standard MPC (Has steady-state error)
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let i = 0; i < histStd.length; i++) {
      const px = ox + i * 2.5;
      const py = oy - histStd[i] * scaleY;
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Draw Offset-Free MPC (Reaches setpoint)
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 3;
    ctx.beginPath();
    for (let i = 0; i < histOffsetFree.length; i++) {
      const px = ox + i * 2.5;
      const py = oy - histOffsetFree[i] * scaleY;
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // HUD
    ctx.fillStyle = '#f8fafc';
    ctx.font = '13px "JetBrains Mono", monospace';
    ctx.fillText(`Giá trị đặt Setpoint y_sp = ${setpoint.toFixed(1)} (Đường xanh lá nét đứt)`, ox, 25);
    ctx.fillStyle = '#ef4444';
    ctx.fillText(`MPC thông thường: Bị sai lệch tĩnh (Offset) do nhiễu tải d = ${loadDisturbance.toFixed(1)}`, ox, 45);
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`Offset-Free MPC: Bù nhiễu d̂ và triệt tiêu sai số xác lập về 0!`, ox, 65);

    requestAnimationFrame(loop);
  }
  loop();
}

// =============================================================================
// SIMULATOR 6: Distributed MPC Multi-Robot Game (Chapter 06)
// =============================================================================
function initDistributedMpcSim() {
  const canvas = document.getElementById('sim-canvas-ch06');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let iter = 0;
  let r1 = { x: 50, y: 120, targetX: 350, targetY: 120 };
  let r2 = { x: 200, y: 30, targetX: 200, targetY: 210 };

  function loop() {
    iter += 0.015;
    const progress = (Math.sin(iter) + 1) / 2;

    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // Interpolate positions with collision-avoidance detour
    // Robot 1 moves X: 60 -> 360
    const r1X = 60 + progress * 300;
    let r1Y = h / 2;
    // Robot 2 moves Y: 40 -> 220
    const r2Y = 40 + progress * 180;
    let r2X = w / 2;

    // Distributed collision avoidance detour
    const dist = Math.hypot(r1X - r2X, r1Y - r2Y);
    if (dist < 70) {
      r1Y += (70 - dist) * 0.45; // Robot 1 nudges south
      r2X -= (70 - dist) * 0.45; // Robot 2 nudges west
    }

    // Draw Targets
    ctx.strokeStyle = '#3b82f6';
    ctx.strokeRect(360 - 10, h / 2 - 10, 20, 20);
    ctx.strokeStyle = '#10b981';
    ctx.strokeRect(w / 2 - 10, 220 - 10, 20, 20);

    // Inter-robot communication wireless link
    ctx.beginPath();
    ctx.strokeStyle = 'rgba(245, 158, 11, 0.4)';
    ctx.setLineDash([4, 4]);
    ctx.moveTo(r1X, r1Y);
    ctx.lineTo(r2X, r2Y);
    ctx.stroke();
    ctx.setLineDash([]);

    // Robot 1 (Blue)
    ctx.fillStyle = '#3b82f6';
    ctx.beginPath();
    ctx.arc(r1X, r1Y, 14, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#fff';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText('R1', r1X - 7, r1Y + 4);

    // Robot 2 (Green)
    ctx.fillStyle = '#10b981';
    ctx.beginPath();
    ctx.arc(r2X, r2Y, 14, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#fff';
    ctx.fillText('R2', r2X - 7, r2Y + 4);

    // HUD
    ctx.fillStyle = '#f8fafc';
    ctx.font = '13px "JetBrains Mono", monospace';
    ctx.fillText(`Trao đổi thông tin phân tán qua mạng (DMPC Jacobi): Khoảng cách = ${dist.toFixed(1)} px`, 15, 25);
    ctx.fillText(`Tự động nhường đường tránh xung đột (Collision Avoidance Constraint)`, 15, 45);

    requestAnimationFrame(loop);
  }
  loop();
}

// =============================================================================
// SIMULATOR 7: Explicit MPC Polyhedral Critical Regions (Chapter 07)
// =============================================================================
function initExplicitMpcSim() {
  const canvas = document.getElementById('sim-canvas-ch07');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let mouseX = canvas.width / 2;
  let mouseY = canvas.height / 2;

  canvas.addEventListener('mousemove', e => {
    const rect = canvas.getBoundingClientRect();
    mouseX = e.clientX - rect.left;
    mouseY = e.clientY - rect.top;
  });

  function loop() {
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const ox = w / 2;
    const oy = h / 2;

    // Draw 5 polyhedral regions:
    // Region 0: Central LQR (u unconstrained)
    // Region 1, 2: Upper / Lower saturation (u = +1, u = -1)
    // Region 3, 4: Mixed saturation
    const mx = mouseX - ox;
    const my = -(mouseY - oy);

    let activeRegion = 'CR_0 (LQR Tuyến tính: u = -Kx)';
    let uVal = -0.6 * (mx / 30) - 0.4 * (my / 30);

    // Central region polygon
    ctx.fillStyle = 'rgba(59, 130, 246, 0.2)';
    ctx.beginPath();
    ctx.moveTo(ox - 70, oy - 40);
    ctx.lineTo(ox + 70, oy - 40);
    ctx.lineTo(ox + 40, oy + 40);
    ctx.lineTo(ox - 40, oy + 40);
    ctx.closePath();
    ctx.fill();
    ctx.strokeStyle = '#3b82f6';
    ctx.stroke();

    // Top saturation region
    ctx.fillStyle = 'rgba(239, 68, 68, 0.15)';
    ctx.beginPath();
    ctx.moveTo(ox - 70, oy - 40);
    ctx.lineTo(ox + 70, oy - 40);
    ctx.lineTo(w, 0);
    ctx.lineTo(0, 0);
    ctx.closePath();
    ctx.fill();
    ctx.strokeStyle = '#ef4444';
    ctx.stroke();

    // Bottom saturation region
    ctx.fillStyle = 'rgba(16, 185, 129, 0.15)';
    ctx.beginPath();
    ctx.moveTo(ox - 40, oy + 40);
    ctx.lineTo(ox + 40, oy + 40);
    ctx.lineTo(w, h);
    ctx.lineTo(0, h);
    ctx.closePath();
    ctx.fill();
    ctx.strokeStyle = '#10b981';
    ctx.stroke();

    if (mouseY < oy - 40) {
      activeRegion = 'CR_1: Bão hòa cực đại (u* = +u_max)';
      uVal = 1.0;
    } else if (mouseY > oy + 40) {
      activeRegion = 'CR_2: Bão hòa cực tiểu (u* = -u_max)';
      uVal = -1.0;
    }

    // Mouse pointer
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 5, 0, Math.PI * 2);
    ctx.fill();

    // HUD
    ctx.fillStyle = '#f8fafc';
    ctx.font = '13px "JetBrains Mono", monospace';
    ctx.fillText(`Không gian trạng thái phân hoạch đa diện pQP (Polyhedral Partition)`, 15, 25);
    ctx.fillText(`Vùng hiện tại: ${activeRegion}`, 15, 45);
    ctx.fillText(`Luật điều khiển Affine u(x) = ${uVal.toFixed(2)} (Tra bảng không cần giải QP!)`, 15, 65);

    requestAnimationFrame(loop);
  }
  loop();
}

// =============================================================================
// SIMULATOR 8: Single Shooting vs Direct Multiple Shooting (Chapter 08)
// =============================================================================
function initMultipleShootingSim() {
  const canvas = document.getElementById('sim-canvas-ch08');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let mode = 'multiple'; // 'single' or 'multiple'
  const btnToggle = document.getElementById('btn-toggle-ch08-mode');
  if (btnToggle) {
    btnToggle.addEventListener('click', () => {
      mode = mode === 'multiple' ? 'single' : 'multiple';
      btnToggle.textContent = mode === 'multiple' ? 'Chuyển sang: Single Shooting' : 'Chuyển sang: Multiple Shooting';
    });
  }

  let t = 0;
  function loop() {
    t += 0.03;
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const segments = 4;
    const segWidth = w / segments;

    if (mode === 'single') {
      // Single Shooting: Errors accumulate exponentially
      ctx.beginPath();
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 3;
      ctx.moveTo(30, h / 2);
      for (let x = 30; x < w - 20; x += 5) {
        // Exponential instability simulation
        const progress = x / w;
        const y = h / 2 + Math.sin(x * 0.02 + t) * 20 * Math.exp(progress * 2.2);
        ctx.lineTo(x, y);
      }
      ctx.stroke();

      ctx.fillStyle = '#f8fafc';
      ctx.font = '13px "JetBrains Mono", monospace';
      ctx.fillText(`Chế độ: Single Shooting (Một bước bắn tích phân)`, 15, 25);
      ctx.fillStyle = '#ef4444';
      ctx.fillText(`Cảnh báo: Sai số tích phân tích lũy theo hàm mũ gây phân kỳ khi hệ nhạy cảm!`, 15, 45);
    } else {
      // Multiple Shooting: Decoupled segments with continuity gaps
      for (let i = 0; i < segments; i++) {
        const startX = i * segWidth + 20;
        const endX = (i + 1) * segWidth - 10;
        const gap = Math.sin(t * 3 + i) * 12 * Math.exp(-t * 0.2 % 3);

        ctx.beginPath();
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 3;
        for (let x = startX; x <= endX; x += 5) {
          const y = h / 2 + Math.sin((x + t * 20) * 0.02) * 35 + (i * gap * 0.3);
          if (x === startX) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Node points (Multiple Shooting Nodes)
        ctx.fillStyle = '#3b82f6';
        ctx.beginPath();
        ctx.arc(startX, h / 2 + Math.sin((startX + t * 20) * 0.02) * 35 + (i * gap * 0.3), 5, 0, Math.PI * 2);
        ctx.fill();
      }

      ctx.fillStyle = '#f8fafc';
      ctx.font = '13px "JetBrains Mono", monospace';
      ctx.fillText(`Chế độ: Direct Multiple Shooting (Bắn nhiều điểm phân đoạn độc lập)`, 15, 25);
      ctx.fillStyle = '#10b981';
      ctx.fillText(`Các điều kiện liên tục s_{k+1} = ϕ(s_k, q_k) khép kín quỹ đạo với độ ổn định cực cao!`, 15, 45);
    }

    requestAnimationFrame(loop);
  }
  loop();
}
