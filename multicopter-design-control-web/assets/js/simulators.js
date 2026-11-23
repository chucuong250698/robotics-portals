/**
 * Multicopter Design and Control Practice (Prof. Quan Quan, Xunhua Dai, Shuai Wang - Springer)
 * 12 Interactive 60 FPS HTML5 Canvas 2D Simulators
 * 
 * Simulators List:
 *  1. initLiftEquilibriumSim       - Quadcopter Lift & Rotor Torque Equilibrium
 *  2. initPixhawkSignalFlowSim     - Pixhawk Hardware/Software Realtime Signal Flow
 *  3. initSILvsHILSimulationSim     - SIL vs HIL Closed-Loop MAVLink Simulation
 *  4. initMBDPipelineSim           - Model-Based Design 4-Phase Lifecycle
 *  5. initPropulsionDesignSim      - Motor-Propeller-Battery Matching & Thrust/Weight
 *  6. init6DoFDynamicsSim          - 6-DoF Rigid Body Dynamics & Control Allocation
 *  7. initSensorCalibrationSim     - Triaxial Sensor Calibration & Ellipsoid Fitting
 *  8. initAttitudeFilterSim        - Complementary vs Kalman/EKF Attitude Filter
 *  9. initCascadeAttitudePIDSim    - Cascade Attitude Angle & Angular Rate PID
 * 10. initPosition3DSetPointSim    - 3D Position Set-Point Control with Anti-Windup
 * 11. initFlightModeStateMachineSim - Semi-Autonomous Flight Modes & Mode Switching
 * 12. initFailsafeProtectionSim     - Emergency Failsafe State Machine & RTL Navigation
 */

// Global registry for simulators
window.MCSimulators = {};

// Helper: Get Canvas and Retina 2D Context
function setupCanvas(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return null;
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  const width = rect.width || canvas.width || 600;
  const height = rect.height || canvas.height || 350;
  
  canvas.width = width * dpr;
  canvas.height = height * dpr;
  ctx.scale(dpr, dpr);
  return { canvas, ctx, width, height };
}

// ============================================================================
// SIMULATOR 1: Quadcopter Lift & Rotor Equilibrium (Ch 01)
// ============================================================================
window.MCSimulators.initLiftEquilibriumSim = function() {
  const setup = setupCanvas('canvas-lift-equilibrium');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let rpm1 = 5000, rpm2 = 5000, rpm3 = 5000, rpm4 = 5000;
  const mass = 1.5; // kg
  const g = 9.81;
  const W = mass * g; // 14.715 N
  const kT = 1.5e-7; // N / (RPM)^2

  const sliderAll = document.getElementById('slider-ch01-all-rpm');
  const sliderPitch = document.getElementById('slider-ch01-pitch-diff');
  const sliderYaw = document.getElementById('slider-ch01-yaw-diff');

  function updateRPMs() {
    const baseRPM = sliderAll ? parseFloat(sliderAll.value) : 5000;
    const pitchDiff = sliderPitch ? parseFloat(sliderPitch.value) : 0;
    const yawDiff = sliderYaw ? parseFloat(sliderYaw.value) : 0;

    rpm1 = Math.max(1000, Math.min(9000, baseRPM - pitchDiff - yawDiff));
    rpm2 = Math.max(1000, Math.min(9000, baseRPM + pitchDiff + yawDiff));
    rpm3 = Math.max(1000, Math.min(9000, baseRPM + pitchDiff - yawDiff));
    rpm4 = Math.max(1000, Math.min(9000, baseRPM - pitchDiff + yawDiff));

    const valEl = document.getElementById('val-ch01-rpms');
    if (valEl) {
      valEl.innerText = `R1:${Math.round(rpm1)} | R2:${Math.round(rpm2)} | R3:${Math.round(rpm3)} | R4:${Math.round(rpm4)} RPM`;
    }
  }

  if (sliderAll) sliderAll.addEventListener('input', updateRPMs);
  if (sliderPitch) sliderPitch.addEventListener('input', updateRPMs);
  if (sliderYaw) sliderYaw.addEventListener('input', updateRPMs);
  updateRPMs();

  let quadAngle = 0;
  let quadY = height * 0.55;

  function render() {
    ctx.clearRect(0, 0, width, height);

    // Background Grid
    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = 1;
    for (let x = 0; x < width; x += 40) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
    }
    for (let y = 0; y < height; y += 40) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
    }

    const t1 = kT * rpm1 * rpm1;
    const t2 = kT * rpm2 * rpm2;
    const t3 = kT * rpm3 * rpm3;
    const t4 = kT * rpm4 * rpm4;
    const totalThrust = t1 + t2 + t3 + t4;
    const netForceY = totalThrust - W;

    const pitchTorque = (t2 + t3) - (t1 + t4);
    const targetAngle = Math.max(-0.4, Math.min(0.4, pitchTorque * 0.08));
    quadAngle += (targetAngle - quadAngle) * 0.1;

    const targetY = height * 0.55 - Math.max(-100, Math.min(100, netForceY * 12));
    quadY += (targetY - quadY) * 0.08;

    const cx = width / 2;
    const cy = quadY;

    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(quadAngle);

    // Draw Quadcopter Frame
    const armL = 90;
    ctx.strokeStyle = '#0284c7';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.moveTo(-armL, 0);
    ctx.lineTo(armL, 0);
    ctx.stroke();

    // Central Body
    ctx.fillStyle = '#0f172a';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(0, 0, 24, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // Center of Gravity
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.arc(0, 0, 5, 0, Math.PI * 2);
    ctx.fill();

    // Rotors & Thrust Vectors
    const rotorOffsets = [-armL, armL];
    const thrusts = [(t3 + t4) / 2, (t1 + t2) / 2];
    const rpms = [(rpm3 + rpm4) / 2, (rpm1 + rpm2) / 2];

    rotorOffsets.forEach((ox, idx) => {
      ctx.fillStyle = '#334155';
      ctx.fillRect(ox - 10, -8, 20, 16);

      const propW = 45;
      ctx.strokeStyle = idx === 0 ? '#10b981' : '#06b6d4';
      ctx.lineWidth = 3;
      const spinAngle = Date.now() * 0.001 * (rpms[idx] / 60) * Math.PI * 2;
      const propScale = Math.cos(spinAngle);
      ctx.beginPath();
      ctx.moveTo(ox - propW * propScale, -12);
      ctx.lineTo(ox + propW * propScale, -12);
      ctx.stroke();

      const arrowLen = Math.min(90, (thrusts[idx] / W) * 80);
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(ox, -16);
      ctx.lineTo(ox, -16 - arrowLen);
      ctx.stroke();

      ctx.fillStyle = '#10b981';
      ctx.beginPath();
      ctx.moveTo(ox, -20 - arrowLen);
      ctx.lineTo(ox - 5, -14 - arrowLen);
      ctx.lineTo(ox + 5, -14 - arrowLen);
      ctx.fill();

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px monospace';
      ctx.textAlign = 'center';
      ctx.fillText(`${thrusts[idx].toFixed(1)}N`, ox, -24 - arrowLen);
    });

    // Gravity Arrow
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, 55);
    ctx.stroke();
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.moveTo(0, 60); ctx.lineTo(-5, 50); ctx.lineTo(5, 50); ctx.fill();
    ctx.fillText(`W = ${W.toFixed(1)}N`, 0, 72);

    ctx.restore();

    // Telemetry HUD overlay
    ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 1;
    ctx.fillRect(15, 15, 230, 95);
    ctx.strokeRect(15, 15, 230, 95);

    ctx.fillStyle = '#f8fafc';
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText(`Tổng Lực Nâng (ΣT): ${totalThrust.toFixed(2)} N`, 25, 35);
    ctx.fillText(`Trọng Lượng (W = mg): ${W.toFixed(2)} N`, 25, 55);
    
    const accZ = (totalThrust - W) / mass;
    const accColor = accZ > 0.05 ? '#10b981' : (accZ < -0.05 ? '#ef4444' : '#f59e0b');
    ctx.fillStyle = accColor;
    const stateStr = accZ > 0.1 ? 'ĐANG BAY LÊN (Climbing)' : (accZ < -0.1 ? 'ĐANG RƠI (Descending)' : 'CÂN BẰNG LƠ LỬNG (Hovering)');
    ctx.fillText(`Gia tốc az: ${accZ.toFixed(2)} m/s²`, 25, 75);
    ctx.fillText(`Trạng thái: ${stateStr}`, 25, 95);

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 2: Pixhawk Realtime Signal Flow (Ch 02)
// ============================================================================
window.MCSimulators.initPixhawkSignalFlowSim = function() {
  const setup = setupCanvas('canvas-pixhawk-signal-flow');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let loopRate = 400; // Hz
  const sliderRate = document.getElementById('slider-ch02-rate');
  if (sliderRate) {
    sliderRate.addEventListener('input', (e) => {
      loopRate = parseInt(e.target.value);
      const valEl = document.getElementById('val-ch02-rate');
      if (valEl) valEl.innerText = `${loopRate} Hz (${(1000/loopRate).toFixed(2)} ms)`;
    });
  }

  let packets = [];
  let lastTime = Date.now();

  function render() {
    ctx.clearRect(0, 0, width, height);

    const nodes = [
      { id: 'rc', name: 'RC Transmitter\n(SBUS / PPM)', x: width * 0.12, y: height * 0.35, color: '#f59e0b' },
      { id: 'fmu', name: 'Pixhawk FMU\n(STM32F4/F7 Cortex-M4)', x: width * 0.5, y: height * 0.35, color: '#0284c7' },
      { id: 'esc', name: '4x ESC & BLDC\n(DShot / PWM 400Hz)', x: width * 0.88, y: height * 0.35, color: '#10b981' },
      { id: 'imu', name: 'SPI IMU / Baro\n(ICM-20689, MS5611)', x: width * 0.5, y: height * 0.82, color: '#8b5cf6' }
    ];

    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 4;
    ctx.beginPath(); ctx.moveTo(nodes[0].x, nodes[0].y); ctx.lineTo(nodes[1].x, nodes[1].y); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(nodes[1].x, nodes[1].y); ctx.lineTo(nodes[2].x, nodes[2].y); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(nodes[3].x, nodes[3].y); ctx.lineTo(nodes[1].x, nodes[1].y); ctx.stroke();

    const now = Date.now();
    if (now - lastTime > (1000 / loopRate) * 20) {
      lastTime = now;
      packets.push({ from: 0, to: 1, prog: 0, color: '#f59e0b' });
      packets.push({ from: 3, to: 1, prog: 0, color: '#8b5cf6' });
    }

    for (let i = packets.length - 1; i >= 0; i--) {
      const p = packets[i];
      p.prog += 0.025;
      if (p.prog >= 1) {
        if (p.to === 1 && p.from !== 1) {
          packets.push({ from: 1, to: 2, prog: 0, color: '#10b981' });
        }
        packets.splice(i, 1);
        continue;
      }
      const nFrom = nodes[p.from];
      const nTo = nodes[p.to];
      const px = nFrom.x + (nTo.x - nFrom.x) * p.prog;
      const py = nFrom.y + (nTo.y - nFrom.y) * p.prog;

      ctx.fillStyle = p.color;
      ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();
    }

    nodes.forEach(n => {
      const nw = 120, nh = 65;
      ctx.fillStyle = '#0f172a'; ctx.strokeStyle = n.color; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.roundRect(n.x - nw/2, n.y - nh/2, nw, nh, 8); ctx.fill(); ctx.stroke();

      ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 11px Inter, sans-serif'; ctx.textAlign = 'center';
      const lines = n.name.split('\n');
      lines.forEach((line, li) => {
        ctx.fillText(line, n.x, n.y - 8 + li * 16);
      });
    });

    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)'; ctx.strokeStyle = '#334155'; ctx.lineWidth = 1;
    ctx.fillRect(15, 15, 220, 60); ctx.strokeRect(15, 15, 220, 60);
    ctx.fillStyle = '#38bdf8'; ctx.font = '12px Inter, sans-serif'; ctx.textAlign = 'left';
    ctx.fillText(`Chu kỳ điều khiển: ${(1000/loopRate).toFixed(2)} ms`, 25, 35);
    ctx.fillText(`Tần số ngắt FMU: ${loopRate} Hz`, 25, 55);

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 3: SIL vs HIL Simulation Platform (Ch 03)
// ============================================================================
window.MCSimulators.initSILvsHILSimulationSim = function() {
  const setup = setupCanvas('canvas-sil-hil-sim');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let mode = 'hil';
  const btnSil = document.getElementById('btn-ch03-mode-sil');
  const btnHil = document.getElementById('btn-ch03-mode-hil');

  if (btnSil && btnHil) {
    btnSil.addEventListener('click', () => { mode = 'sil'; btnSil.className = 'btn btn-primary'; btnHil.className = 'btn btn-secondary'; });
    btnHil.addEventListener('click', () => { mode = 'hil'; btnHil.className = 'btn btn-primary'; btnSil.className = 'btn btn-secondary'; });
  }

  let simTime = 0;
  function render() {
    simTime += 0.02;
    ctx.clearRect(0, 0, width, height);

    const hostX = width * 0.25, hostY = height * 0.5;
    const targetX = width * 0.75, targetY = height * 0.5;

    // Host Box
    ctx.fillStyle = '#0f172a'; ctx.strokeStyle = '#0284c7'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.roundRect(hostX - 110, hostY - 80, 220, 160, 10); ctx.fill(); ctx.stroke();
    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 13px Inter, sans-serif'; ctx.textAlign = 'center';
    ctx.fillText('MÁY TÍNH TRẠM (PC)', hostX, hostY - 55);
    ctx.font = '11px monospace'; ctx.fillStyle = '#94a3b8';
    ctx.fillText('• Simulink Flight Model', hostX, hostY - 30);
    ctx.fillText('• CopterSim Physics 60FPS', hostX, hostY - 10);
    ctx.fillText('• 3DDisplay / FlightGear', hostX, hostY + 10);
    ctx.fillText(mode === 'sil' ? '• Simulink Controller (SIL)' : '• MAVLink UDP Gateway', hostX, hostY + 30);

    // Target Box
    ctx.fillStyle = '#0f172a'; ctx.strokeStyle = mode === 'hil' ? '#10b981' : '#64748b'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.roundRect(targetX - 110, targetY - 80, 220, 160, 10); ctx.fill(); ctx.stroke();
    ctx.fillStyle = mode === 'hil' ? '#34d399' : '#94a3b8'; ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText(mode === 'hil' ? 'PHẦN CỨNG THẬT (PIXHAWK)' : 'MÔ HÌNH ẢO (VIRTUAL)', targetX, targetY - 55);
    ctx.font = '11px monospace'; ctx.fillStyle = '#94a3b8';
    if (mode === 'hil') {
      ctx.fillText('• STM32F4 FMU Bộ Vi Xử Lý', targetX, targetY - 30);
      ctx.fillText('• PX4 Realtime Firmware', targetX, targetY - 10);
      ctx.fillText('• Cảm biến HIL_SENSOR', targetX, targetY + 10);
      ctx.fillText('• Điều khiển HIL_ACTUATOR', targetX, targetY + 30);
    } else {
      ctx.fillText('• Thuần túy tính toán số', targetX, targetY - 30);
      ctx.fillText('• Bỏ qua trễ truyền thông', targetX, targetY - 10);
      ctx.fillText('• Đồng hồ mô phỏng ảo', targetX, targetY + 10);
      ctx.fillText('• Chưa kiểm chứng nhúng', targetX, targetY + 30);
    }

    ctx.strokeStyle = mode === 'hil' ? '#f59e0b' : '#3b82f6';
    ctx.lineWidth = 3; ctx.setLineDash([6, 4]);
    ctx.beginPath(); ctx.moveTo(hostX + 110, hostY - 20); ctx.lineTo(targetX - 110, targetY - 20); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(targetX - 110, hostY + 20); ctx.lineTo(hostX + 110, targetY + 20); ctx.stroke();
    ctx.setLineDash([]);

    const pktProg = (simTime * 2) % 1;
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath(); ctx.arc((hostX + 110) + (targetX - hostX - 220) * pktProg, hostY - 20, 5, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#10b981';
    ctx.beginPath(); ctx.arc((targetX - 110) - (targetX - hostX - 220) * pktProg, hostY + 20, 5, 0, Math.PI * 2); ctx.fill();

    ctx.fillStyle = mode === 'hil' ? 'rgba(16, 185, 129, 0.2)' : 'rgba(59, 130, 246, 0.2)';
    ctx.strokeStyle = mode === 'hil' ? '#10b981' : '#3b82f6';
    ctx.lineWidth = 1;
    ctx.fillRect(width / 2 - 140, 20, 280, 40); ctx.strokeRect(width / 2 - 140, 20, 280, 40);
    ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText(mode === 'hil' ? 'CHẾ ĐỘ: HIL (Hardware-In-The-Loop)' : 'CHẾ ĐỘ: SIL (Software-In-The-Loop)', width / 2, 45);

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 4: MBD 4-Phase Lifecycle Simulator (Ch 04)
// ============================================================================
window.MCSimulators.initMBDPipelineSim = function() {
  const setup = setupCanvas('canvas-mbd-pipeline');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let currentPhase = 1;
  const btnNext = document.getElementById('btn-ch04-next-phase');
  if (btnNext) {
    btnNext.addEventListener('click', () => {
      currentPhase = (currentPhase % 4) + 1;
      const lbl = document.getElementById('val-ch04-phase');
      if (lbl) lbl.innerText = `Pha ${currentPhase}/4`;
    });
  }

  const phases = [
    { num: 1, title: 'SIL Mô Phỏng Thuần', err: 0.05, color: '#38bdf8' },
    { num: 2, title: 'Sinh Mã C/C++ Tự Động', err: 0.08, color: '#818cf8' },
    { num: 3, title: 'HIL Thử Nghiệm Phần Cứng', err: 0.18, color: '#f59e0b' },
    { num: 4, title: 'Bay Thật Thực Địa (Flight)', err: 0.25, color: '#10b981' }
  ];

  let simTime = 0;
  function render() {
    simTime += 0.03;
    ctx.clearRect(0, 0, width, height);

    const stepW = (width - 80) / 4;
    phases.forEach((p, idx) => {
      const sx = 40 + idx * stepW;
      const sy = 30;
      const isAct = p.num === currentPhase;

      ctx.fillStyle = isAct ? 'rgba(2, 132, 199, 0.25)' : '#0f172a';
      ctx.strokeStyle = isAct ? p.color : '#334155';
      ctx.lineWidth = isAct ? 2 : 1;
      ctx.beginPath(); ctx.roundRect(sx + 5, sy, stepW - 10, 80, 8); ctx.fill(); ctx.stroke();

      ctx.fillStyle = p.color; ctx.font = 'bold 12px Inter, sans-serif'; ctx.textAlign = 'center';
      ctx.fillText(`PHA ${p.num}`, sx + stepW / 2, sy + 25);
      ctx.fillStyle = '#f8fafc'; ctx.font = '10px Inter, sans-serif';
      ctx.fillText(p.title, sx + stepW / 2, sy + 45);
      ctx.fillStyle = '#94a3b8';
      ctx.fillText(`Sai lệch: ±${(p.err * 100).toFixed(0)}%`, sx + stepW / 2, sy + 65);
    });

    const graphX = 40, graphY = 135, graphW = width - 80, graphH = height - 160;
    ctx.fillStyle = '#0f172a'; ctx.strokeStyle = '#334155'; ctx.lineWidth = 1;
    ctx.fillRect(graphX, graphY, graphW, graphH); ctx.strokeRect(graphX, graphY, graphW, graphH);

    const targetY = graphY + graphH * 0.3;
    ctx.strokeStyle = '#ef4444'; ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(graphX, targetY); ctx.lineTo(graphX + graphW, targetY); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = '#ef4444'; ctx.font = '10px monospace'; ctx.textAlign = 'left';
    ctx.fillText('Mục tiêu θd = 10°', graphX + 10, targetY - 6);

    ctx.strokeStyle = phases[currentPhase - 1].color; ctx.lineWidth = 2;
    ctx.beginPath();
    const noiseAmp = phases[currentPhase - 1].err * 15;
    for (let x = 0; x < graphW; x++) {
      const t = x * 0.05;
      const baseResponse = 1 - Math.exp(-t * 1.5) * Math.cos(t * 3);
      const noise = Math.sin(t * 18 + simTime * 5) * (x > 50 ? noiseAmp : 0);
      const yVal = targetY + (1 - baseResponse) * 60 + noise;
      if (x === 0) ctx.moveTo(graphX + x, yVal); else ctx.lineTo(graphX + x, yVal);
    }
    ctx.stroke();

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 5: Propulsion System Design & Thrust/Weight (Ch 05)
// ============================================================================
window.MCSimulators.initPropulsionDesignSim = function() {
  const setup = setupCanvas('canvas-propulsion-design');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let massKg = 1.6;
  let kvRPM = 920;
  let propDiamIn = 10;
  let cells = 4;
  let batMah = 4500;

  const sliderMass = document.getElementById('slider-ch05-mass');
  const sliderKv = document.getElementById('slider-ch05-kv');
  const sliderProp = document.getElementById('slider-ch05-prop');
  const selBattery = document.getElementById('select-ch05-battery');

  function updateParams() {
    if (sliderMass) massKg = parseFloat(sliderMass.value);
    if (sliderKv) kvRPM = parseFloat(sliderKv.value);
    if (sliderProp) propDiamIn = parseFloat(sliderProp.value);
    if (selBattery) cells = parseInt(selBattery.value);

    const valEl = document.getElementById('val-ch05-specs');
    if (valEl) {
      valEl.innerText = `Khối lượng: ${massKg.toFixed(1)}kg | Động cơ: ${kvRPM}KV | Cánh: ${propDiamIn}\" | Pin: ${cells}S (${(cells*3.7).toFixed(1)}V)`;
    }
  }

  if (sliderMass) sliderMass.addEventListener('input', updateParams);
  if (sliderKv) sliderKv.addEventListener('input', updateParams);
  if (sliderProp) sliderProp.addEventListener('input', updateParams);
  if (selBattery) selBattery.addEventListener('change', updateParams);
  updateParams();

  function render() {
    ctx.clearRect(0, 0, width, height);

    const voltage = cells * 3.7;
    const maxRPM = kvRPM * voltage * 0.75;
    const rho = 1.225;
    const D_m = propDiamIn * 0.0254;
    const n_rev_s = maxRPM / 60;
    const CT = 0.11;
    const singleThrustN = CT * rho * (n_rev_s * n_rev_s) * Math.pow(D_m, 4);
    const totalThrustN = 4 * singleThrustN;
    const totalThrustKg = totalThrustN / 9.81;
    const twRatio = totalThrustKg / massKg;

    const hoverThrustPerMotor = (massKg * 9.81) / 4;
    const hoverRPM = Math.sqrt(hoverThrustPerMotor / (CT * rho * Math.pow(D_m, 4))) * 60;
    const hoverPowerWatt = 4 * (0.04 * rho * Math.pow(hoverRPM/60, 3) * Math.pow(D_m, 5) * 2 * Math.PI);
    const hoverCurrentAmp = hoverPowerWatt / voltage;
    const hoverTimeMin = (batMah * 0.001 * 0.8) / hoverCurrentAmp * 60;

    const barX = 40, barY = 40, barW = width - 80, barH = 30;
    ctx.fillStyle = '#0f172a'; ctx.strokeStyle = '#334155'; ctx.lineWidth = 1;
    ctx.fillRect(barX, barY, barW, barH); ctx.strokeRect(barX, barY, barW, barH);

    const safeTW = 2.0;
    const twFillW = Math.min(barW, (twRatio / 4.0) * barW);
    const twColor = twRatio >= 2.0 ? '#10b981' : (twRatio >= 1.5 ? '#f59e0b' : '#ef4444');
    ctx.fillStyle = twColor; ctx.fillRect(barX, barY, twFillW, barH);

    const markerX = barX + (safeTW / 4.0) * barW;
    ctx.strokeStyle = '#f8fafc'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(markerX, barY - 6); ctx.lineTo(markerX, barY + barH + 6); ctx.stroke();
    ctx.fillStyle = '#f8fafc'; ctx.font = '10px Inter, sans-serif'; ctx.textAlign = 'center';
    ctx.fillText('Chuẩn T/W ≥ 2.0', markerX, barY - 10);

    ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 12px Inter, sans-serif'; ctx.textAlign = 'center';
    ctx.fillText(`Tỉ lệ Lực Nâng / Trọng Lượng (T/W) = ${twRatio.toFixed(2)}`, width / 2, barY + 20);

    const cards = [
      { label: 'Tổng Lực Đẩy Cực Đại', val: `${totalThrustN.toFixed(1)} N (${totalThrustKg.toFixed(2)} kg)`, color: '#38bdf8' },
      { label: 'Trọng Lượng Máy Bay', val: `${(massKg*9.81).toFixed(1)} N (${massKg.toFixed(2)} kg)`, color: '#94a3b8' },
      { label: 'Dòng Điện Lơ Lửng (Hover)', val: `${hoverCurrentAmp.toFixed(1)} A (${hoverPowerWatt.toFixed(0)} W)`, color: '#f59e0b' },
      { label: 'Thời Gian Lơ Lửng Ước Tính', val: `${hoverTimeMin.toFixed(1)} Phút`, color: twRatio >= 1.5 ? '#10b981' : '#ef4444' }
    ];

    const cardW = (width - 100) / 2;
    const cardH = 80;
    cards.forEach((c, idx) => {
      const row = Math.floor(idx / 2);
      const col = idx % 2;
      const cx = 40 + col * (cardW + 20);
      const cy = 110 + row * (cardH + 15);

      ctx.fillStyle = '#0f172a'; ctx.strokeStyle = '#334155'; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.roundRect(cx, cy, cardW, cardH, 8); ctx.fill(); ctx.stroke();

      ctx.fillStyle = '#94a3b8'; ctx.font = '11px Inter, sans-serif'; ctx.textAlign = 'left';
      ctx.fillText(c.label, cx + 15, cy + 30);
      ctx.fillStyle = c.color; ctx.font = 'bold 16px Inter, sans-serif';
      ctx.fillText(c.val, cx + 15, cy + 60);
    });

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 6: 6-DoF Dynamics & Control Allocation (Ch 06)
// ============================================================================
window.MCSimulators.init6DoFDynamicsSim = function() {
  const setup = setupCanvas('canvas-6dof-dynamics');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let f_cmd = 16.0;
  let tau_x = 0.0;
  let tau_y = 0.0;
  let tau_z = 0.0;

  const sF = document.getElementById('slider-ch06-f');
  const sTx = document.getElementById('slider-ch06-tx');
  const sTy = document.getElementById('slider-ch06-ty');
  const sTz = document.getElementById('slider-ch06-tz');

  function updateSliders() {
    if (sF) f_cmd = parseFloat(sF.value);
    if (sTx) tau_x = parseFloat(sTx.value);
    if (sTy) tau_y = parseFloat(sTy.value);
    if (sTz) tau_z = parseFloat(sTz.value);
  }
  if (sF) sF.addEventListener('input', updateSliders);
  if (sTx) sTx.addEventListener('input', updateSliders);
  if (sTy) sTy.addEventListener('input', updateSliders);
  if (sTz) sTz.addEventListener('input', updateSliders);

  const cT = 1.1e-5;
  const cM = 1.8e-7;
  const d = 0.225;
  const k = (Math.SQRT2 / 2) * d * cT;

  function render() {
    ctx.clearRect(0, 0, width, height);

    const w1_sq = (f_cmd / (4 * cT)) - (tau_x / (4 * k)) + (tau_y / (4 * k)) - (tau_z / (4 * cM));
    const w2_sq = (f_cmd / (4 * cT)) + (tau_x / (4 * k)) + (tau_y / (4 * k)) + (tau_z / (4 * cM));
    const w3_sq = (f_cmd / (4 * cT)) + (tau_x / (4 * k)) - (tau_y / (4 * k)) - (tau_z / (4 * cM));
    const w4_sq = (f_cmd / (4 * cT)) - (tau_x / (4 * k)) - (tau_y / (4 * k)) + (tau_z / (4 * cM));

    const w1 = w1_sq > 0 ? Math.sqrt(w1_sq) : 0;
    const w2 = w2_sq > 0 ? Math.sqrt(w2_sq) : 0;
    const w3 = w3_sq > 0 ? Math.sqrt(w3_sq) : 0;
    const w4 = w4_sq > 0 ? Math.sqrt(w4_sq) : 0;

    const maxW = 900;
    const wVals = [w1, w2, w3, w4];

    const qX = width * 0.3, qY = height * 0.52;
    const armR = 75;

    ctx.strokeStyle = '#475569'; ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.moveTo(qX - armR, qY - armR); ctx.lineTo(qX + armR, qY + armR);
    ctx.moveTo(qX + armR, qY - armR); ctx.lineTo(qX - armR, qY + armR);
    ctx.stroke();

    ctx.fillStyle = '#0f172a'; ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(qX, qY, 20, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
    ctx.fillStyle = '#f8fafc'; ctx.font = '10px Inter, sans-serif'; ctx.textAlign = 'center';
    ctx.fillText('Đầu Bay ↑', qX, qY - 26);

    const mCoords = [
      { x: qX + armR, y: qY - armR, id: 1, w: w1 },
      { x: qX + armR, y: qY + armR, id: 2, w: w2 },
      { x: qX - armR, y: qY + armR, id: 3, w: w3 },
      { x: qX - armR, y: qY - armR, id: 4, w: w4 }
    ];

    mCoords.forEach(m => {
      const isSat = m.w >= maxW || m.w <= 0;
      ctx.fillStyle = isSat ? '#ef4444' : '#10b981';
      ctx.beginPath(); ctx.arc(m.x, m.y, 16, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 10px monospace';
      ctx.fillText(`M${m.id}`, m.x, m.y + 3);
      ctx.fillStyle = '#94a3b8'; ctx.font = '9px monospace';
      ctx.fillText(`${Math.round(m.w)} rad/s`, m.x, m.y + (m.y > qY ? 24 : -20));
    });

    const barBaseX = width * 0.65;
    const barBaseW = width * 0.28;
    ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 12px Inter, sans-serif'; ctx.textAlign = 'left';
    ctx.fillText('Phân Phối Tốc Độ 4 Động Cơ (rad/s):', barBaseX, 40);

    wVals.forEach((w, idx) => {
      const by = 70 + idx * 45;
      ctx.fillStyle = '#94a3b8'; ctx.font = '11px monospace';
      ctx.fillText(`M${idx+1}: ${Math.round(w)} / ${maxW} rad/s`, barBaseX, by);
      ctx.fillStyle = '#1e293b'; ctx.fillRect(barBaseX, by + 6, barBaseW, 14);
      const fillW = Math.min(barBaseW, (w / maxW) * barBaseW);
      ctx.fillStyle = w >= maxW ? '#ef4444' : '#38bdf8';
      ctx.fillRect(barBaseX, by + 6, fillW, 14);
    });

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 7: Sensor Calibration & Ellipsoid Fitting (Ch 07)
// ============================================================================
window.MCSimulators.initSensorCalibrationSim = function() {
  const setup = setupCanvas('canvas-sensor-calibration');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let isCalibrated = false;
  const btnCal = document.getElementById('btn-ch07-calibrate');
  if (btnCal) {
    btnCal.addEventListener('click', () => {
      isCalibrated = !isCalibrated;
      btnCal.innerText = isCalibrated ? 'Đặt Lại Dữ Liệu Thô (Raw)' : 'Chạy Hiệu Chuẩn Ellipsoid (Least Squares)';
    });
  }

  const rawPoints = [];
  const numPts = 60;
  for (let i = 0; i < numPts; i++) {
    const u = Math.random() * Math.PI * 2;
    const v = Math.random() * Math.PI - Math.PI / 2;
    const x0 = Math.cos(v) * Math.cos(u);
    const y0 = Math.cos(v) * Math.sin(u);
    const rx = 1.4 * x0 + 0.35 + (Math.random() - 0.5) * 0.08;
    const ry = 0.75 * y0 - 0.25 + (Math.random() - 0.5) * 0.08;
    rawPoints.push({ rx, ry, cx: x0, cy: y0 });
  }

  function render() {
    ctx.clearRect(0, 0, width, height);

    const midX = width / 2;
    const midY = height / 2;
    const scale = 80;

    ctx.strokeStyle = '#334155'; ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(midX, 20); ctx.lineTo(midX, height - 20);
    ctx.moveTo(20, midY); ctx.lineTo(width - 20, midY);
    ctx.stroke();

    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.arc(midX, midY, scale, 0, Math.PI * 2); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = '#10b981'; ctx.font = '10px Inter, sans-serif'; ctx.textAlign = 'right';
    ctx.fillText('Chuẩn R = 1.0', midX + scale - 5, midY - 6);

    rawPoints.forEach(p => {
      const px = isCalibrated ? midX + p.cx * scale : midX + p.rx * scale;
      const py = isCalibrated ? midY - p.cy * scale : midY - p.ry * scale;
      ctx.fillStyle = isCalibrated ? '#10b981' : '#f59e0b';
      ctx.beginPath(); ctx.arc(px, py, 3.5, 0, Math.PI * 2); ctx.fill();
    });

    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)'; ctx.strokeStyle = '#334155'; ctx.lineWidth = 1;
    ctx.fillRect(20, 20, 240, 75); ctx.strokeRect(20, 20, 240, 75);
    ctx.fillStyle = isCalibrated ? '#10b981' : '#f59e0b';
    ctx.font = 'bold 12px Inter, sans-serif'; ctx.textAlign = 'left';
    ctx.fillText(isCalibrated ? '✓ ĐÃ HIỆU CHUẨN (Calibrated)' : '⚠ DỮ LIỆU THÔ BỊ MÉO (Raw)', 30, 40);
    ctx.fillStyle = '#94a3b8'; ctx.font = '10px monospace';
    ctx.fillText(isCalibrated ? 'Vector Bias b: [0.00, 0.00]' : 'Vector Bias b: [+0.35, -0.25]', 30, 60);
    ctx.fillText(isCalibrated ? 'Tỉ lệ trục K: diag(1.0, 1.0)' : 'Tỉ lệ trục K: diag(1.40, 0.75)', 30, 76);

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 8: Attitude Filter (Complementary vs Kalman) (Ch 08)
// ============================================================================
window.MCSimulators.initAttitudeFilterSim = function() {
  const setup = setupCanvas('canvas-attitude-filter');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let tau = 0.95;
  const sliderTau = document.getElementById('slider-ch08-tau');
  if (sliderTau) {
    sliderTau.addEventListener('input', (e) => {
      tau = parseFloat(e.target.value);
      const valEl = document.getElementById('val-ch08-tau');
      if (valEl) valEl.innerText = tau.toFixed(2);
    });
  }

  let hist = [];
  const maxPts = 300;
  let simT = 0;
  let gyroDrift = 0;
  let compEst = 0;

  function render() {
    simT += 0.04;
    const trueAngle = Math.sin(simT * 0.8) * 20;
    const gyroRate = 0.8 * Math.cos(simT * 0.8) * 20;
    gyroDrift += 0.003;
    const gyroAngle = trueAngle + gyroDrift * 20;
    const accelAngle = trueAngle + (Math.random() - 0.5) * 12;

    compEst = tau * (compEst + gyroRate * 0.04) + (1 - tau) * accelAngle;

    hist.push({ trueVal: trueAngle, gyroVal: gyroAngle, accVal: accelAngle, compVal: compEst });
    if (hist.length > maxPts) hist.shift();

    ctx.clearRect(0, 0, width, height);

    const ox = 40, oy = 30, ow = width - 80, oh = height - 70;
    ctx.fillStyle = '#0f172a'; ctx.strokeStyle = '#334155'; ctx.lineWidth = 1;
    ctx.fillRect(ox, oy, ow, oh); ctx.strokeRect(ox, oy, ow, oh);

    const midY = oy + oh / 2;
    ctx.strokeStyle = '#1e293b';
    ctx.beginPath(); ctx.moveTo(ox, midY); ctx.lineTo(ox + ow, midY); ctx.stroke();

    const drawLine = (key, color, widthLine) => {
      ctx.strokeStyle = color; ctx.lineWidth = widthLine;
      ctx.beginPath();
      hist.forEach((pt, idx) => {
        const px = ox + (idx / maxPts) * ow;
        const py = midY - pt[key] * 2.2;
        if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      });
      ctx.stroke();
    };

    drawLine('accVal', 'rgba(239, 68, 68, 0.35)', 1);
    drawLine('gyroVal', 'rgba(245, 158, 11, 0.5)', 1.5);
    drawLine('trueVal', '#f8fafc', 2);
    drawLine('compVal', '#10b981', 2.5);

    ctx.fillStyle = '#f8fafc'; ctx.font = '10px Inter, sans-serif'; ctx.textAlign = 'left';
    ctx.fillText('— Chuẩn (Truth)', ox + 15, oy + 20);
    ctx.fillStyle = '#10b981'; ctx.fillText('— Bộ Lọc Bù (Filtered)', ox + 115, oy + 20);
    ctx.fillStyle = '#f59e0b'; ctx.fillText('— Con quay (Gyro Drift)', ox + 245, oy + 20);
    ctx.fillStyle = '#ef4444'; ctx.fillText('— Gia tốc kế (Accel Noise)', ox + 390, oy + 20);

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 9: Cascade Attitude PID Controller (Ch 09)
// ============================================================================
window.MCSimulators.initCascadeAttitudePIDSim = function() {
  const setup = setupCanvas('canvas-cascade-attitude-pid');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let targetAngle = 0;
  const btnStep = document.getElementById('btn-ch09-step');
  const btnWind = document.getElementById('btn-ch09-wind');

  if (btnStep) btnStep.addEventListener('click', () => { targetAngle = targetAngle === 0 ? 20 : 0; });
  let windGust = 0;
  if (btnWind) btnWind.addEventListener('click', () => { windGust = 15; });

  let curAngle = 0;
  let curRate = 0;
  let hist = [];

  function render() {
    windGust *= 0.95;
    const kp_angle = 6.0;
    const rate_des = kp_angle * (targetAngle - curAngle);

    const kp_rate = 0.15;
    const torque = kp_rate * (rate_des - curRate) + windGust;

    const J = 0.015;
    const dt = 0.02;
    const rate_dot = torque / J - 0.2 * curRate;
    curRate += rate_dot * dt;
    curAngle += curRate * dt;

    hist.push({ des: targetAngle, act: curAngle });
    if (hist.length > 250) hist.shift();

    ctx.clearRect(0, 0, width, height);

    const gx = 40, gy = 30, gw = width - 80, gh = height - 60;
    ctx.fillStyle = '#0f172a'; ctx.strokeStyle = '#334155'; ctx.lineWidth = 1;
    ctx.fillRect(gx, gy, gw, gh); ctx.strokeRect(gx, gy, gw, gh);

    const midY = gy + gh * 0.7;
    ctx.strokeStyle = '#f59e0b'; ctx.setLineDash([4, 4]); ctx.lineWidth = 1.5;
    ctx.beginPath();
    hist.forEach((pt, idx) => {
      const px = gx + (idx / 250) * gw;
      const py = midY - pt.des * 3.5;
      if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    });
    ctx.stroke(); ctx.setLineDash([]);

    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5;
    ctx.beginPath();
    hist.forEach((pt, idx) => {
      const px = gx + (idx / 250) * gw;
      const py = midY - pt.act * 3.5;
      if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    });
    ctx.stroke();

    ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 12px Inter, sans-serif'; ctx.textAlign = 'left';
    ctx.fillText(`Góc Đặt θd: ${targetAngle.toFixed(1)}° | Góc Thật θ: ${curAngle.toFixed(1)}°`, gx + 15, gy + 20);

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 10: 3D Position Set-Point & Anti-Windup (Ch 10)
// ============================================================================
window.MCSimulators.initPosition3DSetPointSim = function() {
  const setup = setupCanvas('canvas-position-3d-setpoint');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let antiWindup = true;
  const btnToggleAW = document.getElementById('btn-ch10-toggle-aw');
  if (btnToggleAW) {
    btnToggleAW.addEventListener('click', () => {
      antiWindup = !antiWindup;
      btnToggleAW.innerText = antiWindup ? 'Anti-Windup: BẬT (Enabled)' : 'Anti-Windup: TẮT (Disabled)';
    });
  }

  let posX = 50, velX = 0, integralX = 0;
  let targetX = 250;

  canvas.addEventListener('click', (e) => {
    const rect = canvas.getBoundingClientRect();
    targetX = e.clientX - rect.left;
  });

  function render() {
    ctx.clearRect(0, 0, width, height);

    const err = targetX - posX;
    const Kp = 1.2, Ki = 0.05, Kd = 0.8;
    const maxThrust = 80;

    let u_unsat = Kp * err + Ki * integralX - Kd * velX;
    let u_sat = Math.max(-maxThrust, Math.min(maxThrust, u_unsat));

    if (antiWindup) {
      if ((u_unsat === u_sat) || (err * u_unsat < 0)) {
        integralX += err * 0.02;
      }
    } else {
      integralX += err * 0.02;
    }

    const acc = u_sat * 0.08;
    velX += acc;
    velX *= 0.94;
    posX += velX;

    const trackY = height * 0.6;
    ctx.strokeStyle = '#334155'; ctx.lineWidth = 4;
    ctx.beginPath(); ctx.moveTo(40, trackY); ctx.lineTo(width - 40, trackY); ctx.stroke();

    ctx.fillStyle = '#ef4444';
    ctx.beginPath(); ctx.arc(targetX, trackY, 6, 0, Math.PI * 2); ctx.fill();
    ctx.font = '11px Inter, sans-serif'; ctx.textAlign = 'center';
    ctx.fillText('Điểm Đích (Click để đổi)', targetX, trackY + 24);

    ctx.fillStyle = antiWindup ? '#10b981' : '#f59e0b';
    ctx.beginPath(); ctx.roundRect(posX - 25, trackY - 20, 50, 20, 4); ctx.fill();
    ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 10px monospace';
    ctx.fillText('QUAD', posX, trackY - 6);

    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)'; ctx.strokeStyle = '#334155'; ctx.lineWidth = 1;
    ctx.fillRect(20, 20, 280, 65); ctx.strokeRect(20, 20, 280, 65);
    ctx.fillStyle = antiWindup ? '#34d399' : '#f59e0b';
    ctx.font = 'bold 12px Inter, sans-serif'; ctx.textAlign = 'left';
    ctx.fillText(antiWindup ? '✓ Chế Độ: Anti-Windup Đang BẬT' : '⚠ Chế Độ: Anti-Windup TẮT (Dễ Vọt Lố)', 30, 40);
    ctx.fillStyle = '#94a3b8'; ctx.font = '10px monospace';
    ctx.fillText(`Tích phân I-term: ${integralX.toFixed(1)} | Lực đẩy u: ${u_sat.toFixed(1)}`, 30, 60);

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 11: Semi-Autonomous Flight Modes (Ch 11)
// ============================================================================
window.MCSimulators.initFlightModeStateMachineSim = function() {
  const setup = setupCanvas('canvas-flight-mode-state-machine');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let currentMode = 'ALT_HOLD';
  const modes = ['MANUAL', 'ALT_HOLD', 'POS_HOLD', 'AUTO_RTL'];
  const btnNextMode = document.getElementById('btn-ch11-next-mode');
  if (btnNextMode) {
    btnNextMode.addEventListener('click', () => {
      const idx = (modes.indexOf(currentMode) + 1) % modes.length;
      currentMode = modes[idx];
    });
  }

  function render() {
    ctx.clearRect(0, 0, width, height);

    const modeConfigs = [
      { id: 'MANUAL', label: '1. Manual (Thủ Công)', desc: 'RC trực tiếp -> Góc nghiêng', color: '#f59e0b', x: width * 0.18, y: height * 0.4 },
      { id: 'ALT_HOLD', label: '2. Altitude Hold', desc: 'Tự giữ cao độ bằng Baro', color: '#0284c7', x: width * 0.42, y: height * 0.4 },
      { id: 'POS_HOLD', label: '3. Position Hold', desc: 'Tự giữ vị trí 3D bằng GPS', color: '#10b981', x: width * 0.66, y: height * 0.4 },
      { id: 'AUTO_RTL', label: '4. Return-To-Launch', desc: 'Tự động bay về Home & Hạ cánh', color: '#8b5cf6', x: width * 0.88, y: height * 0.4 }
    ];

    modeConfigs.forEach(m => {
      const isCur = m.id === currentMode;
      const mw = 120, mh = 80;

      ctx.fillStyle = isCur ? 'rgba(2, 132, 199, 0.3)' : '#0f172a';
      ctx.strokeStyle = isCur ? m.color : '#334155';
      ctx.lineWidth = isCur ? 3 : 1;
      ctx.beginPath(); ctx.roundRect(m.x - mw/2, m.y - mh/2, mw, mh, 10); ctx.fill(); ctx.stroke();

      ctx.fillStyle = m.color; ctx.font = 'bold 11px Inter, sans-serif'; ctx.textAlign = 'center';
      ctx.fillText(m.label, m.x, m.y - 15);
      ctx.fillStyle = '#94a3b8'; ctx.font = '9px Inter, sans-serif';
      ctx.fillText(m.desc, m.x, m.y + 15);
    });

    requestAnimationFrame(render);
  }
  render();
};

// ============================================================================
// SIMULATOR 12: Emergency Failsafe State Machine (Ch 12)
// ============================================================================
window.MCSimulators.initFailsafeProtectionSim = function() {
  const setup = setupCanvas('canvas-failsafe-protection');
  if (!setup) return;
  const { canvas, ctx } = setup;
  let width = setup.width, height = setup.height;

  let state = 'NORMAL';
  const btnRcLost = document.getElementById('btn-ch12-rc-lost');
  const btnLowBat = document.getElementById('btn-ch12-low-bat');
  const btnReset = document.getElementById('btn-ch12-reset');

  let quadPos = { x: width * 0.75, y: height * 0.45 };
  const homePos = { x: width * 0.25, y: height * 0.7 };
  const safeAltY = height * 0.25;

  if (btnRcLost) btnRcLost.addEventListener('click', () => { state = 'RTL_CLIMB'; });
  if (btnLowBat) btnLowBat.addEventListener('click', () => { state = 'LOW_BAT'; });
  if (btnReset) btnReset.addEventListener('click', () => { state = 'NORMAL'; quadPos = { x: width * 0.75, y: height * 0.45 }; });

  function render() {
    ctx.clearRect(0, 0, width, height);

    ctx.strokeStyle = '#334155'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(20, height * 0.85); ctx.lineTo(width - 20, height * 0.85); ctx.stroke();

    ctx.fillStyle = '#10b981';
    ctx.beginPath(); ctx.arc(homePos.x, height * 0.85, 8, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#f8fafc'; ctx.font = '11px Inter, sans-serif'; ctx.textAlign = 'center';
    ctx.fillText('⌂ HOME CẤT CÁNH', homePos.x, height * 0.85 + 20);

    if (state === 'RTL_CLIMB') {
      if (quadPos.y > safeAltY) quadPos.y -= 1.2;
      else state = 'RTL_CRUISE';
    } else if (state === 'RTL_CRUISE') {
      if (quadPos.x > homePos.x) quadPos.x -= 1.5;
      else state = 'LANDED';
    } else if (state === 'LANDED' || state === 'LOW_BAT') {
      if (quadPos.y < height * 0.82) quadPos.y += 1.2;
    }

    ctx.fillStyle = state === 'NORMAL' ? '#0284c7' : (state === 'LANDED' ? '#10b981' : '#ef4444');
    ctx.beginPath(); ctx.roundRect(quadPos.x - 20, quadPos.y - 12, 40, 16, 4); ctx.fill();

    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)'; ctx.strokeStyle = '#334155'; ctx.lineWidth = 1;
    ctx.fillRect(20, 20, 260, 60); ctx.strokeRect(20, 20, 260, 60);
    ctx.fillStyle = '#f8fafc'; ctx.font = 'bold 12px Inter, sans-serif'; ctx.textAlign = 'left';
    ctx.fillText(`Trạng Thái Failsafe: ${state}`, 30, 40);
    ctx.fillStyle = '#94a3b8'; ctx.font = '10px monospace';
    ctx.fillText(state === 'NORMAL' ? 'Hệ thống an toàn, sóng RC tốt' : 'KÍCH HOẠT QUY TRÌNH RTL KHẨN CẤP', 30, 60);

    requestAnimationFrame(render);
  }
  render();
};

// Automatic simulator auto-boot on load
document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    Object.keys(window.MCSimulators).forEach(simFn => {
      try { window.MCSimulators[simFn](); } catch(e) { console.warn(e); }
    });
  }, 300);
});
