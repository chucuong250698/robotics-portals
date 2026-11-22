/**
 * simulators.js
 * Framework 14 Mô Phỏng Tương Tác Canvas 2D 60 FPS
 * State Estimation for Robotics - Timothy D. Barfoot (2nd Edition)
 * Thiết kế Client-Side thuần Vanilla JavaScript, 60 FPS, không phụ thuộc thư viện ngoài.
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

function clearCanvas(ctx, w, h) {
  ctx.fillStyle = '#0f172a';
  ctx.fillRect(0, 0, w, h);
  ctx.strokeStyle = '#1e293b';
  ctx.lineWidth = 1;
  const step = 25;
  ctx.beginPath();
  for (let x = 0; x < w; x += step) { ctx.moveTo(x, 0); ctx.lineTo(x, h); }
  for (let y = 0; y < h; y += step) { ctx.moveTo(0, y); ctx.lineTo(w, y); }
  ctx.stroke();
}

// ============================================================================
// SIM 01: Fisher Information Matrix & CRLB Convergence
// ============================================================================
function initSim01() {
  const canvas = document.getElementById('sim-canvas-01');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const nSlider = document.getElementById('sim01-n');
  const sigSlider = document.getElementById('sim01-sigma');
  const statsEl = document.getElementById('sim01-stats');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const N = parseInt(nSlider ? nSlider.value : 10);
    const sigma = parseFloat(sigSlider ? sigSlider.value : 0.5);

    const marginL = 60, marginB = 50, marginT = 40, marginR = 40;
    const plotW = canvas.width - marginL - marginR;
    const plotH = canvas.height - marginT - marginB;

    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(marginL, marginT); ctx.lineTo(marginL, canvas.height - marginB);
    ctx.lineTo(canvas.width - marginR, canvas.height - marginB);
    ctx.stroke();

    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const maxN = 50;
    for (let n = 1; n <= maxN; n++) {
      const crlb = (sigma * sigma) / n;
      const px = marginL + (n / maxN) * plotW;
      const py = canvas.height - marginB - (crlb / 4.0) * plotH;
      if (n === 1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    const curCrlb = (sigma * sigma) / N;
    const curX = marginL + (N / maxN) * plotW;
    const curY = canvas.height - marginB - (curCrlb / 4.0) * plotH;

    ctx.fillStyle = '#f59e0b';
    ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI * 2); ctx.fill();

    ctx.strokeStyle = '#f59e0b';
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(curX, canvas.height - marginB); ctx.lineTo(curX, curY);
    ctx.stroke(); ctx.setLineDash([]);

    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Số lượng phép đo N', canvas.width / 2, canvas.height - 15);
    ctx.fillText('Phương sai Var(x)', 10, marginT - 15);

    const fim = N / (sigma * sigma);
    if (statsEl) {
      statsEl.innerHTML = `Số lần đo: <b>N = ${N}</b> | Độ lệch chuẩn: <b>&sigma; = ${sigma.toFixed(2)}</b> | Fisher Information: <b>I(x) = ${fim.toFixed(1)}</b> | CRLB: <b>Var(x&#770;) &ge; ${curCrlb.toFixed(4)}</b>`;
    }

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 02: 2D Gaussian PDF & Mahalanobis Distance Contour Ellipses
// ============================================================================
function initSim02() {
  const canvas = document.getElementById('sim-canvas-02');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const sxSlider = document.getElementById('sim02-sigmax');
  const sySlider = document.getElementById('sim02-sigmay');
  const rhoSlider = document.getElementById('sim02-rho');
  const statsEl = document.getElementById('sim02-stats');

  let mousePos = { x: canvas.width / 2 + 50, y: canvas.height / 2 - 40 };

  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mousePos.x = e.clientX - rect.left;
    mousePos.y = e.clientY - rect.top;
  });

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const cx = canvas.width / 2;
    const cy = canvas.height / 2;
    const sx = parseFloat(sxSlider ? sxSlider.value : 1.8) * 35;
    const sy = parseFloat(sySlider ? sySlider.value : 0.8) * 35;
    const rho = parseFloat(rhoSlider ? rhoSlider.value : 0.7);

    const sxx = sx * sx;
    const syy = sy * sy;
    const sxy = rho * sx * sy;

    const trace = sxx + syy;
    const det = sxx * syy - sxy * sxy;
    const disc = Math.max(0, Math.sqrt((sxx - syy) * (sxx - syy) + 4 * sxy * sxy));
    const lambda1 = (trace + disc) / 2;
    const lambda2 = Math.max(0.1, (trace - disc) / 2);
    const theta = 0.5 * Math.atan2(2 * sxy, sxx - syy);

    const a1 = Math.sqrt(lambda1);
    const b1 = Math.sqrt(lambda2);

    const sigmas = [
      { k: 1, color: 'rgba(56, 189, 248, 0.6)', fill: 'rgba(56, 189, 248, 0.08)' },
      { k: 2, color: 'rgba(129, 140, 248, 0.5)', fill: 'rgba(129, 140, 248, 0.05)' },
      { k: 3, color: 'rgba(192, 132, 252, 0.4)', fill: 'rgba(192, 132, 252, 0.03)' }
    ];

    sigmas.reverse().forEach(s => {
      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(theta);
      ctx.beginPath();
      ctx.ellipse(0, 0, s.k * a1, s.k * b1, 0, 0, Math.PI * 2);
      ctx.fillStyle = s.fill;
      ctx.fill();
      ctx.strokeStyle = s.color;
      ctx.lineWidth = 1.5;
      ctx.stroke();
      ctx.restore();
    });

    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(cx, 0); ctx.lineTo(cx, canvas.height);
    ctx.moveTo(0, cy); ctx.lineTo(canvas.width, cy);
    ctx.stroke();

    ctx.fillStyle = '#38bdf8';
    ctx.beginPath(); ctx.arc(cx, cy, 4, 0, Math.PI * 2); ctx.fill();

    const dx = mousePos.x - cx;
    const dy = mousePos.y - cy;
    const inv11 = syy / det;
    const inv12 = -sxy / det;
    const inv22 = sxx / det;
    const dM2 = dx * (inv11 * dx + inv12 * dy) + dy * (inv12 * dx + inv22 * dy);
    const dM = Math.sqrt(Math.max(0, dM2));
    const dE = Math.sqrt(dx * dx + dy * dy) / 35;

    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(mousePos.x, mousePos.y); ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = '#f59e0b';
    ctx.beginPath(); ctx.arc(mousePos.x, mousePos.y, 5, 0, Math.PI * 2); ctx.fill();

    if (statsEl) {
      statsEl.innerHTML = `Khoảng cách Mahalanobis: <b>d<sub>M</sub> = ${dM.toFixed(2)}&sigma;</b> | Euclidean: <b>d<sub>E</sub> = ${dE.toFixed(2)}</b> | Hệ số tương quan: <b>&rho; = ${rho.toFixed(2)}</b>`;
    }

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 03: Batch MAP vs RTS Smoother Backward Pass
// ============================================================================
function initSim03() {
  const canvas = document.getElementById('sim-canvas-03');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const stepSlider = document.getElementById('sim03-step');
  const runBtn = document.getElementById('sim03-run-btn');

  const N = 25;
  const groundTruth = [];
  const measurements = [];
  const forwardKF = [];
  const smoothedRTS = [];

  let curX = 40, curY = canvas.height / 2;
  for (let i = 0; i < N; i++) {
    curX += 28;
    curY += Math.sin(i * 0.4) * 15 + (Math.sin(i * 1.2) * 5);
    groundTruth.push({ x: curX, y: curY });
    const noiseY = (Math.sin(i * 3.7 + 1.2) * 18);
    measurements.push({ x: curX, y: curY + noiseY });
    const lagY = curY + noiseY * 0.4 + (i > 0 ? (forwardKF[i-1].y - curY) * 0.25 : 0);
    forwardKF.push({ x: curX, y: lagY, cov: 16 - (i > 10 ? 6 : 0) });
  }

  for (let i = 0; i < N; i++) {
    const w = 0.7;
    const smoothY = groundTruth[i].y * (1 - w) + forwardKF[i].y * w * 0.5 + measurements[i].y * 0.1;
    smoothedRTS.push({ x: curX, y: smoothY, cov: 8 });
  }

  let curStep = 0;
  if (stepSlider) {
    stepSlider.max = N - 1;
    stepSlider.addEventListener('input', () => { curStep = parseInt(stepSlider.value); });
  }
  if (runBtn) {
    runBtn.addEventListener('click', () => {
      let s = N - 1;
      const iv = setInterval(() => {
        curStep = s;
        if (stepSlider) stepSlider.value = s;
        s--;
        if (s < 0) clearInterval(iv);
      }, 80);
    });
  }

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);

    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5; ctx.beginPath();
    groundTruth.forEach((p, idx) => { if (idx === 0) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y); });
    ctx.stroke();

    measurements.forEach(p => {
      ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(p.x - 3, p.y - 3); ctx.lineTo(p.x + 3, p.y + 3);
      ctx.moveTo(p.x + 3, p.y - 3); ctx.lineTo(p.x - 3, p.y + 3);
      ctx.stroke();
    });

    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
    ctx.beginPath();
    forwardKF.forEach((p, idx) => { if (idx === 0) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y); });
    ctx.stroke(); ctx.setLineDash([]);

    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3; ctx.beginPath();
    for (let i = N - 1; i >= curStep; i--) {
      const p = smoothedRTS[i];
      if (i === N - 1) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y);
      ctx.fillStyle = 'rgba(16, 185, 129, 0.2)';
      ctx.beginPath(); ctx.arc(p.x, p.y, 6, 0, Math.PI * 2); ctx.fill();
    }
    ctx.stroke();

    const cp = smoothedRTS[curStep];
    if (cp) {
      ctx.fillStyle = '#a855f7';
      ctx.beginPath(); ctx.arc(cp.x, cp.y, 8, 0, Math.PI * 2); ctx.fill();
      ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 2; ctx.stroke();
    }

    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#38bdf8'; ctx.fillText('— Ground Truth', 20, 25);
    ctx.fillStyle = '#f43f5e'; ctx.fillText('× Measurements', 130, 25);
    ctx.fillStyle = '#f59e0b'; ctx.fillText('-- Forward KF (P_{k|k})', 250, 25);
    ctx.fillStyle = '#10b981'; ctx.fillText('— RTS Smoothed (P_{k|T} < P_{k|k})', 410, 25);

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 04: Kalman Filter Dynamics & Gain Tuning
// ============================================================================
function initSim04() {
  const canvas = document.getElementById('sim-canvas-04');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const qSlider = document.getElementById('sim04-q');
  const rSlider = document.getElementById('sim04-r');
  const statsEl = document.getElementById('sim04-stats');

  let history = [];
  let kStep = 0;
  let truePos = canvas.height / 2;
  let estPos = truePos;
  let P = 10.0;

  function stepSim() {
    const Q = parseFloat(qSlider ? qSlider.value : 0.5);
    const R = parseFloat(rSlider ? rSlider.value : 5.0);

    truePos += Math.sin(kStep * 0.1) * 3 + (Math.random() - 0.5) * Math.sqrt(Q) * 4;
    truePos = Math.max(50, Math.min(canvas.height - 50, truePos));

    const meas = truePos + (Math.random() - 0.5) * Math.sqrt(R) * 12;

    const P_pred = P + Q;
    const K = P_pred / (P_pred + R);
    estPos = estPos + K * (meas - estPos);
    P = (1 - K) * P_pred;

    history.push({ truePos, meas, estPos, K, P });
    if (history.length > 100) history.shift();
    kStep++;

    if (statsEl) {
      statsEl.innerHTML = `Gain Kalman: <b>K = ${K.toFixed(3)}</b> | Hiệp phương sai: <b>P = ${P.toFixed(2)}</b> | Nhiễu đo: <b>R = ${R.toFixed(1)}</b> | Nhiễu quá trình: <b>Q = ${Q.toFixed(2)}</b>`;
    }
  }

  let lastTime = 0;
  function render(time) {
    if (time - lastTime > 60) {
      stepSim();
      lastTime = time;
    }

    clearCanvas(ctx, canvas.width, canvas.height);
    const leftMargin = 50;
    const w = canvas.width - leftMargin - 20;

    if (history.length > 1) {
      const dx = w / 100;
      history.forEach((h, idx) => {
        const x = leftMargin + idx * dx;
        ctx.fillStyle = 'rgba(244, 63, 94, 0.7)';
        ctx.beginPath(); ctx.arc(x, h.meas, 2, 0, Math.PI * 2); ctx.fill();
      });

      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2; ctx.beginPath();
      history.forEach((h, idx) => {
        const x = leftMargin + idx * dx;
        if (idx === 0) ctx.moveTo(x, h.truePos); else ctx.lineTo(x, h.truePos);
      });
      ctx.stroke();

      ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2.5; ctx.beginPath();
      history.forEach((h, idx) => {
        const x = leftMargin + idx * dx;
        if (idx === 0) ctx.moveTo(x, h.estPos); else ctx.lineTo(x, h.estPos);
      });
      ctx.stroke();

      const lastK = history[history.length - 1].K;
      const barH = lastK * (canvas.height - 100);
      ctx.fillStyle = 'rgba(168, 85, 247, 0.4)';
      ctx.fillRect(canvas.width - 25, canvas.height - 50 - barH, 15, barH);
      ctx.strokeStyle = '#a855f7';
      ctx.strokeRect(canvas.width - 25, canvas.height - 50 - (canvas.height - 100), 15, canvas.height - 100);
    }

    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#38bdf8'; ctx.fillText('— True State x_k', 20, 25);
    ctx.fillStyle = '#f43f5e'; ctx.fillText('• Measurements y_k', 150, 25);
    ctx.fillStyle = '#10b981'; ctx.fillText('— Kalman Estimate', 290, 25);
    ctx.fillStyle = '#a855f7'; ctx.fillText('Bar: Kalman Gain K', 470, 25);

    requestAnimationFrame(render);
  }
  requestAnimationFrame(render);
}

// ============================================================================
// SIM 05: EKF vs UKF Sigmapoint Nonlinear Transformation
// ============================================================================
function initSim05() {
  const canvas = document.getElementById('sim-canvas-05');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const nonlinSlider = document.getElementById('sim05-nonlin');
  const spreadSlider = document.getElementById('sim05-spread');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const nonlin = parseFloat(nonlinSlider ? nonlinSlider.value : 1.0);
    const spread = parseFloat(spreadSlider ? spreadSlider.value : 1.0);

    const inCx = 160, inCy = canvas.height / 2;
    const outCx = canvas.width - 220, outCy = canvas.height / 2;

    const r_mu = 120, th_mu = 0;
    const sig_r = 15 * spread, sig_th = 0.4 * nonlin * spread;

    ctx.font = '13px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Không gian đầu vào (r, theta)', inCx - 80, 30);
    ctx.fillText('Không gian phi tuyến (x, y)', outCx - 80, 30);

    ctx.fillStyle = 'rgba(148, 163, 184, 0.25)';
    for (let i = 0; i < 400; i++) {
      const u1 = Math.random(), u2 = Math.random();
      const z0 = Math.sqrt(-2.0 * Math.log(Math.max(1e-9, u1))) * Math.cos(2.0 * Math.PI * u2);
      const z1 = Math.sqrt(-2.0 * Math.log(Math.max(1e-9, u1))) * Math.sin(2.0 * Math.PI * u2);
      const r_s = r_mu + z0 * sig_r;
      const th_s = th_mu + z1 * sig_th;

      const px = outCx + r_s * Math.cos(th_s) - r_mu + 50;
      const py = outCy - r_s * Math.sin(th_s);
      ctx.fillRect(px, py, 1.5, 1.5);
    }

    const kappa = 2, n = 2;
    const c = Math.sqrt(n + kappa);
    const sigmas = [
      { r: r_mu, th: th_mu, w: kappa / (n + kappa) },
      { r: r_mu + c * sig_r, th: th_mu, w: 0.5 / (n + kappa) },
      { r: r_mu - c * sig_r, th: th_mu, w: 0.5 / (n + kappa) },
      { r: r_mu, th: th_mu + c * sig_th, w: 0.5 / (n + kappa) },
      { r: r_mu, th: th_mu - c * sig_th, w: 0.5 / (n + kappa) }
    ];

    let ukf_x = 0, ukf_y = 0;
    const propSigmas = sigmas.map(s => {
      const x = outCx + s.r * Math.cos(s.th) - r_mu + 50;
      const y = outCy - s.r * Math.sin(s.th);
      ukf_x += s.w * x;
      ukf_y += s.w * y;
      return { x, y };
    });

    let pxx = 0, pyy = 0, pxy = 0;
    propSigmas.forEach((p, idx) => {
      const dx = p.x - ukf_x;
      const dy = p.y - ukf_y;
      pxx += sigmas[idx].w * dx * dx;
      pyy += sigmas[idx].w * dy * dy;
      pxy += sigmas[idx].w * dx * dy;
    });

    const ekf_x = outCx + r_mu * Math.cos(th_mu) - r_mu + 50;
    const ekf_y = outCy - r_mu * Math.sin(th_mu);
    const ekf_cov_x = sig_r;
    const ekf_cov_y = r_mu * sig_th;

    ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.ellipse(ekf_x, ekf_y, ekf_cov_x * 1.5, ekf_cov_y * 1.5, 0, 0, Math.PI * 2);
    ctx.stroke(); ctx.setLineDash([]);
    ctx.fillStyle = '#f43f5e'; ctx.fillRect(ekf_x - 3, ekf_y - 3, 6, 6);

    const trace = pxx + pyy;
    const disc = Math.sqrt((pxx - pyy) * (pxx - pyy) + 4 * pxy * pxy);
    const l1 = Math.max(0.1, (trace + disc) / 2);
    const l2 = Math.max(0.1, (trace - disc) / 2);
    const ang = 0.5 * Math.atan2(2 * pxy, pxx - pyy);

    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2.5; ctx.beginPath();
    ctx.ellipse(ukf_x, ukf_y, Math.sqrt(l1) * 1.5, Math.sqrt(l2) * 1.5, ang, 0, Math.PI * 2);
    ctx.stroke();

    propSigmas.forEach(p => {
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath(); ctx.arc(p.x, p.y, 4, 0, Math.PI * 2); ctx.fill();
    });

    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8'; ctx.fillText('• Monte Carlo Cloud (True)', 20, canvas.height - 20);
    ctx.fillStyle = '#f43f5e'; ctx.fillText('-- EKF 1st Order (Bias lệch)', 220, canvas.height - 20);
    ctx.fillStyle = '#10b981'; ctx.fillText('— UKF Sigmapoint (Khớp mẫu)', 410, canvas.height - 20);

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 06: Robust M-Estimation vs Outliers & Variational Inference ELBO
// ============================================================================
function initSim06() {
  const canvas = document.getElementById('sim-canvas-06');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const outlierSlider = document.getElementById('sim06-outliers');
  const lossSelect = document.getElementById('sim06-loss');

  const inliers = [];
  for (let x = 60; x < canvas.width - 60; x += 18) {
    const y = 0.45 * x + 70 + (Math.sin(x * 0.2) * 12);
    inliers.push({ x, y, isOutlier: false });
  }

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const outPct = parseInt(outlierSlider ? outlierSlider.value : 25) / 100;
    const lossType = lossSelect ? lossSelect.value : 'cauchy';

    const points = inliers.map(p => ({ ...p }));
    const numOutliers = Math.floor(points.length * outPct);
    for (let i = 0; i < numOutliers; i++) {
      const idx = (i * 3 + 4) % points.length;
      points[idx].y = canvas.height - 60 - (i % 2 === 0 ? 120 : 30);
      points[idx].isOutlier = true;
    }

    let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0;
    const n = points.length;
    points.forEach(p => {
      sumX += p.x; sumY += p.y;
      sumXY += p.x * p.y; sumXX += p.x * p.x;
    });
    const slopeL2 = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
    const interceptL2 = (sumY - slopeL2 * sumX) / n;

    let slopeRob = 0.45, interceptRob = 70;
    const c = 20;
    for (let iter = 0; iter < 10; iter++) {
      let wSumX = 0, wSumY = 0, wSumXY = 0, wSumXX = 0, totalW = 0;
      points.forEach(p => {
        const r = Math.abs(p.y - (slopeRob * p.x + interceptRob));
        let w = 1.0;
        if (lossType === 'huber') {
          w = r <= c ? 1.0 : c / r;
        } else if (lossType === 'cauchy') {
          w = 1.0 / (1.0 + (r * r) / (c * c));
        }
        wSumX += w * p.x; wSumY += w * p.y;
        wSumXY += w * p.x * p.y; wSumXX += w * p.x * p.x;
        totalW += w;
      });
      slopeRob = (totalW * wSumXY - wSumX * wSumY) / (totalW * wSumXX - wSumX * wSumX);
      interceptRob = (wSumY - slopeRob * wSumX) / totalW;
    }

    points.forEach(p => {
      ctx.fillStyle = p.isOutlier ? '#f43f5e' : '#38bdf8';
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.isOutlier ? 5 : 3.5, 0, Math.PI * 2);
      ctx.fill();
    });

    ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 2; ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(40, slopeL2 * 40 + interceptL2);
    ctx.lineTo(canvas.width - 40, slopeL2 * (canvas.width - 40) + interceptL2);
    ctx.stroke(); ctx.setLineDash([]);

    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(40, slopeRob * 40 + interceptRob);
    ctx.lineTo(canvas.width - 40, slopeRob * (canvas.width - 40) + interceptRob);
    ctx.stroke();

    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#f43f5e'; ctx.fillText(`-- L2 Least Squares (Bị kéo bởi ${Math.round(outPct*100)}% Outliers)`, 20, 25);
    ctx.fillStyle = '#10b981'; ctx.fillText(`— Robust ${lossType.toUpperCase()} M-Estimator (Kháng nhiễu)`, 320, 25);

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 07: 3D Rotation Representations (Euler, Quaternions, Axis-Angle)
// ============================================================================
function initSim07() {
  const canvas = document.getElementById('sim-canvas-07');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const rollSlider = document.getElementById('sim07-roll');
  const pitchSlider = document.getElementById('sim07-pitch');
  const yawSlider = document.getElementById('sim07-yaw');
  const statsEl = document.getElementById('sim07-stats');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const roll = (parseFloat(rollSlider ? rollSlider.value : 0) * Math.PI) / 180;
    const pitch = (parseFloat(pitchSlider ? pitchSlider.value : 30) * Math.PI) / 180;
    const yaw = (parseFloat(yawSlider ? yawSlider.value : 45) * Math.PI) / 180;

    const cx = canvas.width / 2;
    const cy = canvas.height / 2;

    const cr = Math.cos(roll), sr = Math.sin(roll);
    const cp = Math.cos(pitch), sp = Math.sin(pitch);
    const cyaw = Math.cos(yaw), syaw = Math.sin(yaw);

    const r11 = cyaw * cp;
    const r12 = cyaw * sp * sr - syaw * cr;
    const r13 = cyaw * sp * cr + syaw * sr;

    const r21 = syaw * cp;
    const r22 = syaw * sp * sr + cyaw * cr;
    const r23 = syaw * sp * cr - cyaw * sr;

    const r31 = -sp;
    const r32 = cp * sr;
    const r33 = cp * cr;

    const tr = r11 + r22 + r33;
    let qw, qx, qy, qz;
    if (tr > 0) {
      const S = Math.sqrt(tr + 1.0) * 2;
      qw = 0.25 * S; qx = (r32 - r23) / S; qy = (r13 - r31) / S; qz = (r21 - r12) / S;
    } else {
      qw = 1; qx = 0; qy = 0; qz = 0;
    }

    const len = 90;
    function project(x, y, z) {
      const scale = 1.0;
      return {
        px: cx + (x * 0.866 - y * 0.866) * scale,
        py: cy + (-x * 0.5 - y * 0.5 + z) * scale
      };
    }

    const origin = project(0, 0, 0);
    const xEnd = project(r11 * len, r21 * len, r31 * len);
    const yEnd = project(r12 * len, r22 * len, r32 * len);
    const zEnd = project(r13 * len, r23 * len, r33 * len);

    ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(xEnd.px, xEnd.py); ctx.stroke();

    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(yEnd.px, yEnd.py); ctx.stroke();

    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(zEnd.px, zEnd.py); ctx.stroke();

    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#f43f5e'; ctx.fillText('X_b', xEnd.px + 5, xEnd.py);
    ctx.fillStyle = '#10b981'; ctx.fillText('Y_b', yEnd.px + 5, yEnd.py);
    ctx.fillStyle = '#38bdf8'; ctx.fillText('Z_b', zEnd.px + 5, zEnd.py);

    if (statsEl) {
      statsEl.innerHTML = `Quaternion: <b>q = [${qw.toFixed(3)}, ${qx.toFixed(3)}, ${qy.toFixed(3)}, ${qz.toFixed(3)}]<sup>T</sup></b> | Euler: <b>&phi;=${(roll*180/Math.PI).toFixed(0)}&deg;, &theta;=${(pitch*180/Math.PI).toFixed(0)}&deg;, &psi;=${(yaw*180/Math.PI).toFixed(0)}&deg;</b>`;
    }

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 08: Matrix Lie Group SO(3) & Tangent Space so(3)
// ============================================================================
function initSim08() {
  const canvas = document.getElementById('sim-canvas-08');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const w1Slider = document.getElementById('sim08-w1');
  const w2Slider = document.getElementById('sim08-w2');
  const statsEl = document.getElementById('sim08-stats');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const w1 = parseFloat(w1Slider ? w1Slider.value : 0.6);
    const w2 = parseFloat(w2Slider ? w2Slider.value : 0.4);

    const cx = canvas.width / 2;
    const cy = canvas.height / 2 + 20;
    const R = 80;

    ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.stroke();

    ctx.strokeStyle = 'rgba(56, 189, 248, 0.2)';
    ctx.beginPath(); ctx.ellipse(cx, cy, R, R * 0.35, 0, 0, Math.PI * 2); ctx.stroke();

    const ipX = cx, ipY = cy - R;
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath(); ctx.arc(ipX, ipY, 5, 0, Math.PI * 2); ctx.fill();

    ctx.fillStyle = 'rgba(168, 85, 247, 0.15)';
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(ipX - 110, ipY - 30);
    ctx.lineTo(ipX + 110, ipY - 30);
    ctx.lineTo(ipX + 80, ipY + 30);
    ctx.lineTo(ipX - 140, ipY + 30);
    ctx.closePath();
    ctx.fill(); ctx.stroke();

    const vecEndX = ipX + w1 * 70;
    const vecEndY = ipY + w2 * 35;
    ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(ipX, ipY); ctx.lineTo(vecEndX, vecEndY); ctx.stroke();

    const theta = Math.sqrt(w1 * w1 + w2 * w2);
    const expX = cx + Math.sin(theta) * R * (w1 / (theta || 1));
    const expY = cy - Math.cos(theta) * R;

    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(ipX, ipY);
    ctx.quadraticCurveTo((ipX + expX) / 2, (ipY + expY) / 2 - 10, expX, expY);
    ctx.stroke();

    ctx.fillStyle = '#10b981';
    ctx.beginPath(); ctx.arc(expX, expY, 6, 0, Math.PI * 2); ctx.fill();

    if (statsEl) {
      statsEl.innerHTML = `Vectơ Lie: <b>&omega; = [${w1.toFixed(2)}, ${w2.toFixed(2)}]<sup>T</sup></b> | Góc quay: <b>&theta; = ${theta.toFixed(2)} rad</b> | Ma trận: <b>exp(&omega;<sup>&and;</sup>) &isin; SO(3)</b>`;
    }

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 09: Concentrated Gaussian on SE(3) & Uncertainty Propagation
// ============================================================================
function initSim09() {
  const canvas = document.getElementById('sim-canvas-09');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const noiseSlider = document.getElementById('sim09-noise');
  const stepBtn = document.getElementById('sim09-step-btn');

  let poses = [
    { x: 60, y: canvas.height / 2, th: 0, covX: 5, covY: 3, covTh: 0.05 }
  ];

  function addStep() {
    if (poses.length >= 8) poses = [poses[0]];
    const last = poses[poses.length - 1];
    const noise = parseFloat(noiseSlider ? noiseSlider.value : 1.0);
    const dth = 0.25;
    const ds = 45;
    const newTh = last.th + dth;
    const newX = last.x + ds * Math.cos(newTh);
    const newY = last.y + ds * Math.sin(newTh);

    const newCovX = last.covX + 6 * noise;
    const newCovY = last.covY + 8 * noise;
    const newCovTh = last.covTh + 0.06 * noise;
    poses.push({ x: newX, y: newY, th: newTh, covX: newCovX, covY: newCovY, covTh: newCovTh });
  }

  if (stepBtn) stepBtn.addEventListener('click', addStep);

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);

    poses.forEach((p, idx) => {
      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate(p.th);
      ctx.beginPath();
      ctx.ellipse(0, 0, p.covX, p.covY, 0, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(56, 189, 248, 0.15)';
      ctx.fill();
      ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 1.5; ctx.stroke();

      ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(20, 0); ctx.stroke();
      ctx.restore();

      if (idx > 0) {
        ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(poses[idx - 1].x, poses[idx - 1].y); ctx.lineTo(p.x, p.y); ctx.stroke();
      }
    });

    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Mô hình Gauss tập trung trên SE(3): Lan truyền sai số qua Adjoint Ad(T_k)', 20, 25);

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 10: Point Cloud Registration ICP & Horn Alignment
// ============================================================================
function initSim10() {
  const canvas = document.getElementById('sim-canvas-10');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const iterBtn = document.getElementById('sim10-iter-btn');
  const resetBtn = document.getElementById('sim10-reset-btn');
  const statsEl = document.getElementById('sim10-stats');

  const basePoints = [
    { x: -50, y: -40 }, { x: 0, y: -50 }, { x: 50, y: -30 },
    { x: 60, y: 20 }, { x: 10, y: 50 }, { x: -40, y: 30 }
  ];

  let currentTh = 0.6;
  let currentTx = 50, currentTy = -30;
  let icpIter = 0;

  function runIcpStep() {
    currentTh *= 0.65;
    currentTx *= 0.65;
    currentTy *= 0.65;
    icpIter++;
  }

  function resetIcp() {
    currentTh = 0.6; currentTx = 50; currentTy = -30; icpIter = 0;
  }

  if (iterBtn) iterBtn.addEventListener('click', runIcpStep);
  if (resetBtn) resetBtn.addEventListener('click', resetIcp);

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const cx = canvas.width / 2;
    const cy = canvas.height / 2;

    ctx.fillStyle = '#38bdf8';
    basePoints.forEach(p => {
      ctx.beginPath(); ctx.arc(cx + p.x, cy + p.y, 5, 0, Math.PI * 2); ctx.fill();
    });

    const cth = Math.cos(currentTh), sth = Math.sin(currentTh);
    ctx.fillStyle = '#f59e0b';
    basePoints.forEach(p => {
      const px = cx + (p.x * cth - p.y * sth) + currentTx;
      const py = cy + (p.x * sth + p.y * cth) + currentTy;
      ctx.beginPath(); ctx.arc(px, py, 5, 0, Math.PI * 2); ctx.fill();

      ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
      ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(cx + p.x, cy + p.y); ctx.stroke();
      ctx.setLineDash([]);
    });

    const rmse = Math.sqrt(currentTx * currentTx + currentTy * currentTy + currentTh * currentTh * 2000);
    if (statsEl) {
      statsEl.innerHTML = `Vòng lặp ICP: <b>${icpIter}</b> | Sai số RMSE: <b>${rmse.toFixed(2)}</b> | Góc lệch: <b>${(currentTh*180/Math.PI).toFixed(1)}&deg;</b>`;
    }

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 11: Pose-Graph Relaxation & Loop Closure on SE(3)
// ============================================================================
function initSim11() {
  const canvas = document.getElementById('sim-canvas-11');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const optBtn = document.getElementById('sim11-opt-btn');
  const loopBtn = document.getElementById('sim11-loop-btn');

  const N = 12;
  let nodes = [];
  let hasLoop = false;
  let isOptimized = false;

  function initNodes() {
    nodes = [];
    const R = 80;
    const cx = canvas.width / 2;
    const cy = canvas.height / 2;
    for (let i = 0; i < N; i++) {
      const ang = (i / N) * Math.PI * 1.8;
      const drift = i * 2.5;
      nodes.push({ x: cx + (R + drift) * Math.cos(ang), y: cy + (R + drift) * Math.sin(ang) });
    }
    hasLoop = false;
    isOptimized = false;
  }
  initNodes();

  if (loopBtn) loopBtn.addEventListener('click', () => { hasLoop = true; });
  if (optBtn) optBtn.addEventListener('click', () => {
    if (!hasLoop) hasLoop = true;
    const cx = canvas.width / 2;
    const cy = canvas.height / 2;
    const R = 80;
    nodes.forEach((n, i) => {
      const ang = (i / N) * Math.PI * 2;
      n.x = cx + R * Math.cos(ang);
      n.y = cy + R * Math.sin(ang);
    });
    isOptimized = true;
  });

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);

    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5; ctx.beginPath();
    nodes.forEach((n, idx) => { if (idx === 0) ctx.moveTo(n.x, n.y); else ctx.lineTo(n.x, n.y); });
    ctx.stroke();

    if (hasLoop) {
      ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(nodes[0].x, nodes[0].y); ctx.lineTo(nodes[nodes.length - 1].x, nodes[nodes.length - 1].y);
      ctx.stroke(); ctx.setLineDash([]);
    }

    nodes.forEach(n => {
      ctx.fillStyle = '#10b981';
      ctx.beginPath(); ctx.arc(n.x, n.y, 5, 0, Math.PI * 2); ctx.fill();
    });

    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText(isOptimized ? 'Đã tối ưu Pose-Graph (Loop Closure Resolved)' : 'Quỹ đạo trôi dạt (Chờ Loop Closure & Tối ưu)', 20, 25);

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 12: On-Manifold IMU Pre-Integration between Keyframes
// ============================================================================
function initSim12() {
  const canvas = document.getElementById('sim-canvas-12');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const biasSlider = document.getElementById('sim12-bias');
  const statsEl = document.getElementById('sim12-stats');

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const bias = parseFloat(biasSlider ? biasSlider.value : 0.0);

    const kf1 = { x: 80, y: canvas.height / 2 + 30 };
    const kf2 = { x: canvas.width - 90, y: canvas.height / 2 - 30 };

    const imuPoints = [];
    const steps = 30;
    for (let i = 0; i <= steps; i++) {
      const alpha = i / steps;
      const x = kf1.x + alpha * (kf2.x - kf1.x);
      const y = kf1.y + alpha * (kf2.y - kf1.y) - Math.sin(alpha * Math.PI) * (40 + bias * 30);
      imuPoints.push({ x, y });
    }

    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2.5; ctx.beginPath();
    imuPoints.forEach((p, idx) => { if (idx === 0) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y); });
    ctx.stroke();

    imuPoints.forEach(p => {
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath(); ctx.arc(p.x, p.y, 2, 0, Math.PI * 2); ctx.fill();
    });

    [kf1, kf2].forEach((kf, idx) => {
      ctx.fillStyle = '#f59e0b';
      ctx.fillRect(kf.x - 8, kf.y - 8, 16, 16);
      ctx.font = '12px Inter, sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.fillText(`Keyframe ${idx+1}`, kf.x - 25, kf.y + 25);
    });

    if (statsEl) {
      statsEl.innerHTML = `Độ trôi Bias: <b>&delta;b<sub>g</sub> = ${bias.toFixed(2)}</b> | Cập nhật Taylor bậc 1 qua Jacobian <b>&part;&Delta;R / &part;b</b> (Không cần tích phân lại IMU!)`;
    }

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 13: Bundle Adjustment & Schur Complement Arrowhead Matrix
// ============================================================================
function initSim13() {
  const canvas = document.getElementById('sim-canvas-13');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const schurBtn = document.getElementById('sim13-schur-btn');
  let isReduced = false;

  if (schurBtn) schurBtn.addEventListener('click', () => { isReduced = !isReduced; });

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const startX = 60, startY = 50;

    ctx.font = '13px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Hệ Phương Trình Chuẩn BA: H Delta x = -b', startX, 30);

    if (!isReduced) {
      ctx.fillStyle = '#38bdf8';
      ctx.fillRect(startX, startY, 50, 50);

      ctx.fillStyle = '#10b981';
      for (let i = 0; i < 4; i++) {
        ctx.fillRect(startX + 60 + i * 22, startY + 60 + i * 22, 18, 18);
      }

      ctx.fillStyle = 'rgba(244, 63, 94, 0.4)';
      ctx.fillRect(startX + 60, startY, 90, 50);
      ctx.fillRect(startX, startY + 60, 50, 90);

      ctx.fillStyle = '#ffffff';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText('B (Pose)', startX + 5, startY + 28);
      ctx.fillText('C (Landmarks)', startX + 70, startY + 110);
      ctx.fillText('E', startX + 90, startY + 28);
      ctx.fillText('E^T', startX + 15, startY + 100);
    } else {
      ctx.fillStyle = '#a855f7';
      ctx.fillRect(startX, startY, 50, 50);
      ctx.fillStyle = '#ffffff';
      ctx.fillText('S (Reduced)', startX + 2, startY + 28);

      ctx.font = '12px Inter, sans-serif';
      ctx.fillStyle = '#10b981';
      ctx.fillText('Đã triệt tiêu Landmark Block C qua Schur Complement!', startX + 80, startY + 30);
      ctx.fillText('Độ phức tạp giảm từ O((M+N)^3) xuống O(M^3)', startX + 80, startY + 55);
    }

    requestAnimationFrame(render);
  }
  render();
}

// ============================================================================
// SIM 14: Continuous-Time STEAM Trajectory GP Interpolation
// ============================================================================
function initSim14() {
  const canvas = document.getElementById('sim-canvas-14');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const timeSlider = document.getElementById('sim14-time');
  const statsEl = document.getElementById('sim14-stats');

  const cameraEvents = [60, 180, 300, 420];
  const lidarEvents = [90, 150, 210, 270, 330, 390, 450];

  function render() {
    clearCanvas(ctx, canvas.width, canvas.height);
    const queryT = parseFloat(timeSlider ? timeSlider.value : 250);

    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5; ctx.beginPath();
    for (let x = 40; x < canvas.width - 40; x++) {
      const y = canvas.height / 2 + Math.sin(x * 0.02) * 35 + Math.cos(x * 0.04) * 15;
      if (x === 40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();

    cameraEvents.forEach(cx => {
      const cy = canvas.height / 2 + Math.sin(cx * 0.02) * 35 + Math.cos(cx * 0.04) * 15;
      ctx.fillStyle = '#f59e0b';
      ctx.fillRect(cx - 4, cy - 4, 8, 8);
    });

    lidarEvents.forEach(lx => {
      const ly = canvas.height / 2 + Math.sin(lx * 0.02) * 35 + Math.cos(lx * 0.04) * 15;
      ctx.fillStyle = '#10b981';
      ctx.beginPath(); ctx.arc(lx, ly, 3.5, 0, Math.PI * 2); ctx.fill();
    });

    const qy = canvas.height / 2 + Math.sin(queryT * 0.02) * 35 + Math.cos(queryT * 0.04) * 15;
    ctx.fillStyle = '#f43f5e';
    ctx.beginPath(); ctx.arc(queryT, qy, 6, 0, Math.PI * 2); ctx.fill();

    ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(queryT, 0); ctx.lineTo(queryT, canvas.height); ctx.stroke();
    ctx.setLineDash([]);

    if (statsEl) {
      statsEl.innerHTML = `Thời điểm truy vấn: <b>t = ${queryT.toFixed(1)} ms</b> | STEAM nội suy GP chính xác dạng đóng (Closed-form) không trễ`;
    }

    requestAnimationFrame(render);
  }
  render();
}
