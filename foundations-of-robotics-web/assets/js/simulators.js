/**
 * Foundations of Robotics - Interactive 60 FPS Canvas 2D Simulators Suite
 * Based on 'Foundations of Robotics' (Siciliano, Sciavicco, Villani, Oriolo)
 *
 * Implements 12 distinct simulations:
 *  - Sim 01: Kiến Trúc DoF & Khảo Sát Không Gian Làm Việc Cánh Tay Robot (Ch 01)
 *  - Sim 02: Biến Đổi Hệ Tọa Độ & Ma Trận Xoay / Góc Roll-Pitch-Yaw 3D (Ch 02)
 *  - Sim 03: Động Học Vi Phân, Jacobian & Elip Độ Khả Điều Khiển (Ch 03)
 *  - Sim 04: Hoạch Định Quỹ Đạo Chuyển Động (LSPB Hình Thang vs Bậc 5) (Ch 04)
 *  - Sim 05: Động Lực Học Robot Manipulator Euler-Lagrange (Ch 05)
 *  - Sim 06: Điều Khiển Chuyển Động (Computed Torque vs PID) (Ch 06)
 *  - Sim 07: Robot Di Động Bánh Xe & Ràng Buộc Phi Holonomic (Ch 07)
 *  - Sim 08: Điều Khiển Bằng Thị Giác Robot (IBVS Visual Servoing) (Ch 08)
 *  - Sim 09: Hoạch Định Chuyển Động Bằng Trường Thế Năng Nhân Tạo (Ch 09)
 *  - Sim 10: Điều Khiển Lực & Tương Tác Vật Lý Impedance Control (Ch 10)
 *  - Sim 11: Robot Khớp Đàn Hồi Manipulator with Elastic Joints (Ch 11)
 *  - Sim 12: Thao Tác Hợp Tác Đa Robot & Cầm Nắm Cùng Vật Thể (Ch 12)
 */

// Global registry of simulator cancellation handles
window._forSimHandles = window._forSimHandles || {};

// Helper to get canvas and 2D context safely
function getSimCanvas(id) {
  const canvas = document.getElementById(id);
  if (!canvas) return null;
  const ctx = canvas.getContext('2d');
  return { canvas, ctx };
}

// Helper to get theme color
function isDarkTheme() {
  return document.documentElement.getAttribute('data-theme') === 'dark';
}

// =========================================================================
// SIM 01: Kiến Trúc Bậc Tự Do & Khảo Sát Không Gian Làm Việc (Workspace)
// =========================================================================
window.initSim01 = function() {
  const sim = getSimCanvas('sim-canvas-01');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['01']) cancelAnimationFrame(window._forSimHandles['01']);

  const sliderL1 = document.getElementById('sim01-l1');
  const sliderL2 = document.getElementById('sim01-l2');
  const valL1 = document.getElementById('sim01-l1-val');
  const valL2 = document.getElementById('sim01-l2-val');
  const stats = document.getElementById('sim01-stats');

  let q1 = 0.5;
  let q2 = 0.8;
  let t = 0;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const l1 = sliderL1 ? parseFloat(sliderL1.value) : 100;
    const l2 = sliderL2 ? parseFloat(sliderL2.value) : 75;
    if (valL1) valL1.textContent = l1.toFixed(0) + ' px';
    if (valL2) valL2.textContent = l2.toFixed(0) + ' px';

    // Articulate angles slowly
    t += 0.02;
    q1 = 0.6 * Math.sin(t * 0.8) + 0.3;
    q2 = 0.9 * Math.cos(t * 1.2);

    const ox = canvas.width / 2;
    const oy = canvas.height / 2 + 20;

    // Outer and Inner reachable workspace boundaries
    const rMax = l1 + l2;
    const rMin = Math.abs(l1 - l2);

    // Draw Reachable Workspace Rings
    ctx.save();
    ctx.beginPath();
    ctx.arc(ox, oy, rMax, 0, Math.PI * 2);
    ctx.arc(ox, oy, rMin, 0, Math.PI * 2, true);
    ctx.fillStyle = dark ? 'rgba(56, 189, 248, 0.07)' : 'rgba(37, 99, 235, 0.07)';
    ctx.fill();

    ctx.strokeStyle = dark ? 'rgba(56, 189, 248, 0.35)' : 'rgba(37, 99, 235, 0.35)';
    ctx.setLineDash([4, 4]);
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(ox, oy, rMax, 0, Math.PI * 2);
    ctx.stroke();

    if (rMin > 5) {
      ctx.beginPath();
      ctx.arc(ox, oy, rMin, 0, Math.PI * 2);
      ctx.stroke();
    }
    ctx.setLineDash([]);
    ctx.restore();

    // Base coordinate frame (X0, Y0)
    ctx.strokeStyle = dark ? '#475569' : '#cbd5e1';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(ox - rMax - 20, oy);
    ctx.lineTo(ox + rMax + 20, oy);
    ctx.moveTo(ox, oy - rMax - 20);
    ctx.lineTo(ox, oy + rMax + 20);
    ctx.stroke();

    // Joint 1 position (Origin)
    const x1 = ox + l1 * Math.cos(q1);
    const y1 = oy - l1 * Math.sin(q1);

    // End-Effector position
    const xe = x1 + l2 * Math.cos(q1 + q2);
    const ye = y1 - l2 * Math.sin(q1 + q2);

    // Link 1
    ctx.strokeStyle = '#2563eb';
    ctx.lineWidth = 8;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(ox, oy);
    ctx.lineTo(x1, y1);
    ctx.stroke();

    // Link 2
    ctx.strokeStyle = '#7c3aed';
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(xe, ye);
    ctx.stroke();

    // Base joint
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.arc(ox, oy, 10, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#60a5fa';
    ctx.beginPath();
    ctx.arc(ox, oy, 5, 0, Math.PI * 2);
    ctx.fill();

    // Elbow Joint
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.arc(x1, y1, 8, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#a78bfa';
    ctx.beginPath();
    ctx.arc(x1, y1, 4, 0, Math.PI * 2);
    ctx.fill();

    // End-Effector Tip
    ctx.fillStyle = '#10b981';
    ctx.beginPath();
    ctx.arc(xe, ye, 7, 0, Math.PI * 2);
    ctx.fill();

    // Stats Readout
    if (stats) {
      const area = (Math.PI * (rMax * rMax - rMin * rMin) / 100).toFixed(0);
      const curX = ((xe - ox) / 10).toFixed(1);
      const curY = ((oy - ye) / 10).toFixed(1);
      stats.innerHTML = `Vị trí khâu tác động cuối: <b>P_e = [${curX}, ${curY}] cm</b> | Bán kính cực đại <b>R_max = ${((l1+l2)/10).toFixed(1)} cm</b> | Bán kính cực tiểu <b>R_min = ${(rMin/10).toFixed(1)} cm</b> | Diện tích vùng làm việc: <b>${area} cm²</b>`;
    }

    window._forSimHandles['01'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 02: Biến Đổi Hệ Tọa Độ & Góc Định Hướng 3D (Roll-Pitch-Yaw / Quaternion)
// =========================================================================
window.initSim02 = function() {
  const sim = getSimCanvas('sim-canvas-02');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['02']) cancelAnimationFrame(window._forSimHandles['02']);

  const sliderRoll = document.getElementById('sim02-roll');
  const sliderPitch = document.getElementById('sim02-pitch');
  const sliderYaw = document.getElementById('sim02-yaw');
  const valRoll = document.getElementById('sim02-roll-val');
  const valPitch = document.getElementById('sim02-pitch-val');
  const valYaw = document.getElementById('sim02-yaw-val');
  const stats = document.getElementById('sim02-stats');

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const rollDeg = sliderRoll ? parseFloat(sliderRoll.value) : 25;
    const pitchDeg = sliderPitch ? parseFloat(sliderPitch.value) : 35;
    const yawDeg = sliderYaw ? parseFloat(sliderYaw.value) : 45;

    if (valRoll) valRoll.textContent = rollDeg.toFixed(0) + '°';
    if (valPitch) valPitch.textContent = pitchDeg.toFixed(0) + '°';
    if (valYaw) valYaw.textContent = yawDeg.toFixed(0) + '°';

    const phi = (rollDeg * Math.PI) / 180;
    const theta = (pitchDeg * Math.PI) / 180;
    const psi = (yawDeg * Math.PI) / 180;

    // Rotation Matrix R = Rz(psi) * Ry(theta) * Rx(phi)
    const c1 = Math.cos(psi), s1 = Math.sin(psi);
    const c2 = Math.cos(theta), s2 = Math.sin(theta);
    const c3 = Math.cos(phi), s3 = Math.sin(phi);

    const r11 = c1 * c2, r12 = c1 * s2 * s3 - s1 * c3, r13 = c1 * s2 * c3 + s1 * s3;
    const r21 = s1 * c2, r22 = s1 * s2 * s3 + c1 * c3, r23 = s1 * s2 * c3 - c1 * s3;
    const r31 = -s2,     r32 = c2 * s3,               r33 = c2 * c3;

    // Unit Quaternion calculation
    const trace = r11 + r22 + r33;
    let qw = 1, qx = 0, qy = 0, qz = 0;
    if (trace > 0) {
      const s = 0.5 / Math.sqrt(trace + 1.0);
      qw = 0.25 / s;
      qx = (r32 - r23) * s;
      qy = (r13 - r31) * s;
      qz = (r21 - r12) * s;
    } else if (r11 > r22 && r11 > r33) {
      const s = 2.0 * Math.sqrt(1.0 + r11 - r22 - r33);
      qw = (r32 - r23) / s;
      qx = 0.25 * s;
      qy = (r12 + r21) / s;
      qz = (r13 + r31) / s;
    } else if (r22 > r33) {
      const s = 2.0 * Math.sqrt(1.0 + r22 - r11 - r33);
      qw = (r13 - r31) / s;
      qx = (r12 + r21) / s;
      qy = 0.25 * s;
      qz = (r23 + r32) / s;
    } else {
      const s = 2.0 * Math.sqrt(1.0 + r33 - r11 - r22);
      qw = (r21 - r12) / s;
      qx = (r13 + r31) / s;
      qy = (r23 + r32) / s;
      qz = 0.25 * s;
    }

    const ox = canvas.width / 2;
    const oy = canvas.height / 2 + 10;
    const axisLen = 95;

    // Isometric 3D Projection: projX = x - y * 0.5, projY = -z + y * 0.3
    const project = (x, y, z) => {
      const isoX = ox + (x - y * 0.55);
      const isoY = oy - (z - y * 0.35);
      return { x: isoX, y: isoY };
    };

    // Draw Reference Fixed World Frame (dashed gray)
    const pOrigin = project(0, 0, 0);
    const pX0 = project(axisLen, 0, 0);
    const pY0 = project(0, axisLen, 0);
    const pZ0 = project(0, 0, axisLen);

    ctx.save();
    ctx.setLineDash([3, 3]);
    ctx.strokeStyle = dark ? '#475569' : '#94a3b8';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(pOrigin.x, pOrigin.y); ctx.lineTo(pX0.x, pX0.y);
    ctx.moveTo(pOrigin.x, pOrigin.y); ctx.lineTo(pY0.x, pY0.y);
    ctx.moveTo(pOrigin.x, pOrigin.y); ctx.lineTo(pZ0.x, pZ0.y);
    ctx.stroke();
    ctx.restore();

    // Draw 3D Box in Body Frame
    const boxSize = 40;
    const vertices = [
      [-boxSize, -boxSize, -boxSize], [boxSize, -boxSize, -boxSize],
      [boxSize, boxSize, -boxSize],   [-boxSize, boxSize, -boxSize],
      [-boxSize, -boxSize, boxSize],  [boxSize, -boxSize, boxSize],
      [boxSize, boxSize, boxSize],    [-boxSize, boxSize, boxSize],
    ];
    const rotatedVertices = vertices.map(([bx, by, bz]) => {
      const rx = r11 * bx + r12 * by + r13 * bz;
      const ry = r21 * bx + r22 * by + r23 * bz;
      const rz = r31 * bx + r32 * by + r33 * bz;
      return project(rx, ry, rz);
    });

    const edges = [
      [0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]
    ];
    ctx.strokeStyle = dark ? 'rgba(148, 163, 184, 0.4)' : 'rgba(100, 116, 139, 0.4)';
    ctx.lineWidth = 1;
    edges.forEach(([i, j]) => {
      ctx.beginPath();
      ctx.moveTo(rotatedVertices[i].x, rotatedVertices[i].y);
      ctx.lineTo(rotatedVertices[j].x, rotatedVertices[j].y);
      ctx.stroke();
    });

    // Draw Transformed Tool Frame (RGB Triad: X-Red, Y-Green, Z-Blue)
    const drawArrow = (from, to, color, label) => {
      ctx.strokeStyle = color;
      ctx.fillStyle = color;
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(from.x, from.y);
      ctx.lineTo(to.x, to.y);
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(to.x, to.y, 4, 0, Math.PI * 2);
      ctx.fill();

      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(label, to.x + 8, to.y + 4);
    };

    const pX = project(r11 * axisLen, r21 * axisLen, r31 * axisLen);
    const pY = project(r12 * axisLen, r22 * axisLen, r32 * axisLen);
    const pZ = project(r13 * axisLen, r23 * axisLen, r33 * axisLen);

    drawArrow(pOrigin, pX, '#ef4444', 'X_b (Roll)');
    drawArrow(pOrigin, pY, '#10b981', 'Y_b (Pitch)');
    drawArrow(pOrigin, pZ, '#3b82f6', 'Z_b (Yaw)');

    if (stats) {
      stats.innerHTML = `Unit Quaternion: <b>q = [${qw.toFixed(3)}, ${qx.toFixed(3)}i, ${qy.toFixed(3)}j, ${qz.toFixed(3)}k]</b> | Chuẩn: <b>||q|| = ${(Math.sqrt(qw*qw+qx*qx+qy*qy+qz*qz)).toFixed(3)}</b> | Tránh điểm kỳ dị vặn góc (Gimbal Lock).`;
    }

    window._forSimHandles['02'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 03: Động Học Vi Phân, Jacobian & Elip Độ Khả Điều Khiển (Manipulability)
// =========================================================================
window.initSim03 = function() {
  const sim = getSimCanvas('sim-canvas-03');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['03']) cancelAnimationFrame(window._forSimHandles['03']);

  const sliderQ1 = document.getElementById('sim03-q1');
  const sliderQ2 = document.getElementById('sim03-q2');
  const valQ1 = document.getElementById('sim03-q1-val');
  const valQ2 = document.getElementById('sim03-q2-val');
  const stats = document.getElementById('sim03-stats');

  const l1 = 90, l2 = 75;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const q1Deg = sliderQ1 ? parseFloat(sliderQ1.value) : 40;
    const q2Deg = sliderQ2 ? parseFloat(sliderQ2.value) : 60;

    if (valQ1) valQ1.textContent = q1Deg.toFixed(0) + '°';
    if (valQ2) valQ2.textContent = q2Deg.toFixed(0) + '°';

    const q1 = (q1Deg * Math.PI) / 180;
    const q2 = (q2Deg * Math.PI) / 180;

    const ox = canvas.width / 2 - 40;
    const oy = canvas.height / 2 + 30;

    // Forward Kinematics
    const x1 = ox + l1 * Math.cos(q1);
    const y1 = oy - l1 * Math.sin(q1);
    const xe = x1 + l2 * Math.cos(q1 + q2);
    const ye = y1 - l2 * Math.sin(q1 + q2);

    // 2x2 Jacobian for position: J = [[-l1 s1 - l2 s12, -l2 s12], [l1 c1 + l2 c12, l2 c12]]
    const s1 = Math.sin(q1), c1 = Math.cos(q1);
    const s12 = Math.sin(q1 + q2), c12 = Math.cos(q1 + q2);

    const j11 = -l1 * s1 - l2 * s12;
    const j12 = -l2 * s12;
    const j21 = l1 * c1 + l2 * c12;
    const j22 = l2 * c12;

    // Determinant: det(J) = l1 * l2 * sin(q2)
    const detJ = (l1 / 100) * (l2 / 100) * Math.sin(q2);
    const wYoshikawa = Math.abs(detJ);

    // Matrix JJ^T
    const a = j11 * j11 + j12 * j12;
    const b = j11 * j21 + j12 * j22;
    const c = b;
    const d = j21 * j21 + j22 * j22;

    // Eigenvalues of 2x2 symmetric matrix: lambda = (tr +- sqrt(tr^2 - 4 det)) / 2
    const trace = a + d;
    const disc = Math.sqrt(Math.max(0, (a - d) * (a - d) + 4 * b * b));
    const eig1 = Math.max(0.1, (trace + disc) / 2);
    const eig2 = Math.max(0.1, (trace - disc) / 2);
    const angle = 0.5 * Math.atan2(2 * b, a - d);

    // Scale axes for visualization
    const axisA = Math.sqrt(eig1) * 0.45;
    const axisB = Math.sqrt(eig2) * 0.45;

    // Draw Links
    ctx.strokeStyle = '#2563eb';
    ctx.lineWidth = 7;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(ox, oy);
    ctx.lineTo(x1, y1);
    ctx.stroke();

    ctx.strokeStyle = '#7c3aed';
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(xe, ye);
    ctx.stroke();

    // Joints
    ctx.fillStyle = '#1e293b';
    ctx.beginPath(); ctx.arc(ox, oy, 8, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.arc(x1, y1, 6, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#10b981';
    ctx.beginPath(); ctx.arc(xe, ye, 6, 0, Math.PI * 2); ctx.fill();

    // Velocity Manipulability Ellipse at End-Effector
    ctx.save();
    ctx.translate(xe, ye);
    ctx.rotate(-angle);
    ctx.beginPath();
    ctx.ellipse(0, 0, Math.max(2, axisA), Math.max(2, axisB), 0, 0, Math.PI * 2);
    ctx.fillStyle = dark ? 'rgba(56, 189, 248, 0.2)' : 'rgba(14, 165, 233, 0.2)';
    ctx.fill();
    ctx.strokeStyle = '#0284c7';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Principal axes of ellipse
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(-axisA, 0); ctx.lineTo(axisA, 0);
    ctx.stroke();

    ctx.strokeStyle = '#10b981';
    ctx.beginPath();
    ctx.moveTo(0, -axisB); ctx.lineTo(0, axisB);
    ctx.stroke();
    ctx.restore();

    // Singularity check
    const isSingular = Math.abs(Math.sin(q2)) < 0.08;
    if (isSingular) {
      ctx.fillStyle = '#ef4444';
      ctx.font = 'bold 13px Inter, sans-serif';
      ctx.fillText('⚠ ĐIỂM KỲ DỊ: det(J) ≈ 0 (Mất bậc tự do chuyển động)', ox - 60, oy - 120);
    }

    if (stats) {
      stats.innerHTML = `Chỉ số Yoshikawa: <b>w = ${wYoshikawa.toFixed(3)}</b> | <b>det(J) = ${detJ.toFixed(3)}</b> | Tỉ số bán trục <b>σ₁/σ₂ = ${(axisA / Math.max(0.1, axisB)).toFixed(2)}</b> ${isSingular ? '<span style="color:#ef4444;font-weight:700;">(Kỳ dị biên/trong!)</span>' : ''}`;
    }

    window._forSimHandles['03'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 04: Hoạch Định Quỹ Đạo Chuyển Động (Trapezoidal vs Quintic Polynomial)
// =========================================================================
window.initSim04 = function() {
  const sim = getSimCanvas('sim-canvas-04');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['04']) cancelAnimationFrame(window._forSimHandles['04']);

  const selProfile = document.getElementById('sim04-profile');
  const sliderT = document.getElementById('sim04-duration');
  const valT = document.getElementById('sim04-duration-val');
  const stats = document.getElementById('sim04-stats');

  let time = 0;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const T = sliderT ? parseFloat(sliderT.value) : 3.0;
    if (valT) valT.textContent = T.toFixed(1) + ' s';
    const profile = selProfile ? selProfile.value : 'quintic';

    time += 0.02;
    if (time > T + 0.5) time = 0;

    const q0 = 0, q1 = 100;
    const w = canvas.width - 80;
    const h = canvas.height;
    const originX = 60;

    // Draw Plot Axes
    ctx.strokeStyle = dark ? '#334155' : '#cbd5e1';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(originX, 30); ctx.lineTo(originX, h - 30);
    ctx.moveTo(originX, h / 2); ctx.lineTo(canvas.width - 20, h / 2);
    ctx.stroke();

    // Trajectory curves computation
    const calcState = (tNorm) => {
      const tau = Math.max(0, Math.min(1, tNorm));
      if (profile === 'quintic') {
        // Quintic: s(tau) = 10 tau^3 - 15 tau^4 + 6 tau^5
        const pos = 10 * Math.pow(tau, 3) - 15 * Math.pow(tau, 4) + 6 * Math.pow(tau, 5);
        const vel = (30 * Math.pow(tau, 2) - 60 * Math.pow(tau, 3) + 30 * Math.pow(tau, 4)) / T;
        const acc = (60 * tau - 180 * Math.pow(tau, 2) + 120 * Math.pow(tau, 3)) / (T * T);
        return { pos, vel, acc };
      } else {
        // Trapezoidal velocity profile (LSPB) with tb = T/3
        const tb = 1 / 3;
        const aVal = 1 / (tb * (1 - tb));
        let pos = 0, vel = 0, acc = 0;
        if (tau <= tb) {
          pos = 0.5 * aVal * tau * tau;
          vel = aVal * tau / T;
          acc = aVal / (T * T);
        } else if (tau <= 1 - tb) {
          pos = aVal * tb * (tau - tb / 2);
          vel = aVal * tb / T;
          acc = 0;
        } else {
          pos = 1 - 0.5 * aVal * Math.pow(1 - tau, 2);
          vel = aVal * (1 - tau) / T;
          acc = -aVal / (T * T);
        }
        return { pos, vel, acc };
      }
    };

    // Plot Curves: Position (blue), Velocity (emerald), Acceleration (amber)
    ctx.lineWidth = 2.5;

    // 1. Position curve q(t)
    ctx.strokeStyle = '#3b82f6';
    ctx.beginPath();
    for (let i = 0; i <= w; i += 2) {
      const st = calcState(i / w);
      const px = originX + i;
      const py = (h - 40) - st.pos * (h - 80);
      if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // 2. Velocity curve dot{q}(t)
    ctx.strokeStyle = '#10b981';
    ctx.beginPath();
    for (let i = 0; i <= w; i += 2) {
      const st = calcState(i / w);
      const px = originX + i;
      const py = (h / 2) - st.vel * 40 * T;
      if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Current Time Marker
    const curNorm = Math.min(1, time / T);
    const curX = originX + curNorm * w;
    const curState = calcState(curNorm);

    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(curX, 20); ctx.lineTo(curX, h - 20);
    ctx.stroke();
    ctx.setLineDash([]);

    // Indicator head
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(curX, (h - 40) - curState.pos * (h - 80), 5, 0, Math.PI * 2);
    ctx.fill();

    // Legend
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6'; ctx.fillText('— Vị trí q(t)', originX + 20, 30);
    ctx.fillStyle = '#10b981'; ctx.fillText('— Vận tốc v(t)', originX + 130, 30);
    ctx.fillStyle = '#ef4444'; ctx.fillText(`t = ${Math.min(T, time).toFixed(2)}s / ${T.toFixed(1)}s`, canvas.width - 120, 30);

    if (stats) {
      stats.innerHTML = `Hành trình: <b>${(curState.pos * 100).toFixed(1)}%</b> | Vận tốc tức thời: <b>${(curState.vel * 100).toFixed(1)} deg/s</b> | Gia tốc: <b>${(curState.acc * 100).toFixed(1)} deg/s²</b> | Chế độ: <b>${profile === 'quintic' ? 'Đa thức bậc 5 (Mượt cấp Jerk)' : 'Hình thang LSPB (Gia tốc gián đoạn)'}</b>`;
    }

    window._forSimHandles['04'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 05: Động Lực Học Robot Manipulator Euler-Lagrange
// =========================================================================
window.initSim05 = function() {
  const sim = getSimCanvas('sim-canvas-05');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['05']) cancelAnimationFrame(window._forSimHandles['05']);

  const sliderMass = document.getElementById('sim05-mass');
  const sliderGrav = document.getElementById('sim05-gravity');
  const valMass = document.getElementById('sim05-mass-val');
  const valGrav = document.getElementById('sim05-gravity-val');
  const stats = document.getElementById('sim05-stats');

  let theta1 = Math.PI / 2, theta2 = 0;
  let omega1 = 0, omega2 = 0;
  const l1 = 80, l2 = 70;
  const dt = 0.02;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const m2 = sliderMass ? parseFloat(sliderMass.value) : 2.0;
    const g = sliderGrav ? parseFloat(sliderGrav.value) : 9.81;
    const m1 = 3.0;

    if (valMass) valMass.textContent = m2.toFixed(1) + ' kg';
    if (valGrav) valGrav.textContent = g.toFixed(1) + ' m/s²';

    // Physics step (Double Pendulum / 2R Euler-Lagrange under gravity)
    const damping = 0.994;
    const dTheta = theta1 - theta2;

    const num1 = -g * (2 * m1 + m2) * Math.sin(theta1) - m2 * g * Math.sin(theta1 - 2 * theta2) - 2 * Math.sin(dTheta) * m2 * (omega2 * omega2 * l2 + omega1 * omega1 * l1 * Math.cos(dTheta));
    const den1 = l1 * (2 * m1 + m2 - m2 * Math.cos(2 * theta1 - 2 * theta2));
    const alpha1 = num1 / Math.max(1, den1);

    const num2 = 2 * Math.sin(dTheta) * (omega1 * omega1 * l1 * (m1 + m2) + g * (m1 + m2) * Math.cos(theta1) + omega2 * omega2 * l2 * m2 * Math.cos(dTheta));
    const den2 = l2 * (2 * m1 + m2 - m2 * Math.cos(2 * theta1 - 2 * theta2));
    const alpha2 = num2 / Math.max(1, den2);

    omega1 = (omega1 + alpha1 * dt) * damping;
    omega2 = (omega2 + alpha2 * dt) * damping;
    theta1 += omega1 * dt;
    theta2 += omega2 * dt;

    const ox = canvas.width / 2;
    const oy = canvas.height / 3 + 20;

    const x1 = ox + l1 * Math.sin(theta1);
    const y1 = oy + l1 * Math.cos(theta1);
    const x2 = x1 + l2 * Math.sin(theta2);
    const y2 = y1 + l2 * Math.cos(theta2);

    // Draw Links
    ctx.strokeStyle = '#2563eb';
    ctx.lineWidth = 7;
    ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(x1, y1); ctx.stroke();

    ctx.strokeStyle = '#7c3aed';
    ctx.lineWidth = 5;
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();

    // Masses
    ctx.fillStyle = '#1e293b'; ctx.beginPath(); ctx.arc(ox, oy, 8, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#3b82f6'; ctx.beginPath(); ctx.arc(x1, y1, 10, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#a855f7'; ctx.beginPath(); ctx.arc(x2, y2, 8 + m2 * 2, 0, Math.PI * 2); ctx.fill();

    // Gravity vector indicators
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2, y2 + g * 3);
    ctx.stroke();

    // Energy calculation
    const kinetic = 0.5 * m1 * Math.pow(l1 * omega1, 2) + 0.5 * m2 * (Math.pow(l1 * omega1, 2) + Math.pow(l2 * omega2, 2) + 2 * l1 * l2 * omega1 * omega2 * Math.cos(dTheta));
    const potential = -(m1 + m2) * g * l1 * Math.cos(theta1) - m2 * g * l2 * Math.cos(theta2);
    const totalE = kinetic + potential;

    if (stats) {
      stats.innerHTML = `Động năng: <b>T = ${Math.abs(kinetic).toFixed(1)} J</b> | Thế năng: <b>U = ${potential.toFixed(1)} J</b> | Năng lượng cơ học toàn phần: <b>E = ${totalE.toFixed(1)} J</b>`;
    }

    window._forSimHandles['05'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 06: Điều Khiển Chuyển Động (Computed Torque Control vs PID)
// =========================================================================
window.initSim06 = function() {
  const sim = getSimCanvas('sim-canvas-06');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['06']) cancelAnimationFrame(window._forSimHandles['06']);

  const selMode = document.getElementById('sim06-mode');
  const sliderKp = document.getElementById('sim06-kp');
  const sliderKd = document.getElementById('sim06-kd');
  const valKp = document.getElementById('sim06-kp-val');
  const valKd = document.getElementById('sim06-kd-val');
  const stats = document.getElementById('sim06-stats');

  let q = 0, qDot = 0;
  let time = 0;
  const history = [];

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const mode = selMode ? selMode.value : 'ctc';
    const Kp = sliderKp ? parseFloat(sliderKp.value) : 100;
    const Kd = sliderKd ? parseFloat(sliderKd.value) : 20;

    if (valKp) valKp.textContent = Kp.toFixed(0);
    if (valKd) valKd.textContent = Kd.toFixed(1);

    time += 0.02;
    // Desired trajectory: step or sinusoidal
    const qd = 60 * Math.sin(time * 1.5);
    const qdDot = 60 * 1.5 * Math.cos(time * 1.5);
    const qdDDot = -60 * 1.5 * 1.5 * Math.sin(time * 1.5);

    // Plant: J * qDDot + b * qDot + g * sin(q) = tau
    const J = 2.0, b = 0.5, g_term = 15;
    let tau = 0;

    const e = qd - q;
    const eDot = qdDot - qDot;

    if (mode === 'ctc') {
      // Feedback Linearization / Computed Torque: tau = J * (qdDDot + Kd*eDot + Kp*e) + b*qDot + g_term*sin(q)
      const u = qdDDot + Kd * eDot + Kp * e;
      tau = J * u + b * qDot + g_term * Math.sin((q * Math.PI) / 180);
    } else {
      // Independent PID (Linear control without gravity compensation)
      tau = Kp * e + Kd * eDot;
    }

    // Integrate Plant
    const qDDot = (tau - b * qDot - g_term * Math.sin((q * Math.PI) / 180)) / J;
    qDot += qDDot * 0.02;
    q += qDot * 0.02;

    history.push({ qd, q, e });
    if (history.length > 220) history.shift();

    // Render Response Plot
    const ox = 50;
    const midY = canvas.height / 2;
    const w = canvas.width - 70;

    ctx.strokeStyle = dark ? '#334155' : '#cbd5e1';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(ox, midY); ctx.lineTo(ox + w, midY);
    ctx.stroke();

    // Target trajectory q_d
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    history.forEach((pt, idx) => {
      const px = ox + (idx / 220) * w;
      const py = midY - pt.qd * 1.1;
      if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    });
    ctx.stroke();
    ctx.setLineDash([]);

    // Actual tracked trajectory q
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    history.forEach((pt, idx) => {
      const px = ox + (idx / 220) * w;
      const py = midY - pt.q * 1.1;
      if (idx === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Legend
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b'; ctx.fillText('--- Mục tiêu q_d(t)', ox + 20, 25);
    ctx.fillStyle = '#3b82f6'; ctx.fillText('— Đáp ứng thực tế q(t)', ox + 150, 25);

    if (stats) {
      stats.innerHTML = `Thuật toán: <b>${mode === 'ctc' ? 'Computed Torque Control (Bù phi tuyến hoàn hảo)' : 'PID Độc Lập (Bị trễ pha do trọng lực)'}</b> | Sai số bám: <b>|e| = ${Math.abs(e).toFixed(2)}°</b> | Mô-men điều khiển: <b>τ = ${tau.toFixed(1)} Nm</b>`;
    }

    window._forSimHandles['06'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 07: Robot Di Động Bánh Xe & Ràng Buộc Phi Holonomic (Unicycle Model)
// =========================================================================
window.initSim07 = function() {
  const sim = getSimCanvas('sim-canvas-07');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['07']) cancelAnimationFrame(window._forSimHandles['07']);

  const sliderV = document.getElementById('sim07-v');
  const sliderW = document.getElementById('sim07-omega');
  const valV = document.getElementById('sim07-v-val');
  const valW = document.getElementById('sim07-omega-val');
  const stats = document.getElementById('sim07-stats');

  let x = canvas.width / 2, y = canvas.height / 2;
  let theta = 0;
  const trail = [];

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const v = sliderV ? parseFloat(sliderV.value) : 1.2;
    const omega = sliderW ? parseFloat(sliderW.value) : 0.8;

    if (valV) valV.textContent = v.toFixed(1) + ' m/s';
    if (valW) valW.textContent = omega.toFixed(2) + ' rad/s';

    // Nonholonomic Unicycle Kinematics: x' = v cos(theta), y' = v sin(theta), theta' = omega
    theta += omega * 0.03;
    x += v * 28 * Math.cos(theta) * 0.03;
    y += v * 28 * Math.sin(theta) * 0.03;

    // Wrap around screen boundaries
    if (x < 20) x = canvas.width - 20;
    if (x > canvas.width - 20) x = 20;
    if (y < 20) y = canvas.height - 20;
    if (y > canvas.height - 20) y = 20;

    trail.push({ x, y });
    if (trail.length > 180) trail.shift();

    // Draw Trail
    ctx.strokeStyle = dark ? 'rgba(56, 189, 248, 0.45)' : 'rgba(37, 99, 235, 0.45)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    trail.forEach((pt, idx) => {
      if (idx === 0) ctx.moveTo(pt.x, pt.y); else ctx.lineTo(pt.x, pt.y);
    });
    ctx.stroke();

    // Instantaneous Center of Curvature (ICC)
    if (Math.abs(omega) > 0.05) {
      const R = (v * 28) / omega;
      const iccX = x - R * Math.sin(theta);
      const iccY = y + R * Math.cos(theta);

      ctx.strokeStyle = 'rgba(239, 68, 68, 0.3)';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(x, y); ctx.lineTo(iccX, iccY);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#ef4444';
      ctx.beginPath(); ctx.arc(iccX, iccY, 4, 0, Math.PI * 2); ctx.fill();
    }

    // Draw Robot Chassis
    ctx.save();
    ctx.translate(x, y);
    ctx.rotate(theta);

    // Chassis Box
    ctx.fillStyle = dark ? '#1e293b' : '#334155';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(-20, -15, 40, 30, 6);
    ctx.fill();
    ctx.stroke();

    // Left & Right Wheels
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(-12, -18, 24, 6);
    ctx.fillRect(-12, 12, 24, 6);

    // Heading Arrow
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(0, 0); ctx.lineTo(26, 0);
    ctx.stroke();
    ctx.restore();

    if (stats) {
      const R_m = Math.abs(omega) > 0.05 ? (v / omega).toFixed(2) + ' m' : '∞';
      stats.innerHTML = `Vận tốc tịnh tiến: <b>v = ${v.toFixed(1)} m/s</b> | Vận tốc góc: <b>ω = ${omega.toFixed(2)} rad/s</b> | Bán kính quay vòng: <b>R = ${R_m}</b> | Ràng buộc phi holonomic: <b>ẏ·cos(θ) - ẋ·sin(θ) = 0</b> (Không trượt ngang).`;
    }

    window._forSimHandles['07'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 08: Điều Khiển Bằng Thị Giác Robot (Image-Based Visual Servoing - IBVS)
// =========================================================================
window.initSim08 = function() {
  const sim = getSimCanvas('sim-canvas-08');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['08']) cancelAnimationFrame(window._forSimHandles['08']);

  const sliderGain = document.getElementById('sim08-gain');
  const valGain = document.getElementById('sim08-gain-val');
  const stats = document.getElementById('sim08-stats');

  // Desired feature points (Green targets)
  const cx = canvas.width / 2, cy = canvas.height / 2;
  const targetPts = [
    { x: cx - 70, y: cy - 50 },
    { x: cx + 70, y: cy - 50 },
    { x: cx + 70, y: cy + 50 },
    { x: cx - 70, y: cy + 50 }
  ];

  // Current feature points (starting offset)
  let currentPts = [
    { x: cx - 130, y: cy - 90 },
    { x: cx + 20, y: cy - 110 },
    { x: cx + 110, y: cy + 20 },
    { x: cx - 40, y: cy + 80 }
  ];

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const lambda = sliderGain ? parseFloat(sliderGain.value) : 1.5;
    if (valGain) valGain.textContent = lambda.toFixed(1);

    // Sensor Grid
    ctx.strokeStyle = dark ? 'rgba(51, 65, 85, 0.4)' : 'rgba(203, 213, 225, 0.5)';
    ctx.lineWidth = 1;
    ctx.strokeRect(30, 20, canvas.width - 60, canvas.height - 40);

    // Target polygon (Desired feature polygon)
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    targetPts.forEach((p, i) => {
      if (i === 0) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y);
    });
    ctx.closePath();
    ctx.stroke();
    ctx.setLineDash([]);

    targetPts.forEach(p => {
      ctx.fillStyle = '#10b981';
      ctx.beginPath(); ctx.arc(p.x, p.y, 5, 0, Math.PI * 2); ctx.fill();
    });

    // IBVS update law: dot{s} = -lambda * (s - s*)
    let totalError = 0;
    currentPts.forEach((p, i) => {
      const errX = p.x - targetPts[i].x;
      const errY = p.y - targetPts[i].y;
      totalError += Math.sqrt(errX * errX + errY * errY);

      p.x -= lambda * errX * 0.02;
      p.y -= lambda * errY * 0.02;

      // Trajectory from current to target
      ctx.strokeStyle = 'rgba(239, 68, 68, 0.4)';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(p.x, p.y); ctx.lineTo(targetPts[i].x, targetPts[i].y);
      ctx.stroke();
    });

    // Current Feature Polygon
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    currentPts.forEach((p, i) => {
      if (i === 0) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y);
    });
    ctx.closePath();
    ctx.stroke();

    currentPts.forEach(p => {
      ctx.fillStyle = '#3b82f6';
      ctx.beginPath(); ctx.arc(p.x, p.y, 6, 0, Math.PI * 2); ctx.fill();
    });

    // Auto-reset when converged
    if (totalError < 2.0) {
      currentPts = [
        { x: cx - 130 + Math.random() * 40, y: cy - 90 + Math.random() * 30 },
        { x: cx + 20 + Math.random() * 50, y: cy - 110 + Math.random() * 30 },
        { x: cx + 110 + Math.random() * 40, y: cy + 20 + Math.random() * 40 },
        { x: cx - 40 + Math.random() * 30, y: cy + 80 + Math.random() * 30 }
      ];
    }

    if (stats) {
      stats.innerHTML = `Mô hình: <b>Image-Based Visual Servoing (IBVS)</b> | Chuẩn sai số điểm ảnh: <b>||e|| = ${totalError.toFixed(1)} px</b> | Ma trận tương tác L_e hội tụ tiệm cận mũ với hệ số λ = ${lambda.toFixed(1)}.`;
    }

    window._forSimHandles['08'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 09: Hoạch Định Chuyển Động Bằng Trường Thế Năng Nhân Tạo (APF)
// =========================================================================
window.initSim09 = function() {
  const sim = getSimCanvas('sim-canvas-09');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['09']) cancelAnimationFrame(window._forSimHandles['09']);

  const sliderKatt = document.getElementById('sim09-katt');
  const sliderKrep = document.getElementById('sim09-krep');
  const valKatt = document.getElementById('sim09-katt-val');
  const valKrep = document.getElementById('sim09-krep-val');
  const stats = document.getElementById('sim09-stats');

  const goal = { x: canvas.width - 60, y: canvas.height / 2 };
  const obstacles = [
    { x: canvas.width / 2 - 40, y: canvas.height / 2 - 35, r: 28 },
    { x: canvas.width / 2 + 30, y: canvas.height / 2 + 40, r: 24 }
  ];
  let robot = { x: 50, y: canvas.height / 2, vx: 0, vy: 0 };
  const path = [];

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const Katt = sliderKatt ? parseFloat(sliderKatt.value) : 1.2;
    const Krep = sliderKrep ? parseFloat(sliderKrep.value) : 350;

    if (valKatt) valKatt.textContent = Katt.toFixed(1);
    if (valKrep) valKrep.textContent = Krep.toFixed(0);

    // Draw Vector Field arrows on background grid
    ctx.strokeStyle = dark ? 'rgba(56, 189, 248, 0.12)' : 'rgba(37, 99, 235, 0.12)';
    ctx.lineWidth = 1;
    const step = 45;
    for (let gx = 30; gx < canvas.width - 20; gx += step) {
      for (let gy = 25; gy < canvas.height - 20; gy += step) {
        // Attractive gradient
        let fx = -Katt * (gx - goal.x) * 0.01;
        let fy = -Katt * (gy - goal.y) * 0.01;

        // Repulsive gradients
        obstacles.forEach(obs => {
          const dx = gx - obs.x;
          const dy = gy - obs.y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          const rho0 = obs.r + 45;
          if (dist < rho0 && dist > 1) {
            const repMag = Krep * (1 / dist - 1 / rho0) * (1 / (dist * dist));
            fx += repMag * (dx / dist) * 0.8;
            fy += repMag * (dy / dist) * 0.8;
          }
        });

        const fMag = Math.sqrt(fx * fx + fy * fy);
        if (fMag > 0.1) {
          const arrowLen = Math.min(14, fMag * 5);
          const nx = fx / fMag;
          const ny = fy / fMag;
          ctx.beginPath();
          ctx.moveTo(gx, gy);
          ctx.lineTo(gx + nx * arrowLen, gy + ny * arrowLen);
          ctx.stroke();
        }
      }
    }

    // Draw Goal
    ctx.fillStyle = '#10b981';
    ctx.beginPath(); ctx.arc(goal.x, goal.y, 10, 0, Math.PI * 2); ctx.fill();
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('Mục Tiêu', goal.x - 20, goal.y + 22);

    // Draw Obstacles
    obstacles.forEach((obs, idx) => {
      ctx.fillStyle = dark ? 'rgba(239, 68, 68, 0.25)' : 'rgba(239, 68, 68, 0.2)';
      ctx.beginPath(); ctx.arc(obs.x, obs.y, obs.r + 30, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = '#ef4444';
      ctx.beginPath(); ctx.arc(obs.x, obs.y, obs.r, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.fillText('Vật cản ' + (idx + 1), obs.x - 22, obs.y + 4);
    });

    // Robot Dynamics under Potential Gradient
    let fx = -Katt * (robot.x - goal.x) * 0.05;
    let fy = -Katt * (robot.y - goal.y) * 0.05;

    obstacles.forEach(obs => {
      const dx = robot.x - obs.x;
      const dy = robot.y - obs.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      const rho0 = obs.r + 40;
      if (dist < rho0 && dist > 1) {
        const repMag = Krep * (1 / dist - 1 / rho0) * (1 / (dist * dist));
        fx += repMag * (dx / dist) * 2.0;
        fy += repMag * (dy / dist) * 2.0;
      }
    });

    robot.vx = (robot.vx + fx * 0.05) * 0.88;
    robot.vy = (robot.vy + fy * 0.05) * 0.88;
    robot.x += robot.vx;
    robot.y += robot.vy;

    path.push({ x: robot.x, y: robot.y });
    if (path.length > 200) path.shift();

    // Draw Robot Path
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2;
    ctx.beginPath();
    path.forEach((pt, i) => {
      if (i === 0) ctx.moveTo(pt.x, pt.y); else ctx.lineTo(pt.x, pt.y);
    });
    ctx.stroke();

    // Draw Robot
    ctx.fillStyle = '#2563eb';
    ctx.beginPath(); ctx.arc(robot.x, robot.y, 7, 0, Math.PI * 2); ctx.fill();

    // Reset when goal reached
    const dGoal = Math.hypot(robot.x - goal.x, robot.y - goal.y);
    if (dGoal < 12) {
      robot = { x: 50, y: canvas.height / 2, vx: 0, vy: 0 };
      path.length = 0;
    }

    if (stats) {
      stats.innerHTML = `Lực tổng hợp: <b>F = -∇U_att - ∇U_rep</b> | Khoảng cách đích: <b>${dGoal.toFixed(1)} px</b> | Thế hút: <b>k_att = ${Katt.toFixed(1)}</b> | Thế đẩy: <b>k_rep = ${Krep.toFixed(0)}</b>`;
    }

    window._forSimHandles['09'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 10: Điều Khiển Lực & Tương Tác Vật Lý Impedance Control
// =========================================================================
window.initSim10 = function() {
  const sim = getSimCanvas('sim-canvas-10');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['10']) cancelAnimationFrame(window._forSimHandles['10']);

  const sliderK = document.getElementById('sim10-stiffness');
  const sliderD = document.getElementById('sim10-damping');
  const valK = document.getElementById('sim10-stiffness-val');
  const valD = document.getElementById('sim10-damping-val');
  const stats = document.getElementById('sim10-stats');

  let x = 60, v = 0;
  let t = 0;
  const wallX = canvas.width - 130;
  const kWall = 350;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const Kd = sliderK ? parseFloat(sliderK.value) : 120;
    const Dd = sliderD ? parseFloat(sliderD.value) : 18;

    if (valK) valK.textContent = Kd.toFixed(0) + ' N/m';
    if (valD) valD.textContent = Dd.toFixed(1) + ' Ns/m';

    t += 0.02;
    // Nominal trajectory x_d pushes into the wall
    const xd = wallX - 30 + 60 * Math.sin(t * 1.2);
    const vd = 60 * 1.2 * Math.cos(t * 1.2);

    // Contact force from wall
    let fExt = 0;
    if (x > wallX) {
      fExt = -kWall * (x - wallX);
    }

    // Target Impedance Dynamics: M*x'' + Dd*(x' - xd') + Kd*(x - xd) = fExt
    const M = 1.5;
    const acc = (-Dd * (v - vd) - Kd * (x - xd) + fExt) / M;
    v += acc * 0.02;
    x += v * 0.02;

    const cy = canvas.height / 2;

    // Draw Compliant Environment / Wall
    ctx.fillStyle = dark ? 'rgba(239, 68, 68, 0.25)' : 'rgba(239, 68, 68, 0.15)';
    ctx.fillRect(wallX, 20, canvas.width - wallX - 20, canvas.height - 40);
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(wallX, 20); ctx.lineTo(wallX, canvas.height - 20);
    ctx.stroke();

    // Wall hatch lines
    ctx.strokeStyle = dark ? '#7f1d1d' : '#fca5a5';
    ctx.lineWidth = 1;
    for (let hy = 30; hy < canvas.height - 30; hy += 15) {
      ctx.beginPath(); ctx.moveTo(wallX, hy); ctx.lineTo(wallX + 15, hy + 15); ctx.stroke();
    }

    // Nominal position indicator (dotted circle)
    ctx.strokeStyle = '#f59e0b';
    ctx.setLineDash([4, 4]);
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(xd, cy, 18, 0, Math.PI * 2);
    ctx.stroke();
    ctx.setLineDash([]);

    // Virtual spring-damper connecting xd and x
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(xd, cy); ctx.lineTo(x, cy);
    ctx.stroke();

    // Actual Robot Tool
    ctx.fillStyle = '#2563eb';
    ctx.beginPath(); ctx.arc(x, cy, 18, 0, Math.PI * 2); ctx.fill();

    // Force vector arrow if in contact
    if (Math.abs(fExt) > 1) {
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(x, cy);
      ctx.lineTo(x + fExt * 0.6, cy);
      ctx.stroke();
    }

    if (stats) {
      const isContact = x > wallX;
      stats.innerHTML = `Trạng thái: <b>${isContact ? '<span style="color:#ef4444">TIẾP XÚC ĐÀN HỒI (Contact Phase)</span>' : 'CHUYỂN ĐỘNG TỰ DO (Free Motion)'}</b> | Lực tiếp xúc: <b>F_ext = ${Math.abs(fExt).toFixed(1)} N</b> | Độ biến dạng lún: <b>${Math.max(0, x - wallX).toFixed(1)} px</b> | Độ cứng ảo <b>K_d = ${Kd.toFixed(0)} N/m</b>.`;
    }

    window._forSimHandles['10'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 11: Robot Khớp Đàn Hồi (Manipulators with Elastic Joints - Spong Model)
// =========================================================================
window.initSim11 = function() {
  const sim = getSimCanvas('sim-canvas-11');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['11']) cancelAnimationFrame(window._forSimHandles['11']);

  const sliderK = document.getElementById('sim11-k');
  const sliderD = document.getElementById('sim11-damping');
  const valK = document.getElementById('sim11-k-val');
  const valD = document.getElementById('sim11-damping-val');
  const stats = document.getElementById('sim11-stats');

  let qL = 0, qM = 0;
  let vL = 0, vM = 0;
  let t = 0;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const Kj = sliderK ? parseFloat(sliderK.value) : 80;
    const Dj = sliderD ? parseFloat(sliderD.value) : 1.2;

    if (valK) valK.textContent = Kj.toFixed(0) + ' Nm/rad';
    if (valD) valD.textContent = Dj.toFixed(2);

    t += 0.02;
    // Motor is driven with position step/sine: theta_m
    const qM_target = 0.8 * Math.sin(t * 1.5);
    vM = (qM_target - qM) * 12;
    qM += vM * 0.02;

    // Link Dynamics: J_L * qL'' = Kj * (qM - qL) + Dj * (vM - vL) - g * m * l * sin(qL)
    const JL = 1.2;
    const tauElastic = Kj * (qM - qL) + Dj * (vM - vL);
    const accL = tauElastic / JL;
    vL += accL * 0.02;
    qL += vL * 0.02;

    const ox = canvas.width / 2;
    const oy = canvas.height / 2 + 10;
    const linkLen = 110;

    // Motor rotor indicator
    const mx = ox + 40 * Math.cos(qM - Math.PI / 2);
    const my = oy + 40 * Math.sin(qM - Math.PI / 2);

    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.arc(ox, oy, 40, -Math.PI / 2, qM - Math.PI / 2, qM < 0);
    ctx.stroke();

    // Torsional spring coiled arc between Motor and Link
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(ox, oy, 25, qM - Math.PI / 2, qL - Math.PI / 2, qL < qM);
    ctx.stroke();

    // Robot Link
    const lx = ox + linkLen * Math.cos(qL - Math.PI / 2);
    const ly = oy + linkLen * Math.sin(qL - Math.PI / 2);

    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 8;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(ox, oy);
    ctx.lineTo(lx, ly);
    ctx.stroke();

    // Motor Hub and Link Tip
    ctx.fillStyle = '#1e293b';
    ctx.beginPath(); ctx.arc(ox, oy, 14, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#3b82f6';
    ctx.beginPath(); ctx.arc(lx, ly, 10, 0, Math.PI * 2); ctx.fill();

    // Tần số dao động riêng tự nhiên
    const omegaN = Math.sqrt(Kj / JL);

    if (stats) {
      const defl = ((qM - qL) * 180 / Math.PI).toFixed(1);
      stats.innerHTML = `Góc lệch xoắn trục khớp đàn hồi: <b>Δθ = ${defl}°</b> | Mô-men đàn hồi truyền qua khớp: <b>τ_j = ${tauElastic.toFixed(2)} Nm</b> | Tần số cộng hưởng dao động: <b>ω_n = ${omegaN.toFixed(1)} rad/s</b>.`;
    }

    window._forSimHandles['11'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// SIM 12: Thao Tác Hợp Tác Đa Robot & Cầm Nắm Đối Tượng (Cooperative Manipulation)
// =========================================================================
window.initSim12 = function() {
  const sim = getSimCanvas('sim-canvas-12');
  if (!sim) return;
  const { canvas, ctx } = sim;
  if (window._forSimHandles['12']) cancelAnimationFrame(window._forSimHandles['12']);

  const sliderFint = document.getElementById('sim12-fint');
  const sliderMass = document.getElementById('sim12-mass');
  const valFint = document.getElementById('sim12-fint-val');
  const valMass = document.getElementById('sim12-mass-val');
  const stats = document.getElementById('sim12-stats');

  let t = 0;

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const dark = isDarkTheme();

    const fInt = sliderFint ? parseFloat(sliderFint.value) : 25;
    const mass = sliderMass ? parseFloat(sliderMass.value) : 3.0;

    if (valFint) valFint.textContent = fInt.toFixed(0) + ' N';
    if (valMass) valMass.textContent = mass.toFixed(1) + ' kg';

    t += 0.02;

    // Moving cooperative payload object
    const objW = 100, objH = 36;
    const objX = canvas.width / 2 + 35 * Math.sin(t * 1.2);
    const objY = canvas.height / 2 - 20 + 20 * Math.cos(t * 1.2);

    // Left Robot Arm Base and Tip
    const base1X = 60, base1Y = canvas.height - 40;
    const tip1X = objX - objW / 2;
    const tip1Y = objY;

    // Right Robot Arm Base and Tip
    const base2X = canvas.width - 60, base2Y = canvas.height - 40;
    const tip2X = objX + objW / 2;
    const tip2Y = objY;

    // Inverse kinematics 2R representation for Arm 1
    const mid1X = (base1X + tip1X) / 2 - 25;
    const mid1Y = (base1Y + tip1Y) / 2 - 35;

    ctx.strokeStyle = '#2563eb';
    ctx.lineWidth = 7;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(base1X, base1Y); ctx.lineTo(mid1X, mid1Y); ctx.lineTo(tip1X, tip1Y);
    ctx.stroke();

    // Inverse kinematics 2R representation for Arm 2
    const mid2X = (base2X + tip2X) / 2 + 25;
    const mid2Y = (base2Y + tip2Y) / 2 - 35;

    ctx.strokeStyle = '#7c3aed';
    ctx.lineWidth = 7;
    ctx.beginPath();
    ctx.moveTo(base2X, base2Y); ctx.lineTo(mid2X, mid2Y); ctx.lineTo(tip2X, tip2Y);
    ctx.stroke();

    // Robot Bases
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(base1X - 20, base1Y, 40, 20);
    ctx.fillRect(base2X - 20, base2Y, 40, 20);

    // Shared Rigid Payload Object
    ctx.fillStyle = dark ? '#0284c7' : '#0ea5e9';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(objX - objW / 2, objY - objH / 2, objW, objH, 6);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText(`Vật thể ${mass.toFixed(1)}kg`, objX - 35, objY + 4);

    // Contact Grippers
    ctx.fillStyle = '#10b981';
    ctx.fillRect(tip1X - 6, tip1Y - 12, 6, 24);
    ctx.fillRect(tip2X, tip2Y - 12, 6, 24);

    // Internal Force vectors (Squeeze forces f1_int ->, <- f2_int)
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 3;
    // Arrow 1 pushing right
    ctx.beginPath();
    ctx.moveTo(tip1X, tip1Y); ctx.lineTo(tip1X + fInt * 0.8, tip1Y);
    ctx.stroke();
    // Arrow 2 pushing left
    ctx.beginPath();
    ctx.moveTo(tip2X, tip2Y); ctx.lineTo(tip2X - fInt * 0.8, tip2Y);
    ctx.stroke();

    if (stats) {
      stats.innerHTML = `Lực nội bóp giữ (Internal Force): <b>F_int = ${fInt.toFixed(0)} N</b> | Ma trận Grasp Matrix G: Đảm bảo không trượt rơi vật mà không phá hủy cấu trúc | Tải hợp tác: <b>m = ${mass.toFixed(1)} kg</b>.`;
    }

    window._forSimHandles['12'] = requestAnimationFrame(render);
  }
  render();
};

// =========================================================================
// Automatic Simulator Loader on DOMContentLoaded
// =========================================================================
document.addEventListener('DOMContentLoaded', () => {
  for (let i = 1; i <= 12; i++) {
    const pad = i < 10 ? '0' + i : '' + i;
    const canvasId = 'sim-canvas-' + pad;
    if (document.getElementById(canvasId)) {
      const initFn = window['initSim' + pad];
      if (typeof initFn === 'function') {
        initFn();
      }
    }
  }
});
