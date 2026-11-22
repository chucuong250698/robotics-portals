/**
 * ============================================================================
 * ELEMENTS OF ROBOTICS - INTERACTIVE EXPLORABLE SIMULATORS (HTML5 CANVAS)
 * 8 Bộ mô phỏng đồ thị & hoạt họa tương tác thời gian thực cho Web Tri Thức
 * ============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initPIDSimulator();
  initDiffDriveSimulator();
  initHysteresisSimulator();
  initBayesSimulator();
  initArmSimulator();
  initAStarSimulator();
  initBraitenbergSimulator();
  initToFSimulator();
});

// ============================================================================
// SIMULATOR 1: PID POSITION CONTROL WITH ANTI-WINDUP TUNER (CHƯƠNG 6)
// ============================================================================
function initPIDSimulator() {
  const canvas = document.getElementById('pid-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const kpSlider = document.getElementById('pid-kp');
  const kiSlider = document.getElementById('pid-ki');
  const kdSlider = document.getElementById('pid-kd');
  const umaxSlider = document.getElementById('pid-umax');
  const antiWindupToggle = document.getElementById('pid-antiwindup');
  const resetBtn = document.getElementById('pid-reset');

  const kpValue = document.getElementById('pid-kp-val');
  const kiValue = document.getElementById('pid-ki-val');
  const kdValue = document.getElementById('pid-kd-val');
  const umaxValue = document.getElementById('pid-umax-val');

  const metricOvershoot = document.getElementById('pid-metric-overshoot');
  const metricSettling = document.getElementById('pid-metric-settling');
  const metricStatus = document.getElementById('pid-metric-status');

  function simulate() {
    const Kp = parseFloat(kpSlider.value);
    const Ki = parseFloat(kiSlider.value);
    const Kd = parseFloat(kdSlider.value);
    const uMax = parseFloat(umaxSlider.value);
    const useAntiWindup = antiWindupToggle ? antiWindupToggle.checked : true;

    kpValue.textContent = Kp.toFixed(1);
    kiValue.textContent = Ki.toFixed(1);
    kdValue.textContent = Kd.toFixed(2);
    umaxValue.textContent = uMax.toFixed(1) + ' V';

    const tMax = 8.0;
    const dt = 0.02;
    const steps = Math.floor(tMax / dt);
    const setpoint = 2.0;
    const tau = 0.5;

    const tArr = [];
    const yArr = [];
    const uArr = [];

    let pos = 0.0;
    let vel = 0.0;
    let integral = 0.0;
    let prevErr = setpoint;

    for (let k = 0; k < steps; k++) {
      const t = k * dt;
      tArr.push(t);
      yArr.push(pos);

      const err = setpoint - pos;
      const derivative = (err - prevErr) / dt;
      const tentativeI = integral + err * dt;
      const uRaw = Kp * err + Ki * tentativeI + Kd * derivative;

      let uSat = Math.max(-uMax, Math.min(uMax, uRaw));
      if (useAntiWindup) {
        if ((uRaw > uMax && err < 0) || (uRaw < -uMax && err > 0) || (uRaw >= -uMax && uRaw <= uMax)) {
          integral = tentativeI;
        }
      } else {
        integral = tentativeI;
      }

      uArr.push(uSat);
      prevErr = err;

      vel += ((uSat - vel) / tau) * dt;
      pos += vel * dt;
    }

    const maxY = Math.max(...yArr);
    const overshoot = maxY > setpoint ? ((maxY - setpoint) / setpoint) * 100 : 0;
    metricOvershoot.textContent = overshoot.toFixed(1) + '%';

    let settlingIdx = steps - 1;
    for (let k = steps - 1; k >= 0; k--) {
      if (Math.abs(yArr[k] - setpoint) > 0.05 * setpoint) {
        settlingIdx = k;
        break;
      }
    }
    const settlingTime = settlingIdx < steps - 1 ? (settlingIdx * dt).toFixed(2) + ' s' : '> 8.0 s';
    metricSettling.textContent = settlingTime;

    if (overshoot < 5.0) {
      metricStatus.textContent = 'Rất êm (Không vọt lố)';
      metricStatus.style.color = '#10b981';
    } else if (overshoot < 25.0) {
      metricStatus.textContent = 'Vọt lố vừa phải';
      metricStatus.style.color = '#f59e0b';
    } else {
      metricStatus.textContent = 'Bão hòa / Vọt lố lớn';
      metricStatus.style.color = '#ef4444';
    }

    drawPID(tArr, yArr, uArr, setpoint, uMax, tMax);
  }

  function drawPID(tArr, yArr, uArr, setpoint, uMax, tMax) {
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    const padL = 55;
    const padR = 25;
    const padT = 25;
    const padB = 40;
    const gap = 35;
    const h1 = (h - padT - padB - gap) * 0.62;
    const h2 = (h - padT - padB - gap) * 0.38;
    const yTop2 = padT + h1 + gap;

    const plotW = w - padL - padR;

    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const yMaxVal = 3.2;
    function mapX(t) { return padL + (t / tMax) * plotW; }
    function mapY1(y) { return padT + h1 - (y / yMaxVal) * h1; }
    function mapY2(u) { return yTop2 + h2 / 2 - (u / (uMax * 1.3)) * (h2 / 2); }

    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    for (let y = 0; y <= 3.0; y += 1.0) {
      const py = mapY1(y);
      ctx.beginPath();
      ctx.moveTo(padL, py);
      ctx.lineTo(w - padR, py);
      ctx.stroke();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px JetBrains Mono, monospace';
      ctx.textAlign = 'right';
      ctx.fillText(y.toFixed(1) + 'm', padL - 8, py + 4);
    }

    const spY = mapY1(setpoint);
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 1.8;
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(padL, spY);
    ctx.lineTo(w - padR, spY);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = '#f59e0b';
    ctx.textAlign = 'left';
    ctx.fillText('Setpoint (2.0 m)', padL + 10, spY - 6);

    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let k = 0; k < tArr.length; k++) {
      const px = mapX(tArr[k]);
      const py = mapY1(yArr[k]);
      if (k === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    ctx.fillStyle = '#f1f5f9';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('Đáp ứng vị trí y(t)', padL, padT - 8);

    ctx.fillStyle = '#f1f5f9';
    ctx.fillText('Điện áp điều khiển u(t) (V)', padL, yTop2 - 8);

    ctx.strokeStyle = '#334155';
    ctx.beginPath();
    ctx.moveTo(padL, mapY2(0));
    ctx.lineTo(w - padR, mapY2(0));
    ctx.stroke();

    ctx.strokeStyle = '#ef4444';
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(padL, mapY2(uMax));
    ctx.lineTo(w - padR, mapY2(uMax));
    ctx.moveTo(padL, mapY2(-uMax));
    ctx.lineTo(w - padR, mapY2(-uMax));
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let k = 0; k < tArr.length; k++) {
      const px = mapX(tArr[k]);
      const py = mapY2(uArr[k]);
      if (k === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px JetBrains Mono, monospace';
    ctx.textAlign = 'center';
    for (let t = 0; t <= tMax; t += 2) {
      const px = mapX(t);
      ctx.fillText(t + 's', px, h - 15);
    }
  }

  [kpSlider, kiSlider, kdSlider, umaxSlider].forEach(slider => {
    slider.addEventListener('input', simulate);
  });
  if (antiWindupToggle) antiWindupToggle.addEventListener('change', simulate);
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      kpSlider.value = 2.5;
      kiSlider.value = 1.0;
      kdSlider.value = 0.4;
      umaxSlider.value = 1.5;
      if (antiWindupToggle) antiWindupToggle.checked = true;
      simulate();
    });
  }

  simulate();
}

// ============================================================================
// SIMULATOR 2: DIFFERENTIAL DRIVE KINEMATICS & ICC VISUALIZER (CHƯƠNG 5)
// ============================================================================
function initDiffDriveSimulator() {
  const canvas = document.getElementById('diff-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const vlSlider = document.getElementById('diff-vl');
  const vrSlider = document.getElementById('diff-vr');
  const bSlider = document.getElementById('diff-b');
  const playBtn = document.getElementById('diff-play');
  const resetBtn = document.getElementById('diff-reset');

  const vlVal = document.getElementById('diff-vl-val');
  const vrVal = document.getElementById('diff-vr-val');
  const bVal = document.getElementById('diff-b-val');

  const metricV = document.getElementById('diff-metric-v');
  const metricOmega = document.getElementById('diff-metric-omega');
  const metricRadius = document.getElementById('diff-metric-rc');

  let isPlaying = true;
  let robotX = 0;
  let robotY = 0;
  let robotTheta = 0;
  let trajectory = [];

  function updateParams() {
    const vl = parseFloat(vlSlider.value);
    const vr = parseFloat(vrSlider.value);
    const b = parseFloat(bSlider.value);

    vlVal.textContent = vl.toFixed(2) + ' m/s';
    vrVal.textContent = vr.toFixed(2) + ' m/s';
    bVal.textContent = b.toFixed(2) + ' m';

    const v = (vr + vl) / 2;
    const omega = (vr - vl) / b;
    let rcStr = '∞ (Chạy thẳng)';
    if (Math.abs(vr - vl) > 0.01) {
      const rc = (b / 2) * (vr + vl) / (vr - vl);
      rcStr = rc.toFixed(2) + ' m';
    } else if (Math.abs(v) < 0.01 && Math.abs(omega) > 0.01) {
      rcStr = '0.00 m (Xoay tại chỗ)';
    }

    metricV.textContent = v.toFixed(2) + ' m/s';
    metricOmega.textContent = omega.toFixed(2) + ' rad/s';
    metricRadius.textContent = rcStr;
  }

  function resetSim() {
    robotX = 0;
    robotY = 0;
    robotTheta = 0;
    trajectory = [];
  }

  function render() {
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const cx = w / 2;
    const cy = h / 2;
    const scale = 110;

    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    for (let x = 0; x < w; x += 40) {
      ctx.beginPath();
      ctx.moveTo(x, 0); ctx.lineTo(x, h);
      ctx.stroke();
    }
    for (let y = 0; y < h; y += 40) {
      ctx.beginPath();
      ctx.moveTo(0, y); ctx.lineTo(w, y);
      ctx.stroke();
    }

    const vl = parseFloat(vlSlider.value);
    const vr = parseFloat(vrSlider.value);
    const b = parseFloat(bSlider.value);
    const v = (vr + vl) / 2;
    const omega = (vr - vl) / b;

    if (isPlaying) {
      const dt = 0.03;
      robotTheta += omega * dt;
      robotX += v * Math.cos(robotTheta) * dt;
      robotY += v * Math.sin(robotTheta) * dt;

      trajectory.push({ x: robotX, y: robotY });
      if (trajectory.length > 350) trajectory.shift();
    }

    if (trajectory.length > 1) {
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i < trajectory.length; i++) {
        const px = cx + trajectory[i].x * scale;
        const py = cy - trajectory[i].y * scale;
        if (i === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();
    }

    const rx = cx + robotX * scale;
    const ry = cy - robotY * scale;

    if (Math.abs(vr - vl) > 0.02) {
      const R = (b / 2) * (vr + vl) / (vr - vl);
      const iccX = rx - R * scale * Math.sin(robotTheta);
      const iccY = ry - R * scale * Math.cos(robotTheta);

      ctx.strokeStyle = '#e2e8f0';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(rx, ry);
      ctx.lineTo(iccX, iccY);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(iccX, iccY, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#fca5a5';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillText('ICC', iccX + 8, iccY + 4);
    }

    ctx.save();
    ctx.translate(rx, ry);
    ctx.rotate(-robotTheta);

    ctx.fillStyle = '#1e3a8a';
    ctx.strokeStyle = '#60a5fa';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(0, 0, (b * scale) / 2 + 5, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#10b981';
    ctx.beginPath();
    ctx.moveTo(18, 0);
    ctx.lineTo(-6, -10);
    ctx.lineTo(-6, 10);
    ctx.closePath();
    ctx.fill();

    ctx.fillStyle = '#0f172a';
    ctx.strokeStyle = '#cbd5e1';
    ctx.fillRect(-12, -(b * scale) / 2 - 4, 24, 8);
    ctx.strokeRect(-12, -(b * scale) / 2 - 4, 24, 8);

    ctx.fillRect(-12, (b * scale) / 2 - 4, 24, 8);
    ctx.strokeRect(-12, (b * scale) / 2 - 4, 24, 8);

    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(0, -(b * scale) / 2);
    ctx.lineTo(vl * 40, -(b * scale) / 2);
    ctx.moveTo(0, (b * scale) / 2);
    ctx.lineTo(vr * 40, (b * scale) / 2);
    ctx.stroke();

    ctx.restore();

    requestAnimationFrame(render);
  }

  [vlSlider, vrSlider, bSlider].forEach(slider => {
    slider.addEventListener('input', updateParams);
  });
  if (playBtn) {
    playBtn.addEventListener('click', () => {
      isPlaying = !isPlaying;
      playBtn.textContent = isPlaying ? 'Tạm Dừng' : 'Tiếp Tục';
    });
  }
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      vlSlider.value = 0.3;
      vrSlider.value = 0.6;
      bSlider.value = 0.25;
      updateParams();
      resetSim();
    });
  }

  updateParams();
  requestAnimationFrame(render);
}

// ============================================================================
// SIMULATOR 3: FSM HYSTERESIS WALL-FOLLOWING SIMULATOR (CHƯƠNG 4)
// ============================================================================
function initHysteresisSimulator() {
  const canvas = document.getElementById('hysteresis-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const dSlider = document.getElementById('hys-d');
  const tauLowSlider = document.getElementById('hys-low');
  const tauHighSlider = document.getElementById('hys-high');
  const resetBtn = document.getElementById('hys-reset');

  const dVal = document.getElementById('hys-d-val');
  const lowVal = document.getElementById('hys-low-val');
  const highVal = document.getElementById('hys-high-val');

  const stateBadge = document.getElementById('hys-state-badge');
  const deadbandMetric = document.getElementById('hys-deadband-metric');

  let currentState = 'RẼ PHẢI (ÉP SÁT)';

  function update() {
    const d = parseFloat(dSlider.value);
    let low = parseFloat(tauLowSlider.value);
    let high = parseFloat(tauHighSlider.value);

    if (low >= high) {
      low = high - 2.0;
      tauLowSlider.value = low;
    }

    dVal.textContent = d.toFixed(1) + ' cm';
    lowVal.textContent = low.toFixed(1) + ' cm';
    highVal.textContent = high.toFixed(1) + ' cm';

    const deadband = high - low;
    deadbandMetric.textContent = deadband.toFixed(1) + ' cm';

    if (d < low) {
      currentState = 'RẼ TRÁI (TRÁNH XA)';
    } else if (d > high) {
      currentState = 'RẼ PHẢI (ÉP SÁT)';
    }

    stateBadge.textContent = currentState;
    if (currentState.includes('TRÁI')) {
      stateBadge.style.background = '#ef4444';
      stateBadge.style.color = '#fff';
    } else {
      stateBadge.style.background = '#2563eb';
      stateBadge.style.color = '#fff';
    }

    drawHysteresis(d, low, high, currentState);
  }

  function drawHysteresis(d, low, high, state) {
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const maxD = 32.0;
    const padL = 70;
    const padR = 40;
    const scaleX = (w - padL - padR) / maxD;

    function mapX(val) { return padL + val * scaleX; }

    ctx.fillStyle = '#475569';
    ctx.fillRect(padL - 18, 20, 18, h - 50);
    ctx.fillStyle = '#f8fafc';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.save();
    ctx.translate(padL - 6, h / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.textAlign = 'center';
    ctx.fillText('BỨC TƯỜNG (WALL)', 0, 0);
    ctx.restore();

    const xLow = mapX(low);
    const xHigh = mapX(high);
    ctx.fillStyle = 'rgba(59, 130, 246, 0.18)';
    ctx.fillRect(xLow, 20, xHigh - xLow, h - 50);

    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(xLow, 20); ctx.lineTo(xLow, h - 30);
    ctx.stroke();

    ctx.strokeStyle = '#3b82f6';
    ctx.beginPath();
    ctx.moveTo(xHigh, 20); ctx.lineTo(xHigh, h - 30);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.font = '11px JetBrains Mono, monospace';
    ctx.fillStyle = '#fca5a5';
    ctx.textAlign = 'center';
    ctx.fillText('τ_low = ' + low.toFixed(1), xLow, 15);
    ctx.fillStyle = '#93c5fd';
    ctx.fillText('τ_high = ' + high.toFixed(1), xHigh, 15);

    ctx.fillStyle = '#a78bfa';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('VÙNG TRỄ HYSTERESIS (Δ = ' + (high - low).toFixed(1) + ' cm)', (xLow + xHigh) / 2, h / 2 - 35);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillText('(Giữ nguyên trạng thái cũ, khử rung giật)', (xLow + xHigh) / 2, h / 2 - 18);

    const rx = mapX(d);
    const ry = h / 2 + 30;

    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(padL, ry);
    ctx.lineTo(rx, ry);
    ctx.stroke();

    ctx.fillStyle = state.includes('TRÁI') ? '#ef4444' : '#2563eb';
    ctx.beginPath();
    ctx.arc(rx, ry, 16, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.fillStyle = '#fff';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('BOT', rx, ry + 4);

    ctx.fillStyle = '#fbbf24';
    ctx.font = 'bold 12px JetBrains Mono, monospace';
    ctx.fillText('d = ' + d.toFixed(1) + ' cm', rx, ry + 36);

    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(padL, h - 25);
    ctx.lineTo(w - padR, h - 25);
    ctx.stroke();

    for (let tick = 0; tick <= maxD; tick += 5) {
      const tx = mapX(tick);
      ctx.beginPath();
      ctx.moveTo(tx, h - 25);
      ctx.lineTo(tx, h - 18);
      ctx.stroke();
      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px JetBrains Mono, monospace';
      ctx.fillText(tick, tx, h - 6);
    }
  }

  [dSlider, tauLowSlider, tauHighSlider].forEach(slider => {
    slider.addEventListener('input', update);
  });
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      dSlider.value = 15;
      tauLowSlider.value = 12;
      tauHighSlider.value = 18;
      update();
    });
  }

  update();
}

// ============================================================================
// SIMULATOR 4: 1D DISCRETE BAYES LOCALIZATION FILTER (CHƯƠNG 8)
// ============================================================================
function initBayesSimulator() {
  const canvas = document.getElementById('bayes-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const btnInit = document.getElementById('bayes-btn-init');
  const btnMove = document.getElementById('bayes-btn-move');
  const btnSense = document.getElementById('bayes-btn-sense');
  const stepLabel = document.getElementById('bayes-step-label');

  let belief = [0.25, 0.25, 0.25, 0.25];
  let currentStep = 'Khởi tạo: Tiên nghiệm đều (Uniform Prior)';

  function renderBayes() {
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const cells = [
      { name: 'Ô c_1', isLandmark: false },
      { name: 'Ô c_2 (MỐC)', isLandmark: true },
      { name: 'Ô c_3', isLandmark: false },
      { name: 'Ô c_4 (MỐC)', isLandmark: true }
    ];

    const padL = 60;
    const padR = 40;
    const padT = 30;
    const padB = 60;
    const colW = (w - padL - padR) / 4;
    const barW = colW * 0.6;
    const chartH = h - padT - padB;

    ctx.fillStyle = '#f8fafc';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('Trạng thái niềm tin: ' + currentStep, padL, padT - 10);

    for (let i = 0; i < 4; i++) {
      const cx = padL + i * colW + colW / 2;
      const bx = cx - barW / 2;
      const prob = belief[i];
      const barH = prob * chartH * 1.25;
      const by = padT + chartH - barH;

      ctx.fillStyle = cells[i].isLandmark ? 'rgba(16, 185, 129, 0.12)' : 'rgba(30, 41, 59, 0.5)';
      ctx.strokeStyle = cells[i].isLandmark ? '#10b981' : '#334155';
      ctx.lineWidth = 1.5;
      ctx.fillRect(padL + i * colW + 4, padT, colW - 8, chartH);
      ctx.strokeRect(padL + i * colW + 4, padT, colW - 8, chartH);

      const gradient = ctx.createLinearGradient(0, by, 0, by + barH);
      if (cells[i].isLandmark && prob > 0.3) {
        gradient.addColorStop(0, '#10b981');
        gradient.addColorStop(1, '#047857');
      } else {
        gradient.addColorStop(0, '#3b82f6');
        gradient.addColorStop(1, '#1d4ed8');
      }

      ctx.fillStyle = gradient;
      ctx.fillRect(bx, by, barW, barH);
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 1;
      ctx.strokeRect(bx, by, barW, barH);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 13px JetBrains Mono, monospace';
      ctx.textAlign = 'center';
      ctx.fillText((prob * 100).toFixed(1) + '%', cx, by - 8);

      ctx.fillStyle = cells[i].isLandmark ? '#34d399' : '#94a3b8';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(cells[i].name, cx, h - padB + 20);

      if (cells[i].isLandmark) {
        ctx.fillStyle = '#10b981';
        ctx.font = '10px Inter, sans-serif';
        ctx.fillText('🏛️ Landmark', cx, h - padB + 36);
      }
    }
  }

  if (btnInit) {
    btnInit.addEventListener('click', () => {
      belief = [0.25, 0.25, 0.25, 0.25];
      currentStep = '1. Khởi tạo tiên nghiệm đều Bel(x) = 25%';
      stepLabel.textContent = currentStep;
      renderBayes();
    });
  }

  if (btnMove) {
    btnMove.addEventListener('click', () => {
      const nextBelief = [0, 0, 0, 0];
      for (let i = 0; i < 4; i++) {
        const stayP = 0.2 * belief[i];
        const moveP = 0.8 * belief[i];
        nextBelief[i] += stayP;
        const target = Math.min(3, i + 1);
        nextBelief[target] += moveP;
      }
      belief = nextBelief;
      currentStep = '2. Sau di chuyển +1 ô (Toán tử tích chập phân tán)';
      stepLabel.textContent = currentStep;
      renderBayes();
    });
  }

  if (btnSense) {
    btnSense.addEventListener('click', () => {
      const likelihood = [0.1, 0.8, 0.1, 0.8];
      let sum = 0;
      for (let i = 0; i < 4; i++) {
        belief[i] = belief[i] * likelihood[i];
        sum += belief[i];
      }
      for (let i = 0; i < 4; i++) {
        belief[i] = belief[i] / sum;
      }
      currentStep = '3. Đo đạc thấy mốc (Quy tắc Bayes: Hội tụ vào c_2 và c_4)';
      stepLabel.textContent = currentStep;
      renderBayes();
    });
  }

  renderBayes();
}

// ============================================================================
// SIMULATOR 5: 2-DOF ROBOT ARM FORWARD & INVERSE KINEMATICS (CHƯƠNG 16)
// ============================================================================
function initArmSimulator() {
  const canvas = document.getElementById('arm-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const th1Slider = document.getElementById('arm-th1');
  const th2Slider = document.getElementById('arm-th2');
  const elbowToggle = document.getElementById('arm-elbow-toggle');
  const resetBtn = document.getElementById('arm-reset');

  const th1Val = document.getElementById('arm-th1-val');
  const th2Val = document.getElementById('arm-th2-val');
  const posVal = document.getElementById('arm-pos-val');

  const l1 = 120;
  const l2 = 100;

  let isDragging = false;

  function updateFromSliders() {
    const th1Deg = parseFloat(th1Slider.value);
    const th2Deg = parseFloat(th2Slider.value);

    th1Val.textContent = th1Deg.toFixed(0) + '°';
    th2Val.textContent = th2Deg.toFixed(0) + '°';

    const th1 = (th1Deg * Math.PI) / 180;
    const th2 = (th2Deg * Math.PI) / 180;

    const x = l1 * Math.cos(th1) + l2 * Math.cos(th1 + th2);
    const y = l1 * Math.sin(th1) + l2 * Math.sin(th1 + th2);

    posVal.textContent = `(${x.toFixed(0)}, ${y.toFixed(0)}) px`;
    drawArm(th1, th2, x, y);
  }

  function solveIK(targetX, targetY, elbowDown = true) {
    const r2 = targetX * targetX + targetY * targetY;
    const cosTh2 = (r2 - l1 * l1 - l2 * l2) / (2 * l1 * l2);

    if (cosTh2 < -1 || cosTh2 > 1) {
      posVal.textContent = 'NGOÀI TẦM VỚI!';
      return null;
    }

    const sinTh2 = (elbowDown ? 1 : -1) * Math.sqrt(1 - cosTh2 * cosTh2);
    const th2 = Math.atan2(sinTh2, cosTh2);

    const k1 = l1 + l2 * cosTh2;
    const k2 = l2 * sinTh2;
    const th1 = Math.atan2(targetY, targetX) - Math.atan2(k2, k1);

    return { th1, th2 };
  }

  function drawArm(th1, th2, eeX, eeY) {
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const baseX = w / 2;
    const baseY = h / 2 + 50;

    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.arc(baseX, baseY, l1 + l2, 0, Math.PI * 2);
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(baseX, baseY, Math.abs(l1 - l2), 0, Math.PI * 2);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = '#475569';
    ctx.fillRect(baseX - 25, baseY, 50, 15);
    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.arc(baseX, baseY, 10, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#94a3b8';
    ctx.stroke();

    const j2X = baseX + l1 * Math.cos(-th1);
    const j2Y = baseY + l1 * Math.sin(-th1);

    const eeCanvasX = baseX + eeX;
    const eeCanvasY = baseY - eeY;

    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 8;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(baseX, baseY);
    ctx.lineTo(j2X, j2Y);
    ctx.stroke();

    ctx.strokeStyle = '#8b5cf6';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.moveTo(j2X, j2Y);
    ctx.lineTo(eeCanvasX, eeCanvasY);
    ctx.stroke();

    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.arc(j2X, j2Y, 7, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(eeCanvasX, eeCanvasY, 9, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Nhấp & kéo chuột trên Canvas để điều khiển Inverse Kinematics (IK)!', 15, 20);
  }

  canvas.addEventListener('mousedown', (e) => { isDragging = true; handleDrag(e); });
  window.addEventListener('mouseup', () => { isDragging = false; });
  canvas.addEventListener('mousemove', (e) => { if (isDragging) handleDrag(e); });

  function handleDrag(e) {
    const rect = canvas.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    const baseX = canvas.width / 2;
    const baseY = canvas.height / 2 + 50;

    const targetX = mouseX - baseX;
    const targetY = baseY - mouseY;

    const elbowDown = elbowToggle ? elbowToggle.checked : true;
    const sol = solveIK(targetX, targetY, elbowDown);

    if (sol) {
      th1Slider.value = (sol.th1 * 180 / Math.PI).toFixed(0);
      th2Slider.value = (sol.th2 * 180 / Math.PI).toFixed(0);
      th1Val.textContent = th1Slider.value + '°';
      th2Val.textContent = th2Slider.value + '°';
      posVal.textContent = `(${targetX.toFixed(0)}, ${targetY.toFixed(0)}) px`;
      drawArm(sol.th1, sol.th2, targetX, targetY);
    }
  }

  [th1Slider, th2Slider].forEach(s => s.addEventListener('input', updateFromSliders));
  if (elbowToggle) elbowToggle.addEventListener('change', updateFromSliders);
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      th1Slider.value = 45;
      th2Slider.value = 45;
      if (elbowToggle) elbowToggle.checked = true;
      updateFromSliders();
    });
  }

  updateFromSliders();
}

// ============================================================================
// SIMULATOR 6: INTERACTIVE A* SEARCH PATHFINDING GRID VISUALIZER (CHƯƠNG 10)
// ============================================================================
function initAStarSimulator() {
  const canvas = document.getElementById('astar-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const heuristicSlider = document.getElementById('astar-weight');
  const heuristicVal = document.getElementById('astar-weight-val');
  const runBtn = document.getElementById('astar-btn-run');
  const clearBtn = document.getElementById('astar-btn-clear');
  const statusLabel = document.getElementById('astar-status');

  const rows = 12;
  const cols = 20;
  const cellSize = 30;

  // Grid states: 0 = free, 1 = obstacle, 2 = start, 3 = goal, 4 = open, 5 = closed, 6 = path
  let grid = Array(rows).fill(0).map(() => Array(cols).fill(0));
  let start = { r: 1, c: 1 };
  let goal = { r: 10, c: 18 };

  // Set default obstacles
  function setDefaultObstacles() {
    grid = Array(rows).fill(0).map(() => Array(cols).fill(0));
    for (let r = 2; r <= 9; r++) grid[r][6] = 1;
    for (let r = 3; r <= 10; r++) grid[r][13] = 1;
    grid[start.r][start.c] = 2;
    grid[goal.r][goal.c] = 3;
  }
  setDefaultObstacles();

  function drawGrid() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const x = c * cellSize + 20;
        const y = r * cellSize + 20;
        const val = grid[r][c];

        if (r === start.r && c === start.c) {
          ctx.fillStyle = '#10b981'; // Start green
        } else if (r === goal.r && c === goal.c) {
          ctx.fillStyle = '#ef4444'; // Goal red
        } else if (val === 1) {
          ctx.fillStyle = '#475569'; // Obstacle
        } else if (val === 6) {
          ctx.fillStyle = '#f59e0b'; // Path yellow
        } else if (val === 5) {
          ctx.fillStyle = 'rgba(59, 130, 246, 0.25)'; // Closed blue-dim
        } else if (val === 4) {
          ctx.fillStyle = 'rgba(168, 85, 247, 0.4)'; // Open purple
        } else {
          ctx.fillStyle = '#1e293b'; // Free
        }

        ctx.fillRect(x, y, cellSize - 2, cellSize - 2);

        if (r === start.r && c === start.c) {
          ctx.fillStyle = '#fff';
          ctx.font = 'bold 11px Inter';
          ctx.textAlign = 'center';
          ctx.fillText('S', x + cellSize/2 - 1, y + cellSize/2 + 4);
        } else if (r === goal.r && c === goal.c) {
          ctx.fillStyle = '#fff';
          ctx.font = 'bold 11px Inter';
          ctx.textAlign = 'center';
          ctx.fillText('G', x + cellSize/2 - 1, y + cellSize/2 + 4);
        }
      }
    }
  }

  function runAStar() {
    const eps = parseFloat(heuristicSlider.value);
    heuristicVal.textContent = eps.toFixed(1) + (eps === 0 ? ' (Dijkstra)' : eps === 1.0 ? ' (A* Chuẩn)' : ' (Greedy)');

    // Reset path / open / closed
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        if (grid[r][c] > 3) grid[r][c] = 0;
      }
    }

    function h(r, c) {
      // Manhattan distance
      return eps * (Math.abs(r - goal.r) + Math.abs(c - goal.c));
    }

    const openSet = [{ r: start.r, c: start.c, g: 0, f: h(start.r, start.c), parent: null }];
    const closed = Array(rows).fill(false).map(() => Array(cols).fill(false));
    const gScore = Array(rows).fill(Infinity).map(() => Array(cols).fill(Infinity));
    gScore[start.r][start.c] = 0;

    let found = false;
    let endNode = null;

    let stepCount = 0;
    while (openSet.length > 0) {
      stepCount++;
      // Sort to get lowest f
      openSet.sort((a, b) => a.f - b.f);
      const current = openSet.shift();

      if (current.r === goal.r && current.c === goal.c) {
        found = true;
        endNode = current;
        break;
      }

      closed[current.r][current.c] = true;
      if (!(current.r === start.r && current.c === start.c)) {
        grid[current.r][current.c] = 5; // closed
      }

      // 4 Neighbors
      const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
      for (const [dr, dc] of dirs) {
        const nr = current.r + dr;
        const nc = current.c + dc;

        if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
        if (grid[nr][nc] === 1 || closed[nr][nc]) continue;

        const tentativeG = current.g + 1;
        if (tentativeG < gScore[nr][nc]) {
          gScore[nr][nc] = tentativeG;
          const fScore = tentativeG + h(nr, nc);
          openSet.push({ r: nr, c: nc, g: tentativeG, f: fScore, parent: current });
          if (!(nr === goal.r && nc === goal.c)) {
            grid[nr][nc] = 4; // open
          }
        }
      }
    }

    if (found && endNode) {
      let curr = endNode.parent;
      let pathLen = 0;
      while (curr && !(curr.r === start.r && curr.c === start.c)) {
        grid[curr.r][curr.c] = 6; // path
        curr = curr.parent;
        pathLen++;
      }
      statusLabel.textContent = `✓ Tìm thấy đường đi! Độ dài: ${pathLen + 1} bước (${stepCount} nút mở)`;
      statusLabel.style.color = '#10b981';
    } else {
      statusLabel.textContent = '✗ Bị chặn! Không tìm thấy đường đi.';
      statusLabel.style.color = '#ef4444';
    }

    drawGrid();
  }

  // Click canvas to toggle obstacle
  canvas.addEventListener('click', (e) => {
    const rect = canvas.getBoundingClientRect();
    const mx = e.clientX - rect.left - 20;
    const my = e.clientY - rect.top - 20;
    const c = Math.floor(mx / cellSize);
    const r = Math.floor(my / cellSize);

    if (r >= 0 && r < rows && c >= 0 && c < cols) {
      if (!(r === start.r && c === start.c) && !(r === goal.r && c === goal.c)) {
        grid[r][c] = grid[r][c] === 1 ? 0 : 1;
        drawGrid();
      }
    }
  });

  if (heuristicSlider) {
    heuristicSlider.addEventListener('input', () => {
      const eps = parseFloat(heuristicSlider.value);
      heuristicVal.textContent = eps.toFixed(1) + (eps === 0 ? ' (Dijkstra)' : eps === 1.0 ? ' (A* Chuẩn)' : ' (Greedy)');
    });
  }

  if (runBtn) runBtn.addEventListener('click', runAStar);
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      setDefaultObstacles();
      statusLabel.textContent = 'Sẵn sàng. Nhấp trên ô để vẽ/xóa vật cản!';
      statusLabel.style.color = 'var(--text-muted)';
      drawGrid();
    });
  }

  drawGrid();
}

// ============================================================================
// SIMULATOR 7: INTERACTIVE BRAITENBERG VEHICLE 2D LIGHT-TRACKER (CHƯƠNG 3)
// ============================================================================
function initBraitenbergSimulator() {
  const canvas = document.getElementById('braitenberg-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const typeSelect = document.getElementById('bv-type');
  const resetBtn = document.getElementById('bv-reset');
  const behaviorDesc = document.getElementById('bv-desc');

  let botX = 150;
  let botY = 220;
  let botAngle = 0;
  let lightX = 480;
  let lightY = 160;

  const wheelBase = 32;
  const sensorDist = 24;

  const descriptions = {
    '2a': 'Xe 2a (FEAR - Sợ hãi): Dây thẳng kích thích (+). Cảm biến gần nguồn sáng kích thích bánh cùng bên quay mạnh hơn → Xe ngoảnh mặt rẽ xa khỏi nguồn sáng!',
    '2b': 'Xe 2b (AGGRESSION - Hung hăng): Dây chéo kích thích (+). Cảm biến gần ánh sáng truyền tín hiệu sang bánh đối diện → Xe đổi hướng lao thẳng vào nguồn sáng!',
    '3a': 'Xe 3a (LOVE - Gắn kết): Dây thẳng ức chế (-). Càng gần ánh sáng bánh xe càng giảm tốc → Xe tiến lại gần nguồn sáng rồi dừng lại êm ái ngắm nhìn!',
    '3b': 'Xe 3b (EXPLORER - Khám phá): Dây chéo ức chế (-). Cảm biến gần ức chế bánh đối diện → Xe lượn một đường vòng qua nguồn sáng rồi tiếp tục thám hiểm!'
  };

  function updateDesc() {
    const vType = typeSelect ? typeSelect.value : '2a';
    if (behaviorDesc) behaviorDesc.textContent = descriptions[vType];
  }

  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    lightX = e.clientX - rect.left;
    lightY = e.clientY - rect.top;
  });

  function stepSim() {
    const vType = typeSelect ? typeSelect.value : '2a';

    // Sensor positions (Left and Right)
    const slX = botX + sensorDist * Math.cos(botAngle - 0.4);
    const slY = botY + sensorDist * Math.sin(botAngle - 0.4);
    const srX = botX + sensorDist * Math.cos(botAngle + 0.4);
    const srY = botY + sensorDist * Math.sin(botAngle + 0.4);

    // Light distance
    const dl = Math.hypot(lightX - slX, lightY - slY);
    const dr = Math.hypot(lightX - srX, lightY - srY);

    // Light intensity: inverse square law
    const il = Math.min(10.0, 8000 / (dl * dl + 400));
    const ir = Math.min(10.0, 8000 / (dr * dr + 400));

    let vl = 1.0;
    let vr = 1.0;

    if (vType === '2a') {
      // Fear: straight excitatory
      vl = 0.8 + il * 1.5;
      vr = 0.8 + ir * 1.5;
    } else if (vType === '2b') {
      // Aggression: crossed excitatory
      vl = 0.8 + ir * 1.5;
      vr = 0.8 + il * 1.5;
    } else if (vType === '3a') {
      // Love: straight inhibitory
      vl = Math.max(0.0, 3.5 - il * 1.5);
      vr = Math.max(0.0, 3.5 - ir * 1.5);
    } else if (vType === '3b') {
      // Explorer: crossed inhibitory
      vl = Math.max(0.2, 3.5 - ir * 1.4);
      vr = Math.max(0.2, 3.5 - il * 1.4);
    }

    const dt = 0.25;
    const v = (vr + vl) / 2;
    const omega = (vr - vl) / wheelBase;

    botAngle += omega * dt;
    botX += v * Math.cos(botAngle) * dt;
    botY += v * Math.sin(botAngle) * dt;

    // Wrap canvas boundaries
    if (botX < 10) botX = canvas.width - 20;
    if (botX > canvas.width - 10) botX = 20;
    if (botY < 10) botY = canvas.height - 20;
    if (botY > canvas.height - 10) botY = 20;
  }

  function render() {
    stepSim();

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw Light Source (glow circle)
    const glow = ctx.createRadialGradient(lightX, lightY, 5, lightX, lightY, 90);
    glow.addColorStop(0, 'rgba(251, 191, 36, 0.9)');
    glow.addColorStop(0.3, 'rgba(245, 158, 11, 0.3)');
    glow.addColorStop(1, 'rgba(245, 158, 11, 0)');
    ctx.fillStyle = glow;
    ctx.beginPath();
    ctx.arc(lightX, lightY, 90, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = '#fbbf24';
    ctx.beginPath();
    ctx.arc(lightX, lightY, 12, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#0f172a';
    ctx.font = '10px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('💡', lightX, lightY + 3);

    // Draw Robot Body
    ctx.save();
    ctx.translate(botX, botY);
    ctx.rotate(botAngle);

    // Chassis
    ctx.fillStyle = '#1e3a8a';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(-15, -12, 30, 24, 6);
    ctx.fill();
    ctx.stroke();

    // Wheels
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(-8, -16, 16, 4);
    ctx.fillRect(-8, 12, 16, 4);

    // Sensors
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(15, -8, 4, 0, Math.PI * 2);
    ctx.arc(15, 8, 4, 0, Math.PI * 2);
    ctx.fill();

    ctx.restore();

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('Rê chuột trên khung Canvas để dịch chuyển nguồn sáng!', 15, 20);

    requestAnimationFrame(render);
  }

  if (typeSelect) typeSelect.addEventListener('change', updateDesc);
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      botX = 150;
      botY = 220;
      botAngle = 0;
      lightX = 480;
      lightY = 160;
    });
  }

  updateDesc();
  requestAnimationFrame(render);
}

// ============================================================================
// SIMULATOR 8: ULTRASOUND ToF SENSOR WAVE SIMULATOR (CHƯƠNG 2)
// ============================================================================
function initToFSimulator() {
  const canvas = document.getElementById('tof-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const distSlider = document.getElementById('tof-dist');
  const tempSlider = document.getElementById('tof-temp');
  const distVal = document.getElementById('tof-dist-val');
  const tempVal = document.getElementById('tof-temp-val');

  const metricSpeed = document.getElementById('tof-metric-speed');
  const metricTime = document.getElementById('tof-metric-time');

  let wavePhase = 0;

  function update() {
    const d = parseFloat(distSlider.value); // meters (0.2 to 4.0)
    const T = parseFloat(tempSlider.value); // Celsius (-10 to 45)

    distVal.textContent = d.toFixed(2) + ' m';
    tempVal.textContent = T.toFixed(0) + ' °C';

    // Speed of sound in air: v = 331.3 + 0.606 * T
    const v = 331.3 + 0.606 * T;
    const tofTime = (2 * d / v) * 1000; // ms

    metricSpeed.textContent = v.toFixed(1) + ' m/s';
    metricTime.textContent = tofTime.toFixed(2) + ' ms';
  }

  function render() {
    const d = parseFloat(distSlider.value);
    const T = parseFloat(tempSlider.value);
    const v = 331.3 + 0.606 * T;

    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, w, h);

    const padL = 70;
    const padR = 50;
    const maxD = 4.0;
    const scale = (w - padL - padR) / maxD;

    const sensorX = padL;
    const sensorY = h / 2;
    const obsX = padL + d * scale;

    // Draw Ultrasound Sensor (HC-SR04 body)
    ctx.fillStyle = '#1e3a8a';
    ctx.fillRect(sensorX - 45, sensorY - 35, 45, 70);
    ctx.strokeStyle = '#60a5fa';
    ctx.strokeRect(sensorX - 45, sensorY - 35, 45, 70);

    // Emitter & Receiver Transducers
    ctx.fillStyle = '#cbd5e1';
    ctx.beginPath();
    ctx.arc(sensorX - 10, sensorY - 18, 12, 0, Math.PI * 2);
    ctx.arc(sensorX - 10, sensorY + 18, 12, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#475569';
    ctx.stroke();

    ctx.fillStyle = '#f8fafc';
    ctx.font = '9px JetBrains Mono';
    ctx.textAlign = 'center';
    ctx.fillText('TX', sensorX - 10, sensorY - 15);
    ctx.fillText('RX', sensorX - 10, sensorY + 21);

    // Draw Moving Sound Waves (Arcs)
    wavePhase = (wavePhase + 3) % (d * scale);

    // Outgoing wave pulse (blue)
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    for (let r = wavePhase; r < d * scale; r += 35) {
      if (r > 0 && r < d * scale) {
        ctx.beginPath();
        ctx.arc(sensorX, sensorY - 18, r, -0.4, 0.4);
        ctx.stroke();
      }
    }

    // Reflected wave pulse (orange)
    ctx.strokeStyle = '#f59e0b';
    ctx.setLineDash([3, 3]);
    for (let r = (d * scale - wavePhase); r > 0; r -= 35) {
      ctx.beginPath();
      ctx.arc(obsX, sensorY, r, Math.PI - 0.4, Math.PI + 0.4);
      ctx.stroke();
    }
    ctx.setLineDash([]);

    // Draw Obstacle
    ctx.fillStyle = '#475569';
    ctx.fillRect(obsX, sensorY - 55, 20, 110);
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 2;
    ctx.strokeRect(obsX, sensorY - 55, 20, 110);

    ctx.fillStyle = '#f8fafc';
    ctx.font = 'bold 11px Inter';
    ctx.textAlign = 'left';
    ctx.fillText('VẬT CẢN', obsX + 26, sensorY + 4);

    // Measurement Dimension Line
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(sensorX, h - 35);
    ctx.lineTo(obsX, h - 35);
    ctx.stroke();

    ctx.fillStyle = '#10b981';
    ctx.font = 'bold 12px JetBrains Mono';
    ctx.textAlign = 'center';
    ctx.fillText(`d = ${d.toFixed(2)} m (ToF = ${((2 * d / v) * 1000).toFixed(2)} ms)`, (sensorX + obsX) / 2, h - 15);

    requestAnimationFrame(render);
  }

  [distSlider, tempSlider].forEach(s => s.addEventListener('input', update));
  update();
  requestAnimationFrame(render);
}
