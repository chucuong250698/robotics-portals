/**
 * Analytical System Dynamics: Modeling and Simulation (Prof. Brian C. Fabien, Springer)
 * Interactive 60 FPS HTML5 Canvas Simulators:
 *  1. initPaynterEnergySim - Ch 1: Unified Multi-Domain Paynter Energy & Bond Variables
 *  2. initFourBarKinematicsSim - Ch 2: Planar 4-Bar Mechanism Kinematics & Coriolis Vector Field
 *  3. initChaoticDoublePendulumSim - Ch 3: Chaotic Double Pendulum Euler-Lagrange Dynamics (RK4)
 *  4. initNonholonomicWheeledSim - Ch 4: Nonholonomic Wheeled Robot & Lagrange Multiplier Constraint Force
 *  5. initBaumgarteDriftSim - Ch 5: DAE Constraint Drift vs Baumgarte Stabilization (Index Reduction)
 *  6. initLyapunovPhaseVectorSim - Ch 6: Nonlinear Phase Portrait, Vector Field & Lyapunov Contours
 */

// Helper: Setup High-DPI Canvas
function setupHiDPICanvas(canvas) {
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  const width = rect.width || canvas.width;
  const height = rect.height || canvas.height;
  canvas.width = width * dpr;
  canvas.height = height * dpr;
  const ctx = canvas.getContext('2d');
  ctx.scale(dpr, dpr);
  return { ctx, width, height, dpr };
}

// =============================================================================
// SIMULATOR 1: Paynter Unified Multi-Domain Energy Exchange (Ch 1)
// =============================================================================
function initPaynterEnergySim(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;

  const sliderI = document.getElementById('sim1-i'); // Inductor / Mass
  const sliderC = document.getElementById('sim1-c'); // Capacitor / Spring
  const sliderR = document.getElementById('sim1-r'); // Resistor / Damper
  const resetBtn = document.getElementById('sim1-reset');

  let I = sliderI ? parseFloat(sliderI.value) : 1.0;
  let C = sliderC ? parseFloat(sliderC.value) : 1.0;
  let R = sliderR ? parseFloat(sliderR.value) : 0.2;

  // System state: displacement q, momentum p (flow f = p/I, effort e = q/C)
  let q = 1.8;
  let p = 0.0;
  let time = 0;
  const dt = 0.02;

  let history = [];
  const maxHistory = 150;

  function reset() {
    q = 1.8;
    p = 0.0;
    time = 0;
    history = [];
  }

  if (resetBtn) resetBtn.addEventListener('click', reset);
  if (sliderI) sliderI.addEventListener('input', (e) => { I = parseFloat(e.target.value); });
  if (sliderC) sliderC.addEventListener('input', (e) => { C = parseFloat(e.target.value); });
  if (sliderR) sliderR.addEventListener('input', (e) => { R = parseFloat(e.target.value); });

  function stepPhysics() {
    // State equations:
    // dq/dt = f = p / I
    // dp/dt = -e - e_R = - (q / C) - R * (p / I)
    const f = p / I;
    const e_c = q / C;
    const e_r = R * f;

    const dq = f;
    const dp = -e_c - e_r;

    q += dq * dt;
    p += dp * dt;
    time += dt;

    const Ek = 0.5 * (p * p) / I;      // Kinetic coenergy in I
    const Ep = 0.5 * (q * q) / C;      // Potential energy in C
    const E_total = Ek + Ep;

    history.push({ time, q, f, Ek, Ep, E_total });
    if (history.length > maxHistory) history.shift();
  }

  function render() {
    const { ctx, width, height } = setupHiDPICanvas(canvas);
    ctx.clearRect(0, 0, width, height);

    stepPhysics();

    // Background Grid
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    ctx.lineWidth = 1;
    for (let x = 0; x < width; x += 40) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
    }
    for (let y = 0; y < height; y += 40) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
    }

    // Left Panel: Physical Mass-Spring-Damper (or RLC equivalent)
    const leftW = width * 0.45;
    const centerY = height * 0.45;
    const originX = 60;
    const massX = originX + 100 + q * 35;

    // Fixed wall
    ctx.fillStyle = '#475569';
    ctx.fillRect(originX - 15, centerY - 50, 15, 100);
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 2;
    for (let y = centerY - 45; y < centerY + 45; y += 12) {
      ctx.beginPath(); ctx.moveTo(originX - 15, y); ctx.lineTo(originX - 5, y + 8); ctx.stroke();
    }

    // Spring (C)
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(originX, centerY - 15);
    const coils = 10;
    const springLen = massX - originX - 30;
    for (let i = 0; i <= coils; i++) {
      const sx = originX + (i / coils) * springLen;
      const sy = centerY - 15 + (i % 2 === 0 ? -12 : 12);
      ctx.lineTo(sx, sy);
    }
    ctx.lineTo(massX - 30, centerY - 15);
    ctx.stroke();

    // Damper (R)
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(originX, centerY + 20);
    ctx.lineTo(originX + springLen * 0.5, centerY + 20);
    ctx.stroke();

    // Damper cylinder & piston
    const dampX = originX + springLen * 0.5;
    ctx.fillStyle = '#334155';
    ctx.fillRect(dampX, centerY + 12, 25, 16);
    ctx.strokeStyle = '#cbd5e1';
    ctx.beginPath();
    ctx.moveTo(dampX + 12, centerY + 15);
    ctx.lineTo(massX - 30, centerY + 20);
    ctx.stroke();

    // Mass block (I)
    ctx.fillStyle = '#2563eb';
    ctx.strokeStyle = '#60a5fa';
    ctx.lineWidth = 2;
    ctx.fillRect(massX - 30, centerY - 35, 60, 70);
    ctx.strokeRect(massX - 30, centerY - 35, 60, 70);

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Khối I', massX, centerY - 5);
    ctx.font = '11px monospace';
    ctx.fillText(`p=${p.toFixed(2)}`, massX, centerY + 12);

    // Labels
    ctx.fillStyle = '#38bdf8';
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(`Tụ C: ${C.toFixed(1)} F/m`, originX + springLen * 0.5, centerY - 35);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`Trở R: ${R.toFixed(2)} Ns/m`, originX + springLen * 0.5, centerY + 45);

    // Right Panel: Paynter Energy Bar & Time Curves
    const rightX = width * 0.52;
    const rightW = width * 0.44;

    ctx.fillStyle = '#94a3b8';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('CÂN BẰNG NĂNG LƯỢNG PAYNTER (TỨ DIỆN TRẠNG THÁI)', rightX, 28);

    const latest = history[history.length - 1] || { Ek: 0, Ep: 0, E_total: 0 };
    const maxBarW = rightW - 40;
    const scaleE = 50;

    // Energy Bars
    const barY = 50;
    ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
    ctx.fillRect(rightX, barY, maxBarW, 16);
    ctx.fillRect(rightX, barY + 28, maxBarW, 16);

    // Ek Bar
    const ekW = Math.min(maxBarW, latest.Ek * scaleE);
    ctx.fillStyle = '#3b82f6';
    ctx.fillRect(rightX, barY, ekW, 16);
    ctx.fillStyle = '#f1f5f9';
    ctx.font = '11px monospace';
    ctx.fillText(`Động năng E_I (p²/2I) = ${latest.Ek.toFixed(3)} J`, rightX + 6, barY + 12);

    // Ep Bar
    const epW = Math.min(maxBarW, latest.Ep * scaleE);
    ctx.fillStyle = '#06b6d4';
    ctx.fillRect(rightX, barY + 28, epW, 16);
    ctx.fillStyle = '#f1f5f9';
    ctx.fillText(`Thế năng E_C (q²/2C) = ${latest.Ep.toFixed(3)} J`, rightX + 6, barY + 40);

    // Waveform Graph: q(t) & f(t)
    const graphY = 130;
    const graphH = height - graphY - 25;
    ctx.fillStyle = 'rgba(15, 23, 42, 0.6)';
    ctx.fillRect(rightX, graphY, rightW, graphH);
    ctx.strokeStyle = '#334155';
    ctx.strokeRect(rightX, graphY, rightW, graphH);

    // Zero line
    const zeroY = graphY + graphH * 0.5;
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(rightX, zeroY); ctx.lineTo(rightX + rightW, zeroY);
    ctx.stroke();
    ctx.setLineDash([]);

    if (history.length > 1) {
      // Draw q(t)
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i < history.length; i++) {
        const hx = rightX + (i / maxHistory) * rightW;
        const hy = zeroY - history[i].q * 25;
        if (i === 0) ctx.moveTo(hx, hy);
        else ctx.lineTo(hx, hy);
      }
      ctx.stroke();

      // Draw f(t)
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let i = 0; i < history.length; i++) {
        const hx = rightX + (i / maxHistory) * rightW;
        const hy = zeroY - history[i].f * 25;
        if (i === 0) ctx.moveTo(hx, hy);
        else ctx.lineTo(hx, hy);
      }
      ctx.stroke();
    }

    // Legend
    ctx.fillStyle = '#38bdf8';
    ctx.font = '11px sans-serif';
    ctx.fillText('— Dịch chuyển q(t)', rightX + 10, height - 10);
    ctx.fillStyle = '#f43f5e';
    ctx.fillText('— Dòng chảy f(t) = dq/dt', rightX + 140, height - 10);

    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
}

// =============================================================================
// SIMULATOR 2: Planar 4-Bar Mechanism & Coriolis Acceleration (Ch 2)
// =============================================================================
function initFourBarKinematicsSim(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;

  const sliderOmega = document.getElementById('sim2-omega');
  const sliderCrank = document.getElementById('sim2-crank');
  const resetBtn = document.getElementById('sim2-reset');

  let omega2 = sliderOmega ? parseFloat(sliderOmega.value) : 1.5; // rad/s
  let r2 = sliderCrank ? parseFloat(sliderCrank.value) : 60;     // Crank length
  let theta2 = 0.5; // Current crank angle (rad)

  // Ground link r1, Coupler r3, Rocker r4
  const r1 = 180; // Distance O2 to O4
  const r3 = 160; // Coupler AB
  const r4 = 130; // Rocker BO4

  let couplerPath = [];
  const maxPath = 200;

  if (sliderOmega) sliderOmega.addEventListener('input', (e) => { omega2 = parseFloat(e.target.value); });
  if (sliderCrank) sliderCrank.addEventListener('input', (e) => { 
    r2 = parseFloat(e.target.value); 
    couplerPath = [];
  });
  if (resetBtn) resetBtn.addEventListener('click', () => {
    theta2 = 0.5;
    couplerPath = [];
  });

  // Solve Freudenstein 4-bar position loop closure
  function solveFourBar(th2) {
    // Crank tip A
    const Ax = r2 * Math.cos(th2);
    const Ay = r2 * Math.sin(th2);

    // Distance from A to O4 (O4 is at (r1, 0))
    const dAx = r1 - Ax;
    const dAy = -Ay;
    const d = Math.sqrt(dAx * dAx + dAy * dAy);

    // Check Grashof reachability
    if (d > r3 + r4 || d < Math.abs(r3 - r4)) {
      return null; // Cannot close loop
    }

    // Angle of vector from A to O4
    const alpha = Math.atan2(-Ay, r1 - Ax);

    // Law of cosines for triangle A - B - O4
    const cosBeta = (r3 * r3 + d * d - r4 * r4) / (2 * r3 * d);
    const beta = Math.acos(Math.max(-1, Math.min(1, cosBeta)));

    // Coupler angle theta3
    const th3 = alpha + beta;
    const Bx = Ax + r3 * Math.cos(th3);
    const By = Ay + r3 * Math.sin(th3);

    // Rocker angle theta4
    const th4 = Math.atan2(By, Bx - r1);

    // Coupler Point P (midpoint + perpendicular offset for coupler curve)
    const Px = Ax + 0.5 * r3 * Math.cos(th3) - 30 * Math.sin(th3);
    const Py = Ay + 0.5 * r3 * Math.sin(th3) + 30 * Math.cos(th3);

    return { Ax, Ay, Bx, By, Px, Py, th3, th4 };
  }

  function render() {
    const { ctx, width, height } = setupHiDPICanvas(canvas);
    ctx.clearRect(0, 0, width, height);

    theta2 += omega2 * 0.016;
    if (theta2 > 2 * Math.PI) theta2 -= 2 * Math.PI;

    const sol = solveFourBar(theta2);

    const originX = width * 0.28;
    const originY = height * 0.65;

    // Draw Ground Link O2 - O4
    ctx.fillStyle = '#64748b';
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(originX, originY);
    ctx.lineTo(originX + r1, originY);
    ctx.stroke();

    // Pivots O2, O4
    ctx.fillStyle = '#0f172a';
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 3;
    ctx.beginPath(); ctx.arc(originX, originY, 7, 0, 2*Math.PI); ctx.fill(); ctx.stroke();
    ctx.beginPath(); ctx.arc(originX + r1, originY, 7, 0, 2*Math.PI); ctx.fill(); ctx.stroke();

    ctx.fillStyle = '#94a3b8';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('O₂ (Khớp quay 1)', originX - 10, originY + 22);
    ctx.fillText('O₄ (Khớp quay 4)', originX + r1 - 10, originY + 22);

    if (sol) {
      const ax = originX + sol.Ax;
      const ay = originY - sol.Ay; // Inverted Y for screen coords
      const bx = originX + sol.Bx;
      const by = originY - sol.By;
      const px = originX + sol.Px;
      const py = originY - sol.Py;

      // Update coupler path
      couplerPath.push({ x: px, y: py });
      if (couplerPath.length > maxPath) couplerPath.shift();

      // Draw Coupler Curve
      if (couplerPath.length > 2) {
        ctx.strokeStyle = 'rgba(236, 72, 153, 0.6)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let i = 0; i < couplerPath.length; i++) {
          if (i === 0) ctx.moveTo(couplerPath[i].x, couplerPath[i].y);
          else ctx.lineTo(couplerPath[i].x, couplerPath[i].y);
        }
        ctx.stroke();
      }

      // Draw Crank (r2 - Blue)
      ctx.strokeStyle = '#2563eb';
      ctx.lineWidth = 5;
      ctx.beginPath(); ctx.moveTo(originX, originY); ctx.lineTo(ax, ay); ctx.stroke();

      // Draw Coupler Triangle (r3 - Purple)
      ctx.fillStyle = 'rgba(124, 58, 237, 0.15)';
      ctx.strokeStyle = '#7c3aed';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(ax, ay);
      ctx.lineTo(bx, by);
      ctx.lineTo(px, py);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Draw Rocker (r4 - Emerald)
      ctx.strokeStyle = '#059669';
      ctx.lineWidth = 5;
      ctx.beginPath(); ctx.moveTo(originX + r1, originY); ctx.lineTo(bx, by); ctx.stroke();

      // Joint Pins A, B, P
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath(); ctx.arc(ax, ay, 6, 0, 2*Math.PI); ctx.fill();
      ctx.beginPath(); ctx.arc(bx, by, 6, 0, 2*Math.PI); ctx.fill();

      // Coupler tracer point P
      ctx.fillStyle = '#ec4899';
      ctx.beginPath(); ctx.arc(px, py, 7, 0, 2*Math.PI); ctx.fill();

      // Coriolis Acceleration Vector Display
      // a_c = 2 * omega x v_rel
      const vRelX = -omega2 * r2 * Math.sin(theta2) * 0.4;
      const vRelY = omega2 * r2 * Math.cos(theta2) * 0.4;
      const corX = -2 * omega2 * vRelY * 0.2;
      const corY = 2 * omega2 * vRelX * 0.2;

      // Draw Coriolis arrow from point P
      ctx.strokeStyle = '#e11d48';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(px, py);
      ctx.lineTo(px + corX, py + corY);
      ctx.stroke();

      // Arrow head
      ctx.fillStyle = '#e11d48';
      const arrowAngle = Math.atan2(corY, corX);
      ctx.beginPath();
      ctx.moveTo(px + corX, py + corY);
      ctx.lineTo(px + corX - 10 * Math.cos(arrowAngle - 0.4), py + corY - 10 * Math.sin(arrowAngle - 0.4));
      ctx.lineTo(px + corX - 10 * Math.cos(arrowAngle + 0.4), py + corY - 10 * Math.sin(arrowAngle + 0.4));
      ctx.closePath();
      ctx.fill();

      ctx.fillStyle = '#e11d48';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('a_cor (Gia tốc Coriolis)', px + corX + 8, py + corY);
    }

    // Info overlay
    ctx.fillStyle = 'rgba(15, 23, 42, 0.75)';
    ctx.fillRect(width - 240, 15, 225, 95);
    ctx.strokeStyle = '#334155';
    ctx.strokeRect(width - 240, 15, 225, 95);

    ctx.fillStyle = '#f1f5f9';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('ĐỘNG HỌC CƠ CẤU 4 KHÂU', width - 225, 35);
    ctx.font = '11px monospace';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`θ₂ (Góc tay quay): ${(theta2 * 180 / Math.PI).toFixed(1)}°`, width - 225, 55);
    ctx.fillStyle = '#ec4899';
    ctx.fillText(`Quỹ đạo điểm P: Coupler Curve`, width - 225, 73);
    ctx.fillStyle = '#e11d48';
    ctx.fillText(`ω₂: ${omega2.toFixed(2)} rad/s (Vận tốc góc)`, width - 225, 91);

    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
}

// =============================================================================
// SIMULATOR 3: Chaotic Double Pendulum Lagrangian Dynamics (Ch 3)
// =============================================================================
function initChaoticDoublePendulumSim(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;

  const sliderL1 = document.getElementById('sim3-l1');
  const sliderL2 = document.getElementById('sim3-l2');
  const resetBtn = document.getElementById('sim3-reset');

  let L1 = sliderL1 ? parseFloat(sliderL1.value) : 100;
  let L2 = sliderL2 ? parseFloat(sliderL2.value) : 90;
  const m1 = 1.0;
  const m2 = 1.0;
  const g = 9.81;

  // Generalized coordinates: theta1, theta2, omega1, omega2
  let th1 = Math.PI / 2;
  let th2 = Math.PI / 2;
  let w1 = 0.0;
  let w2 = 0.0;

  let tipHistory = [];
  const maxTip = 180;

  if (sliderL1) sliderL1.addEventListener('input', (e) => { L1 = parseFloat(e.target.value); tipHistory = []; });
  if (sliderL2) sliderL2.addEventListener('input', (e) => { L2 = parseFloat(e.target.value); tipHistory = []; });
  if (resetBtn) resetBtn.addEventListener('click', () => {
    th1 = Math.PI / 2 + 0.1;
    th2 = Math.PI / 2;
    w1 = 0;
    w2 = 0;
    tipHistory = [];
  });

  // Lagrangian derivatives function
  function derivatives(t1, t2, w_1, w_2) {
    const delta = t1 - t2;
    const den1 = (2 * m1 + m2 - m2 * Math.cos(2 * t1 - 2 * t2));
    const den2 = (L2 / L1) * den1;

    // dw1/dt
    const num1 = -g * (2 * m1 + m2) * Math.sin(t1) - m2 * g * Math.sin(t1 - 2 * t2) 
                 - 2 * Math.sin(delta) * m2 * (w_2 * w_2 * L2 + w_1 * w_1 * L1 * Math.cos(delta));
    const alpha1 = num1 / (L1 * den1);

    // dw2/dt
    const num2 = 2 * Math.sin(delta) * (w_1 * w_1 * L1 * (m1 + m2) + g * (m1 + m2) * Math.cos(t1) 
                 + w_2 * w_2 * L2 * m2 * Math.cos(delta));
    const alpha2 = num2 / (L2 * den1);

    return { dth1: w_1, dth2: w_2, dw1: alpha1, dw2: alpha2 };
  }

  // 4th Order Runge-Kutta integrator
  function rk4Step(dt) {
    const k1 = derivatives(th1, th2, w1, w2);
    const k2 = derivatives(th1 + 0.5 * dt * k1.dth1, th2 + 0.5 * dt * k1.dth2, w1 + 0.5 * dt * k1.dw1, w2 + 0.5 * dt * k1.dw2);
    const k3 = derivatives(th1 + 0.5 * dt * k2.dth1, th2 + 0.5 * dt * k2.dth2, w1 + 0.5 * dt * k2.dw1, w2 + 0.5 * dt * k2.dw2);
    const k4 = derivatives(th1 + dt * k3.dth1, th2 + dt * k3.dth2, w1 + dt * k3.dw1, w2 + dt * k3.dw2);

    th1 += (dt / 6) * (k1.dth1 + 2 * k2.dth1 + 2 * k3.dth1 + k4.dth1);
    th2 += (dt / 6) * (k1.dth2 + 2 * k2.dth2 + 2 * k3.dth2 + k4.dth2);
    w1 += (dt / 6) * (k1.dw1 + 2 * k2.dw1 + 2 * k3.dw1 + k4.dw1);
    w2 += (dt / 6) * (k1.dw2 + 2 * k2.dw2 + 2 * k3.dw2 + k4.dw2);

    // Light viscous air damping
    w1 *= 0.9998;
    w2 *= 0.9998;
  }

  function render() {
    const { ctx, width, height } = setupHiDPICanvas(canvas);
    ctx.clearRect(0, 0, width, height);

    // Physics substeps for stability
    for (let s = 0; s < 4; s++) {
      rk4Step(0.04);
    }

    const originX = width * 0.42;
    const originY = height * 0.35;

    const x1 = originX + L1 * Math.sin(th1);
    const y1 = originY + L1 * Math.cos(th1);
    const x2 = x1 + L2 * Math.sin(th2);
    const y2 = y1 + L2 * Math.cos(th2);

    tipHistory.push({ x: x2, y: y2 });
    if (tipHistory.length > maxTip) tipHistory.shift();

    // Chaotic Trace
    if (tipHistory.length > 2) {
      for (let i = 1; i < tipHistory.length; i++) {
        const alpha = (i / tipHistory.length) * 0.7;
        ctx.strokeStyle = `rgba(244, 63, 94, ${alpha})`;
        ctx.lineWidth = 1.8;
        ctx.beginPath();
        ctx.moveTo(tipHistory[i - 1].x, tipHistory[i - 1].y);
        ctx.lineTo(tipHistory[i].x, tipHistory[i].y);
        ctx.stroke();
      }
    }

    // Pivot mount
    ctx.fillStyle = '#475569';
    ctx.fillRect(originX - 20, originY - 10, 40, 10);
    ctx.fillStyle = '#cbd5e1';
    ctx.beginPath(); ctx.arc(originX, originY, 6, 0, 2*Math.PI); ctx.fill();

    // Rod 1 (Blue)
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 4;
    ctx.beginPath(); ctx.moveTo(originX, originY); ctx.lineTo(x1, y1); ctx.stroke();

    // Bob 1
    ctx.fillStyle = '#1d4ed8';
    ctx.beginPath(); ctx.arc(x1, y1, 10, 0, 2*Math.PI); ctx.fill();
    ctx.strokeStyle = '#93c5fd';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Rod 2 (Purple)
    ctx.strokeStyle = '#8b5cf6';
    ctx.lineWidth = 3.5;
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();

    // Bob 2
    ctx.fillStyle = '#e11d48';
    ctx.beginPath(); ctx.arc(x2, y2, 11, 0, 2*Math.PI); ctx.fill();
    ctx.strokeStyle = '#fda4af';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Right: Phase Portrait (theta1 vs omega1)
    const ppX = width * 0.72;
    const ppY = 40;
    const ppW = width * 0.25;
    const ppH = height - 70;

    ctx.fillStyle = 'rgba(15, 23, 42, 0.7)';
    ctx.fillRect(ppX, ppY, ppW, ppH);
    ctx.strokeStyle = '#334155';
    ctx.strokeRect(ppX, ppY, ppW, ppH);

    ctx.fillStyle = '#94a3b8';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('KHÔNG GIAN PHA (θ₁ - ω₁)', ppX + 10, ppY + 20);

    // Cross axes
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(ppX, ppY + ppH / 2); ctx.lineTo(ppX + ppW, ppY + ppH / 2);
    ctx.moveTo(ppX + ppW / 2, ppY); ctx.lineTo(ppX + ppW / 2, ppY + ppH);
    ctx.stroke();
    ctx.setLineDash([]);

    // Plot current state dot
    const normTh1 = ((th1 % (2 * Math.PI)) + Math.PI) / (2 * Math.PI);
    const pDotX = ppX + normTh1 * ppW;
    const pDotY = (ppY + ppH / 2) - w1 * 12;
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath(); ctx.arc(pDotX, pDotY, 4, 0, 2*Math.PI); ctx.fill();

    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
}

// =============================================================================
// SIMULATOR 4: Nonholonomic Wheeled Robot & Constraint Force (Ch 4)
// =============================================================================
function initNonholonomicWheeledSim(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;

  const sliderV = document.getElementById('sim4-v');
  const sliderW = document.getElementById('sim4-w');
  const resetBtn = document.getElementById('sim4-reset');

  let v = sliderV ? parseFloat(sliderV.value) : 1.2;  // Linear velocity
  let w = sliderW ? parseFloat(sliderW.value) : 0.8;  // Angular velocity

  // Robot state: x, y, theta
  let rx = 100;
  let ry = 150;
  let rTheta = 0;

  let path = [];
  const maxPath = 250;

  if (sliderV) sliderV.addEventListener('input', (e) => { v = parseFloat(e.target.value); });
  if (sliderW) sliderW.addEventListener('input', (e) => { w = parseFloat(e.target.value); });
  if (resetBtn) resetBtn.addEventListener('click', () => {
    rx = 100; ry = 150; rTheta = 0; path = [];
  });

  function render() {
    const { ctx, width, height } = setupHiDPICanvas(canvas);
    ctx.clearRect(0, 0, width, height);

    // Nonholonomic kinematic update:
    // dx/dt = v * cos(theta), dy/dt = v * sin(theta), dtheta/dt = w
    // Lateral velocity vy = -x_dot * sin(theta) + y_dot * cos(theta) = 0 (PFALZ / PFAFFIAN CONSTRAINT)
    const dt = 0.03;
    rx += v * 35 * Math.cos(rTheta) * dt;
    ry += v * 35 * Math.sin(rTheta) * dt;
    rTheta += w * dt;

    // Wrap boundaries
    if (rx > width + 40) rx = -40;
    if (rx < -40) rx = width + 40;
    if (ry > height + 40) ry = -40;
    if (ry < -40) ry = height + 40;

    path.push({ x: rx, y: ry });
    if (path.length > maxPath) path.shift();

    // Draw Trail
    if (path.length > 2) {
      ctx.strokeStyle = 'rgba(14, 165, 233, 0.4)';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i < path.length; i++) {
        if (i === 0) ctx.moveTo(path[i].x, path[i].y);
        else ctx.lineTo(path[i].x, path[i].y);
      }
      ctx.stroke();
    }

    // Draw Wheeled Robot Chassis
    ctx.save();
    ctx.translate(rx, ry);
    ctx.rotate(rTheta);

    // Chassis Body
    ctx.fillStyle = '#1e293b';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.fillRect(-22, -18, 44, 36);
    ctx.strokeRect(-22, -18, 44, 36);

    // Drive Wheels (Left & Right)
    ctx.fillStyle = '#f59e0b';
    ctx.fillRect(-10, -23, 20, 6);
    ctx.fillRect(-10, 17, 20, 6);

    // Front Caster
    ctx.fillStyle = '#94a3b8';
    ctx.beginPath(); ctx.arc(14, 0, 4, 0, 2*Math.PI); ctx.fill();

    // Direction Heading Line
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(30, 0); ctx.stroke();

    // Nonholonomic Lateral Constraint Force Vector: Lambda * a_n
    // Force resisting lateral sliding: F_lateral = m * v * w
    const lambdaForce = v * w * 18;
    ctx.strokeStyle = '#e11d48';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, -lambdaForce);
    ctx.stroke();

    ctx.restore();

    // Panel Overlay
    ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
    ctx.fillRect(15, 15, 340, 100);
    ctx.strokeStyle = '#334155';
    ctx.strokeRect(15, 15, 340, 100);

    ctx.fillStyle = '#f8fafc';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('RÀNG BUỘC PHI HOLONOMIC (NONHOLONOMIC)', 25, 35);
    ctx.font = '11px monospace';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('Phương trình: ẋ·sin(θ) - ẏ·cos(θ) = 0 (Không trượt ngang)', 25, 55);
    ctx.fillStyle = '#22c55e';
    ctx.fillText(`Vận tốc dọc v: ${v.toFixed(2)} m/s | Tốc độ góc w: ${w.toFixed(2)} rad/s`, 25, 75);
    ctx.fillStyle = '#e11d48';
    ctx.fillText(`Lực ràng buộc (Nhân tử λ): ${(v * w).toFixed(2)} N (Chống lật/trượt)`, 25, 95);

    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
}

// =============================================================================
// SIMULATOR 5: DAE Constraint Drift vs Baumgarte Stabilization (Ch 5)
// =============================================================================
function initBaumgarteDriftSim(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;

  const sliderAlpha = document.getElementById('sim5-alpha');
  const sliderH = document.getElementById('sim5-h');
  const toggleBtn = document.getElementById('sim5-toggle');
  const resetBtn = document.getElementById('sim5-reset');

  let alpha = sliderAlpha ? parseFloat(sliderAlpha.value) : 5.0; // Baumgarte damping
  let beta = alpha; // Critically damped beta = alpha
  let dt = sliderH ? parseFloat(sliderH.value) : 0.05;

  let mode = 'baumgarte'; // 'naive' or 'baumgarte'

  const L0 = 120; // Nominal rod length
  const g = 9.81;

  // Pendulum Cartesian states: x, y, vx, vy
  let x = L0 * Math.sin(0.8);
  let y = L0 * Math.cos(0.8);
  let vx = 0;
  let vy = 0;

  let driftHistory = [];
  const maxHistory = 150;

  if (sliderAlpha) sliderAlpha.addEventListener('input', (e) => { 
    alpha = parseFloat(e.target.value); 
    beta = alpha; 
  });
  if (sliderH) sliderH.addEventListener('input', (e) => { dt = parseFloat(e.target.value); });
  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      mode = (mode === 'baumgarte') ? 'naive' : 'baumgarte';
      toggleBtn.textContent = mode === 'baumgarte' ? 'Chế độ: Ổn định hóa Baumgarte' : 'Chế độ: Euler/RK Thô (Trôi dạt)';
      reset();
    });
  }
  if (resetBtn) resetBtn.addEventListener('click', reset);

  function reset() {
    x = L0 * Math.sin(0.8);
    y = L0 * Math.cos(0.8);
    vx = 0;
    vy = 0;
    driftHistory = [];
  }

  function stepPhysics() {
    // Constraint: Phi = 0.5 * (x^2 + y^2 - L0^2) = 0
    const phi = 0.5 * (x * x + y * y - L0 * L0);
    // dPhi/dt = x * vx + y * vy
    const phiDot = x * vx + y * vy;

    // Lagrangian multiplier lambda:
    // (x^2 + y^2) * lambda = - (vx^2 + vy^2) + g * y  [Underlying ODE]
    let rhs = -(vx * vx + vy * vy) + g * y;

    if (mode === 'baumgarte') {
      // Baumgarte stabilized rhs: rhs - 2*alpha*phiDot - beta^2*phi
      rhs -= (2 * alpha * phiDot + beta * beta * phi);
    }

    const rSq = x * x + y * y;
    const lambda = rhs / (rSq || 1);

    // Accelerations:
    const ax = -lambda * x;
    const ay = g - lambda * y;

    // Numerical integration (Euler-Cromer)
    vx += ax * dt;
    vy += ay * dt;
    x += vx * dt;
    y += vy * dt;

    // Calculate actual rod length error (drift in pixels)
    const currentL = Math.sqrt(x * x + y * y);
    const drift = currentL - L0;

    driftHistory.push(drift);
    if (driftHistory.length > maxHistory) driftHistory.shift();
  }

  function render() {
    const { ctx, width, height } = setupHiDPICanvas(canvas);
    ctx.clearRect(0, 0, width, height);

    stepPhysics();

    // Left Viewport: Pendulum Animation
    const originX = width * 0.28;
    const originY = 60;

    // Pivot
    ctx.fillStyle = '#64748b';
    ctx.fillRect(originX - 25, originY - 12, 50, 12);
    ctx.fillStyle = '#cbd5e1';
    ctx.beginPath(); ctx.arc(originX, originY, 6, 0, 2*Math.PI); ctx.fill();

    // Ideal circle track
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
    ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.arc(originX, originY, L0, 0, 2*Math.PI); ctx.stroke();
    ctx.setLineDash([]);

    const px = originX + x;
    const py = originY + y;

    // Rod
    ctx.strokeStyle = (mode === 'baumgarte') ? '#22c55e' : '#ef4444';
    ctx.lineWidth = 3.5;
    ctx.beginPath(); ctx.moveTo(originX, originY); ctx.lineTo(px, py); ctx.stroke();

    // Bob
    ctx.fillStyle = (mode === 'baumgarte') ? '#10b981' : '#dc2626';
    ctx.beginPath(); ctx.arc(px, py, 12, 0, 2*Math.PI); ctx.fill();

    // Right Viewport: Drift Error Plot Phi(t)
    const graphX = width * 0.55;
    const graphY = 40;
    const graphW = width * 0.40;
    const graphH = height - 70;

    ctx.fillStyle = 'rgba(15, 23, 42, 0.75)';
    ctx.fillRect(graphX, graphY, graphW, graphH);
    ctx.strokeStyle = '#334155';
    ctx.strokeRect(graphX, graphY, graphW, graphH);

    ctx.fillStyle = '#f1f5f9';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('SAI SỐ TRÔI DẠT RÀNG BUỘC (CONSTRAINT DRIFT)', graphX + 10, graphY + 20);

    const zeroY = graphY + graphH * 0.5;
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
    ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(graphX, zeroY); ctx.lineTo(graphX + graphW, zeroY); ctx.stroke();
    ctx.setLineDash([]);

    if (driftHistory.length > 1) {
      ctx.strokeStyle = (mode === 'baumgarte') ? '#22c55e' : '#ef4444';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i < driftHistory.length; i++) {
        const hx = graphX + (i / maxHistory) * graphW;
        const hy = zeroY - driftHistory[i] * 5; // Scaled error
        if (i === 0) ctx.moveTo(hx, hy);
        else ctx.lineTo(hx, hy);
      }
      ctx.stroke();
    }

    const latestDrift = driftHistory[driftHistory.length - 1] || 0;
    ctx.fillStyle = (mode === 'baumgarte') ? '#22c55e' : '#ef4444';
    ctx.font = '11px monospace';
    ctx.fillText(`ΔL (Độ giãn dài): ${latestDrift.toFixed(3)} px`, graphX + 10, graphY + graphH - 12);

    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
}

// =============================================================================
// SIMULATOR 6: Lyapunov Phase Vector Field & Stability Contours (Ch 6)
// =============================================================================
function initLyapunovPhaseVectorSim(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;

  const sliderMu = document.getElementById('sim6-mu');
  const resetBtn = document.getElementById('sim6-reset');

  let mu = sliderMu ? parseFloat(sliderMu.value) : 0.4; // Damping parameter

  // Multiple trajectories from clicks
  let trajectories = [
    [{ x: 2.0, y: 1.5 }]
  ];

  if (sliderMu) sliderMu.addEventListener('input', (e) => { mu = parseFloat(e.target.value); });
  if (resetBtn) resetBtn.addEventListener('click', () => {
    trajectories = [[{ x: 2.0, y: 1.5 }]];
  });

  // Click to add trajectory
  canvas.addEventListener('click', (e) => {
    const rect = canvas.getBoundingClientRect();
    const cx = (e.clientX - rect.left);
    const cy = (e.clientY - rect.top);
    // Convert to state space coords
    const originX = rect.width * 0.5;
    const originY = rect.height * 0.5;
    const scale = 50;
    const x0 = (cx - originX) / scale;
    const y0 = -(cy - originY) / scale;
    trajectories.push([{ x: x0, y: y0 }]);
    if (trajectories.length > 5) trajectories.shift();
  });

  // Nonlinear oscillator dynamics: x1_dot = x2, x2_dot = -sin(x1) - mu * x2
  function f(x1, x2) {
    return {
      dx1: x2,
      dx2: -Math.sin(x1) - mu * x2
    };
  }

  function render() {
    const { ctx, width, height } = setupHiDPICanvas(canvas);
    ctx.clearRect(0, 0, width, height);

    const originX = width * 0.5;
    const originY = height * 0.5;
    const scale = 55; // Pixels per unit

    // Draw Vector Field Arrows
    const gridStep = 35;
    ctx.strokeStyle = 'rgba(148, 163, 184, 0.25)';
    ctx.lineWidth = 1;

    for (let px = 20; px < width; px += gridStep) {
      for (let py = 20; py < height; py += gridStep) {
        const x1 = (px - originX) / scale;
        const x2 = -(py - originY) / scale;
        const flow = f(x1, x2);
        const len = Math.sqrt(flow.dx1 * flow.dx1 + flow.dx2 * flow.dx2);
        if (len > 0.001) {
          const arrowLen = 14;
          const u = (flow.dx1 / len) * arrowLen;
          const v = -(flow.dx2 / len) * arrowLen;
          ctx.beginPath();
          ctx.moveTo(px, py);
          ctx.lineTo(px + u, py + v);
          ctx.stroke();
        }
      }
    }

    // Axes
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(0, originY); ctx.lineTo(width, originY);
    ctx.moveTo(originX, 0); ctx.lineTo(originX, height);
    ctx.stroke();

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px sans-serif';
    ctx.fillText('x₁ (Tọa độ q)', width - 80, originY - 10);
    ctx.fillText('x₂ (Vận tốc q̇)', originX + 10, 20);

    // Draw Lyapunov Ellipses: V(x) = 0.5 * x2^2 + (1 - cos(x1)) = c
    ctx.lineWidth = 1.2;
    [0.2, 0.6, 1.2, 2.0].forEach((c, idx) => {
      ctx.strokeStyle = `rgba(168, 85, 247, ${0.3 + idx * 0.15})`;
      ctx.beginPath();
      for (let th = 0; th <= 2 * Math.PI; th += 0.05) {
        const rx = Math.sqrt(2 * c) * Math.cos(th);
        const ry = Math.sqrt(2 * c) * Math.sin(th);
        const sx = originX + rx * scale;
        const sy = originY - ry * scale;
        if (th === 0) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.closePath();
      ctx.stroke();
    });

    // Step Trajectories
    const dt = 0.02;
    trajectories.forEach((traj, tIdx) => {
      const last = traj[traj.length - 1];
      if (traj.length < 300) {
        const flow = f(last.x, last.y);
        const nextX = last.x + flow.dx1 * dt;
        const nextY = last.y + flow.dx2 * dt;
        traj.push({ x: nextX, y: nextY });
      }

      // Draw Trajectory curve
      ctx.strokeStyle = tIdx === 0 ? '#38bdf8' : '#f59e0b';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i < traj.length; i++) {
        const sx = originX + traj[i].x * scale;
        const sy = originY - traj[i].y * scale;
        if (i === 0) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.stroke();

      // Current Head Dot
      const headX = originX + last.x * scale;
      const headY = originY - last.y * scale;
      ctx.fillStyle = '#ffffff';
      ctx.beginPath(); ctx.arc(headX, headY, 5, 0, 2*Math.PI); ctx.fill();
    });

    // Info
    ctx.fillStyle = 'rgba(15, 23, 42, 0.8)';
    ctx.fillRect(15, 15, 260, 75);
    ctx.strokeStyle = '#334155';
    ctx.strokeRect(15, 15, 260, 75);

    ctx.fillStyle = '#f1f5f9';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('TRƯỜNG VECTOR & ĐƯỜNG MỨC LYAPUNOV', 25, 32);
    ctx.font = '11px sans-serif';
    ctx.fillStyle = '#a855f7';
    ctx.fillText('— Đường cong tím: Hàm thế V(x) = c', 25, 50);
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('👉 Nhấp chuột lên màn hình để thả quỹ đạo!', 25, 70);

    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
}

// Auto-initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('sim-canvas-01')) initPaynterEnergySim('sim-canvas-01');
  if (document.getElementById('sim-canvas-02')) initFourBarKinematicsSim('sim-canvas-02');
  if (document.getElementById('sim-canvas-03')) initChaoticDoublePendulumSim('sim-canvas-03');
  if (document.getElementById('sim-canvas-04')) initNonholonomicWheeledSim('sim-canvas-04');
  if (document.getElementById('sim-canvas-05')) initBaumgarteDriftSim('sim-canvas-05');
  if (document.getElementById('sim-canvas-06')) initLyapunovPhaseVectorSim('sim-canvas-06');
});
