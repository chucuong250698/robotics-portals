/**
 * Particle Filter Made Simple: A Step-by-Step Beginner-friendly Guide
 * (Sahil Rajesh Dhayalkar - Arizona State University)
 * 5 Interactive Canvas 2D 60 FPS Simulators Suite
 */

// Helper: Setup High-DPI Canvas
function setupCanvas(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return null;
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  const width = rect.width || canvas.width || 760;
  const height = rect.height || canvas.height || 360;
  
  canvas.width = width * dpr;
  canvas.height = height * dpr;
  ctx.scale(dpr, dpr);
  return { canvas, ctx, width, height };
}

// Gaussian Random Generator (Box-Muller)
function randomGaussian(mean = 0, std = 1) {
  let u = 0, v = 0;
  while (u === 0) u = Math.random();
  while (v === 0) v = Math.random();
  const num = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
  return num * std + mean;
}

// Gaussian PDF evaluation
function gaussianPdf(x, mean, variance) {
  const std = Math.sqrt(variance);
  const denom = std * Math.sqrt(2 * Math.PI);
  const num = Math.exp(-Math.pow(x - mean, 2) / (2 * variance));
  return num / (denom || 1e-6);
}

// -----------------------------------------------------------------------------
// 1. CH01: Kalman Failure vs Multimodal Particle Cloud
// -----------------------------------------------------------------------------
function initGaussianVsMultimodalSim() {
  const c = setupCanvas('sim-canvas-ch01');
  if (!c) return;
  const { canvas, ctx } = c;

  let width = canvas.width / (window.devicePixelRatio || 1);
  let height = canvas.height / (window.devicePixelRatio || 1);

  const doors = [180, 480]; // Two symmetric doors
  let robotX = 180;
  let N = 160;
  let particles = [];
  let weights = [];

  // Kalman filter single Gaussian belief
  let kalmanMean = 330; // Starts in the middle
  let kalmanVar = 6400; // Large uncertainty

  const initParticles = () => {
    particles = [];
    weights = [];
    for (let i = 0; i < N; i++) {
      // 50% around door 1, 50% around door 2 initially
      const base = Math.random() < 0.5 ? doors[0] : doors[1];
      particles.push(base + randomGaussian(0, 35));
      weights.push(1 / N);
    }
    kalmanMean = (doors[0] + doors[1]) / 2;
    kalmanVar = 8000;
  };
  initParticles();

  const updateMeasurement = () => {
    // Robot senses it is at a door
    // Kalman tries to update with z=0 (distance to door), but which door?
    // Kalman takes the average observation, trapping mean between doors
    kalmanVar = 1 / (1 / kalmanVar + 1 / 400);
    // Particle Filter weights particles near either door
    let totalW = 0;
    for (let i = 0; i < N; i++) {
      const p = particles[i];
      const likelihood = Math.max(
        gaussianPdf(p, doors[0], 900),
        gaussianPdf(p, doors[1], 900)
      );
      weights[i] = likelihood;
      totalW += likelihood;
    }
    if (totalW > 0) {
      for (let i = 0; i < N; i++) weights[i] /= totalW;
    }

    // Systematic resample
    const newParticles = [];
    const step = 1 / N;
    let r = Math.random() * step;
    let cSum = weights[0];
    let idx = 0;
    for (let m = 0; m < N; m++) {
      const u = r + m * step;
      while (u > cSum && idx < N - 1) {
        idx++;
        cSum += weights[idx];
      }
      newParticles.push(particles[idx] + randomGaussian(0, 5));
    }
    particles = newParticles;
    for (let i = 0; i < N; i++) weights[i] = 1 / N;

    render();
  };

  const moveRobot = (dx = 40) => {
    robotX = (robotX + dx) % (width - 80) + 40;
    // Kalman motion update
    kalmanMean += dx;
    kalmanVar += 400; // Process noise
    // Particle motion update
    for (let i = 0; i < N; i++) {
      particles[i] = (particles[i] + dx + randomGaussian(0, 15)) % (width - 80) + 40;
    }
    render();
  };

  const render = () => {
    width = canvas.width / (window.devicePixelRatio || 1);
    height = canvas.height / (window.devicePixelRatio || 1);

    ctx.clearRect(0, 0, width, height);

    // Background
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Grid lines
    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    for (let x = 0; x < width; x += 50) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
    }
    for (let y = 0; y < height; y += 40) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
    }

    // Ground line
    const groundY = height - 60;
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(30, groundY);
    ctx.lineTo(width - 30, groundY);
    ctx.stroke();

    // Draw Doors (Landmarks)
    doors.forEach((dx, idx) => {
      ctx.fillStyle = '#334155';
      ctx.fillRect(dx - 20, groundY - 70, 40, 70);
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.strokeRect(dx - 20, groundY - 70, 40, 70);

      ctx.fillStyle = '#38bdf8';
      ctx.font = '12px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(`Cửa ${idx + 1} (${dx}m)`, dx, groundY - 80);
    });

    // Draw True Robot
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.arc(robotX, groundY - 18, 16, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#fbbf24';
    ctx.lineWidth = 3;
    ctx.stroke();
    ctx.fillStyle = '#0f172a';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('ROBOT', robotX, groundY - 14);

    // Draw Particles (Cloud on ground & KDE above)
    ctx.fillStyle = 'rgba(16, 185, 129, 0.7)';
    for (let i = 0; i < N; i++) {
      const px = particles[i];
      const py = groundY - 15 + (i % 5) * 5 - 10;
      ctx.beginPath();
      ctx.arc(px, py, 3.5, 0, Math.PI * 2);
      ctx.fill();
    }

    // Draw Kalman Filter Gaussian Curve (Red)
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const kStd = Math.sqrt(kalmanVar);
    for (let x = 30; x < width - 30; x += 4) {
      const pdf = gaussianPdf(x, kalmanMean, kalmanVar);
      const y = (groundY - 100) - pdf * 8000;
      if (x === 30) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Kalman mean line & label
    ctx.strokeStyle = 'rgba(239, 68, 68, 0.6)';
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(kalmanMean, groundY - 100);
    ctx.lineTo(kalmanMean, groundY);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = '#ef4444';
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(`Kalman μ = ${kalmanMean.toFixed(0)}m (Thất bại: Đỉnh nằm giữa 2 cửa!)`, kalmanMean, groundY - 175);

    // Particle Empirical Density Curve (Emerald)
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    const bw = 25;
    for (let x = 30; x < width - 30; x += 4) {
      let kde = 0;
      for (let i = 0; i < N; i++) {
        kde += gaussianPdf(x, particles[i], bw * bw);
      }
      kde /= N;
      const y = (groundY - 100) - kde * 8000;
      if (x === 30) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Legends & Telemetry Box
    ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
    ctx.fillRect(40, 20, 360, 65);
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 1;
    ctx.strokeRect(40, 20, 360, 65);

    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('— Phân bố Gauss (Kalman): Ép buộc đơn đỉnh, không bắt được 2 cửa', 50, 40);
    ctx.fillStyle = '#10b981';
    ctx.fillText(`— Đám mây hạt ($N=${N}$): Bắt trọn 2 đỉnh xác suất (Multimodal)`, 50, 58);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`● Robot thật: x = ${robotX.toFixed(1)}m | Phát hiện cửa đối xứng`, 50, 75);
  };

  render();

  // Attach controls
  const btnMeasure = document.getElementById('btn-measure-ch01');
  const btnMove = document.getElementById('btn-move-ch01');
  const btnReset = document.getElementById('btn-reset-ch01');

  if (btnMeasure) btnMeasure.onclick = updateMeasurement;
  if (btnMove) btnMove.onclick = () => moveRobot(50);
  if (btnReset) btnReset.onclick = () => { initParticles(); robotX = 180; render(); };
}

// -----------------------------------------------------------------------------
// 2. CH02: Monte Carlo Histogram in Motion & Nonlinear Transformation
// -----------------------------------------------------------------------------
function initMonteCarloHistogramSim() {
  const c = setupCanvas('sim-canvas-ch02');
  if (!c) return;
  const { canvas, ctx } = c;

  let width = canvas.width / (window.devicePixelRatio || 1);
  let height = canvas.height / (window.devicePixelRatio || 1);

  let N = 350;
  let particles = [];
  let isRunning = false;
  let animId = null;
  let timeStep = 0;

  const initSamples = () => {
    particles = [];
    timeStep = 0;
    for (let i = 0; i < N; i++) {
      particles.push(randomGaussian(0, 1.8));
    }
  };
  initSamples();

  const stepNonlinear = () => {
    timeStep++;
    // Nonlinear system: x_k = 0.5 * x_{k-1} + 25 * x_{k-1} / (1 + x_{k-1}^2) + 8 * cos(1.2 * t) + noise
    const t = timeStep * 0.2;
    for (let i = 0; i < N; i++) {
      const x = particles[i];
      const fx = 0.5 * x + (2.5 * x) / (1 + x * x) + 1.2 * Math.cos(t);
      particles[i] = fx + randomGaussian(0, 0.6);
    }
  };

  const render = () => {
    width = canvas.width / (window.devicePixelRatio || 1);
    height = canvas.height / (window.devicePixelRatio || 1);

    ctx.clearRect(0, 0, width, height);

    // Background
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Coordinates mapping
    const minX = -12;
    const maxX = 12;
    const toPx = (v) => 60 + ((v - minX) / (maxX - minX)) * (width - 120);

    // Grid
    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    for (let v = minX; v <= maxX; v += 2) {
      const px = toPx(v);
      ctx.beginPath(); ctx.moveTo(px, 30); ctx.lineTo(px, height - 40); ctx.stroke();
      ctx.fillStyle = '#64748b';
      ctx.font = '10px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(v.toString(), px, height - 25);
    }

    // Top: Particles Dots Cloud
    const topY = 75;
    ctx.fillStyle = '#94a3b8';
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('Đám mây mẫu ngẫu nhiên (Sample Cloud):', 60, 45);

    ctx.fillStyle = 'rgba(56, 189, 248, 0.7)';
    for (let i = 0; i < N; i++) {
      const px = toPx(particles[i]);
      const py = topY + (i % 6) * 6 - 15;
      ctx.beginPath();
      ctx.arc(px, py, 3, 0, Math.PI * 2);
      ctx.fill();
    }

    // Bottom: Dynamic Probability Histogram
    const numBins = 30;
    const bins = new Array(numBins).fill(0);
    const binWidth = (maxX - minX) / numBins;

    let sum = 0, sumSq = 0;
    particles.forEach(p => {
      sum += p;
      sumSq += p * p;
      const bIdx = Math.floor((p - minX) / binWidth);
      if (bIdx >= 0 && bIdx < numBins) bins[bIdx]++;
    });

    const mean = sum / N;
    const variance = (sumSq / N) - (mean * mean);
    const maxBinCount = Math.max(...bins, 1);
    const histBaseY = height - 50;
    const histMaxHeight = 140;

    ctx.fillStyle = '#94a3b8';
    ctx.fillText('Histogram xác suất động p(x_k):', 60, 135);

    // Draw Bins
    for (let b = 0; b < numBins; b++) {
      const bLeftVal = minX + b * binWidth;
      const bRightVal = bLeftVal + binWidth;
      const pxLeft = toPx(bLeftVal);
      const pxRight = toPx(bRightVal);
      const barW = Math.max(1, pxRight - pxLeft - 1);
      const h = (bins[b] / maxBinCount) * histMaxHeight;

      const grad = ctx.createLinearGradient(0, histBaseY - h, 0, histBaseY);
      grad.addColorStop(0, '#10b981');
      grad.addColorStop(1, '#064e3b');
      ctx.fillStyle = grad;
      ctx.fillRect(pxLeft, histBaseY - h, barW, h);

      ctx.strokeStyle = '#34d399';
      ctx.lineWidth = 1;
      ctx.strokeRect(pxLeft, histBaseY - h, barW, h);
    }

    // Mean Marker
    const pxMean = toPx(mean);
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2.5;
    ctx.setLineDash([5, 4]);
    ctx.beginPath();
    ctx.moveTo(pxMean, 40);
    ctx.lineTo(pxMean, histBaseY);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = '#f59e0b';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(`Trung bình mẫu E[x] = ${mean.toFixed(2)}`, pxMean, 35);

    // Metric Summary HUD
    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
    ctx.fillRect(width - 240, 20, 210, 80);
    ctx.strokeStyle = '#334155';
    ctx.strokeRect(width - 240, 20, 210, 80);

    ctx.font = '11px JetBrains Mono, monospace';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#38bdf8';
    ctx.fillText(`Số mẫu N:       ${N}`, width - 230, 40);
    ctx.fillStyle = '#10b981';
    ctx.fillText(`Kỳ vọng E[x]:   ${mean.toFixed(3)}`, width - 230, 58);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`Phương sai s²:  ${variance.toFixed(3)}`, width - 230, 76);
    ctx.fillStyle = '#94a3b8';
    ctx.fillText(`Bước thời gian: k = ${timeStep}`, width - 230, 94);
  };

  render();

  const loop = () => {
    if (isRunning) {
      stepNonlinear();
      render();
      animId = setTimeout(loop, 120);
    }
  };

  const btnStep = document.getElementById('btn-step-ch02');
  const btnToggle = document.getElementById('btn-toggle-ch02');
  const btnReset = document.getElementById('btn-reset-ch02');
  const sliderN = document.getElementById('slider-n-ch02');
  const labelN = document.getElementById('label-n-ch02');

  if (btnStep) btnStep.onclick = () => { stepNonlinear(); render(); };
  if (btnToggle) {
    btnToggle.onclick = () => {
      isRunning = !isRunning;
      btnToggle.textContent = isRunning ? 'Tạm dừng (Pause)' : 'Chạy liên tục (Play)';
      if (isRunning) loop();
    };
  }
  if (btnReset) {
    btnReset.onclick = () => {
      isRunning = false;
      if (btnToggle) btnToggle.textContent = 'Chạy liên tục (Play)';
      initSamples();
      render();
    };
  }
  if (sliderN) {
    sliderN.oninput = (e) => {
      N = parseInt(e.target.value);
      if (labelN) labelN.textContent = N;
      initSamples();
      render();
    };
  }
}

// -----------------------------------------------------------------------------
// 3. CH03: Degeneracy, Neff & Systematic Resampling Roulette
// -----------------------------------------------------------------------------
function initSIRDegeneracySim() {
  const c = setupCanvas('sim-canvas-ch03');
  if (!c) return;
  const { canvas, ctx } = c;

  let width = canvas.width / (window.devicePixelRatio || 1);
  let height = canvas.height / (window.devicePixelRatio || 1);

  const N = 16;
  let weights = new Array(N).fill(1 / N);
  let stepCount = 0;
  let isResampled = true;
  let systematicPointers = [];

  const updateWeights = () => {
    stepCount++;
    isResampled = false;
    systematicPointers = [];

    // Simulate measurement update without resampling -> creates heavy degeneracy!
    // Some particles are closer to sensor reading, their weight explodes
    let totalW = 0;
    const dominantIndex = (stepCount * 3) % N;
    for (let i = 0; i < N; i++) {
      const dist = Math.abs(i - dominantIndex);
      const factor = Math.exp(-dist * 1.6) * (0.8 + Math.random() * 0.4);
      weights[i] = weights[i] * factor;
      totalW += weights[i];
    }
    for (let i = 0; i < N; i++) weights[i] /= totalW;

    render();
  };

  const runSystematicResampling = () => {
    isResampled = true;
    systematicPointers = [];

    // Systematic resampling algorithm
    const u0 = Math.random() / N;
    for (let j = 0; j < N; j++) {
      systematicPointers.push(u0 + j / N);
    }

    // Cumulative sum
    const cSum = [];
    let acc = 0;
    for (let i = 0; i < N; i++) {
      acc += weights[i];
      cSum.push(acc);
    }

    // Count offspring
    const offspring = new Array(N).fill(0);
    let i = 0;
    for (let j = 0; j < N; j++) {
      const u = systematicPointers[j];
      while (u > cSum[i] && i < N - 1) i++;
      offspring[i]++;
    }

    // Reset weights to uniform 1/N
    weights.fill(1 / N);
    render(offspring);
  };

  const render = (offspring = null) => {
    width = canvas.width / (window.devicePixelRatio || 1);
    height = canvas.height / (window.devicePixelRatio || 1);

    ctx.clearRect(0, 0, width, height);

    // Background
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Compute Neff
    let sumSq = 0;
    weights.forEach(w => sumSq += w * w);
    const neff = 1 / (sumSq || 1e-6);
    const threshold = N / 2;
    const isDegenerate = neff < threshold;

    // Header & Guidance
    ctx.fillStyle = '#f8fafc';
    ctx.font = '14px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('Phân phối trọng số hạt (Particle Weight Distribution) & Thoái hóa mẫu:', 40, 35);

    // Draw Bars
    const barW = (width - 120) / N;
    const baseY = height - 90;
    const maxBarH = 140;

    for (let i = 0; i < N; i++) {
      const bx = 60 + i * barW;
      const bwVal = weights[i];
      const bh = Math.min(maxBarH, bwVal * maxBarH * 3.5);

      // Color coding: green for healthy, red/orange for spiked degenerate
      let barCol = '#38bdf8';
      if (bwVal > 0.3) barCol = '#ef4444';
      else if (bwVal > 0.15) barCol = '#f59e0b';
      else if (bwVal < 0.02) barCol = '#475569';

      ctx.fillStyle = barCol;
      ctx.fillRect(bx + 4, baseY - bh, barW - 8, bh);

      ctx.strokeStyle = '#0f172a';
      ctx.lineWidth = 1;
      ctx.strokeRect(bx + 4, baseY - bh, barW - 8, bh);

      // Label particle index
      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px JetBrains Mono, monospace';
      ctx.textAlign = 'center';
      ctx.fillText(`p${i+1}`, bx + barW / 2, baseY + 18);

      // Percentage label
      const pct = (bwVal * 100).toFixed(1);
      ctx.fillStyle = bwVal > 0.3 ? '#f87171' : '#cbd5e1';
      ctx.fillText(`${pct}%`, bx + barW / 2, baseY - bh - 6);
    }

    // Ground line
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(50, baseY);
    ctx.lineTo(width - 50, baseY);
    ctx.stroke();

    // Cumulative Roulette Bar (Bottom)
    const rouY = height - 45;
    const rouW = width - 120;
    let accW = 0;

    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('Vòng quay Systematic Resampling (Cumulative Roulette [0, 1]):', 60, rouY - 14);

    ctx.strokeStyle = '#475569';
    ctx.strokeRect(60, rouY, rouW, 18);

    for (let i = 0; i < N; i++) {
      const segW = weights[i] * rouW;
      const segX = 60 + accW * rouW;
      ctx.fillStyle = i % 2 === 0 ? '#1e293b' : '#334155';
      ctx.fillRect(segX, rouY, segW, 18);
      accW += weights[i];
    }

    // Draw systematic pointers if resampled
    if (systematicPointers.length > 0) {
      systematicPointers.forEach((u, pIdx) => {
        const px = 60 + u * rouW;
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(px, rouY - 6);
        ctx.lineTo(px, rouY + 24);
        ctx.stroke();
      });
    }

    // Telemetry & Neff Display Box
    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
    ctx.fillRect(width - 290, 15, 250, 75);
    ctx.strokeStyle = isDegenerate ? '#ef4444' : '#10b981';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(width - 290, 15, 250, 75);

    ctx.font = '12px JetBrains Mono, monospace';
    ctx.textAlign = 'left';
    ctx.fillStyle = isDegenerate ? '#f87171' : '#34d399';
    ctx.fillText(`Kích thước hiệu dụng N_eff: ${neff.toFixed(2)}`, width - 280, 35);
    ctx.fillStyle = '#94a3b8';
    ctx.fillText(`Ngưỡng Resampling (N/2):     ${threshold.toFixed(1)}`, width - 280, 52);
    ctx.fillStyle = isDegenerate ? '#fbbf24' : '#38bdf8';
    const statusText = isDegenerate ? '⚠ BỊ THOÁI HÓA (Cần Resample!)' : '✓ Mẫu phân bố đồng đều';
    ctx.fillText(`Trạng thái: ${statusText}`, width - 280, 70);
  };

  render();

  const btnUpdateW = document.getElementById('btn-update-w-ch03');
  const btnResample = document.getElementById('btn-resample-ch03');
  const btnReset = document.getElementById('btn-reset-ch03');

  if (btnUpdateW) btnUpdateW.onclick = updateWeights;
  if (btnResample) btnResample.onclick = runSystematicResampling;
  if (btnReset) {
    btnReset.onclick = () => {
      weights.fill(1 / N);
      stepCount = 0;
      isResampled = true;
      systematicPointers = [];
      render();
    };
  }
}

// -----------------------------------------------------------------------------
// 4. CH04: Live 1D Object Tracking (Step-by-step numbers, Q=1.0, R=4.0)
// -----------------------------------------------------------------------------
function init1DTrackingLiveSim() {
  const c = setupCanvas('sim-canvas-ch04');
  if (!c) return;
  const { canvas, ctx } = c;

  let width = canvas.width / (window.devicePixelRatio || 1);
  let height = canvas.height / (window.devicePixelRatio || 1);

  let N = 80;
  let Q = 1.0; // Process noise
  let R = 4.0; // Measurement noise
  let u = 0.5; // Constant control input

  let k = 0;
  let maxK = 25;
  let trueState = 0;
  let particles = [];
  let weights = [];

  let historyTrue = [0];
  let historyMeas = [0];
  let historyEst = [0];
  let historyParticles = [];

  const initTracking = () => {
    k = 0;
    trueState = 0;
    particles = [];
    weights = [];
    for (let i = 0; i < N; i++) {
      particles.push(randomGaussian(0, 1.0));
      weights.push(1 / N);
    }
    historyTrue = [trueState];
    historyMeas = [null];
    historyEst = [0];
    historyParticles = [particles.slice()];
    render();
  };
  initTracking();

  const stepFilter = () => {
    if (k >= maxK) return;
    k++;

    // 1. True system evolves: x_k = x_{k-1} + u + w_k
    trueState = trueState + u + randomGaussian(0, Math.sqrt(Q));
    historyTrue.push(trueState);

    // 2. Sensor measurement: z_k = x_k + v_k
    const z = trueState + randomGaussian(0, Math.sqrt(R));
    historyMeas.push(z);

    // 3. Prediction step for each particle: x_k^(i) = x_{k-1}^(i) + u + w_k^(i)
    for (let i = 0; i < N; i++) {
      particles[i] = particles[i] + u + randomGaussian(0, Math.sqrt(Q));
    }

    // 4. Weighting step: w_k^(i) = p(z_k | x_k^(i)) = N(z_k; x_k^(i), R)
    let totalW = 0;
    for (let i = 0; i < N; i++) {
      const p = particles[i];
      const lik = gaussianPdf(z, p, R);
      weights[i] = lik;
      totalW += lik;
    }
    for (let i = 0; i < N; i++) weights[i] /= (totalW || 1e-6);

    // 5. State estimation: \hat{x}_k = sum(w^(i) * x^(i))
    let est = 0;
    for (let i = 0; i < N; i++) est += weights[i] * particles[i];
    historyEst.push(est);

    // 6. Resampling (Systematic)
    const newP = [];
    const step = 1 / N;
    let r = Math.random() * step;
    let cSum = weights[0];
    let idx = 0;
    for (let m = 0; m < N; m++) {
      const uVal = r + m * step;
      while (uVal > cSum && idx < N - 1) {
        idx++;
        cSum += weights[idx];
      }
      newP.push(particles[idx]);
    }
    particles = newP;
    weights.fill(1 / N);
    historyParticles.push(particles.slice());

    render();
  };

  const render = () => {
    width = canvas.width / (window.devicePixelRatio || 1);
    height = canvas.height / (window.devicePixelRatio || 1);

    ctx.clearRect(0, 0, width, height);

    // Background
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Margins
    const mLeft = 60, mRight = 30, mTop = 40, mBottom = 40;
    const plotW = width - mLeft - mRight;
    const plotH = height - mTop - mBottom;

    // Scale
    const minVal = -2;
    const maxVal = Math.max(16, ...historyTrue, ...historyEst) + 2;
    const toPxX = (step) => mLeft + (step / maxK) * plotW;
    const toPxY = (val) => mTop + plotH - ((val - minVal) / (maxVal - minVal)) * plotH;

    // Grid lines
    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    for (let s = 0; s <= maxK; s += 5) {
      const px = toPxX(s);
      ctx.beginPath(); ctx.moveTo(px, mTop); ctx.lineTo(px, mTop + plotH); ctx.stroke();
      ctx.fillStyle = '#64748b';
      ctx.font = '10px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(`k=${s}`, px, mTop + plotH + 18);
    }

    for (let v = 0; v <= maxVal; v += 4) {
      const py = toPxY(v);
      ctx.beginPath(); ctx.moveTo(mLeft, py); ctx.lineTo(mLeft + plotW, py); ctx.stroke();
      ctx.fillStyle = '#64748b';
      ctx.font = '10px Inter, sans-serif';
      ctx.textAlign = 'right';
      ctx.fillText(v.toString(), mLeft - 8, py + 3);
    }

    // 1. Draw Particle Cloud across steps
    for (let s = 0; s <= k; s++) {
      const pList = historyParticles[s];
      if (!pList) continue;
      const px = toPxX(s);
      ctx.fillStyle = 'rgba(56, 189, 248, 0.25)';
      pList.forEach(pVal => {
        const py = toPxY(pVal);
        ctx.beginPath();
        ctx.arc(px, py, 2.5, 0, Math.PI * 2);
        ctx.fill();
      });
    }

    // 2. Draw Measurements (Red x)
    for (let s = 1; s <= k; s++) {
      const z = historyMeas[s];
      if (z === null) continue;
      const px = toPxX(s);
      const py = toPxY(z);
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(px - 4, py - 4); ctx.lineTo(px + 4, py + 4);
      ctx.moveTo(px + 4, py - 4); ctx.lineTo(px - 4, py + 4);
      ctx.stroke();
    }

    // 3. Draw True State (Black / White line)
    ctx.strokeStyle = '#f8fafc';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let s = 0; s <= k; s++) {
      const px = toPxX(s);
      const py = toPxY(historyTrue[s]);
      if (s === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // 4. Draw Estimated State (Bold Emerald line)
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 3;
    ctx.beginPath();
    for (let s = 0; s <= k; s++) {
      const px = toPxX(s);
      const py = toPxY(historyEst[s]);
      if (s === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Legends Box
    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
    ctx.fillRect(mLeft + 15, mTop + 10, 320, 60);
    ctx.strokeStyle = '#334155';
    ctx.strokeRect(mLeft + 15, mTop + 10, 320, 60);

    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#f8fafc';
    ctx.fillText('— Vị trí thật x_k', mLeft + 25, mTop + 26);
    ctx.fillStyle = '#ef4444';
    ctx.fillText('✕ Phép đo cảm biến có nhiễu z_k', mLeft + 140, mTop + 26);
    ctx.fillStyle = '#10b981';
    ctx.fillText('— Ước lượng Particle Filter x̂_k', mLeft + 25, mTop + 45);
    ctx.fillStyle = '#38bdf8';
    ctx.fillText('● Đám mây hạt (Particle Cloud)', mLeft + 185, mTop + 45);

    // Current Values HUD
    const curTrue = historyTrue[k].toFixed(2);
    const curMeas = historyMeas[k] !== null ? historyMeas[k].toFixed(2) : 'N/A';
    const curEst = historyEst[k].toFixed(2);
    const curErr = Math.abs(historyTrue[k] - historyEst[k]).toFixed(2);

    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
    ctx.fillRect(width - 240, mTop + 10, 200, 85);
    ctx.strokeStyle = '#10b981';
    ctx.strokeRect(width - 240, mTop + 10, 200, 85);

    ctx.font = '11px JetBrains Mono, monospace';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText(`Bước k:       ${k} / ${maxK}`, width - 230, mTop + 28);
    ctx.fillStyle = '#f8fafc';
    ctx.fillText(`Vị trí thật:  ${curTrue}`, width - 230, mTop + 45);
    ctx.fillStyle = '#ef4444';
    ctx.fillText(`Cảm biến z:   ${curMeas}`, width - 230, mTop + 62);
    ctx.fillStyle = '#10b981';
    ctx.fillText(`Ước lượng x̂:  ${curEst}`, width - 230, mTop + 79);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`Sai số |e|:   ${curErr}`, width - 230, mTop + 96);
  };

  const btnStep = document.getElementById('btn-step-ch04');
  const btnReset = document.getElementById('btn-reset-ch04');
  const sliderR = document.getElementById('slider-r-ch04');
  const labelR = document.getElementById('label-r-ch04');

  if (btnStep) btnStep.onclick = stepFilter;
  if (btnReset) btnReset.onclick = initTracking;
  if (sliderR) {
    sliderR.oninput = (e) => {
      R = parseFloat(e.target.value);
      if (labelR) labelR.textContent = R.toFixed(1);
    };
  }
}

// -----------------------------------------------------------------------------
// 5. CH05: 2D Robot Localization with Kidnapped Recovery
// -----------------------------------------------------------------------------
function init2DRobotLocalizationSim() {
  const c = setupCanvas('sim-canvas-ch05');
  if (!c) return;
  const { canvas, ctx } = c;

  let width = canvas.width / (window.devicePixelRatio || 1);
  let height = canvas.height / (window.devicePixelRatio || 1);

  // 4 Distinct Landmarks
  const landmarks = [
    { x: 100, y: 70, id: 'L1', color: '#ec4899' },
    { x: 640, y: 70, id: 'L2', color: '#8b5cf6' },
    { x: 640, y: 270, id: 'L3', color: '#06b6d4' },
    { x: 100, y: 270, id: 'L4', color: '#f59e0b' }
  ];

  let N = 260;
  let robot = { x: 370, y: 170, vx: 2.2, vy: 1.2, heading: 0.5 };
  let particles = [];
  let isPatrolling = true;
  let animId = null;

  const initGlobalParticles = () => {
    particles = [];
    for (let i = 0; i < N; i++) {
      particles.push({
        x: Math.random() * (width - 120) + 60,
        y: Math.random() * (height - 100) + 50,
        weight: 1 / N
      });
    }
  };
  initGlobalParticles();

  const updateRobotMotion = () => {
    robot.x += robot.vx;
    robot.y += robot.vy;

    // Bounce off walls
    if (robot.x < 70 || robot.x > width - 70) robot.vx *= -1;
    if (robot.y < 50 || robot.y > height - 50) robot.vy *= -1;

    robot.heading = Math.atan2(robot.vy, robot.vx);
  };

  const updateFilter = () => {
    // 1. Predict particles with noisy motion model
    for (let i = 0; i < N; i++) {
      particles[i].x += robot.vx + randomGaussian(0, 1.2);
      particles[i].y += robot.vy + randomGaussian(0, 1.2);

      // Boundaries
      particles[i].x = Math.max(40, Math.min(width - 40, particles[i].x));
      particles[i].y = Math.max(30, Math.min(height - 30, particles[i].y));
    }

    // 2. Measure distances from true robot to all 4 landmarks
    const measDist = landmarks.map(lm => {
      const d = Math.hypot(robot.x - lm.x, robot.y - lm.y);
      return d + randomGaussian(0, 8.0); // 8px measurement noise
    });

    // 3. Weighting particles by likelihood
    let totalW = 0;
    const sensorVar = 144.0; // std = 12
    for (let i = 0; i < N; i++) {
      const p = particles[i];
      let pLik = 1.0;
      landmarks.forEach((lm, lIdx) => {
        const predD = Math.hypot(p.x - lm.x, p.y - lm.y);
        pLik *= gaussianPdf(measDist[lIdx], predD, sensorVar);
      });
      p.weight = pLik;
      totalW += pLik;
    }

    // Normalize
    if (totalW > 0) {
      for (let i = 0; i < N; i++) particles[i].weight /= totalW;
    } else {
      for (let i = 0; i < N; i++) particles[i].weight = 1 / N;
    }

    // 4. Low-variance Systematic Resampling
    const newParticles = [];
    const step = 1 / N;
    let r = Math.random() * step;
    let cSum = particles[0].weight;
    let idx = 0;

    for (let m = 0; m < N; m++) {
      const u = r + m * step;
      while (u > cSum && idx < N - 1) {
        idx++;
        cSum += particles[idx].weight;
      }
      // Add small jitter to avoid sample depletion
      newParticles.push({
        x: particles[idx].x + randomGaussian(0, 2.0),
        y: particles[idx].y + randomGaussian(0, 2.0),
        weight: 1 / N
      });
    }
    particles = newParticles;
  };

  const kidnapRobot = () => {
    // Teleport robot to random corner
    robot.x = Math.random() < 0.5 ? 120 : width - 120;
    robot.y = Math.random() < 0.5 ? 80 : height - 80;
    robot.vx = (Math.random() - 0.5) * 4;
    robot.vy = (Math.random() - 0.5) * 4;

    // Notice: We do NOT re-initialize particles here immediately!
    // Shows the kidnap discrepancy and recovery
    render();
  };

  const render = () => {
    width = canvas.width / (window.devicePixelRatio || 1);
    height = canvas.height / (window.devicePixelRatio || 1);

    ctx.clearRect(0, 0, width, height);

    // Arena Background
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    // Wall border
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 3;
    ctx.strokeRect(40, 30, width - 80, height - 60);

    // Grid
    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    for (let x = 40; x < width - 40; x += 50) {
      ctx.beginPath(); ctx.moveTo(x, 30); ctx.lineTo(x, height - 30); ctx.stroke();
    }
    for (let y = 30; y < height - 30; y += 50) {
      ctx.beginPath(); ctx.moveTo(40, y); ctx.lineTo(width - 40, y); ctx.stroke();
    }

    // Draw Landmarks
    landmarks.forEach(lm => {
      ctx.fillStyle = lm.color;
      ctx.beginPath();
      ctx.arc(lm.x, lm.y, 8, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(lm.id, lm.x, lm.y - 12);
    });

    // Draw Particles
    ctx.fillStyle = 'rgba(16, 185, 129, 0.65)';
    particles.forEach(p => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, 2.8, 0, Math.PI * 2);
      ctx.fill();
    });

    // Compute PF Estimate (Centroid)
    let estX = 0, estY = 0;
    particles.forEach(p => {
      estX += p.x;
      estY += p.y;
    });
    estX /= N;
    estY /= N;

    // Draw PF Estimated Pose (Cyan Diamond)
    ctx.fillStyle = '#06b6d4';
    ctx.strokeStyle = '#22d3ee';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(estX, estY - 10);
    ctx.lineTo(estX + 10, estY);
    ctx.lineTo(estX, estY + 10);
    ctx.lineTo(estX - 10, estY);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    // Draw True Robot (Orange circle with direction pointer)
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.arc(robot.x, robot.y, 11, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#fbbf24';
    ctx.lineWidth = 2.5;
    ctx.stroke();

    // Direction line
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(robot.x, robot.y);
    ctx.lineTo(robot.x + Math.cos(robot.heading) * 20, robot.y + Math.sin(robot.heading) * 20);
    ctx.stroke();

    // Sensor beams from robot to landmarks
    landmarks.forEach(lm => {
      ctx.strokeStyle = 'rgba(245, 158, 11, 0.15)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(robot.x, robot.y);
      ctx.lineTo(lm.x, lm.y);
      ctx.stroke();
    });

    // Telemetry Box
    const err = Math.hypot(robot.x - estX, robot.y - estY);
    const isConverged = err < 25;

    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
    ctx.fillRect(55, 45, 270, 95);
    ctx.strokeStyle = isConverged ? '#10b981' : '#f59e0b';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(55, 45, 270, 95);

    ctx.font = '11px JetBrains Mono, monospace';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText(`Robot thật:   (${robot.x.toFixed(1)}, ${robot.y.toFixed(1)})`, 65, 65);
    ctx.fillStyle = '#06b6d4';
    ctx.fillText(`Ước lượng PF: (${estX.toFixed(1)}, ${estY.toFixed(1)})`, 65, 83);
    ctx.fillStyle = isConverged ? '#34d399' : '#f87171';
    ctx.fillText(`Sai số vị trí: ${err.toFixed(1)} px`, 65, 101);
    ctx.fillStyle = isConverged ? '#34d399' : '#fbbf24';
    const convText = isConverged ? '✓ HỘI TỤ ĐỊNH VỊ CHÍNH XÁC' : '⏳ ĐANG PHÂN BỐ LẠI MẪU';
    ctx.fillText(`Hội tụ: ${convText}`, 65, 119);
  };

  render();

  const loop = () => {
    if (isPatrolling) {
      updateRobotMotion();
      updateFilter();
      render();
    }
    animId = requestAnimationFrame(loop);
  };
  animId = requestAnimationFrame(loop);

  const btnPatrol = document.getElementById('btn-patrol-ch05');
  const btnKidnap = document.getElementById('btn-kidnap-ch05');
  const btnReset = document.getElementById('btn-reset-ch05');

  if (btnPatrol) {
    btnPatrol.onclick = () => {
      isPatrolling = !isPatrolling;
      btnPatrol.textContent = isPatrolling ? 'Tạm dừng (Pause)' : 'Tiếp tục tuần tra (Patrol)';
    };
  }
  if (btnKidnap) btnKidnap.onclick = kidnapRobot;
  if (btnReset) btnReset.onclick = () => {
    robot.x = 370; robot.y = 170;
    initGlobalParticles();
    render();
  };
}

// -----------------------------------------------------------------------------
// Auto-initialize simulators on page load
// -----------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('sim-canvas-ch01')) initGaussianVsMultimodalSim();
  if (document.getElementById('sim-canvas-ch02')) initMonteCarloHistogramSim();
  if (document.getElementById('sim-canvas-ch03')) initSIRDegeneracySim();
  if (document.getElementById('sim-canvas-ch04')) init1DTrackingLiveSim();
  if (document.getElementById('sim-canvas-ch05')) init2DRobotLocalizationSim();
});
