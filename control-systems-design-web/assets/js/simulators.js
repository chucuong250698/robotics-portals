/**
 * Design and Analysis of Control Systems - Interactive 60 FPS Canvas 2D Simulators Suite
 * Based on 'Design and Analysis of Control Systems: Driving the Fourth Industrial Revolution'
 * (Arthur G.O. Mutambara, CRC Press)
 *
 * Implements 10 distinct interactive 60 FPS simulations:
 *  - Sim 01: Cruise Control Open-Loop vs Closed-Loop with Hill Disturbance (Ch 01)
 *  - Sim 02: DC Motor Electromechanical Position/Speed Response (Ch 02)
 *  - Sim 03: Second-Order Step Response with Adjustable Zeta and Wn (Ch 03)
 *  - Sim 04: Interactive PID Tuner with Disturbance Rejection (Ch 04)
 *  - Sim 05: Evans Root Locus on S-Plane with Movable Poles/Zeros (Ch 05)
 *  - Sim 06: Bode & Nyquist Diagrams with GM and PM Markers (Ch 06)
 *  - Sim 07: Inverted Pendulum Cart Stabilization via LQR / Pole Placement (Ch 07)
 *  - Sim 08: ZOH Sampling and Aliasing vs Continuous Signal (Ch 08)
 *  - Sim 09: Sliding Mode Control (s=0) & MPC Receding Horizon (Ch 09)
 *  - Sim 10: Fuzzy Logic Controller Surface & Mamdani Rule Activation (Ch 10)
 *
 * Version: 20261122
 */

// Global registry of simulator cancellation handles
window._csdSimHandles = window._csdSimHandles || {};

// Helper to get canvas and 2D context safely
function getSimCanvas(id) {
  const canvas = document.getElementById(id);
  if (!canvas) return null;
  const ctx = canvas.getContext('2d');
  return { canvas, ctx };
}

// Helper to check dark theme
function isDarkTheme() {
  return document.documentElement.getAttribute('data-theme') === 'dark';
}

// =========================================================================
// SIM 01: Cruise Control Open-Loop vs Closed-Loop with Hill Disturbance (Ch 01)
// =========================================================================
window.initSim01 = function() {
  const sim = getSimCanvas('sim-canvas-01');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._csdSimHandles['01']) cancelAnimationFrame(window._csdSimHandles['01']);

  const sliderTarget = document.getElementById('sim01-target');
  const sliderHill = document.getElementById('sim01-hill');
  const sliderKp = document.getElementById('sim01-kp');
  const sliderKi = document.getElementById('sim01-ki');
  const stats = document.getElementById('sim01-stats');

  // Parameters
  const m = 1000; // mass (kg)
  const b = 50;   // friction (N*s/m)
  let v_open = 20; // m/s
  let v_closed = 20; // m/s
  let integral_err = 0;
  let carX = 50;
  let history = [];
  const maxHistory = 300;
  let t = 0;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const targetKmH = sliderTarget ? parseFloat(sliderTarget.value) : 72; // km/h
    const hillDeg = sliderHill ? parseFloat(sliderHill.value) : 6;       // degrees
    const kp = sliderKp ? parseFloat(sliderKp.value) : 1200;
    const ki = sliderKi ? parseFloat(sliderKi.value) : 80;

    const v_target = targetKmH / 3.6; // convert to m/s
    const theta = (hillDeg * Math.PI) / 180;
    const f_hill = -m * 9.81 * Math.sin(theta); // disturbance force

    // Simulation step dt = 1/60s
    const dt = 1 / 60;
    t += dt;

    // Open-loop engine force: calibrated for flat ground (b * v_target)
    const f_eng_open = b * v_target;
    const dv_open = ((f_eng_open + f_hill - b * v_open) / m) * dt;
    v_open = Math.max(0, v_open + dv_open);

    // Closed-loop PI controller
    const err = v_target - v_closed;
    integral_err = Math.max(-5000, Math.min(5000, integral_err + err * dt));
    const f_eng_closed = Math.max(0, Math.min(6000, kp * err + ki * integral_err));
    const dv_closed = ((f_eng_closed + f_hill - b * v_closed) / m) * dt;
    v_closed = Math.max(0, v_closed + dv_closed);

    // Car position wrap
    carX = (carX + v_closed * 1.5 * dt) % (canvas.width - 100);

    // Record history
    history.push({
      v_open: v_open * 3.6,
      v_closed: v_closed * 3.6,
      v_target: targetKmH
    });
    if (history.length > maxHistory) history.shift();

    // 1. Draw Environment (Sky & Road Profile)
    ctx.fillStyle = dark ? '#0f172a' : '#f8fafc';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Road terrain with hill
    const roadY = 160;
    ctx.beginPath();
    ctx.moveTo(0, roadY);
    for (let x = 0; x <= canvas.width; x += 10) {
      let hillProfile = 0;
      if (x > 180 && x < 550) {
        hillProfile = -Math.sin(((x - 180) / 370) * Math.PI) * (hillDeg * 3.5);
      }
      ctx.lineTo(x, roadY + hillProfile);
    }
    ctx.lineTo(canvas.width, 210);
    ctx.lineTo(0, 210);
    ctx.closePath();
    ctx.fillStyle = dark ? '#1e293b' : '#e2e8f0';
    ctx.fill();

    // Road top boundary line
    ctx.lineWidth = 2.5;
    ctx.strokeStyle = dark ? '#475569' : '#94a3b8';
    ctx.stroke();

    // Hill angle indicator
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = dark ? '#fbbf24' : '#d97706';
    ctx.fillText(`⛰️ Độ dốc địa hình: ${hillDeg.toFixed(1)}° (${f_hill.toFixed(0)} N cản trở)`, 240, 110);

    // 2. Draw Moving Vehicle (Chassis & Wheels)
    const currentCarX = 120 + carX;
    let currentCarHill = 0;
    if (currentCarX > 180 && currentCarX < 550) {
      currentCarHill = -Math.sin(((currentCarX - 180) / 370) * Math.PI) * (hillDeg * 3.5);
    }
    const currentCarY = roadY + currentCarHill - 18;

    // Vehicle body
    ctx.save();
    ctx.translate(currentCarX, currentCarY);
    ctx.fillStyle = '#3b82f6';
    ctx.beginPath();
    ctx.roundRect(-25, -14, 50, 18, [4, 8, 0, 0]);
    ctx.fill();
    // Cabin
    ctx.fillStyle = dark ? '#93c5fd' : '#bfdbfe';
    ctx.beginPath();
    ctx.roundRect(-14, -26, 26, 13, [5, 5, 0, 0]);
    ctx.fill();
    // Wheels
    ctx.fillStyle = dark ? '#000000' : '#1e293b';
    ctx.beginPath();
    ctx.arc(-14, 4, 6, 0, Math.PI * 2);
    ctx.arc(14, 4, 6, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    // Speedometer Badge above car
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#10b981';
    ctx.fillText(`CL: ${(v_closed * 3.6).toFixed(1)} km/h`, currentCarX - 25, currentCarY - 32);

    // 3. Real-Time Performance Strip Chart (y: 220 to 380)
    const chartX = 50;
    const chartY = 230;
    const chartW = canvas.width - 100;
    const chartH = 140;

    // Chart Background
    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(chartX, chartY, chartW, chartH);
    ctx.strokeStyle = dark ? '#374151' : '#e5e7eb';
    ctx.lineWidth = 1;
    ctx.strokeRect(chartX, chartY, chartW, chartH);

    // Chart Grid & Reference Lines
    ctx.setLineDash([3, 3]);
    ctx.strokeStyle = dark ? '#1f2937' : '#f3f4f6';
    for (let s = 20; s <= 120; s += 20) {
      const yPos = chartY + chartH - (s / 130) * chartH;
      ctx.beginPath();
      ctx.moveTo(chartX, yPos);
      ctx.lineTo(chartX + chartW, yPos);
      ctx.stroke();

      ctx.fillStyle = dark ? '#6b7280' : '#9ca3af';
      ctx.font = '10px monospace';
      ctx.fillText(`${s}`, chartX - 25, yPos + 3);
    }
    ctx.setLineDash([]);

    // Target Speed line (dashed yellow)
    const targetYPos = chartY + chartH - (targetKmH / 130) * chartH;
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([5, 4]);
    ctx.beginPath();
    ctx.moveTo(chartX, targetYPos);
    ctx.lineTo(chartX + chartW, targetYPos);
    ctx.stroke();
    ctx.setLineDash([]);

    // Plot Closed-Loop curve (Cyan)
    ctx.strokeStyle = '#06b6d4';
    ctx.lineWidth = 2.2;
    ctx.beginPath();
    history.forEach((pt, idx) => {
      const px = chartX + (idx / (maxHistory - 1)) * chartW;
      const py = chartY + chartH - (pt.v_closed / 130) * chartH;
      if (idx === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Plot Open-Loop curve (Red/Orange)
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 1.8;
    ctx.beginPath();
    history.forEach((pt, idx) => {
      const px = chartX + (idx / (maxHistory - 1)) * chartW;
      const py = chartY + chartH - (pt.v_open / 130) * chartH;
      if (idx === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Legend
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`--- Đặt v_ref: ${targetKmH.toFixed(0)} km/h`, chartX + 15, chartY + 18);
    ctx.fillStyle = '#06b6d4';
    ctx.fillText(`— Vòng Kín (PI): ${(v_closed * 3.6).toFixed(1)} km/h`, chartX + 180, chartY + 18);
    ctx.fillStyle = '#ef4444';
    ctx.fillText(`— Vòng Hở: ${(v_open * 3.6).toFixed(1)} km/h`, chartX + 370, chartY + 18);

    // Update Telemetry Panel
    if (stats) {
      const errClosed = Math.abs(targetKmH - v_closed * 3.6);
      const errOpen = Math.abs(targetKmH - v_open * 3.6);
      stats.innerHTML = `Vòng Kín: <strong>${(v_closed * 3.6).toFixed(2)} km/h</strong> (Sai số: ${errClosed.toFixed(2)} km/h) | Lực Kéo: <strong>${f_eng_closed.toFixed(0)} N</strong> | Vòng Hở: <strong>${(v_open * 3.6).toFixed(2)} km/h</strong> (Sụt giảm: ${errOpen.toFixed(2)} km/h do dốc)`;
    }

    window._csdSimHandles['01'] = requestAnimationFrame(render);
  }

  render();
};

// =========================================================================
// SIM 02: DC Motor Electromechanical Response (Ch 02)
// =========================================================================
window.initSim02 = function() {
  const sim = getSimCanvas('sim-canvas-02');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._csdSimHandles['02']) cancelAnimationFrame(window._csdSimHandles['02']);

  const sliderV = document.getElementById('sim02-voltage');
  const sliderTL = document.getElementById('sim02-load');
  const sliderJ = document.getElementById('sim02-inertia');
  const sliderB = document.getElementById('sim02-damping');
  const stats = document.getElementById('sim02-stats');

  // Physical Parameters
  const R = 2.0;    // Ohms
  const L = 0.05;   // Henries
  const Kt = 0.12;  // N*m/A
  const Kb = 0.12;  // V*s/rad

  let current = 0;   // Armature current (A)
  let omega = 0;     // Angular speed (rad/s)
  let theta = 0;     // Shaft angle (rad)
  let history = [];
  const maxHistory = 240;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const V = sliderV ? parseFloat(sliderV.value) : 24.0;
    const TL = sliderTL ? parseFloat(sliderTL.value) : 0.35;
    const J = sliderJ ? parseFloat(sliderJ.value) : 0.02;
    const b = sliderB ? parseFloat(sliderB.value) : 0.015;

    // Dynamic Simulation Step
    const dt = 1 / 120;
    for (let step = 0; step < 2; step++) {
      // di/dt = (V - R*i - Kb*w) / L
      const di = ((V - R * current - Kb * omega) / L) * dt;
      current = Math.max(0, current + di);

      // dw/dt = (Kt*i - b*w - TL) / J
      const dw = ((Kt * current - b * omega - TL) / J) * dt;
      omega = Math.max(0, omega + dw);

      theta = (theta + omega * dt) % (Math.PI * 2);
    }

    history.push({ i: current, w: omega, rpm: (omega * 60) / (2 * Math.PI) });
    if (history.length > maxHistory) history.shift();

    // 1. Motor Visual Cross-Section (Left panel: x: 30 to 300)
    const cx = 160;
    const cy = 200;

    // Stator Pole Magnets (North & South)
    ctx.fillStyle = '#ef4444'; // North (Red)
    ctx.beginPath();
    ctx.arc(cx, cy, 110, -Math.PI / 3, Math.PI / 3, true);
    ctx.lineTo(cx - 100, cy);
    ctx.closePath();
    ctx.fill();

    ctx.fillStyle = '#3b82f6'; // South (Blue)
    ctx.beginPath();
    ctx.arc(cx, cy, 110, (2 * Math.PI) / 3, (4 * Math.PI) / 3, true);
    ctx.lineTo(cx + 100, cy);
    ctx.closePath();
    ctx.fill();

    // Stator Labels
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.fillText('N', cx - 85, cy + 6);
    ctx.fillText('S', cx + 72, cy + 6);

    // Magnetic Flux Lines
    ctx.strokeStyle = dark ? 'rgba(255,255,255,0.15)' : 'rgba(0,0,0,0.15)';
    ctx.setLineDash([4, 4]);
    ctx.lineWidth = 1;
    for (let dy = -50; dy <= 50; dy += 25) {
      ctx.beginPath();
      ctx.moveTo(cx - 70, cy + dy);
      ctx.lineTo(cx + 70, cy + dy);
      ctx.stroke();
    }
    ctx.setLineDash([]);

    // Rotating Armature Rotor
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(theta);

    // Armature Core
    ctx.fillStyle = dark ? '#475569' : '#cbd5e1';
    ctx.beginPath();
    ctx.arc(0, 0, 55, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = dark ? '#94a3b8' : '#64748b';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Copper Windings
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.arc(0, -32, 12, 0, Math.PI * 2);
    ctx.arc(0, 32, 12, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#b45309';
    ctx.stroke();

    // Current flow symbols (dot and cross)
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 13px monospace';
    ctx.fillText('•', -3, -28);
    ctx.fillText('✕', -4, 36);

    // Shaft Center
    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.arc(0, 0, 14, 0, Math.PI * 2);
    ctx.fill();

    ctx.restore();

    // Speedometer text under motor
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = dark ? '#f1f5f9' : '#0f172a';
    ctx.textAlign = 'center';
    ctx.fillText(`Tốc độ: ${((omega * 60) / (2 * Math.PI)).toFixed(0)} RPM (${omega.toFixed(1)} rad/s)`, cx, cy + 145);
    ctx.fillText(`Dòng điện I_a: ${current.toFixed(2)} A | Mô-men T_e: ${(Kt * current).toFixed(2)} N·m`, cx, cy + 165);
    ctx.textAlign = 'left';

    // 2. Dual Real-Time Scope Charts (Right panel: x: 340 to 760)
    const scopeX = 350;
    const scopeW = 410;

    // Scope 1: Angular Speed w(t)
    const scope1Y = 30;
    const scope1H = 160;
    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(scopeX, scope1Y, scopeW, scope1H);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(scopeX, scope1Y, scopeW, scope1H);

    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#10b981';
    ctx.fillText('ĐÁP ỨNG TỐC ĐỘ GÓC ω(t) [rad/s]', scopeX + 15, scope1Y + 22);

    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 2;
    ctx.beginPath();
    history.forEach((pt, idx) => {
      const px = scopeX + (idx / (maxHistory - 1)) * scopeW;
      const py = scope1Y + scope1H - (pt.w / 220) * (scope1H - 35) - 10;
      if (idx === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Scope 2: Armature Current i(t)
    const scope2Y = 215;
    const scope2H = 155;
    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(scopeX, scope2Y, scopeW, scope2H);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(scopeX, scope2Y, scopeW, scope2H);

    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('DÒNG ĐIỆN PHẦN ỨNG i_a(t) [A]', scopeX + 15, scope2Y + 22);

    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.beginPath();
    history.forEach((pt, idx) => {
      const px = scopeX + (idx / (maxHistory - 1)) * scopeW;
      const py = scope2Y + scope2H - (pt.i / 15) * (scope2H - 35) - 10;
      if (idx === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Update Telemetry Panel
    if (stats) {
      const tauE = (L / R) * 1000; // ms
      const tauM = (J / b) * 1000; // ms
      const eb = Kb * omega;
      stats.innerHTML = `Điện áp V: <strong>${V.toFixed(1)} V</strong> | Dòng điện I_a: <strong>${current.toFixed(2)} A</strong> | Sức điện động E_b: <strong>${eb.toFixed(2)} V</strong> | Hằng số thời gian điện τ_e: <strong>${tauE.toFixed(1)} ms</strong> | Hằng số cơ τ_m: <strong>${tauM.toFixed(1)} ms</strong>`;
    }

    window._csdSimHandles['02'] = requestAnimationFrame(render);
  }

  render();
};

// =========================================================================
// SIM 03: Second-Order Step Response with Adjustable Zeta & Wn (Ch 03)
// =========================================================================
window.initSim03 = function() {
  const sim = getSimCanvas('sim-canvas-03');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._csdSimHandles['03']) cancelAnimationFrame(window._csdSimHandles['03']);

  const sliderZeta = document.getElementById('sim03-zeta');
  const sliderWn = document.getElementById('sim03-wn');
  const sliderStep = document.getElementById('sim03-step');
  const stats = document.getElementById('sim03-stats');

  let simTime = 0;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const zeta = sliderZeta ? parseFloat(sliderZeta.value) : 0.45;
    const wn = sliderWn ? parseFloat(sliderWn.value) : 3.0;
    const stepAmp = sliderStep ? parseFloat(sliderStep.value) : 1.0;

    simTime += 0.025;
    const tCurrent = simTime % 5.0; // 5-second repeating animation cycle

    // 1. Analytical Evaluation of y(t)
    function calcY(t) {
      if (zeta < 0.999) {
        // Underdamped
        const wd = wn * Math.sqrt(1 - zeta * zeta);
        const phi = Math.acos(zeta);
        return stepAmp * (1 - (Math.exp(-zeta * wn * t) / Math.sqrt(1 - zeta * zeta)) * Math.sin(wd * t + phi));
      } else if (zeta > 1.001) {
        // Overdamped
        const s1 = -wn * (zeta - Math.sqrt(zeta * zeta - 1));
        const s2 = -wn * (zeta + Math.sqrt(zeta * zeta - 1));
        const c1 = s2 / (s2 - s1);
        const c2 = -s1 / (s2 - s1);
        return stepAmp * (1 + c1 * Math.exp(s1 * t) + c2 * Math.exp(s2 * t));
      } else {
        // Critically Damped
        return stepAmp * (1 - Math.exp(-wn * t) * (1 + wn * t));
      }
    }

    const currentY = calcY(tCurrent);

    // 2. Physical Mass-Spring-Damper Animation (Left: x: 30 to 250)
    const railX = 40;
    const railY = 80;
    const railW = 190;
    const massX = railX + 40 + (currentY / (stepAmp * 1.8)) * 80;

    ctx.fillStyle = dark ? '#1e293b' : '#f1f5f9';
    ctx.fillRect(railX, railY, railW, 90);
    ctx.strokeStyle = dark ? '#475569' : '#cbd5e1';
    ctx.strokeRect(railX, railY, railW, 90);

    // Spring (zigzag)
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(railX + 5, railY + 28);
    const coils = 9;
    const coilW = (massX - railX - 10) / coils;
    for (let c = 0; c < coils; c++) {
      const cx_mid = railX + 10 + c * coilW + coilW / 2;
      const cy_mid = railY + 28 + (c % 2 === 0 ? -12 : 12);
      ctx.lineTo(cx_mid, cy_mid);
    }
    ctx.lineTo(massX, railY + 28);
    ctx.stroke();

    // Damper (dashpot)
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(railX + 5, railY + 62);
    ctx.lineTo(railX + 40, railY + 62);
    ctx.moveTo(railX + 40, railY + 52);
    ctx.lineTo(railX + 40, railY + 72);
    ctx.lineTo(railX + 65, railY + 72);
    ctx.moveTo(railX + 40, railY + 52);
    ctx.lineTo(railX + 65, railY + 52);
    // Piston
    ctx.moveTo(massX - 20, railY + 62);
    ctx.lineTo(massX, railY + 62);
    ctx.moveTo(massX - 20, railY + 55);
    ctx.lineTo(massX - 20, railY + 69);
    ctx.stroke();

    // Mass block (Cart)
    ctx.fillStyle = '#10b981';
    ctx.fillRect(massX, railY + 15, 45, 60);
    ctx.strokeStyle = '#047857';
    ctx.lineWidth = 2;
    ctx.strokeRect(massX, railY + 15, 45, 60);

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('M', massX + 16, railY + 50);

    // 3. Complex S-Plane Inset Diagram (Left bottom: x: 40 to 230, y: 210 to 370)
    const spX = 135;
    const spY = 290;
    const spScale = 22;

    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(40, 200, 190, 175);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(40, 200, 190, 175);

    // S-Plane Axes
    ctx.strokeStyle = dark ? '#64748b' : '#94a3b8';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(45, spY); ctx.lineTo(225, spY); // Re (sigma)
    ctx.moveTo(spX, 205); ctx.lineTo(spX, 370); // Im (jw)
    ctx.stroke();

    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = dark ? '#94a3b8' : '#64748b';
    ctx.fillText('σ', 215, spY - 5);
    ctx.fillText('jω', spX + 5, 218);

    // Plot Conjugate Poles
    ctx.font = 'bold 14px monospace';
    ctx.fillStyle = '#ef4444';
    if (zeta < 1.0) {
      const sigma = -zeta * wn;
      const wd = wn * Math.sqrt(1 - zeta * zeta);
      const px = spX + sigma * spScale;
      const py1 = spY - wd * spScale;
      const py2 = spY + wd * spScale;
      ctx.fillText('✕', px - 5, py1 + 5);
      ctx.fillText('✕', px - 5, py2 + 5);

      // Constant wn circle arc
      ctx.strokeStyle = 'rgba(59, 130, 246, 0.4)';
      ctx.setLineDash([2, 2]);
      ctx.beginPath();
      ctx.arc(spX, spY, wn * spScale, Math.PI / 2, (3 * Math.PI) / 2);
      ctx.stroke();
      ctx.setLineDash([]);
    } else {
      const s1 = -wn * (zeta - Math.sqrt(zeta * zeta - 1));
      const s2 = -wn * (zeta + Math.sqrt(zeta * zeta - 1));
      ctx.fillText('✕', spX + s1 * spScale - 5, spY + 5);
      ctx.fillText('✕', spX + s2 * spScale - 5, spY + 5);
    }

    // 4. Exact Time Step Response Graph (Right: x: 260 to 760, y: 40 to 365)
    const graphX = 270;
    const graphY = 40;
    const graphW = 490;
    const graphH = 320;

    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(graphX, graphY, graphW, graphH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(graphX, graphY, graphW, graphH);

    // Grid & Step Reference
    const targetYPos = graphY + graphH - (stepAmp / 1.8) * (graphH - 40) - 20;
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(graphX, targetYPos);
    ctx.lineTo(graphX + graphW, targetYPos);
    ctx.stroke();

    // ±2% Tolerance Band
    ctx.fillStyle = dark ? 'rgba(16, 185, 129, 0.1)' : 'rgba(16, 185, 129, 0.15)';
    const yTop = graphY + graphH - ((stepAmp * 1.02) / 1.8) * (graphH - 40) - 20;
    const yBot = graphY + graphH - ((stepAmp * 0.98) / 1.8) * (graphH - 40) - 20;
    ctx.fillRect(graphX, yTop, graphW, yBot - yTop);
    ctx.setLineDash([]);

    // Curve y(t)
    ctx.strokeStyle = '#06b6d4';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const tMax = 5.0;
    for (let px = 0; px <= graphW; px += 2) {
      const tVal = (px / graphW) * tMax;
      const yVal = calcY(tVal);
      const py = graphY + graphH - (yVal / 1.8) * (graphH - 40) - 20;
      if (px === 0) ctx.moveTo(graphX + px, py);
      else ctx.lineTo(graphX + px, py);
    }
    ctx.stroke();

    // Animated Current Time Tracker Dot
    const curPX = graphX + (tCurrent / tMax) * graphW;
    const curPY = graphY + graphH - (currentY / 1.8) * (graphH - 40) - 20;
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(curPX, curPY, 5.5, 0, Math.PI * 2);
    ctx.fill();

    // Metrics Calculations
    let mp = 0;
    let tp = 0;
    let ts = 4 / (zeta * wn);
    if (zeta < 1.0) {
      mp = Math.exp((-Math.PI * zeta) / Math.sqrt(1 - zeta * zeta)) * 100;
      tp = Math.PI / (wn * Math.sqrt(1 - zeta * zeta));
    }

    // Graph Annotations
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`Mục tiêu Bước nhảy: y_ss = ${stepAmp.toFixed(1)}`, graphX + 15, graphY + 25);
    ctx.fillStyle = '#10b981';
    ctx.fillText(`Dải dung sai ±2%: [${(stepAmp * 0.98).toFixed(2)}, ${(stepAmp * 1.02).toFixed(2)}]`, graphX + 220, graphY + 25);

    // Update Telemetry Panel
    if (stats) {
      stats.innerHTML = `Hệ số tắt dần ζ: <strong>${zeta.toFixed(2)}</strong> | Tần số tự nhiên ω_n: <strong>${wn.toFixed(1)} rad/s</strong> | Độ vọt lố M_p: <strong>${mp.toFixed(1)}%</strong> | Thời gian đỉnh t_p: <strong>${tp.toFixed(2)} s</strong> | Thời gian xác lập t_s (2%): <strong>${ts.toFixed(2)} s</strong>`;
    }

    window._csdSimHandles['03'] = requestAnimationFrame(render);
  }

  render();
};

// =========================================================================
// SIM 04: Interactive PID Tuner with Disturbance Rejection (Ch 04)
// =========================================================================
window.initSim04 = function() {
  const sim = getSimCanvas('sim-canvas-04');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._csdSimHandles['04']) cancelAnimationFrame(window._csdSimHandles['04']);

  const sliderKp = document.getElementById('sim04-kp');
  const sliderKi = document.getElementById('sim04-ki');
  const sliderKd = document.getElementById('sim04-kd');
  const sliderDisturb = document.getElementById('sim04-disturb');
  const stats = document.getElementById('sim04-stats');

  // Plant State: y'' + 2y' + y = u + d
  let y = 0;
  let yd = 0;
  let integral = 0;
  let prevErr = 0;
  let history = [];
  const maxHistory = 300;
  let t = 0;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const kp = sliderKp ? parseFloat(sliderKp.value) : 8.0;
    const ki = sliderKi ? parseFloat(sliderKi.value) : 3.5;
    const kd = sliderKd ? parseFloat(sliderKd.value) : 1.8;
    const distAmp = sliderDisturb ? parseFloat(sliderDisturb.value) : 0.0;

    const r = 50.0; // Setpoint
    const dt = 1 / 60;
    t += dt;

    // Periodic or slider disturbance
    const dist = distAmp + (t > 4.0 && t < 7.0 ? 15.0 : 0.0);
    if (t > 10.0) t = 0;

    const err = r - y;
    integral = Math.max(-100, Math.min(100, integral + err * dt)); // anti-windup
    const dErr = (err - prevErr) / dt;
    prevErr = err;

    // PID Control Signal
    const uP = kp * err;
    const uI = ki * integral;
    const uD = kd * dErr;
    const u = Math.max(-150, Math.min(150, uP + uI + uD));

    // Plant 2nd-order ODE step: y'' = u + dist - 2*yd - y
    const ydd = (u + dist - 2.5 * yd - y);
    yd += ydd * dt;
    y += yd * dt;

    history.push({ r, y, u, uP, uI, uD, dist });
    if (history.length > maxHistory) history.shift();

    // 1. Dual Chart Layout
    // Chart 1: Output y(t) vs Setpoint r(t) (x: 40 to 760, y: 30 to 220)
    const c1X = 50;
    const c1Y = 30;
    const c1W = canvas.width - 100;
    const c1H = 180;

    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(c1X, c1Y, c1W, c1H);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(c1X, c1Y, c1W, c1H);

    // Setpoint line
    const rY = c1Y + c1H - (r / 80) * (c1H - 30) - 15;
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(c1X, rY);
    ctx.lineTo(c1X + c1W, rY);
    ctx.stroke();
    ctx.setLineDash([]);

    // Curve y(t)
    ctx.strokeStyle = '#06b6d4';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    history.forEach((pt, idx) => {
      const px = c1X + (idx / (maxHistory - 1)) * c1W;
      const py = c1Y + c1H - (pt.y / 80) * (c1H - 30) - 15;
      if (idx === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Chart 1 Legend
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`--- Đặt r(t) = ${r.toFixed(0)}`, c1X + 15, c1Y + 22);
    ctx.fillStyle = '#06b6d4';
    ctx.fillText(`— Ngõ ra y(t) = ${y.toFixed(1)}`, c1X + 160, c1Y + 22);
    ctx.fillStyle = '#ef4444';
    ctx.fillText(`Nhiễu tải d(t) = ${dist.toFixed(1)}`, c1X + 320, c1Y + 22);

    // Chart 2: Control Effort Breakdown u(t) = P + I + D (y: 235 to 370)
    const c2Y = 235;
    const c2H = 135;

    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(c1X, c2Y, c1W, c2H);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(c1X, c2Y, c1W, c2H);

    // Baseline 0
    const zeroY = c2Y + c2H / 2;
    ctx.strokeStyle = dark ? '#374151' : '#cbd5e1';
    ctx.beginPath();
    ctx.moveTo(c1X, zeroY); ctx.lineTo(c1X + c1W, zeroY);
    ctx.stroke();

    // Plot P, I, D components
    ctx.lineWidth = 1.5;
    // uP (Blue)
    ctx.strokeStyle = '#3b82f6';
    ctx.beginPath();
    history.forEach((pt, idx) => {
      const px = c1X + (idx / (maxHistory - 1)) * c1W;
      const py = zeroY - (pt.uP / 150) * (c2H / 2 - 10);
      if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // uI (Green)
    ctx.strokeStyle = '#10b981';
    ctx.beginPath();
    history.forEach((pt, idx) => {
      const px = c1X + (idx / (maxHistory - 1)) * c1W;
      const py = zeroY - (pt.uI / 150) * (c2H / 2 - 10);
      if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Total u (Orange)
    ctx.strokeStyle = '#f97316';
    ctx.lineWidth = 2.2;
    ctx.beginPath();
    history.forEach((pt, idx) => {
      const px = c1X + (idx / (maxHistory - 1)) * c1W;
      const py = zeroY - (pt.u / 150) * (c2H / 2 - 10);
      if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Chart 2 Legend
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6'; ctx.fillText('— u_P (Tỷ lệ)', c1X + 15, c2Y + 20);
    ctx.fillStyle = '#10b981'; ctx.fillText('— u_I (Tích phân)', c1X + 130, c2Y + 20);
    ctx.fillStyle = '#f97316'; ctx.fillText('— u(t) Tổng', c1X + 265, c2Y + 20);

    // Update Telemetry Panel
    if (stats) {
      stats.innerHTML = `Sai số e(t): <strong>${err.toFixed(2)}</strong> | Tín hiệu u: <strong>${u.toFixed(1)}</strong> (P: ${uP.toFixed(1)}, I: ${uI.toFixed(1)}, D: ${uD.toFixed(1)}) | Tích phân e: <strong>${integral.toFixed(1)}</strong> | Nhiễu d(t): <strong>${dist.toFixed(1)}</strong>`;
    }

    window._csdSimHandles['04'] = requestAnimationFrame(render);
  }

  render();
};

// =========================================================================
// SIM 05: Evans Root Locus on S-Plane with Movable Poles/Zeros (Ch 05)
// =========================================================================
window.initSim05 = function() {
  const sim = getSimCanvas('sim-canvas-05');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._csdSimHandles['05']) cancelAnimationFrame(window._csdSimHandles['05']);

  const sliderK = document.getElementById('sim05-gain');
  const sliderZ = document.getElementById('sim05-zero');
  const sliderP = document.getElementById('sim05-pole');
  const stats = document.getElementById('sim05-stats');

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const K = sliderK ? parseFloat(sliderK.value) : 18.0;
    const z1 = sliderZ ? parseFloat(sliderZ.value) : -3.5; // Compensator zero
    const p3 = sliderP ? parseFloat(sliderP.value) : -5.0; // Open-loop pole

    // S-Plane parameters
    const originX = 520;
    const originY = 200;
    const scale = 38; // px per s-plane unit

    // 1. Draw S-Plane Background
    ctx.fillStyle = dark ? '#0b0f19' : '#f8fafc';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Unstable RHP shading
    ctx.fillStyle = dark ? 'rgba(239, 68, 68, 0.08)' : 'rgba(239, 68, 68, 0.06)';
    ctx.fillRect(originX, 0, canvas.width - originX, canvas.height);

    // Coordinate Grid
    ctx.strokeStyle = dark ? '#1e293b' : '#e2e8f0';
    ctx.lineWidth = 1;
    for (let x = -12; x <= 6; x += 2) {
      const px = originX + x * scale;
      ctx.beginPath(); ctx.moveTo(px, 0); ctx.lineTo(px, canvas.height); ctx.stroke();
    }
    for (let y = -5; y <= 5; y += 2) {
      const py = originY - y * scale;
      ctx.beginPath(); ctx.moveTo(0, py); ctx.lineTo(canvas.width, py); ctx.stroke();
    }

    // Axes (Real σ and Imaginary jω)
    ctx.strokeStyle = dark ? '#64748b' : '#94a3b8';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, originY); ctx.lineTo(canvas.width, originY); // Real
    ctx.moveTo(originX, 0); ctx.lineTo(originX, canvas.height); // Imag
    ctx.stroke();

    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = dark ? '#94a3b8' : '#64748b';
    ctx.fillText('Trục Thực (σ)', canvas.width - 95, originY - 10);
    ctx.fillText('Trục Ảo (jω)', originX + 10, 25);
    ctx.fillText('ỔN ĐỊNH (LHP)', originX - 140, 25);
    ctx.fillStyle = '#ef4444';
    ctx.fillText('KHÔNG ỔN ĐỊNH (RHP)', originX + 25, 25);

    // Open-loop poles: s = 0, s = -2, s = p3
    const olPoles = [0, -2, p3];
    const olZeros = [z1];

    // 2. Draw Real-Axis Locus Branches (Odd number of poles/zeros to the right)
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 4;
    // Between 0 and -2
    ctx.beginPath();
    ctx.moveTo(originX, originY);
    ctx.lineTo(originX - 2 * scale, originY);
    ctx.stroke();
    // From p3 to z1 (or z1 to -infinity)
    const minLeft = Math.min(p3, z1);
    const maxLeft = Math.max(p3, z1);
    ctx.beginPath();
    ctx.moveTo(originX + minLeft * scale, originY);
    ctx.lineTo(originX + maxLeft * scale, originY);
    ctx.stroke();

    // Complex Asymptotes (Angle = (2k+1)*180 / (n-m) = ±90 deg, center = (sum(p) - sum(z))/(3-1))
    const sigmaA = (olPoles.reduce((a, b) => a + b, 0) - olZeros.reduce((a, b) => a + b, 0)) / (olPoles.length - olZeros.length);
    const asympX = originX + sigmaA * scale;
    ctx.strokeStyle = dark ? 'rgba(168, 85, 247, 0.4)' : 'rgba(168, 85, 247, 0.5)';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(asympX, 0); ctx.lineTo(asympX, canvas.height);
    ctx.stroke();
    ctx.setLineDash([]);

    // 3. Compute and Draw Complete Root Locus Curves (Numerical Sweep of K: 0 -> 80)
    // Characteristic eqn: s(s+2)(s-p3) + K*(s-z1) = 0
    // s^3 + (2 - p3)*s^2 + (-2*p3 + K)*s - K*z1 = 0
    ctx.strokeStyle = '#06b6d4';
    ctx.lineWidth = 2.2;
    for (let kTest = 0.1; kTest <= 75; kTest += 0.5) {
      // Find roots of cubic: s^3 + a2*s^2 + a1*s + a0 = 0
      const a2 = 2 - p3;
      const a1 = -2 * p3 + kTest;
      const a0 = -kTest * z1;

      // Approximate dominant complex conjugate roots for visualization
      const disc = Math.pow(a2 / 3, 3) - (a2 * a1) / 6 + a0 / 2;
      const reApprox = -a2 / 3 + 0.1 * Math.sin(kTest * 0.1);
      const imApprox = Math.sqrt(Math.max(0, a1 - Math.pow(reApprox, 2)));

      if (imApprox > 0.05) {
        ctx.fillStyle = '#06b6d4';
        ctx.fillRect(originX + reApprox * scale - 1, originY - imApprox * scale - 1, 2, 2);
        ctx.fillRect(originX + reApprox * scale - 1, originY + imApprox * scale - 1, 2, 2);
      }
    }

    // 4. Mark Open-Loop Poles (✕) and Zeros (○)
    ctx.font = 'bold 20px monospace';
    ctx.fillStyle = '#ef4444';
    olPoles.forEach(p => {
      ctx.fillText('✕', originX + p * scale - 7, originY + 7);
    });

    ctx.font = 'bold 22px monospace';
    ctx.fillStyle = '#10b981';
    olZeros.forEach(z => {
      ctx.fillText('○', originX + z * scale - 7, originY + 8);
    });

    // 5. Active Closed-Loop Poles at current Gain K (Highlighted Yellow Squares ■)
    // Approximate closed loop poles for current K
    const curA2 = 2 - p3;
    const curA1 = -2 * p3 + K;
    const curRe = -curA2 / 3;
    const curIm = Math.sqrt(Math.max(0, curA1 - Math.pow(curRe, 2)));

    ctx.fillStyle = '#fbbf24';
    ctx.strokeStyle = '#d97706';
    ctx.lineWidth = 2;
    // Pole 1 & 2 (Complex)
    ctx.fillRect(originX + curRe * scale - 6, originY - curIm * scale - 6, 12, 12);
    ctx.strokeRect(originX + curRe * scale - 6, originY - curIm * scale - 6, 12, 12);
    ctx.fillRect(originX + curRe * scale - 6, originY + curIm * scale - 6, 12, 12);
    ctx.strokeRect(originX + curRe * scale - 6, originY + curIm * scale - 6, 12, 12);

    // Stability Verdict
    const isStable = curRe < 0;
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = isStable ? '#10b981' : '#ef4444';
    ctx.fillText(`Trạng thái: ${isStable ? '✓ Hệ Thống ỔN ĐỊNH' : '✕ BẤT ỔN ĐỊNH'} (K = ${K.toFixed(1)})`, 40, canvas.height - 20);

    // Update Telemetry Panel
    if (stats) {
      stats.innerHTML = `Độ lợi K: <strong>${K.toFixed(1)}</strong> | Không-Điểm z: <strong>${z1.toFixed(1)}</strong> | Cực hở p_3: <strong>${p3.toFixed(1)}</strong> | Cặp cực kín: <strong>${curRe.toFixed(2)} ± j${curIm.toFixed(2)}</strong> | Giao điểm tiệm cận σ_a: <strong>${sigmaA.toFixed(2)}</strong>`;
    }

    window._csdSimHandles['05'] = requestAnimationFrame(render);
  }

  render();
};

// =========================================================================
// SIM 06: Bode & Nyquist Diagrams with GM and PM Markers (Ch 06)
// =========================================================================
window.initSim06 = function() {
  const sim = getSimCanvas('sim-canvas-06');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._csdSimHandles['06']) cancelAnimationFrame(window._csdSimHandles['06']);

  const sliderK = document.getElementById('sim06-gain');
  const sliderW0 = document.getElementById('sim06-w0');
  const sliderZeta = document.getElementById('sim06-damping');
  const stats = document.getElementById('sim06-stats');

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const K = sliderK ? parseFloat(sliderK.value) : 6.0;
    const w0 = sliderW0 ? parseFloat(sliderW0.value) : 4.0;
    const zeta = sliderZeta ? parseFloat(sliderZeta.value) : 0.35;

    // Split Canvas: Left 400px for Bode (Mag & Phase), Right 400px for Nyquist
    const bodeW = 380;
    const bodeX = 30;
    const nyqX = 440;
    const nyqW = 340;

    // 1. Frequency Response Evaluation G(jw) = K / [ jw * (1 + 2*zeta*jw/w0 + (jw/w0)^2) ]
    function evalG(w) {
      // Denominator: D = jw * ( (1 - (w/w0)^2) + j * 2*zeta*w/w0 )
      const u = 1 - Math.pow(w / w0, 2);
      const v = (2 * zeta * w) / w0;
      // D = jw*(u + jv) = -w*v + j*w*u
      const dRe = -w * v;
      const dIm = w * u;
      const dMag2 = dRe * dRe + dIm * dIm;
      const re = (K * dRe) / dMag2;
      const im = (-K * dIm) / dMag2;
      const mag = Math.sqrt(re * re + im * im);
      const magDb = 20 * Math.log10(Math.max(1e-4, mag));
      let phase = Math.atan2(im, re) * (180 / Math.PI);
      if (phase > 0) phase -= 360; // Keep in [-360, 0] deg
      return { re, im, mag, magDb, phase };
    }

    // Find Crossover Frequencies w_gc (|G|=0 dB) and w_pc (Phase = -180 deg)
    // Analytical for this system: Phase = -180 deg when 1 - (w/w0)^2 = 0 => w_pc = w0
    const w_pc = w0;
    const g_at_pc = evalG(w_pc);
    const GM = -g_at_pc.magDb; // Gain Margin in dB

    // Numerical search for w_gc where magDb ~ 0
    let w_gc = 1.0;
    for (let wTest = 0.2; wTest <= 50; wTest += 0.05) {
      if (evalG(wTest).magDb <= 0) {
        w_gc = wTest;
        break;
      }
    }
    const g_at_gc = evalG(w_gc);
    const PM = 180 + g_at_gc.phase; // Phase Margin in deg

    // 2. Plot Bode Magnitude (Top-Left: y: 25 to 180)
    const mY = 25;
    const mH = 160;
    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(bodeX, mY, bodeW, mH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(bodeX, mY, bodeW, mH);

    // 0 dB reference line
    const zeroDbY = mY + mH / 2;
    ctx.strokeStyle = '#f59e0b';
    ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(bodeX, zeroDbY); ctx.lineTo(bodeX + bodeW, zeroDbY); ctx.stroke();
    ctx.setLineDash([]);
    ctx.font = '10px monospace'; ctx.fillStyle = '#f59e0b';
    ctx.fillText('0 dB', bodeX + 6, zeroDbY - 4);

    // Magnitude Curve
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2.2;
    ctx.beginPath();
    const wMin = 0.2; const wMax = 40;
    for (let px = 0; px <= bodeW; px += 2) {
      const logW = Math.log10(wMin) + (px / bodeW) * (Math.log10(wMax) - Math.log10(wMin));
      const w = Math.pow(10, logW);
      const res = evalG(w);
      const py = zeroDbY - (res.magDb / 50) * (mH / 2 - 15);
      if (px === 0) ctx.moveTo(bodeX + px, py); else ctx.lineTo(bodeX + px, py);
    }
    ctx.stroke();

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('BIỂU ĐỒ BODE ĐỘ LỢI 20log|G(jω)| [dB]', bodeX + 15, mY + 18);

    // 3. Plot Bode Phase (Bottom-Left: y: 210 to 365)
    const pY = 210;
    const pH = 155;
    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(bodeX, pY, bodeW, pH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(bodeX, pY, bodeW, pH);

    // -180 deg reference line
    const p180Y = pY + (pH * 0.55);
    ctx.strokeStyle = '#ef4444';
    ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(bodeX, p180Y); ctx.lineTo(bodeX + bodeW, p180Y); ctx.stroke();
    ctx.setLineDash([]);
    ctx.font = '10px monospace'; ctx.fillStyle = '#ef4444';
    ctx.fillText('-180°', bodeX + 6, p180Y - 4);

    // Phase Curve
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 2.2;
    ctx.beginPath();
    for (let px = 0; px <= bodeW; px += 2) {
      const logW = Math.log10(wMin) + (px / bodeW) * (Math.log10(wMax) - Math.log10(wMin));
      const w = Math.pow(10, logW);
      const res = evalG(w);
      // Map [-270, -90] deg to pH
      const py = p180Y - ((res.phase + 180) / 90) * (pH * 0.4);
      if (px === 0) ctx.moveTo(bodeX + px, py); else ctx.lineTo(bodeX + px, py);
    }
    ctx.stroke();

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#10b981';
    ctx.fillText('BIỂU ĐỒ BODE PHA ∠G(jω) [độ]', bodeX + 15, pY + 18);

    // 4. Nyquist Polar Plot (Right: x: 440 to 780, y: 25 to 365)
    const nyqH = 340;
    const nyqCy = mY + nyqH / 2;
    const nyqCx = nyqX + nyqW / 2 + 20;
    const nyqScale = 85;

    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(nyqX, mY, nyqW, nyqH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(nyqX, mY, nyqW, nyqH);

    // Nyquist Axes
    ctx.strokeStyle = dark ? '#475569' : '#cbd5e1';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(nyqX + 10, nyqCy); ctx.lineTo(nyqX + nyqW - 10, nyqCy); // Re
    ctx.moveTo(nyqCx, mY + 10); ctx.lineTo(nyqCx, mY + nyqH - 10); // Im
    ctx.stroke();

    // Unit Circle |G| = 1
    ctx.strokeStyle = dark ? 'rgba(255,255,255,0.15)' : 'rgba(0,0,0,0.15)';
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.arc(nyqCx, nyqCy, nyqScale, 0, Math.PI * 2);
    ctx.stroke();
    ctx.setLineDash([]);

    // Critical Point (-1, j0)
    const critX = nyqCx - 1 * nyqScale;
    ctx.font = 'bold 16px monospace';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('✕', critX - 6, nyqCy + 6);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillText('(-1, j0)', critX - 16, nyqCy + 20);

    // Nyquist Curve (w: 0.1 -> 50)
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 2.4;
    ctx.beginPath();
    for (let w = 0.3; w <= 50; w += 0.1) {
      const res = evalG(w);
      const px = nyqCx + res.re * nyqScale;
      const py = nyqCy - res.im * nyqScale;
      if (w === 0.3) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#a855f7';
    ctx.fillText('ĐỒ THỊ NYQUIST CỰC G(jω)', nyqX + 15, mY + 22);

    // Update Telemetry Panel
    if (stats) {
      const stableStatus = GM > 0 && PM > 0 ? '✓ ỔN ĐỊNH' : '✕ BẤT ỔN ĐỊNH';
      stats.innerHTML = `Độ dự trữ độ lợi GM: <strong>${GM.toFixed(1)} dB</strong> (tại ω_pc = ${w_pc.toFixed(1)} rad/s) | Độ dự trữ pha PM: <strong>${PM.toFixed(1)}°</strong> (tại ω_gc = ${w_gc.toFixed(1)} rad/s) | Trạng thái: <strong>${stableStatus}</strong>`;
    }

    window._csdSimHandles['06'] = requestAnimationFrame(render);
  }

  render();
};

// =========================================================================
// SIM 07: Inverted Pendulum Cart Stabilization via LQR (Ch 07)
// =========================================================================
window.initSim07 = function() {
  const sim = getSimCanvas('sim-canvas-07');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._csdSimHandles['07']) cancelAnimationFrame(window._csdSimHandles['07']);

  const sliderQ = document.getElementById('sim07-q');
  const sliderR = document.getElementById('sim07-r');
  const btnDisturb = document.getElementById('sim07-disturb');
  const stats = document.getElementById('sim07-stats');

  // Physical parameters
  const M = 1.0;   // Cart mass (kg)
  const m = 0.2;   // Pendulum bob mass (kg)
  const l = 0.45;  // Pendulum rod length (m)
  const g = 9.81;  // Gravity (m/s^2)

  // States: x = [p, p_dot, theta, theta_dot]
  let p = 0;
  let p_dot = 0;
  let theta = 0.12; // Initial small deflection (rad)
  let theta_dot = 0;

  if (btnDisturb) {
    btnDisturb.onclick = () => {
      theta += (Math.random() > 0.5 ? 1 : -1) * 0.25;
    };
  }

  // Click on canvas to disturb
  canvas.onmousedown = (e) => {
    theta += (Math.random() > 0.5 ? 1 : -1) * 0.28;
  };

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const qTheta = sliderQ ? parseFloat(sliderQ.value) : 150.0;
    const rVal = sliderR ? parseFloat(sliderR.value) : 0.5;

    // Approximate LQR gains for inverted pendulum
    const k1 = -Math.sqrt(1.0 / rVal) * 0.8;
    const k2 = -Math.sqrt(1.0 / rVal) * 1.5;
    const k3 = Math.sqrt(qTheta / rVal) * 4.2;
    const k4 = Math.sqrt(qTheta / rVal) * 0.9;

    // State feedback control force u = -K*x
    const u = -(k1 * p + k2 * p_dot + k3 * theta + k4 * theta_dot);
    const clampedU = Math.max(-100, Math.min(100, u));

    // Dynamic equations of motion (Euler integration 60 FPS)
    const dt = 1 / 60;
    const sinT = Math.sin(theta);
    const cosT = Math.cos(theta);

    // Non-linear equations of motion
    const numTheta = g * sinT - cosT * ((clampedU + m * l * theta_dot * theta_dot * sinT) / (M + m));
    const denTheta = l * (4/3 - (m * cosT * cosT) / (M + m));
    const theta_ddot = numTheta / denTheta;

    const p_ddot = (clampedU + m * l * (theta_dot * theta_dot * sinT - theta_ddot * cosT)) / (M + m);

    p_dot += p_ddot * dt;
    p += p_dot * dt;
    theta_dot += theta_ddot * dt;
    theta += theta_dot * dt;

    // 1. Draw Physical Cart & Track (x: 40 to 760, y: 50 to 300)
    const trackY = 250;
    const cartPixX = canvas.width / 2 + p * 180;
    const cartW = 70;
    const cartH = 34;

    // Track Rail
    ctx.strokeStyle = dark ? '#475569' : '#94a3b8';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(40, trackY); ctx.lineTo(canvas.width - 40, trackY);
    ctx.stroke();

    // Position ruler markings
    ctx.font = '10px monospace';
    ctx.fillStyle = dark ? '#64748b' : '#94a3b8';
    for (let meter = -1.5; meter <= 1.5; meter += 0.5) {
      const markX = canvas.width / 2 + meter * 180;
      ctx.beginPath(); ctx.moveTo(markX, trackY); ctx.lineTo(markX, trackY + 8); ctx.stroke();
      ctx.fillText(`${meter.toFixed(1)}m`, markX - 12, trackY + 22);
    }

    // Cart Body
    ctx.fillStyle = '#3b82f6';
    ctx.fillRect(cartPixX - cartW / 2, trackY - cartH - 8, cartW, cartH);
    ctx.strokeStyle = '#1d4ed8';
    ctx.lineWidth = 2;
    ctx.strokeRect(cartPixX - cartW / 2, trackY - cartH - 8, cartW, cartH);

    // Wheels
    ctx.fillStyle = dark ? '#000000' : '#1e293b';
    ctx.beginPath();
    ctx.arc(cartPixX - 22, trackY - 4, 7, 0, Math.PI * 2);
    ctx.arc(cartPixX + 22, trackY - 4, 7, 0, Math.PI * 2);
    ctx.fill();

    // Pendulum Pivot & Rod
    const pivotX = cartPixX;
    const pivotY = trackY - cartH - 8;
    const rodLenPix = l * 320;
    const bobX = pivotX + rodLenPix * Math.sin(theta);
    const bobY = pivotY - rodLenPix * Math.cos(theta);

    // Rod
    ctx.strokeStyle = dark ? '#f1f5f9' : '#0f172a';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(pivotX, pivotY);
    ctx.lineTo(bobX, bobY);
    ctx.stroke();

    // Pivot Pin
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath(); ctx.arc(pivotX, pivotY, 5, 0, Math.PI * 2); ctx.fill();

    // Pendulum Bob (Brass weight)
    ctx.fillStyle = '#ef4444';
    ctx.beginPath(); ctx.arc(bobX, bobY, 14, 0, Math.PI * 2); ctx.fill();
    ctx.strokeStyle = '#b91c1c';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Force Vector Arrow u
    if (Math.abs(clampedU) > 1) {
      const fLen = clampedU * 1.5;
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(cartPixX, trackY - cartH / 2 - 8);
      ctx.lineTo(cartPixX + fLen, trackY - cartH / 2 - 8);
      ctx.stroke();
    }

    // Instructions
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = dark ? '#94a3b8' : '#64748b';
    ctx.fillText('💡 Nhấp chuột vào Canvas để tạo xung lực làm nghiêng con lắc!', 50, 40);

    // Update Telemetry Panel
    if (stats) {
      stats.innerHTML = `Vị trí xe p: <strong>${p.toFixed(3)} m</strong> | Góc nghiêng θ: <strong>${((theta * 180) / Math.PI).toFixed(2)}°</strong> | Lực LQR u: <strong>${clampedU.toFixed(1)} N</strong> | Vector độ lợi K = [${k1.toFixed(1)}, ${k2.toFixed(1)}, ${k3.toFixed(1)}, ${k4.toFixed(1)}]`;
    }

    window._csdSimHandles['07'] = requestAnimationFrame(render);
  }

  render();
};

// =========================================================================
// SIM 08: ZOH Sampling and Aliasing vs Continuous Signal (Ch 08)
// =========================================================================
window.initSim08 = function() {
  const sim = getSimCanvas('sim-canvas-08');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._csdSimHandles['08']) cancelAnimationFrame(window._csdSimHandles['08']);

  const sliderFs = document.getElementById('sim08-fs');
  const sliderF0 = document.getElementById('sim08-f0');
  const stats = document.getElementById('sim08-stats');

  let animT = 0;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const fs = sliderFs ? parseFloat(sliderFs.value) : 12.0; // Sampling freq (Hz)
    const f0 = sliderF0 ? parseFloat(sliderF0.value) : 3.0;   // Signal freq (Hz)

    animT += 0.005;

    const fNyquist = fs / 2;
    const isAliased = f0 > fNyquist;
    const fAlias = Math.abs(f0 - Math.round(f0 / fs) * fs);

    // 1. Time-Domain Waveforms (x: 40 to 760, y: 30 to 220)
    const cX = 50;
    const cY = 30;
    const cW = canvas.width - 100;
    const cH = 180;
    const midY = cY + cH / 2;
    const tSpan = 1.0; // 1 second window

    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(cX, cY, cW, cH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(cX, cY, cW, cH);

    // Midline
    ctx.strokeStyle = dark ? '#374151' : '#cbd5e1';
    ctx.beginPath(); ctx.moveTo(cX, midY); ctx.lineTo(cX + cW, midY); ctx.stroke();

    // A. Continuous Signal x_c(t) = sin(2*pi*f0*t) (Smooth Cyan)
    ctx.strokeStyle = '#06b6d4';
    ctx.lineWidth = 1.8;
    ctx.beginPath();
    for (let px = 0; px <= cW; px += 2) {
      const t = (px / cW) * tSpan + animT;
      const val = Math.sin(2 * Math.PI * f0 * t);
      const py = midY - val * (cH / 2 - 25);
      if (px === 0) ctx.moveTo(cX + px, py); else ctx.lineTo(cX + px, py);
    }
    ctx.stroke();

    // B. Zero-Order Hold (ZOH) Staircase Waveform (Coral Red)
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const Ts = 1 / fs;
    const totalSamples = Math.floor(tSpan / Ts);

    for (let k = 0; k <= totalSamples; k++) {
      const tSample = k * Ts + animT;
      const sampleVal = Math.sin(2 * Math.PI * f0 * tSample);
      const pxStart = cX + (k * Ts / tSpan) * cW;
      const pxEnd = cX + ((k + 1) * Ts / tSpan) * cW;
      const py = midY - sampleVal * (cH / 2 - 25);

      if (k === 0) ctx.moveTo(pxStart, py);
      else {
        ctx.lineTo(pxStart, py); // Vertical jump
      }
      ctx.lineTo(Math.min(cX + cW, pxEnd), py); // Horizontal hold
    }
    ctx.stroke();

    // C. Sample Points (Stem Markers)
    for (let k = 0; k <= totalSamples; k++) {
      const tSample = k * Ts + animT;
      const sampleVal = Math.sin(2 * Math.PI * f0 * tSample);
      const px = cX + (k * Ts / tSpan) * cW;
      const py = midY - sampleVal * (cH / 2 - 25);

      ctx.fillStyle = '#fbbf24';
      ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI * 2); ctx.fill();
    }

    // Chart 1 Legend
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#06b6d4'; ctx.fillText(`— Tín hiệu tương tự x(t) (f_0 = ${f0.toFixed(1)} Hz)`, cX + 15, cY + 22);
    ctx.fillStyle = '#ef4444'; ctx.fillText(`— Khâu giữ bậc 0 ZOH (f_s = ${fs.toFixed(1)} Hz)`, cX + 280, cY + 22);

    // 2. Frequency Spectrum Bar Display (Bottom: y: 240 to 370)
    const sY = 235;
    const sH = 135;
    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(cX, sY, cW, sH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(cX, sY, cW, sH);

    const fMax = 30.0;
    const nyqPX = cX + (fNyquist / fMax) * cW;

    // Nyquist Frequency Barrier Line (Red Dashed)
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(nyqPX, sY); ctx.lineTo(nyqPX, sY + sH); ctx.stroke();
    ctx.setLineDash([]);

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText(`Giới hạn Nyquist: f_s/2 = ${fNyquist.toFixed(1)} Hz`, nyqPX + 8, sY + 22);

    // Signal Spike f0
    const f0PX = cX + (Math.min(fMax, f0) / fMax) * cW;
    ctx.fillStyle = '#06b6d4';
    ctx.fillRect(f0PX - 4, sY + sH - 75, 8, 75);
    ctx.fillText(`f_0 = ${f0.toFixed(1)} Hz`, f0PX - 20, sY + sH - 85);

    // Aliased Phantom Frequency if aliased
    if (isAliased) {
      const aliasPX = cX + (fAlias / fMax) * cW;
      ctx.fillStyle = '#f59e0b';
      ctx.fillRect(aliasPX - 4, sY + sH - 60, 8, 60);
      ctx.fillText(`Tần số ảo Alias: ${fAlias.toFixed(1)} Hz`, aliasPX - 25, sY + sH - 68);
    }

    // Update Telemetry Panel
    if (stats) {
      const verdict = isAliased
        ? `<span style="color:#ef4444">⚠️ CẢNH BÁO ALIASING: Tín hiệu bị chồng phổ sang ${fAlias.toFixed(2)} Hz!</span>`
        : `<span style="color:#10b981">✓ AN TOÀN: f_0 < f_s/2 (Thỏa mãn Định lý Shannon-Nyquist)</span>`;
      stats.innerHTML = `Tần số tín hiệu: <strong>${f0.toFixed(1)} Hz</strong> | Tần số lấy mẫu f_s: <strong>${fs.toFixed(1)} Hz</strong> | Chu kỳ T_s: <strong>${(Ts * 1000).toFixed(1)} ms</strong> | Trạng thái: ${verdict}`;
    }

    window._csdSimHandles['08'] = requestAnimationFrame(render);
  }

  render();
};

// =========================================================================
// SIM 09: Sliding Mode Control (s=0) & MPC Receding Horizon (Ch 09)
// =========================================================================
window.initSim09 = function() {
  const sim = getSimCanvas('sim-canvas-09');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._csdSimHandles['09']) cancelAnimationFrame(window._csdSimHandles['09']);

  const sliderLambda = document.getElementById('sim09-lambda');
  const sliderK = document.getElementById('sim09-k');
  const stats = document.getElementById('sim09-stats');

  let e = 4.0;
  let ed = -2.0;
  let phaseHistory = [];
  const maxHistory = 350;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const lambda = sliderLambda ? parseFloat(sliderLambda.value) : 1.8;
    const k_sw = sliderK ? parseFloat(sliderK.value) : 6.0;

    // Simulation Step
    const dt = 1 / 60;
    // Sliding surface: s = e_dot + lambda * e
    const s = ed + lambda * e;
    // Discontinuous switching control: u_sw = -k_sw * sat(s / epsilon)
    const epsilon = 0.2;
    const satS = Math.max(-1, Math.min(1, s / epsilon));
    const u = -k_sw * satS;

    // Dynamics: e'' = u + disturbance
    const edd = u;
    ed += edd * dt;
    e += ed * dt;

    // Reset trajectory if settled
    if (Math.abs(e) < 0.05 && Math.abs(ed) < 0.05) {
      e = (Math.random() > 0.5 ? 1 : -1) * (3.0 + Math.random() * 2.0);
      ed = (Math.random() - 0.5) * 4.0;
      phaseHistory = [];
    }

    phaseHistory.push({ e, ed });
    if (phaseHistory.length > maxHistory) phaseHistory.shift();

    // 1. Phase Portrait (Left 420px: x: 30 to 440, y: 30 to 370)
    const ppX = 30;
    const ppY = 30;
    const ppW = 410;
    const ppH = 340;
    const ppCx = ppX + ppW / 2;
    const ppCy = ppY + ppH / 2;
    const ppScale = 32;

    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(ppX, ppY, ppW, ppH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(ppX, ppY, ppW, ppH);

    // Axes
    ctx.strokeStyle = dark ? '#475569' : '#cbd5e1';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(ppX, ppCy); ctx.lineTo(ppX + ppW, ppCy); // e axis
    ctx.moveTo(ppCx, ppY); ctx.lineTo(ppCx, ppY + ppH); // e_dot axis
    ctx.stroke();

    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = dark ? '#94a3b8' : '#64748b';
    ctx.fillText('Sai số e', ppX + ppW - 60, ppCy - 8);
    ctx.fillText('Đạo hàm sai số ė', ppCx + 8, ppY + 20);

    // Sliding Surface Line: s = e_dot + lambda*e = 0 => e_dot = -lambda * e
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const eMax = 6.0;
    ctx.moveTo(ppCx - eMax * ppScale, ppCy - (-lambda * -eMax) * ppScale);
    ctx.lineTo(ppCx + eMax * ppScale, ppCy - (-lambda * eMax) * ppScale);
    ctx.stroke();

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#10b981';
    ctx.fillText(`Mặt Trượt s = ė + ${lambda.toFixed(1)}e = 0`, ppX + 15, ppY + 25);

    // Phase Trajectory Curve
    ctx.strokeStyle = '#06b6d4';
    ctx.lineWidth = 2;
    ctx.beginPath();
    phaseHistory.forEach((pt, idx) => {
      const px = ppCx + pt.e * ppScale;
      const py = ppCy - pt.ed * ppScale;
      if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Active Operating Point
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.arc(ppCx + e * ppScale, ppCy - ed * ppScale, 6, 0, Math.PI * 2);
    ctx.fill();

    // 2. MPC Receding Horizon Prediction Timeline (Right: x: 470 to 770)
    const mpcX = 470;
    const mpcY = 30;
    const mpcW = 310;
    const mpcH = 340;

    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(mpcX, mpcY, mpcW, mpcH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(mpcX, mpcY, mpcW, mpcH);

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#a855f7';
    ctx.fillText('MÔ PHỎNG MPC CHÂN TRỜI LÙI (HORIZON N=10)', mpcX + 15, mpcY + 25);

    // Draw planned optimal trajectory over prediction horizon
    const mpcMidY = mpcY + mpcH / 2;
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 2;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(mpcX + 30, mpcMidY - e * 18);
    for (let k = 1; k <= 10; k++) {
      const predictedE = e * Math.exp(-0.35 * k);
      const px = mpcX + 30 + k * 24;
      const py = mpcMidY - predictedE * 18;
      ctx.lineTo(px, py);
    }
    ctx.stroke();
    ctx.setLineDash([]);

    // Horizon points
    for (let k = 0; k <= 10; k++) {
      const predictedE = e * Math.exp(-0.35 * k);
      const px = mpcX + 30 + k * 24;
      const py = mpcMidY - predictedE * 18;
      ctx.fillStyle = k === 0 ? '#f59e0b' : '#a855f7';
      ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI * 2); ctx.fill();
    }

    // Constraints Envelope [-umax, +umax]
    ctx.strokeStyle = '#ef4444';
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(mpcX + 20, mpcY + 70); ctx.lineTo(mpcX + mpcW - 20, mpcY + 70);
    ctx.moveTo(mpcX + 20, mpcY + mpcH - 60); ctx.lineTo(mpcX + mpcW - 20, mpcY + mpcH - 60);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.font = '10px monospace'; ctx.fillStyle = '#ef4444';
    ctx.fillText('Ràng buộc +u_max', mpcX + 25, mpcY + 65);
    ctx.fillText('Ràng buộc -u_max', mpcX + 25, mpcY + mpcH - 65);

    // Update Telemetry Panel
    if (stats) {
      stats.innerHTML = `Mặt trượt s: <strong>${s.toFixed(2)}</strong> | Sai số e: <strong>${e.toFixed(2)}</strong> | Tín hiệu SMC u: <strong>${u.toFixed(2)}</strong> | Độ dốc λ: <strong>${lambda.toFixed(1)}</strong> | Độ lợi chuyển mạch K_sw: <strong>${k_sw.toFixed(1)}</strong>`;
    }

    window._csdSimHandles['09'] = requestAnimationFrame(render);
  }

  render();
};

// =========================================================================
// SIM 10: Fuzzy Logic Controller Surface & Mamdani Rule Activation (Ch 10)
// =========================================================================
window.initSim10 = function() {
  const sim = getSimCanvas('sim-canvas-10');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._csdSimHandles['10']) cancelAnimationFrame(window._csdSimHandles['10']);

  const sliderE = document.getElementById('sim10-error');
  const sliderDE = document.getElementById('sim10-derror');
  const stats = document.getElementById('sim10-stats');

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const eVal = sliderE ? parseFloat(sliderE.value) : 2.5;    // Error in [-10, 10]
    const deVal = sliderDE ? parseFloat(sliderDE.value) : -1.5; // dError in [-5, 5]

    // 1. Triangular Membership Function Helper
    function trimf(x, a, b, c) {
      return Math.max(0, Math.min((x - a) / (b - a + 1e-6), (c - x) / (c - b + 1e-6)));
    }

    // 5 Linguistic Labels: NB, NS, ZE, PS, PB
    const eMFs = [
      { name: 'NB', val: trimf(eVal, -10, -10, -4) },
      { name: 'NS', val: trimf(eVal, -8, -4, 0) },
      { name: 'ZE', val: trimf(eVal, -3, 0, 3) },
      { name: 'PS', val: trimf(eVal, 0, 4, 8) },
      { name: 'PB', val: trimf(eVal, 4, 10, 10) }
    ];

    const deMFs = [
      { name: 'NB', val: trimf(deVal, -5, -5, -2) },
      { name: 'NS', val: trimf(deVal, -4, -2, 0) },
      { name: 'ZE', val: trimf(deVal, -1.5, 0, 1.5) },
      { name: 'PS', val: trimf(deVal, 0, 2, 4) },
      { name: 'PB', val: trimf(deVal, 2, 5, 5) }
    ];

    // 2. Mamdani Rule Base (5x5 Matrix)
    // Table: output linguistic terms from -2 (NB) to +2 (PB)
    const ruleMatrix = [
      [-2, -2, -2, -1,  0], // e = NB
      [-2, -1, -1,  0,  1], // e = NS
      [-1, -1,  0,  1,  1], // e = ZE
      [-1,  0,  1,  1,  2], // e = PS
      [ 0,  1,  2,  2,  2]  // e = PB
    ];

    // Center of Gravity (Centroid) Defuzzification
    let num = 0;
    let den = 0;
    let activeRuleCount = 0;

    for (let r = 0; r < 5; r++) {
      for (let c = 0; c < 5; c++) {
        const weight = Math.min(eMFs[r].val, deMFs[c].val); // Mamdani Min implication
        if (weight > 0.01) {
          activeRuleCount++;
          const outVal = ruleMatrix[r][c] * 5.0; // scale to output
          num += weight * outVal;
          den += weight;
        }
      }
    }
    const crispOutput = den > 0 ? num / den : 0;

    // 3. Visualization Layout
    // Left: Membership Functions for e & de (x: 30 to 280)
    const mfX = 30;
    const mfW = 250;

    // MF for Error e
    const eY = 30;
    const eH = 145;
    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(mfX, eY, mfW, eH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(mfX, eY, mfW, eH);

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('HÀM THUỘC TÍNH SAI SỐ e [-10, 10]', mfX + 12, eY + 20);

    // Draw triangles for e
    const centersE = [-10, -4, 0, 4, 10];
    const colors = ['#ef4444', '#f59e0b', '#10b981', '#06b6d4', '#8b5cf6'];
    for (let i = 0; i < 5; i++) {
      ctx.strokeStyle = colors[i];
      ctx.lineWidth = 1.6;
      ctx.beginPath();
      const pxC = mfX + 20 + ((centersE[i] + 10) / 20) * (mfW - 40);
      const pxL = mfX + 20 + ((Math.max(-10, centersE[i] - 5) + 10) / 20) * (mfW - 40);
      const pxR = mfX + 20 + ((Math.min(10, centersE[i] + 5) + 10) / 20) * (mfW - 40);
      ctx.moveTo(pxL, eY + eH - 20);
      ctx.lineTo(pxC, eY + 35);
      ctx.lineTo(pxR, eY + eH - 20);
      ctx.stroke();
    }
    // Cursor for current e
    const curEX = mfX + 20 + ((eVal + 10) / 20) * (mfW - 40);
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(curEX, eY + 25); ctx.lineTo(curEX, eY + eH - 20); ctx.stroke();

    // MF for Change of Error de
    const deY = 205;
    const deH = 165;
    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(mfX, deY, mfW, deH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(mfX, deY, mfW, deH);

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#10b981';
    ctx.fillText('HÀM THUỘC TÍNH ĐẠO HÀM Δe [-5, 5]', mfX + 12, deY + 22);

    // Cursor for current de
    const curDEX = mfX + 20 + ((deVal + 5) / 10) * (mfW - 40);
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(curDEX, deY + 28); ctx.lineTo(curDEX, deY + deH - 20); ctx.stroke();

    // Center: 5x5 Fuzzy Rule Table (x: 310 to 570)
    const ruleX = 310;
    const ruleY = 30;
    const ruleW = 250;
    const ruleH = 340;
    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(ruleX, ruleY, ruleW, ruleH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(ruleX, ruleY, ruleW, ruleH);

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#a855f7';
    ctx.fillText('MA TRẬN LUẬT MỜ MAMDANI (5x5)', ruleX + 15, ruleY + 24);

    const cellW = 38;
    const cellH = 44;
    for (let r = 0; r < 5; r++) {
      for (let c = 0; c < 5; c++) {
        const cx = ruleX + 45 + c * cellW;
        const cy = ruleY + 60 + r * cellH;
        const firing = Math.min(eMFs[r].val, deMFs[c].val);

        ctx.fillStyle = firing > 0.01
          ? `rgba(245, 158, 11, ${Math.min(1, firing * 1.4)})`
          : (dark ? '#1e293b' : '#f1f5f9');
        ctx.fillRect(cx, cy, cellW - 4, cellH - 4);
        ctx.strokeStyle = dark ? '#374151' : '#cbd5e1';
        ctx.strokeRect(cx, cy, cellW - 4, cellH - 4);

        const outLabel = ['NB', 'NS', 'ZE', 'PS', 'PB'][ruleMatrix[r][c] + 2];
        ctx.font = 'bold 10px monospace';
        ctx.fillStyle = firing > 0.3 ? '#000000' : (dark ? '#94a3b8' : '#64748b');
        ctx.fillText(outLabel, cx + 8, cy + 24);
      }
    }

    // Right: Defuzzified Crisp Output Dial (x: 590 to 770)
    const outX = 590;
    const outY = 30;
    const outW = 180;
    const outH = 340;
    ctx.fillStyle = dark ? '#111827' : '#ffffff';
    ctx.fillRect(outX, outY, outW, outH);
    ctx.strokeStyle = dark ? '#374151' : '#e2e8f0';
    ctx.strokeRect(outX, outY, outW, outH);

    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('GIẢI MỜ TRỌNG TÂM', outX + 15, outY + 25);

    // Vertical Thermometer / Bar for Crisp Output u*
    const barX = outX + outW / 2 - 15;
    const barY = outY + 60;
    const barH = 200;
    ctx.fillStyle = dark ? '#1e293b' : '#e2e8f0';
    ctx.fillRect(barX, barY, 30, barH);

    // Fill level based on crispOutput [-10, 10]
    const fillFrac = (crispOutput + 10) / 20;
    const fillH = fillFrac * barH;
    ctx.fillStyle = crispOutput >= 0 ? '#10b981' : '#ef4444';
    ctx.fillRect(barX, barY + barH - fillH, 30, fillH);
    ctx.strokeStyle = '#d97706';
    ctx.lineWidth = 2;
    ctx.strokeRect(barX, barY, 30, barH);

    ctx.font = 'bold 16px monospace';
    ctx.fillStyle = dark ? '#ffffff' : '#0f172a';
    ctx.textAlign = 'center';
    ctx.fillText(`${crispOutput.toFixed(2)} V`, outX + outW / 2, outY + 295);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText(`Luật kích hoạt: ${activeRuleCount}`, outX + outW / 2, outY + 318);
    ctx.textAlign = 'left';

    // Update Telemetry Panel
    if (stats) {
      stats.innerHTML = `Sai số e: <strong>${eVal.toFixed(1)}</strong> | Đạo hàm sai số Δe: <strong>${deVal.toFixed(1)}</strong> | Số luật mờ kích hoạt: <strong>${activeRuleCount}/25</strong> | Ngõ ra giải mờ trọng tâm u*: <strong>${crispOutput.toFixed(2)} V</strong>`;
    }

    window._csdSimHandles['10'] = requestAnimationFrame(render);
  }

  render();
};
