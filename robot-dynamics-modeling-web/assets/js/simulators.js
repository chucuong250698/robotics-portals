// Interactive 60 FPS Canvas 2D Simulators Suite for Robot Dynamics & Modeling
// Olav Egeland & Jan Tommy Gravdahl: Modeling and Simulation for Automatic Control

document.addEventListener('DOMContentLoaded', () => {
  // Safe helper to get canvas context
  const getCanvas = (id) => {
    const canvas = document.getElementById(id);
    if (!canvas) return null;
    const ctx = canvas.getContext('2d');
    return { canvas, ctx };
  };

  // =========================================================================
  // SIM 01: Linear vs Nonlinear Trajectory Comparison
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-01');
    if (!sim) return;
    const { canvas, ctx } = sim;
    const sliderAmp = document.getElementById('sim01-amp');
    const valAmp = document.getElementById('sim01-amp-val');
    let t = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const amp = sliderAmp ? parseFloat(sliderAmp.value) : 1.0;
      if (valAmp) valAmp.textContent = amp.toFixed(1);

      // Draw Grid & Axes
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(60, canvas.height / 2);
      ctx.lineTo(canvas.width - 20, canvas.height / 2);
      ctx.moveTo(60, 20);
      ctx.lineTo(60, canvas.height - 20);
      ctx.stroke();

      // Legend
      ctx.font = '12px Inter, sans-serif';
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('— Hệ Tuyến Tính Hóa (Taylor)', 80, 35);
      ctx.fillStyle = '#ef4444';
      ctx.fillText('— Hệ Phi Tuyến Thực Tế (sin θ)', 260, 35);

      // Trajectories
      const midY = canvas.height / 2;
      ctx.lineWidth = 2.5;

      // Linear: x_lin(t) = amp * cos(omega * t)
      ctx.strokeStyle = '#38bdf8';
      ctx.beginPath();
      for (let x = 0; x < canvas.width - 80; x += 3) {
        const time = (t + x * 0.03);
        const y = midY - amp * 60 * Math.cos(time);
        if (x === 0) ctx.moveTo(60 + x, y);
        else ctx.lineTo(60 + x, y);
      }
      ctx.stroke();

      // Nonlinear: Duffing / pendulum approx
      ctx.strokeStyle = '#ef4444';
      ctx.beginPath();
      for (let x = 0; x < canvas.width - 80; x += 3) {
        const time = (t + x * 0.03);
        // Nonlinear frequency shift and harmonic distortion
        const nonlinY = midY - amp * 60 * Math.sin(Math.sin(time) * (1 + 0.2 * amp));
        if (x === 0) ctx.moveTo(60 + x, nonlinY);
        else ctx.lineTo(60 + x, nonlinY);
      }
      ctx.stroke();

      t += 0.03;
      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 02: Phase Portrait & Passivity (Mass-Spring-Damper)
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-02');
    if (!sim) return;
    const { canvas, ctx } = sim;
    const sliderDamping = document.getElementById('sim02-damping');
    const valDamping = document.getElementById('sim02-damping-val');
    let x = 120, v = 0;

    const render = () => {
      ctx.fillStyle = 'rgba(15, 23, 42, 0.15)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const d = sliderDamping ? parseFloat(sliderDamping.value) : 0.2;
      if (valDamping) valDamping.textContent = d.toFixed(2);

      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      // Physics: x'' + d*x' + k*x = 0
      const k = 0.015;
      const acc = -k * x - d * 0.05 * v;
      v += acc;
      x += v;

      // Draw Phase Plane (x, v)
      ctx.fillStyle = '#10b981';
      ctx.shadowColor = '#10b981';
      ctx.shadowBlur = 10;
      ctx.beginPath();
      ctx.arc(cx + x, cy - v * 8, 5, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;

      // Energy level
      const H = 0.5 * k * x * x + 0.5 * v * v;
      const stats = document.getElementById('sim02-stats');
      if (stats) {
        stats.innerHTML = `Hàm lưu trữ năng lượng Hamiltonian: <b>H = ${H.toFixed(2)} J</b> | Trạng thái: [x=${(x / 100).toFixed(2)} m, v=${(v / 10).toFixed(2)} m/s] (Hệ thụ động tiêu tán dần về gốc [0, 0]).`;
      }

      if (Math.abs(x) < 0.5 && Math.abs(v) < 0.05) {
        x = 120;
        v = 0;
      }

      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 03: Two-Mass Elastic Shaft Drive Resonance
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-03');
    if (!sim) return;
    const { canvas, ctx } = sim;
    const sliderK = document.getElementById('sim03-k');
    const valK = document.getElementById('sim03-k-val');
    let thetaM = 0, thetaL = 0, vM = 0, vL = 0, time = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const k_shaft = sliderK ? parseFloat(sliderK.value) : 50;
      if (valK) valK.textContent = k_shaft.toFixed(0);

      // Motor torque input: step + sine
      const tau = Math.sin(time * 2) > 0 ? 5 : -5;
      const d_shaft = 1.2;

      // Two-mass dynamics
      const torque_spring = k_shaft * 0.005 * (thetaM - thetaL) + d_shaft * (vM - vL);
      vM += (tau - torque_spring) * 0.015;
      vL += (torque_spring - 0.5 * vL) * 0.015;
      thetaM += vM;
      thetaL += vL;
      time += 0.03;

      // Draw Motor & Load Wheels
      const cx1 = 250, cx2 = 550, cy = canvas.height / 2;
      const r = 60;

      // Shaft
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 12;
      ctx.beginPath();
      ctx.moveTo(cx1, cy);
      ctx.lineTo(cx2, cy);
      ctx.stroke();

      // Motor Wheel
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.arc(cx1, cy, r, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#0284c7';
      ctx.lineWidth = 4;
      ctx.stroke();
      // Pointer
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(cx1, cy);
      ctx.lineTo(cx1 + r * Math.cos(thetaM), cy + r * Math.sin(thetaM));
      ctx.stroke();

      // Load Wheel
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(cx2, cy, r, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#d97706';
      ctx.lineWidth = 4;
      ctx.stroke();
      // Pointer
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(cx2, cy);
      ctx.lineTo(cx2 + r * Math.cos(thetaL), cy + r * Math.sin(thetaL));
      ctx.stroke();

      // Labels
      ctx.font = '14px Inter, sans-serif';
      ctx.fillStyle = '#f1f5f9';
      ctx.fillText('Động cơ J_M', cx1 - 40, cy + r + 30);
      ctx.fillText('Tải đàn hồi J_L', cx2 - 40, cy + r + 30);
      const twist = Math.abs(thetaM - thetaL) * 180 / Math.PI;
      ctx.fillText(`Độ vặn trục: ${twist.toFixed(1)}°`, (cx1 + cx2) / 2 - 50, cy - 25);

      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 04: Hydraulic Cylinder & Pressure Wave
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-04');
    if (!sim) return;
    const { canvas, ctx } = sim;
    const sliderP = document.getElementById('sim04-p');
    let waveOffset = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const press = sliderP ? parseFloat(sliderP.value) : 150; // bar

      const cy = canvas.height / 2;
      // Cylinder chamber
      ctx.fillStyle = '#1e293b';
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 4;
      ctx.fillRect(150, cy - 70, 450, 140);
      ctx.strokeRect(150, cy - 70, 450, 140);

      // Piston
      const pistonX = 320 + 80 * Math.sin(waveOffset * 0.05);
      ctx.fillStyle = '#475569';
      ctx.fillRect(pistonX, cy - 65, 40, 130);
      // Rod
      ctx.fillStyle = '#94a3b8';
      ctx.fillRect(pistonX + 40, cy - 20, 280, 40);

      // Fluid pressure color
      ctx.fillStyle = `rgba(2, 132, 199, ${Math.min(0.8, press / 250)})`;
      ctx.fillRect(154, cy - 66, pistonX - 154, 132);

      // Wave pattern
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 160; x < pistonX; x += 10) {
        const y = cy + 20 * Math.sin((x - waveOffset * 10) * 0.08);
        if (x === 160) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      waveOffset += 0.5;
      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 05: LuGre Dynamic Friction (Stick-Slip & Stribeck Curve)
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-05');
    if (!sim) return;
    const { canvas, ctx } = sim;
    const sliderV = document.getElementById('sim05-v');
    const valV = document.getElementById('sim05-v-val');
    let z = 0, blockX = 200, time = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const v_drive = sliderV ? parseFloat(sliderV.value) : 0.05;
      if (valV) valV.textContent = v_drive.toFixed(2);

      // Stribeck function: g(v) = Fc + (Fs - Fc)*exp(-(v/vs)^2)
      const Fc = 20, Fs = 40, vs = 0.08;
      const g_v = Fc + (Fs - Fc) * Math.exp(-Math.pow(v_drive / vs, 2));

      // LuGre bristle deflection: dz/dt = v - sigma0*|v|/g(v) * z
      const sigma0 = 1000, sigma1 = 10, sigma2 = 5;
      const dz = v_drive - (sigma0 * Math.abs(v_drive) / g_v) * z;
      z += dz * 0.016;
      const F_friction = sigma0 * z + sigma1 * dz + sigma2 * v_drive;

      // Block motion with stick-slip
      if (Math.abs(v_drive) < 0.08) {
        // Stick-slip jerking
        blockX += Math.sin(time * 15) > 0.8 ? v_drive * 120 : v_drive * 10;
      } else {
        blockX += v_drive * 40;
      }
      if (blockX > canvas.width - 150) blockX = 100;
      time += 0.03;

      // Draw surface & Block
      const groundY = 280;
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(50, groundY);
      ctx.lineTo(canvas.width - 50, groundY);
      ctx.stroke();

      // Bristles (vi mô lông tơ)
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 1.5;
      for (let bx = blockX; bx < blockX + 100; bx += 8) {
        ctx.beginPath();
        ctx.moveTo(bx, groundY);
        ctx.lineTo(bx - z * 800, groundY - 15);
        ctx.stroke();
      }

      // Block
      ctx.fillStyle = '#3b82f6';
      ctx.fillRect(blockX, groundY - 80, 100, 65);
      ctx.fillStyle = '#ffffff';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('Khối m', blockX + 28, groundY - 45);

      // Force Vector
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(blockX, groundY - 45);
      ctx.lineTo(blockX - F_friction * 1.5, groundY - 45);
      ctx.stroke();

      const stats = document.getElementById('sim05-stats');
      if (stats) {
        stats.innerHTML = `Vận tốc: <b>${v_drive.toFixed(2)} m/s</b> | Lực ma sát LuGre: <b>F_f = ${F_friction.toFixed(1)} N</b> | Độ võng lông tơ: <b>z = ${(z * 1e3).toFixed(2)} mm</b>.`;
      }

      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 06: Gyroscopic Precession & 3D Kinematics
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-06');
    if (!sim) return;
    const { canvas, ctx } = sim;
    let spin = 0, prec = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      // Precession circle
      const r_prec = 140;
      const px = cx + r_prec * Math.cos(prec);
      const py = cy + r_prec * 0.4 * Math.sin(prec);

      // Support pivot
      ctx.fillStyle = '#94a3b8';
      ctx.beginPath();
      ctx.moveTo(cx, cy + 120);
      ctx.lineTo(cx - 30, cy + 160);
      ctx.lineTo(cx + 30, cy + 160);
      ctx.closePath();
      ctx.fill();

      // Gyro Shaft
      ctx.strokeStyle = '#cbd5e1';
      ctx.lineWidth = 6;
      ctx.beginPath();
      ctx.moveTo(cx, cy + 120);
      ctx.lineTo(px, py);
      ctx.stroke();

      // Spinning Flywheel Disc
      ctx.save();
      ctx.translate(px, py);
      ctx.rotate(prec + Math.PI / 2);
      ctx.scale(1, 0.4);
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.arc(0, 0, 50, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#0284c7';
      ctx.lineWidth = 4;
      ctx.stroke();
      // Spin marker
      ctx.strokeStyle = '#ffffff';
      ctx.beginPath();
      ctx.moveTo(-50 * Math.cos(spin), -50 * Math.sin(spin));
      ctx.lineTo(50 * Math.cos(spin), 50 * Math.sin(spin));
      ctx.stroke();
      ctx.restore();

      spin += 0.4;
      prec += 0.02;
      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 07: Rotary Inverted Pendulum (Furuta Pendulum)
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-07');
    if (!sim) return;
    const { canvas, ctx } = sim;
    let phi = 0, theta = Math.PI - 0.2, vPhi = 0, vTheta = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      // Horizontal Arm (length L1 = 120)
      const L1 = 120;
      phi += 0.02;
      const armX = cx + L1 * Math.cos(phi);
      const armY = cy + L1 * 0.35 * Math.sin(phi);

      // Pendulum dynamics around upright
      const g = 9.81, L2 = 100;
      const accTheta = (g / (L2 * 0.01)) * Math.sin(theta) - 0.05 * vTheta;
      vTheta += accTheta * 0.016;
      theta += vTheta * 0.016;

      // Clamp or stabilize near top
      if (Math.abs(theta) < 0.35) {
        theta *= 0.98; // stabilizing control
      }

      const penX = armX + L2 * Math.sin(theta) * Math.sin(phi);
      const penY = armY - L2 * Math.cos(theta);

      // Draw Base & Arm
      ctx.fillStyle = '#475569';
      ctx.beginPath();
      ctx.arc(cx, cy, 18, 0, Math.PI * 2);
      ctx.fill();

      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 6;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(armX, armY);
      ctx.stroke();

      // Pendulum Rod
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(armX, armY);
      ctx.lineTo(penX, penY);
      ctx.stroke();

      // Pendulum Tip Bob
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(penX, penY, 12, 0, Math.PI * 2);
      ctx.fill();

      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 08: 2-DoF Planar Robot Arm (Lagrange Dynamics)
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-08');
    if (!sim) return;
    const { canvas, ctx } = sim;
    let q1 = 0.5, q2 = -1.0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const baseX = canvas.width / 2;
      const baseY = canvas.height - 60;
      const l1 = 130, l2 = 110;

      q1 += 0.015 * Math.sin(Date.now() * 0.002);
      q2 += 0.02 * Math.cos(Date.now() * 0.003);

      const j1X = baseX + l1 * Math.sin(q1);
      const j1Y = baseY - l1 * Math.cos(q1);

      const j2X = j1X + l2 * Math.sin(q1 + q2);
      const j2Y = j1Y - l2 * Math.cos(q1 + q2);

      // Base
      ctx.fillStyle = '#334155';
      ctx.fillRect(baseX - 40, baseY, 80, 30);

      // Link 1
      ctx.strokeStyle = '#3b82f6';
      ctx.lineWidth = 10;
      ctx.beginPath();
      ctx.moveTo(baseX, baseY);
      ctx.lineTo(j1X, j1Y);
      ctx.stroke();

      // Joint 1
      ctx.fillStyle = '#f1f5f9';
      ctx.beginPath();
      ctx.arc(j1X, j1Y, 10, 0, Math.PI * 2);
      ctx.fill();

      // Link 2
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 8;
      ctx.beginPath();
      ctx.moveTo(j1X, j1Y);
      ctx.lineTo(j2X, j2Y);
      ctx.stroke();

      // End-Effector
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(j2X, j2Y, 12, 0, Math.PI * 2);
      ctx.fill();

      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 09: Non-Holonomic Wheeled Robot (Kane's Method)
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-09');
    if (!sim) return;
    const { canvas, ctx } = sim;
    let rx = 200, ry = 200, theta = 0;

    const render = () => {
      ctx.fillStyle = 'rgba(15, 23, 42, 0.1)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const v = 2.0;
      const w = 0.025 * Math.sin(Date.now() * 0.001);
      theta += w;
      rx += v * Math.cos(theta);
      ry += v * Math.sin(theta);

      if (rx < 60 || rx > canvas.width - 60) theta = Math.PI - theta;
      if (ry < 60 || ry > canvas.height - 60) theta = -theta;

      ctx.save();
      ctx.translate(rx, ry);
      ctx.rotate(theta);

      // Chassis
      ctx.fillStyle = '#f59e0b';
      ctx.fillRect(-25, -20, 50, 40);
      // Wheels
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(-15, -26, 30, 6);
      ctx.fillRect(-15, 20, 30, 6);
      // Front caster
      ctx.fillStyle = '#e2e8f0';
      ctx.beginPath();
      ctx.arc(20, 0, 5, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();

      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 10: Port-Hamiltonian Energy Shaping Control
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-10');
    if (!sim) return;
    const { canvas, ctx } = sim;
    let t = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      // Draw Energy Bowl H_d(q, p)
      ctx.strokeStyle = '#6366f1';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = -150; x <= 150; x += 10) {
        const y = 0.004 * x * x;
        if (x === -150) ctx.moveTo(cx + x, cy + 80 - y);
        else ctx.lineTo(cx + x, cy + 80 - y);
      }
      ctx.stroke();

      // Ball sliding down potential bowl to minimum
      const pos = 120 * Math.exp(-t * 0.05) * Math.cos(t * 0.3);
      const bY = cy + 80 - 0.004 * pos * pos;

      ctx.fillStyle = '#10b981';
      ctx.shadowColor = '#10b981';
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.arc(cx + pos, bY - 10, 10, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;

      t += 0.4;
      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 11: Flexible Beam Mode Shapes (FEM Vibrations)
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-11');
    if (!sim) return;
    const { canvas, ctx } = sim;
    let t = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const startX = 100, endX = canvas.width - 100, cy = canvas.height / 2;

      // Clamp fixture
      ctx.fillStyle = '#64748b';
      ctx.fillRect(startX - 20, cy - 60, 20, 120);

      // Beam oscillation: mode 1 (fundamental) + mode 2
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 6;
      ctx.beginPath();
      for (let x = startX; x <= endX; x += 5) {
        const normX = (x - startX) / (endX - startX);
        // Cantilever mode shape approx
        const y = 45 * Math.sin(t * 0.05) * Math.pow(normX, 2) + 
                  15 * Math.sin(t * 0.15) * (Math.pow(normX, 2) - 1.5 * Math.pow(normX, 3));
        if (x === startX) ctx.moveTo(x, cy);
        else ctx.lineTo(x, cy + y);
      }
      ctx.stroke();

      t += 0.8;
      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 12: Flow Around Submarine Body (Navier-Stokes Balance)
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-12');
    if (!sim) return;
    const { canvas, ctx } = sim;
    const particles = Array.from({ length: 60 }, () => ({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      v: 2 + Math.random() * 2
    }));

    const render = () => {
      ctx.fillStyle = 'rgba(15, 23, 42, 0.2)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      // Submarine hull
      ctx.fillStyle = '#475569';
      ctx.beginPath();
      ctx.ellipse(cx, cy, 90, 35, 0, 0, Math.PI * 2);
      ctx.fill();

      // Streamline particles
      ctx.fillStyle = '#38bdf8';
      particles.forEach(p => {
        p.x += p.v;
        // Deflect around body
        const dx = p.x - cx;
        const dy = p.y - cy;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 80) {
          p.y += dy > 0 ? 2 : -2;
        }

        if (p.x > canvas.width) {
          p.x = 0;
          p.y = Math.random() * canvas.height;
        }

        ctx.fillRect(p.x, p.y, 4, 2);
      });

      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 13: Greitzer Compressor Surge Limit Cycle
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-13');
    if (!sim) return;
    const { canvas, ctx } = sim;
    let phi = 0.5, psi = 1.0, time = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      // Greitzer characteristic curve Psi_c(Phi)
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = -150; x <= 150; x += 5) {
        const f = x / 100;
        const p = 1.2 + 0.8 * f - 1.2 * Math.pow(f, 3);
        const scrX = cx + x * 1.5;
        const scrY = cy - (p - 1.0) * 120;
        if (x === -150) ctx.moveTo(scrX, scrY);
        else ctx.lineTo(scrX, scrY);
      }
      ctx.stroke();

      // Surge limit cycle oscillation
      phi = 0.4 * Math.sin(time * 0.08);
      psi = 1.2 + 0.3 * Math.cos(time * 0.08);

      const ptX = cx + (phi * 100) * 1.5;
      const ptY = cy - (psi - 1.0) * 120;

      ctx.fillStyle = '#ef4444';
      ctx.shadowColor = '#ef4444';
      ctx.shadowBlur = 10;
      ctx.beginPath();
      ctx.arc(ptX, ptY, 8, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;

      time += 0.5;
      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 14: Symplectic Integrator vs RK4 (Energy Drift)
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-14');
    if (!sim) return;
    const { canvas, ctx } = sim;
    let t = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const midY = canvas.height / 2;

      // Draw Energy Baseline
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(80, midY);
      ctx.lineTo(canvas.width - 20, midY);
      ctx.stroke();

      ctx.font = '12px Inter, sans-serif';
      ctx.fillStyle = '#10b981';
      ctx.fillText('— Tích phân Symplectic Euler (Năng lượng dao động có chặn)', 100, 35);
      ctx.fillStyle = '#ef4444';
      ctx.fillText('— Tích phân RK4 (Trôi dạt năng lượng theo thời gian dài)', 100, 60);

      // Symplectic line (bounded oscillations around zero error)
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = 0; x < canvas.width - 100; x += 4) {
        const y = midY + 12 * Math.sin((t + x * 0.05) * 2);
        if (x === 0) ctx.moveTo(80 + x, y);
        else ctx.lineTo(80 + x, y);
      }
      ctx.stroke();

      // RK4 line (slow drift upward / dissipating)
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = 0; x < canvas.width - 100; x += 4) {
        const drift = 0.08 * x;
        const y = midY - drift + 8 * Math.cos((t + x * 0.05) * 2);
        if (x === 0) ctx.moveTo(80 + x, y);
        else ctx.lineTo(80 + x, y);
      }
      ctx.stroke();

      t += 0.03;
      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 15: DAEs Index-3 Baumgarte Stabilization (Pendulum Length)
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-15');
    if (!sim) return;
    const { canvas, ctx } = sim;
    let angle = 0.8, vAngle = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = canvas.width / 2;
      const cy = 60;
      const L = 160;

      // Dynamics
      const acc = -0.05 * Math.sin(angle);
      vAngle += acc;
      angle += vAngle;

      const px = cx + L * Math.sin(angle);
      const py = cy + L * Math.cos(angle);

      // Rigid Rod Constraint
      ctx.strokeStyle = '#e2e8f0';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(px, py);
      ctx.stroke();

      // Bob
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.arc(px, py, 14, 0, Math.PI * 2);
      ctx.fill();

      // Pivot
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(cx, cy, 6, 0, Math.PI * 2);
      ctx.fill();

      requestAnimationFrame(render);
    };
    render();
  })();

  // =========================================================================
  // SIM 16: Pinocchio RNEA Gravity Compensation (ROS 2 Control)
  // =========================================================================
  (() => {
    const sim = getCanvas('sim-canvas-16');
    if (!sim) return;
    const { canvas, ctx } = sim;
    let q = 0.8, tauComp = 0;

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const bx = canvas.width / 2;
      const by = canvas.height / 2 + 50;
      const len = 140;

      // User target angle or dynamic motion
      q = 0.7 + 0.3 * Math.sin(Date.now() * 0.002);
      tauComp = 15.0 * Math.sin(q); // m * g * l * sin(q)

      const tipX = bx + len * Math.sin(q);
      const tipY = by - len * Math.cos(q);

      // Link
      ctx.strokeStyle = '#3b82f6';
      ctx.lineWidth = 12;
      ctx.beginPath();
      ctx.moveTo(bx, by);
      ctx.lineTo(tipX, tipY);
      ctx.stroke();

      // Tip mass
      ctx.fillStyle = '#10b981';
      ctx.beginPath();
      ctx.arc(tipX, tipY, 15, 0, Math.PI * 2);
      ctx.fill();

      // Torque arrow
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.arc(bx, by, 40, -Math.PI / 2, -Math.PI / 2 + q);
      ctx.stroke();

      const stats = document.getElementById('sim16-stats');
      if (stats) {
        stats.innerHTML = `Góc khớp q: <b>${(q * 180 / Math.PI).toFixed(1)}°</b> | Mô-men bù trọng lực Pinocchio RNEA: <b>τ_g = ${tauComp.toFixed(2)} N.m</b> (Tần số điều khiển 1000 Hz).`;
      }

      requestAnimationFrame(render);
    };
    render();
  })();
});
