/**
 * Probabilistic Robotics (Prof. Sebastian Thrun, Wolfram Burgard, Dieter Fox - The MIT Press)
 * 17 Interactive Canvas 2D 60 FPS Simulators Suite
 */

// Helper: Setup High-DPI Canvas
function setupCanvas(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return null;
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  const width = rect.width || canvas.width || 700;
  const height = rect.height || canvas.height || 340;
  
  canvas.width = width * dpr;
  canvas.height = height * dpr;
  ctx.scale(dpr, dpr);
  return { canvas, ctx, width, height };
}

// -----------------------------------------------------------------------------
// 1. CH01: Interactive Bayes Inference Visualizer (Binary Door Open/Closed)
// -----------------------------------------------------------------------------
function initBayesInferenceSim() {
  const c = setupCanvas('sim-canvas-ch01');
  if (!c) return;
  const { ctx, width, height } = c;

  let priorOpen = 0.5;
  let pZOpenGivenOpen = 0.8;
  let pZOpenGivenClosed = 0.2;
  let history = [priorOpen];
  let measurements = [];

  const updateSim = () => {
    ctx.clearRect(0, 0, width, height);

    // Background grid
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);
    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    for (let x = 0; x < width; x += 40) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
    }
    for (let y = 0; y < height; y += 40) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
    }

    const currentBel = history[history.length - 1];

    // Left panel: Bar charts for bel(open) and bel(closed)
    const barWidth = 60;
    const maxHeight = 160;
    const baseY = height - 70;

    // Open bar
    const hOpen = currentBel * maxHeight;
    ctx.fillStyle = '#6366f1';
    ctx.fillRect(80, baseY - hOpen, barWidth, hOpen);
    ctx.fillStyle = '#ffffff';
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(`${(currentBel * 100).toFixed(1)}%`, 110, baseY - hOpen - 8);
    ctx.fillText('bel(Open)', 110, baseY + 20);

    // Closed bar
    const hClosed = (1 - currentBel) * maxHeight;
    ctx.fillStyle = '#f59e0b';
    ctx.fillRect(170, baseY - hClosed, barWidth, hClosed);
    ctx.fillStyle = '#ffffff';
    ctx.fillText(`${((1 - currentBel) * 100).toFixed(1)}%`, 200, baseY - hClosed - 8);
    ctx.fillText('bel(Closed)', 200, baseY + 20);

    // Right panel: Belief history graph
    const graphX = 290;
    const graphY = 40;
    const graphW = width - graphX - 40;
    const graphH = height - 100;

    ctx.strokeStyle = '#334155';
    ctx.strokeRect(graphX, graphY, graphW, graphH);

    // 0.5 baseline
    ctx.strokeStyle = '#475569';
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(graphX, graphY + graphH * 0.5);
    ctx.lineTo(graphX + graphW, graphY + graphH * 0.5);
    ctx.stroke();
    ctx.setLineDash([]);

    // Plot history curve
    if (history.length > 1) {
      ctx.beginPath();
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3;
      const stepX = graphW / Math.max(history.length - 1, 10);
      for (let i = 0; i < history.length; i++) {
        const x = graphX + i * stepX;
        const y = graphY + graphH * (1 - history[i]);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Points
      for (let i = 0; i < history.length; i++) {
        const x = graphX + i * stepX;
        const y = graphY + graphH * (1 - history[i]);
        ctx.fillStyle = i === 0 ? '#94a3b8' : (measurements[i - 1] === 'open' ? '#34d399' : '#f87171');
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px JetBrains Mono, monospace';
    ctx.textAlign = 'left';
    ctx.fillText(`Quan sát gần nhất: ${measurements.length ? measurements[measurements.length - 1].toUpperCase() : 'Chưa có'} | Bước: ${history.length - 1}`, graphX, height - 35);
  };

  const applyMeasurement = (meas) => {
    const cur = history[history.length - 1];
    let num, den;
    if (meas === 'open') {
      num = pZOpenGivenOpen * cur;
      den = num + pZOpenGivenClosed * (1 - cur);
    } else {
      num = (1 - pZOpenGivenOpen) * cur;
      den = num + (1 - pZOpenGivenClosed) * (1 - cur);
    }
    const newBel = num / (den || 1e-6);
    history.push(newBel);
    measurements.push(meas);
    updateSim();
  };

  const btnOpen = document.getElementById('ch01-btn-open');
  const btnClosed = document.getElementById('ch01-btn-closed');
  const btnReset = document.getElementById('ch01-btn-reset');
  const sliderPrior = document.getElementById('ch01-slider-prior');

  if (btnOpen) btnOpen.onclick = () => applyMeasurement('open');
  if (btnClosed) btnClosed.onclick = () => applyMeasurement('closed');
  if (btnReset) {
    btnReset.onclick = () => {
      history = [priorOpen];
      measurements = [];
      updateSim();
    };
  }
  if (sliderPrior) {
    sliderPrior.oninput = (e) => {
      priorOpen = parseFloat(e.target.value);
      history = [priorOpen];
      measurements = [];
      updateSim();
    };
  }

  updateSim();
}

// -----------------------------------------------------------------------------
// 2. CH02: 1D Grid Bayes Filter Simulator (Prediction & Update)
// -----------------------------------------------------------------------------
function initGridBayes1DSim() {
  const c = setupCanvas('sim-canvas-ch02');
  if (!c) return;
  const { ctx, width, height } = c;

  const N = 15;
  let bel = new Array(N).fill(1 / N);
  let truePos = 4;
  const landmarkPos = 8;

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    const cellW = (width - 60) / N;
    const startX = 30;
    const baseY = height - 80;
    const maxBarH = 150;

    // Draw landmark
    const lmX = startX + landmarkPos * cellW + cellW / 2;
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.moveTo(lmX, 30);
    ctx.lineTo(lmX - 10, 50);
    ctx.lineTo(lmX + 10, 50);
    ctx.closePath();
    ctx.fill();
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#f87171';
    ctx.textAlign = 'center';
    ctx.fillText('Mốc đo (Landmark)', lmX, 20);

    // Draw grid and belief bars
    for (let i = 0; i < N; i++) {
      const x = startX + i * cellW;
      const bH = bel[i] * maxBarH;

      // Bar
      ctx.fillStyle = i === truePos ? 'rgba(59, 130, 246, 0.85)' : 'rgba(99, 102, 241, 0.45)';
      ctx.fillRect(x + 2, baseY - bH, cellW - 4, bH);

      // Cell border
      ctx.strokeStyle = '#334155';
      ctx.strokeRect(x, baseY, cellW, 30);

      // Cell index
      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px monospace';
      ctx.textAlign = 'center';
      ctx.fillText(i.toString(), x + cellW / 2, baseY + 18);

      // True robot indicator
      if (i === truePos) {
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(x + cellW / 2, baseY + 45, 6, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    ctx.fillStyle = '#38bdf8';
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('● Vị trí robot thực tế | Cột xanh: Phân bố niềm tin bel(x)', 30, height - 15);
  };

  const actionStep = () => {
    // Prediction with slip: 70% move +1, 20% stay, 10% move +2
    const nextBel = new Array(N).fill(0);
    for (let i = 0; i < N; i++) {
      if (bel[i] > 0) {
        const i1 = Math.min(i + 1, N - 1);
        const i2 = Math.min(i + 2, N - 1);
        nextBel[i1] += bel[i] * 0.7;
        nextBel[i] += bel[i] * 0.2;
        nextBel[i2] += bel[i] * 0.1;
      }
    }
    bel = nextBel;
    truePos = Math.min(truePos + 1, N - 1);
    draw();
  };

  const senseStep = () => {
    // Measurement model: senses distance to landmark
    const trueDist = landmarkPos - truePos;
    const measuredDist = trueDist + (Math.random() > 0.5 ? 0 : (Math.random() > 0.5 ? 1 : -1));
    let sum = 0;
    for (let i = 0; i < N; i++) {
      const dist = landmarkPos - i;
      const err = Math.abs(dist - measuredDist);
      const prob = Math.exp(-0.5 * (err * err) / 1.0);
      bel[i] *= prob;
      sum += bel[i];
    }
    if (sum > 0) {
      for (let i = 0; i < N; i++) bel[i] /= sum;
    }
    draw();
  };

  const btnAct = document.getElementById('ch02-btn-act');
  const btnSense = document.getElementById('ch02-btn-sense');
  const btnReset = document.getElementById('ch02-btn-reset');

  if (btnAct) btnAct.onclick = actionStep;
  if (btnSense) btnSense.onclick = senseStep;
  if (btnReset) {
    btnReset.onclick = () => {
      bel = new Array(N).fill(1 / N);
      truePos = 4;
      draw();
    };
  }

  draw();
}

// -----------------------------------------------------------------------------
// 3. CH03: Nonlinear Gaussian Filter Comparison Lab (EKF vs UKF vs Monte Carlo)
// -----------------------------------------------------------------------------
function initNonlinearGaussianSim() {
  const c = setupCanvas('sim-canvas-ch03');
  if (!c) return;
  const { ctx, width, height } = c;

  let muX = 1.2;
  let sigmaX = 0.6;
  const g = (x) => Math.sin(x) + 0.3 * x * x;
  const gPrime = (x) => Math.cos(x) + 0.6 * x;

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // 1. Monte Carlo Ground Truth
    const N = 2000;
    let sumY = 0;
    let sumY2 = 0;
    for (let i = 0; i < N; i++) {
      const u1 = Math.random();
      const u2 = Math.random();
      const z = Math.sqrt(-2.0 * Math.log(u1 || 1e-6)) * Math.cos(2.0 * Math.PI * u2);
      const x = muX + sigmaX * z;
      const y = g(x);
      sumY += y;
      sumY2 += y * y;
    }
    const muMC = sumY / N;
    const varMC = (sumY2 / N) - muMC * muMC;

    // 2. EKF (Taylor first-order)
    const muEKF = g(muX);
    const grad = gPrime(muX);
    const varEKF = grad * grad * (sigmaX * sigmaX);

    // 3. UKF (Unscented Transform 1D, lambda = 2)
    const kappa = 2;
    const scale = Math.sqrt(1 + kappa) * sigmaX;
    const sigmas = [muX, muX + scale, muX - scale];
    const wM = [kappa / (1 + kappa), 0.5 / (1 + kappa), 0.5 / (1 + kappa)];
    const ySigmas = sigmas.map(s => g(s));
    let muUKF = 0;
    for (let i = 0; i < 3; i++) muUKF += wM[i] * ySigmas[i];
    let varUKF = 0;
    for (let i = 0; i < 3; i++) varUKF += wM[i] * Math.pow(ySigmas[i] - muUKF, 2);

    // Visualization: 3 Gaussian PDFs on right, Input on left
    const midX = width / 2;

    // Left divider
    ctx.strokeStyle = '#334155';
    ctx.beginPath(); ctx.moveTo(midX, 20); ctx.lineTo(midX, height - 20); ctx.stroke();

    // Text info
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.textAlign = 'left';
    ctx.fillText('Hàm phi tuyến: g(x) = sin(x) + 0.3x²', 25, 30);
    ctx.fillText(`Đầu vào x ~ N(${muX.toFixed(2)}, ${sigmaX.toFixed(2)}²)`, 25, 50);

    // Draw Comparison Table/Stats
    const drawStat = (label, mu, std, color, yPos) => {
      ctx.fillStyle = color;
      ctx.font = 'bold 12px monospace';
      ctx.fillText(`${label}:`, midX + 20, yPos);
      ctx.font = '12px monospace';
      ctx.fillText(`μ = ${mu.toFixed(3)}, σ = ${Math.sqrt(Math.max(std, 0)).toFixed(3)}`, midX + 160, yPos);
    };

    drawStat('Ground Truth (MC)', muMC, varMC, '#34d399', 60);
    drawStat('EKF (Taylor 1st)', muEKF, varEKF, '#f87171', 95);
    drawStat('UKF (Sigma Points)', muUKF, varUKF, '#38bdf8', 130);

    // Plot curves on bottom
    const plotY = height - 120;
    const plotH = 90;
    const yMin = -1, yMax = 5;
    const toScreenX = (val) => midX + 20 + ((val - yMin) / (yMax - yMin)) * (width - midX - 50);

    const drawGaussian = (mu, variance, color, isDashed) => {
      ctx.beginPath();
      ctx.strokeStyle = color;
      ctx.lineWidth = 2;
      if (isDashed) ctx.setLineDash([4, 4]); else ctx.setLineDash([]);
      const std = Math.sqrt(Math.max(variance, 1e-4));
      for (let py = yMin; py <= yMax; py += 0.05) {
        const sx = toScreenX(py);
        const p = (1 / (std * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * Math.pow((py - mu) / std, 2));
        const sy = plotY + plotH - (p * 40);
        if (py === yMin) ctx.moveTo(sx, sy); else ctx.lineTo(sx, sy);
      }
      ctx.stroke();
      ctx.setLineDash([]);
    };

    drawGaussian(muMC, varMC, '#34d399', false);
    drawGaussian(muEKF, varEKF, '#f87171', true);
    drawGaussian(muUKF, varUKF, '#38bdf8', false);

    ctx.fillStyle = '#64748b';
    ctx.font = '10px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Không gian đầu ra y', midX + (width - midX) / 2, height - 15);
  };

  const sliderMu = document.getElementById('ch03-slider-mu');
  const sliderSigma = document.getElementById('ch03-slider-sigma');
  if (sliderMu) sliderMu.oninput = (e) => { muX = parseFloat(e.target.value); draw(); };
  if (sliderSigma) sliderSigma.oninput = (e) => { sigmaX = parseFloat(e.target.value); draw(); };

  draw();
}

// -----------------------------------------------------------------------------
// 4. CH04: Low Variance Resampling Wheel Lab
// -----------------------------------------------------------------------------
function initParticleResamplingSim() {
  const c = setupCanvas('sim-canvas-ch04');
  if (!c) return;
  const { ctx, width, height } = c;

  const M = 10;
  let weights = [0.05, 0.35, 0.10, 0.02, 0.25, 0.03, 0.05, 0.08, 0.02, 0.05];
  let r = 0.03;
  let resampledIndices = [];

  const runResample = () => {
    resampledIndices = [];
    const step = 1.0 / M;
    let u = r;
    let cSum = weights[0];
    let i = 0;
    for (let m = 0; m < M; m++) {
      while (u > cSum && i < M - 1) {
        i++;
        cSum += weights[i];
      }
      resampledIndices.push(i);
      u += step;
    }
  };

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Wheel visualization on left
    const centerX = 160;
    const centerY = height / 2;
    const radius = 95;

    let startAngle = 0;
    const colors = ['#f43f5e', '#ec4899', '#d946ef', '#a855f7', '#6366f1', '#3b82f6', '#0ea5e9', '#06b6d4', '#14b8a6', '#10b981'];

    for (let i = 0; i < M; i++) {
      const slice = weights[i] * 2 * Math.PI;
      ctx.beginPath();
      ctx.moveTo(centerX, centerY);
      ctx.arc(centerX, centerY, radius, startAngle, startAngle + slice);
      ctx.closePath();
      ctx.fillStyle = colors[i % colors.length];
      ctx.fill();
      ctx.strokeStyle = '#0f172a';
      ctx.stroke();

      // Label
      if (weights[i] > 0.06) {
        const midA = startAngle + slice / 2;
        const tx = centerX + Math.cos(midA) * (radius * 0.65);
        const ty = centerY + Math.sin(midA) * (radius * 0.65);
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 10px monospace';
        ctx.textAlign = 'center';
        ctx.fillText(`x${i + 1}`, tx, ty + 3);
      }
      startAngle += slice;
    }

    // Pointer lines at r + m/M
    ctx.strokeStyle = '#facc15';
    ctx.lineWidth = 2;
    for (let m = 0; m < M; m++) {
      const u = (r + m * (1.0 / M)) % 1.0;
      const ang = u * 2 * Math.PI;
      ctx.beginPath();
      ctx.moveTo(centerX, centerY);
      ctx.lineTo(centerX + Math.cos(ang) * (radius + 15), centerY + Math.sin(ang) * (radius + 15));
      ctx.stroke();
    }

    // Right side: Resampled particle count
    const rightX = 330;
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('KẾT QUẢ LẤY MẪU LẠI (LOW-VARIANCE SAMPLER)', rightX, 35);

    const counts = new Array(M).fill(0);
    resampledIndices.forEach(idx => counts[idx]++);

    for (let i = 0; i < M; i++) {
      const y = 60 + i * 24;
      ctx.fillStyle = colors[i % colors.length];
      ctx.fillRect(rightX, y, 12, 12);
      ctx.fillStyle = '#e2e8f0';
      ctx.font = '11px monospace';
      ctx.fillText(`Hạt x${i + 1} (w = ${(weights[i] * 100).toFixed(0)}%):`, rightX + 22, y + 10);

      // Multiplicity
      ctx.fillStyle = counts[i] > 0 ? '#38bdf8' : '#64748b';
      ctx.fillText(`→ nhân bản ${counts[i]} lần`, rightX + 210, y + 10);
    }
  };

  runResample();
  draw();

  const btnSpin = document.getElementById('ch04-btn-spin');
  if (btnSpin) {
    btnSpin.onclick = () => {
      r = Math.random() * (1.0 / M);
      runResample();
      draw();
    };
  }
}

// -----------------------------------------------------------------------------
// 5. CH05: Banana-Shaped Motion Distribution Lab
// -----------------------------------------------------------------------------
function initBananaMotionSim() {
  const c = setupCanvas('sim-canvas-ch05');
  if (!c) return;
  const { ctx, width, height } = c;

  let a1 = 0.05, a2 = 0.05, a3 = 0.05, a4 = 0.05;
  const v = 1.5;
  const w = 0.8;
  const dt = 1.0;
  const numParticles = 400;

  const sampleNormal = (std) => {
    const u1 = Math.random(), u2 = Math.random();
    return Math.sqrt(-2.0 * Math.log(u1 || 1e-6)) * Math.cos(2.0 * Math.PI * u2) * std;
  };

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Initial pose origin
    const originX = 120;
    const originY = height - 80;
    const scale = 80;

    // Grid
    ctx.strokeStyle = '#1e293b';
    ctx.beginPath();
    ctx.moveTo(0, originY); ctx.lineTo(width, originY);
    ctx.moveTo(originX, 0); ctx.lineTo(originX, height);
    ctx.stroke();

    // Draw initial robot
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(originX, originY, 6, 0, Math.PI * 2);
    ctx.fill();

    // Velocity Motion Model Sampling
    for (let i = 0; i < numParticles; i++) {
      const vHat = v + sampleNormal(Math.sqrt(a1 * v * v + a2 * w * w));
      const wHat = w + sampleNormal(Math.sqrt(a3 * v * v + a4 * w * w));
      const gamma = sampleNormal(Math.sqrt(a1 * v * v + a2 * w * w));

      const rCurv = vHat / (wHat || 1e-4);
      const xNew = originX + (-rCurv * Math.sin(0) + rCurv * Math.sin(wHat * dt)) * scale;
      const yNew = originY - (rCurv * Math.cos(0) - rCurv * Math.cos(wHat * dt)) * scale;

      ctx.fillStyle = 'rgba(244, 63, 94, 0.45)';
      ctx.beginPath();
      ctx.arc(xNew, yNew, 2.5, 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.fillStyle = '#ffffff';
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText(`Mô hình vận tốc: v = ${v} m/s, ω = ${w} rad/s | 400 hạt tư thế phân bố hình quả chuối (Banana Shape)`, 20, 25);
  };

  const sliderA = document.getElementById('ch05-slider-alpha');
  if (sliderA) {
    sliderA.oninput = (e) => {
      const val = parseFloat(e.target.value);
      a1 = a2 = a3 = a4 = val;
      draw();
    };
  }

  draw();
}

// -----------------------------------------------------------------------------
// 6. CH06: Beam Model vs Likelihood Field Simulation
// -----------------------------------------------------------------------------
function initBeamVsLikelihoodSim() {
  const c = setupCanvas('sim-canvas-ch06');
  if (!c) return;
  const { ctx, width, height } = c;

  let mode = 'likelihood';
  const robot = { x: 100, y: height / 2, angle: 0 };
  const obstacle = { x: 420, y: height / 2, r: 60 };

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Obstacle
    ctx.fillStyle = '#475569';
    ctx.beginPath();
    ctx.arc(obstacle.x, obstacle.y, obstacle.r, 0, Math.PI * 2);
    ctx.fill();

    // Robot
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(robot.x, robot.y, 8, 0, Math.PI * 2);
    ctx.fill();

    // Laser rays
    const numRays = 40;
    const fov = Math.PI / 3;
    for (let i = 0; i < numRays; i++) {
      const ang = robot.angle - fov / 2 + (i / (numRays - 1)) * fov;
      const rayLen = 450;
      const endX = robot.x + Math.cos(ang) * rayLen;
      const endY = robot.y + Math.sin(ang) * rayLen;

      ctx.strokeStyle = mode === 'likelihood' ? 'rgba(56, 189, 248, 0.25)' : 'rgba(244, 63, 94, 0.25)';
      ctx.beginPath();
      ctx.moveTo(robot.x, robot.y);
      ctx.lineTo(endX, endY);
      ctx.stroke();
    }

    ctx.fillStyle = '#ffffff';
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText(`Chế độ: ${mode === 'likelihood' ? 'Likelihood Field (Trường khả dĩ Euclidean)' : 'Beam-based Model (Mô hình chùm tia)'}`, 20, 30);
  };

  const btnToggle = document.getElementById('ch06-btn-toggle');
  if (btnToggle) {
    btnToggle.onclick = () => {
      mode = mode === 'likelihood' ? 'beam' : 'likelihood';
      draw();
    };
  }

  draw();
}

// -----------------------------------------------------------------------------
// 7. CH07: 2D EKF Localization & Covariance Ellipse Lab
// -----------------------------------------------------------------------------
function initEKFLocalizationSim() {
  const c = setupCanvas('sim-canvas-ch07');
  if (!c) return;
  const { ctx, width, height } = c;

  let step = 0;
  const landmarks = [{ x: 180, y: 80 }, { x: 500, y: 100 }, { x: 380, y: 260 }];
  let estPose = { x: 100, y: 180, theta: 0 };
  let sigma = 15;

  const loop = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Landmarks
    landmarks.forEach((lm, idx) => {
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(lm.x, lm.y, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = '10px monospace';
      ctx.fillText(`L${idx + 1}`, lm.x - 5, lm.y - 12);
    });

    // Move robot along circle
    step += 0.02;
    const rx = 320 + Math.cos(step) * 160;
    const ry = 170 + Math.sin(step) * 80;

    // Measurement update shrinking ellipse
    let isObserving = false;
    landmarks.forEach(lm => {
      const d = Math.hypot(lm.x - rx, lm.y - ry);
      if (d < 160) {
        isObserving = true;
        ctx.strokeStyle = 'rgba(52, 211, 153, 0.4)';
        ctx.beginPath();
        ctx.moveTo(rx, ry);
        ctx.lineTo(lm.x, lm.y);
        ctx.stroke();
      }
    });

    sigma = isObserving ? Math.max(sigma - 0.4, 6) : Math.min(sigma + 0.3, 26);

    // Robot true pose
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(rx, ry, 6, 0, Math.PI * 2);
    ctx.fill();

    // Covariance 2-sigma ellipse
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.ellipse(rx, ry, sigma * 1.5, sigma, step, 0, Math.PI * 2);
    ctx.stroke();

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText(`Bán kính elip 2σ: ${sigma.toFixed(1)} px (${isObserving ? 'Nhìn thấy mốc: Co hẹp' : 'Mất dấu mốc: Phình to'})`, 20, height - 15);

    requestAnimationFrame(loop);
  };

  requestAnimationFrame(loop);
}

// -----------------------------------------------------------------------------
// 8. CH08: Interactive AMCL & Kidnapped Robot Lab
// -----------------------------------------------------------------------------
function initAMCLKidnapSim() {
  const c = setupCanvas('sim-canvas-ch08');
  if (!c) return;
  const { ctx, width, height } = c;

  let rx = 200, ry = 170;
  const M = 250;
  let particles = Array.from({ length: M }, () => ({
    x: rx + (Math.random() - 0.5) * 50,
    y: ry + (Math.random() - 0.5) * 50
  }));

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Draw Particles
    ctx.fillStyle = 'rgba(244, 63, 94, 0.6)';
    particles.forEach(p => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
      ctx.fill();
    });

    // Robot
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(rx, ry, 7, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = '#ffffff';
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Nhấp "Bắt cóc Robot (Kidnap)" để di chuyển robot sang vị trí mới và kích hoạt Augmented MCL', 20, 25);
  };

  const kidnap = () => {
    rx = 100 + Math.random() * (width - 200);
    ry = 60 + Math.random() * (height - 120);
    // Inject 40% random particles for recovery
    for (let i = 0; i < M * 0.4; i++) {
      particles[i] = { x: Math.random() * width, y: Math.random() * height };
    }
    draw();
  };

  const btnKidnap = document.getElementById('ch08-btn-kidnap');
  if (btnKidnap) btnKidnap.onclick = kidnap;

  draw();
}

// -----------------------------------------------------------------------------
// 9. CH09: Realtime 2D Occupancy Grid Mapper
// -----------------------------------------------------------------------------
function initOccupancyGridSim() {
  const c = setupCanvas('sim-canvas-ch09');
  if (!c) return;
  const { ctx, width, height } = c;

  const gridSize = 20;
  const cols = Math.floor(width / gridSize);
  const rows = Math.floor(height / gridSize);
  let logOdds = Array.from({ length: rows }, () => new Array(cols).fill(0));

  const draw = () => {
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const p = 1.0 - (1.0 / (1.0 + Math.exp(logOdds[r][c])));
        const shade = Math.floor((1 - p) * 255);
        ctx.fillStyle = `rgb(${shade}, ${shade}, ${shade})`;
        ctx.fillRect(c * gridSize, r * gridSize, gridSize - 1, gridSize - 1);
      }
    }
  };

  c.canvas.addEventListener('mousemove', (e) => {
    const rect = c.canvas.getBoundingClientRect();
    const mx = Math.floor((e.clientX - rect.left) / gridSize);
    const my = Math.floor((e.clientY - rect.top) / gridSize);
    if (mx >= 0 && mx < cols && my >= 0 && my < rows) {
      logOdds[my][mx] = Math.min(logOdds[my][mx] + 1.2, 5.0);
      draw();
    }
  });

  draw();
}

// -----------------------------------------------------------------------------
// 10. CH10: EKF Landmark SLAM Interactive Simulator
// -----------------------------------------------------------------------------
function initEKFSLAMSim() {
  const c = setupCanvas('sim-canvas-ch10');
  if (!c) return;
  const { ctx, width, height } = c;

  let t = 0;
  const loop = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    t += 0.02;
    const rx = width / 2 + Math.cos(t) * 140;
    const ry = height / 2 + Math.sin(t) * 90;

    // Robot
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(rx, ry, 7, 0, Math.PI * 2);
    ctx.fill();

    // Landmarks with cross-correlation lines
    const lms = [{ x: 180, y: 120 }, { x: 520, y: 140 }, { x: 350, y: 260 }];
    lms.forEach((lm, i) => {
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(lm.x, lm.y, 6, 0, Math.PI * 2);
      ctx.fill();

      // Correlation dashed lines
      ctx.strokeStyle = 'rgba(99, 102, 241, 0.35)';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(rx, ry);
      ctx.lineTo(lm.x, lm.y);
      ctx.stroke();
      ctx.setLineDash([]);
    });

    ctx.fillStyle = '#e2e8f0';
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Đường đứt nét: Ma trận tương quan chéo hiệp phương sai Σ_RM trong EKF SLAM', 20, 25);

    requestAnimationFrame(loop);
  };
  requestAnimationFrame(loop);
}

// -----------------------------------------------------------------------------
// 11. CH11: Pose Graph Optimization Lab (GraphSLAM)
// -----------------------------------------------------------------------------
function initGraphSLAMSim() {
  const c = setupCanvas('sim-canvas-ch11');
  if (!c) return;
  const { ctx, width, height } = c;

  let nodes = [
    { x: 120, y: 180 }, { x: 220, y: 120 }, { x: 340, y: 110 },
    { x: 460, y: 150 }, { x: 420, y: 250 }, { x: 280, y: 260 }
  ];

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Odometry edges
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      if (i === 0) ctx.moveTo(n.x, n.y); else ctx.lineTo(n.x, n.y);
    }
    ctx.stroke();

    // Loop closure edge (last to first)
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 3;
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(nodes[nodes.length - 1].x, nodes[nodes.length - 1].y);
    ctx.lineTo(nodes[0].x, nodes[0].y);
    ctx.stroke();
    ctx.setLineDash([]);

    // Nodes
    nodes.forEach((n, idx) => {
      ctx.fillStyle = '#6366f1';
      ctx.beginPath();
      ctx.arc(n.x, n.y, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.font = '10px monospace';
      ctx.fillText(`x${idx}`, n.x - 5, n.y - 12);
    });

    ctx.fillStyle = '#ffffff';
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Đường đỏ nét đứt: Ràng buộc khép vòng lặp (Loop Closure Constraint)', 20, 25);
  };

  const btnOptimize = document.getElementById('ch11-btn-optimize');
  if (btnOptimize) {
    btnOptimize.onclick = () => {
      // Pull nodes closer to close loop
      for (let i = 1; i < nodes.length; i++) {
        nodes[i].x += (nodes[0].x - nodes[i].x) * 0.15;
        nodes[i].y += (nodes[0].y - nodes[i].y) * 0.15;
      }
      draw();
    };
  }

  draw();
}

// -----------------------------------------------------------------------------
// 12. CH12: SEIF Sparsification & Spy Plot Lab
// -----------------------------------------------------------------------------
function initSEIFSLAMSim() {
  const c = setupCanvas('sim-canvas-ch12');
  if (!c) return;
  const { ctx, width, height } = c;

  const N = 12;
  let isSparsified = false;

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    const cellSize = 18;
    const startX = (width - N * cellSize) / 2;
    const startY = 50;

    for (let r = 0; r < N; r++) {
      for (let col = 0; col < N; col++) {
        let isNonZero = (r === col) || (r < 2) || (col < 2);
        if (!isSparsified && (Math.abs(r - col) < 3)) isNonZero = true;

        ctx.fillStyle = isNonZero ? '#38bdf8' : '#1e293b';
        ctx.fillRect(startX + col * cellSize, startY + r * cellSize, cellSize - 2, cellSize - 2);
      }
    }

    ctx.fillStyle = '#ffffff';
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(`Ma trận thông tin Ω (${isSparsified ? 'Đã Thưa Hóa - Cập nhật O(1)' : 'Đầy Đủ - Chưa thưa hóa'})`, width / 2, 30);
  };

  const btnToggle = document.getElementById('ch12-btn-sparse');
  if (btnToggle) {
    btnToggle.onclick = () => {
      isSparsified = !isSparsified;
      draw();
    };
  }

  draw();
}

// -----------------------------------------------------------------------------
// 13. CH13: FastSLAM 2.0 Multi-Hypothesis Particle Lab
// -----------------------------------------------------------------------------
function initFastSLAMSim() {
  const c = setupCanvas('sim-canvas-ch13');
  if (!c) return;
  const { ctx, width, height } = c;

  const M = 25;
  const particles = Array.from({ length: M }, () => ({
    pts: [{ x: 100, y: height / 2 }],
    weight: Math.random()
  }));

  for (let step = 1; step < 20; step++) {
    particles.forEach(p => {
      const last = p.pts[p.pts.length - 1];
      p.pts.push({
        x: last.x + 24 + (Math.random() - 0.5) * 8,
        y: last.y + Math.sin(step * 0.4) * 12 + (Math.random() - 0.5) * 10
      });
    });
  }

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    particles.forEach(p => {
      ctx.strokeStyle = `rgba(99, 102, 241, ${0.15 + p.weight * 0.6})`;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      p.pts.forEach((pt, idx) => {
        if (idx === 0) ctx.moveTo(pt.x, pt.y); else ctx.lineTo(pt.x, pt.y);
      });
      ctx.stroke();
    });

    ctx.fillStyle = '#38bdf8';
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('Mỗi hạt mang một quỹ đạo giả định độc lập kèm N bộ lọc EKF riêng cho các mốc', 20, 25);
  };

  draw();
}

// -----------------------------------------------------------------------------
// 14. CH14: Grid World MDP Value Iteration Visualizer
// -----------------------------------------------------------------------------
function initMDPValueIterationSim() {
  const c = setupCanvas('sim-canvas-ch14');
  if (!c) return;
  const { ctx, width, height } = c;

  const R = 3, C = 4;
  let V = Array.from({ length: R }, () => new Array(C).fill(0));
  V[0][3] = 10;   // Goal
  V[1][3] = -10;  // Pit

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    const cellW = 100;
    const cellH = 80;
    const startX = (width - C * cellW) / 2;
    const startY = 40;

    for (let r = 0; r < R; r++) {
      for (let col = 0; col < C; col++) {
        if (r === 1 && col === 1) {
          ctx.fillStyle = '#334155'; // Obstacle
        } else if (r === 0 && col === 3) {
          ctx.fillStyle = '#059669'; // Goal
        } else if (r === 1 && col === 3) {
          ctx.fillStyle = '#dc2626'; // Pit
        } else {
          ctx.fillStyle = '#1e293b';
        }

        ctx.fillRect(startX + col * cellW, startY + r * cellH, cellW - 4, cellH - 4);
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 12px monospace';
        ctx.textAlign = 'center';
        ctx.fillText(V[r][col].toFixed(2), startX + col * cellW + cellW / 2, startY + r * cellH + cellH / 2 + 4);
      }
    }
  };

  const stepVI = () => {
    const nextV = V.map(row => [...row]);
    const gamma = 0.9;
    for (let r = 0; r < R; r++) {
      for (let col = 0; col < C; col++) {
        if ((r === 1 && col === 1) || (r === 0 && col === 3) || (r === 1 && col === 3)) continue;
        const neighbors = [
          r > 0 ? V[r - 1][col] : V[r][col],
          r < R - 1 ? V[r + 1][col] : V[r][col],
          col > 0 ? V[r][col - 1] : V[r][col],
          col < C - 1 ? V[r][col + 1] : V[r][col]
        ];
        nextV[r][col] = -0.04 + gamma * Math.max(...neighbors);
      }
    }
    V = nextV;
    draw();
  };

  const btnStep = document.getElementById('ch14-btn-step');
  if (btnStep) btnStep.onclick = stepVI;

  draw();
}

// -----------------------------------------------------------------------------
// 15. CH15: POMDP Belief Space & Alpha-Vectors Lab
// -----------------------------------------------------------------------------
function initPOMDPBeliefSim() {
  const c = setupCanvas('sim-canvas-ch15');
  if (!c) return;
  const { ctx, width, height } = c;

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    const padL = 80, padR = 80;
    const baseY = height - 60;
    const topY = 40;
    const w = width - padL - padR;

    // Belief axis b(s1) in [0, 1]
    ctx.strokeStyle = '#475569';
    ctx.beginPath();
    ctx.moveTo(padL, baseY); ctx.lineTo(padL + w, baseY);
    ctx.stroke();

    // 2 Alpha-vectors: a1 and a2
    const a1_0 = 10, a1_1 = 40;
    const a2_0 = 45, a2_1 = 5;

    // Draw line 1 (Act Left)
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(padL, baseY - a1_0 * 3);
    ctx.lineTo(padL + w, baseY - a1_1 * 3);
    ctx.stroke();

    // Draw line 2 (Act Right)
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(padL, baseY - a2_0 * 3);
    ctx.lineTo(padL + w, baseY - a2_1 * 3);
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('b(s1) = 0', padL, baseY + 20);
    ctx.fillText('b(s1) = 1', padL + w, baseY + 20);
    ctx.fillText('Hàm giá trị V(b) = max_i (α_i · b) dạng lồi tuyến tính từng đoạn (PWLC)', width / 2, 25);
  };

  draw();
}

// -----------------------------------------------------------------------------
// 16. CH16: QMDP vs AMDP Active Sensing Comparison Lab
// -----------------------------------------------------------------------------
function initApproximatePOMDPSim() {
  const c = setupCanvas('sim-canvas-ch16');
  if (!c) return;
  const { ctx, width, height } = c;

  const draw = () => {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Goal and beacon
    ctx.fillStyle = '#059669';
    ctx.beginPath(); ctx.arc(width - 80, height / 2, 12, 0, Math.PI * 2); ctx.fill();
    ctx.fillText('Đích', width - 80, height / 2 - 18);

    ctx.fillStyle = '#f59e0b';
    ctx.beginPath(); ctx.arc(width / 2, 70, 10, 0, Math.PI * 2); ctx.fill();
    ctx.fillText('Trạm phát tín hiệu (Landmark)', width / 2, 50);

    // QMDP path (straight, naive)
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(80, height / 2);
    ctx.lineTo(width - 80, height / 2);
    ctx.stroke();

    // AMDP path (detour to landmark to reduce entropy)
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(80, height / 2);
    ctx.quadraticCurveTo(width / 2, 100, width - 80, height / 2);
    ctx.stroke();

    ctx.fillStyle = '#e2e8f0';
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('─ Đỏ: QMDP (đi thẳng mù quáng) | ─ Xanh: AMDP (chủ động ghé mốc định vị giảm bất định)', 20, height - 20);
  };

  draw();
}

// -----------------------------------------------------------------------------
// 17. CH17: Autonomous Frontier Exploration Simulator
// -----------------------------------------------------------------------------
function initFrontierExplorationSim() {
  const c = setupCanvas('sim-canvas-ch17');
  if (!c) return;
  const { ctx, width, height } = c;

  let robot = { x: 120, y: height / 2 };
  let rRadius = 60;

  const draw = () => {
    // Unknown fog of war
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(0, 0, width, height);

    // Known free circle
    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.arc(robot.x, robot.y, rRadius, 0, Math.PI * 2);
    ctx.fill();

    // Frontier edge
    ctx.strokeStyle = '#34d399';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.arc(robot.x, robot.y, rRadius, 0, Math.PI * 2);
    ctx.stroke();

    // Robot
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(robot.x, robot.y, 7, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = '#ffffff';
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('Đường viền xanh: Biên giới (Frontier) ngăn giữa vùng đã khám phá và vùng ẩn', 20, 25);
  };

  const btnStep = document.getElementById('ch17-btn-explore');
  if (btnStep) {
    btnStep.onclick = () => {
      robot.x += 35;
      rRadius += 15;
      draw();
    };
  }

  draw();
}

// Global Dispatcher
window.initSimulators = function() {
  initBayesInferenceSim();
  initGridBayes1DSim();
  initNonlinearGaussianSim();
  initParticleResamplingSim();
  initBananaMotionSim();
  initBeamVsLikelihoodSim();
  initEKFLocalizationSim();
  initAMCLKidnapSim();
  initOccupancyGridSim();
  initEKFSLAMSim();
  initGraphSLAMSim();
  initSEIFSLAMSim();
  initFastSLAMSim();
  initMDPValueIterationSim();
  initPOMDPBeliefSim();
  initApproximatePOMDPSim();
  initFrontierExplorationSim();
};

document.addEventListener('DOMContentLoaded', () => {
  window.initSimulators();
});
