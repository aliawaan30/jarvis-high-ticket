import React, { useEffect, useRef } from 'react';
import * as THREE from 'three';

// Jarvis voice orb: a sphere of glowing particles that breathes at rest,
// ripples with the member's voice, and swells smoothly while Jarvis speaks.
// levelRef.current: 0..1 voice level. modeRef.current: idle | listening | thinking | speaking.
const NOISE = `vec3 m289(vec3 x){return x-floor(x*(1.0/289.0))*289.0;} vec4 m289(vec4 x){return x-floor(x*(1.0/289.0))*289.0;}
  vec4 perm(vec4 x){return m289(((x*34.0)+1.0)*x);} vec4 tis(vec4 r){return 1.79284291400159-0.85373472095314*r;}
  float snoise(vec3 v){const vec2 C=vec2(1.0/6.0,1.0/3.0);const vec4 D=vec4(0.0,0.5,1.0,2.0);vec3 i=floor(v+dot(v,C.yyy));vec3 x0=v-i+dot(i,C.xxx);vec3 g=step(x0.yzx,x0.xyz);vec3 l=1.0-g;vec3 i1=min(g.xyz,l.zxy);vec3 i2=max(g.xyz,l.zxy);vec3 x1=x0-i1+C.xxx;vec3 x2=x0-i2+C.yyy;vec3 x3=x0-D.yyy;i=m289(i);vec4 p=perm(perm(perm(i.z+vec4(0.0,i1.z,i2.z,1.0))+i.y+vec4(0.0,i1.y,i2.y,1.0))+i.x+vec4(0.0,i1.x,i2.x,1.0));float n_=0.142857142857;vec3 ns=n_*D.wyz-D.xzx;vec4 j=p-49.0*floor(p*ns.z*ns.z);vec4 x_=floor(j*ns.z);vec4 y_=floor(j-7.0*x_);vec4 x=x_*ns.x+ns.yyyy;vec4 y=y_*ns.x+ns.yyyy;vec4 h=1.0-abs(x)-abs(y);vec4 b0=vec4(x.xy,y.xy);vec4 b1=vec4(x.zw,y.zw);vec4 s0=floor(b0)*2.0+1.0;vec4 s1=floor(b1)*2.0+1.0;vec4 sh=-step(h,vec4(0.0));vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;vec3 p0=vec3(a0.xy,h.x);vec3 p1=vec3(a0.zw,h.y);vec3 p2=vec3(a1.xy,h.z);vec3 p3=vec3(a1.zw,h.w);vec4 norm=tis(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;vec4 m=max(0.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.0);m=m*m;return 42.0*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));}`;

export default function JarvisOrb({ levelRef, modeRef, active, onReady }) {
  const readyRef = useRef(onReady);
  useEffect(() => { readyRef.current = onReady; }, [onReady]);
  const canvasRef = useRef(null);
  const activeRef = useRef(active);
  useEffect(() => { activeRef.current = active; }, [active]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return undefined;
    const reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let renderer;
    try {
      renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: 'high-performance' });
    } catch { return undefined; }
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
    const CYAN = new THREE.Color('#3BB8F5'), CYAN_HOT = new THREE.Color('#B5F0FF'), AMBER = new THREE.Color('#F5A93A'), AMBER_HOT = new THREE.Color('#FFE3B0');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(36, 1, 0.1, 100);
    camera.position.set(0, 0, 16);
    const root = new THREE.Group(); scene.add(root);

    const COUNT = window.innerWidth < 700 ? 9000 : 14000;
    const pos = new Float32Array(COUNT * 3), seed = new Float32Array(COUNT);
    for (let i = 0; i < COUNT; i++) {
      const y = 1 - (i / (COUNT - 1)) * 2, r = Math.sqrt(1 - y * y), th = i * 2.399963229728653;
      pos[i * 3] = Math.cos(th) * r; pos[i * 3 + 1] = y; pos[i * 3 + 2] = Math.sin(th) * r; seed[i] = Math.random();
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('aSeed', new THREE.BufferAttribute(seed, 1));
    const U = { uTime: { value: 0 }, uVoice: { value: 0 }, uBreath: { value: 0 }, uThink: { value: 0 }, uColor: { value: CYAN.clone() }, uHot: { value: CYAN_HOT.clone() }, uPx: { value: renderer.getPixelRatio() } };
    const orbMat = new THREE.ShaderMaterial({
      uniforms: U, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending,
      vertexShader: NOISE + `
        uniform float uTime, uVoice, uBreath, uThink, uPx; attribute float aSeed; varying float vGlow; varying float vEdge;
        void main(){
          vec3 p = position;
          float speed = 0.14 + uThink * 0.5 + uVoice * 0.08;
          float n1 = snoise(p * 1.4 + vec3(0.0, uTime * speed, 0.0));
          float n2 = snoise(p * 2.8 - vec3(uTime * speed * 1.2));
          float disp = n1 * (0.06 + uVoice * 0.14 + uBreath * 0.02) + n2 * (0.02 + uVoice * 0.03);
          float r = 1.0 + disp + uBreath * 0.015;
          r += pow(aSeed, 18.0) * (0.25 + uVoice * 0.6);
          vec4 mv = modelViewMatrix * vec4(p * r, 1.0);
          vec3 n = normalize(normalMatrix * p);
          vEdge = pow(1.0 - abs(n.z), 1.6);
          vGlow = clamp(0.35 + disp * 3.0 + vEdge * 0.55 + uVoice * 0.4, 0.0, 1.6);
          gl_PointSize = (1.6 + aSeed * 1.8 + uVoice * 0.8) * uPx * (9.0 / -mv.z);
          gl_Position = projectionMatrix * mv;
        }`,
      fragmentShader: `
        uniform vec3 uColor, uHot; varying float vGlow; varying float vEdge;
        void main(){
          float d = length(gl_PointCoord - 0.5);
          float a = smoothstep(0.5, 0.0, d);
          vec3 c = mix(uColor, uHot, clamp(vGlow - 0.4, 0.0, 1.0));
          gl_FragColor = vec4(c * a * (0.45 + vGlow * 0.6), a * (0.35 + vEdge * 0.5));
        }`,
    });
    const orb = new THREE.Points(geo, orbMat); root.add(orb);
    const glowMat = (inner) => new THREE.ShaderMaterial({
      uniforms: { uColor: { value: CYAN.clone() }, uIntensity: { value: 0.5 } }, transparent: true, depthWrite: false, depthTest: false, blending: THREE.AdditiveBlending,
      vertexShader: 'varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }',
      fragmentShader: inner
        ? 'uniform vec3 uColor; uniform float uIntensity; varying vec2 vUv; void main(){ float d=length(vUv-0.5)*2.0; float a=pow(max(0.0,1.0-d),2.2)*0.55; gl_FragColor=vec4(uColor*a*uIntensity,a*uIntensity); }'
        : 'uniform vec3 uColor; uniform float uIntensity; varying vec2 vUv; void main(){ float d=length(vUv-0.5)*2.0; float ring=exp(-pow((d-0.42)*7.0,2.0))*0.35; float wide=pow(max(0.0,1.0-d),1.6)*0.35; float a=ring+wide; gl_FragColor=vec4(uColor*a*uIntensity,a*uIntensity); }',
    });
    const innerGlow = new THREE.Mesh(new THREE.PlaneGeometry(2.2, 2.2), glowMat(true)); root.add(innerGlow);
    const halo = new THREE.Mesh(new THREE.PlaneGeometry(5.2, 5.2), glowMat(false)); halo.renderOrder = -1; root.add(halo);
    const dg = new THREE.BufferGeometry(); const N = 240; const dp = new Float32Array(N * 3);
    for (let i = 0; i < N; i++) { const r = 3 + Math.random() * 9, a = Math.random() * Math.PI * 2, b = (Math.random() - 0.5) * Math.PI; dp[i * 3] = Math.cos(a) * Math.cos(b) * r; dp[i * 3 + 1] = Math.sin(b) * r * 0.6; dp[i * 3 + 2] = Math.sin(a) * Math.cos(b) * r - 2; }
    dg.setAttribute('position', new THREE.BufferAttribute(dp, 3));
    const dust = new THREE.Points(dg, new THREE.PointsMaterial({ color: 0x3BB8F5, size: 0.025, transparent: true, opacity: 0.35, blending: THREE.AdditiveBlending, depthWrite: false }));
    scene.add(dust);

    const resize = () => { const w = canvas.clientWidth || 1, h = canvas.clientHeight || 1; renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); };
    resize();
    window.addEventListener('resize', resize);

    const drive = { breath: 0, voice: 0, think: 0 };
    let camZ = 16, scale = 0.25, warm = 0, raf = 0, last = performance.now(), t = 0, frames = 0;
    const loop = (now) => {
      const dt = Math.min((now - last) / 1000, 0.1); last = now; t += dt;
      const mode = (modeRef && modeRef.current) || 'idle';
      const raw = 0.5 - 0.5 * Math.cos((t / 4) * Math.PI * 2);
      drive.breath = raw * raw * (3 - 2 * raw);
      drive.think += ((mode === 'thinking' ? 1 : 0) - drive.think) * 0.04;
      const lv = Math.max(0, Math.min(1, (levelRef && levelRef.current) || 0));
      const rate = mode === 'speaking' ? (lv > drive.voice ? 0.045 : 0.02) : (lv > drive.voice ? 0.3 : 0.06);
      drive.voice += (lv - drive.voice) * rate;
      warm += ((mode === 'speaking' ? 1 : 0) - warm) * 0.05;
      const base = CYAN.clone().lerp(AMBER, warm), hot = CYAN_HOT.clone().lerp(AMBER_HOT, warm);
      U.uColor.value.copy(base); U.uHot.value.copy(hot);
      U.uTime.value = reduced ? 0 : t; U.uVoice.value = drive.voice; U.uBreath.value = reduced ? 0 : drive.breath; U.uThink.value = drive.think;
      innerGlow.material.uniforms.uColor.value.copy(base); halo.material.uniforms.uColor.value.copy(base);
      innerGlow.material.uniforms.uIntensity.value = 0.55 + drive.breath * 0.15 + drive.voice * 0.6 + drive.think * 0.2;
      halo.material.uniforms.uIntensity.value = 0.45 + drive.breath * 0.1 + drive.voice * 0.45 + drive.think * 0.15;
      innerGlow.quaternion.copy(camera.quaternion); halo.quaternion.copy(camera.quaternion);
      if (!reduced) {
        orb.rotation.y += dt * (0.06 + drive.think * 0.5 + drive.voice * 0.15);
        orb.rotation.x = Math.sin(t * 0.17) * 0.12;
        dust.rotation.y += dt * 0.008;
        root.position.y = Math.sin(t * 0.21) * 0.04;
      }
      orb.scale.setScalar(1 + drive.voice * 0.06 + drive.breath * 0.015);
      const k = 1 - Math.pow(0.02, dt);
      const camTarget = activeRef.current ? 8.6 : 16, scaleTarget = activeRef.current ? 1 : 0.25;
      camZ += (camTarget - camZ) * k * 0.9; scale += (scaleTarget - scale) * k;
      camera.position.set(reduced ? 0 : Math.sin(t * 0.11) * 0.25, reduced ? 0 : Math.sin(t * 0.08) * 0.15, camZ);
      camera.lookAt(0, -0.6, 0);
      root.scale.setScalar(scale);
      renderer.render(scene, camera);
      frames += 1;
      if (frames === 3) { try { readyRef.current && readyRef.current(); } catch { /* ignore */ } }
      raf = requestAnimationFrame(loop);
    };
    raf = requestAnimationFrame(loop);
    return () => {
      cancelAnimationFrame(raf);
      window.removeEventListener('resize', resize);
      geo.dispose(); orbMat.dispose(); dg.dispose(); dust.material.dispose();
      innerGlow.geometry.dispose(); innerGlow.material.dispose(); halo.geometry.dispose(); halo.material.dispose();
      renderer.dispose();
    };
  }, [levelRef, modeRef]);

  return <canvas ref={canvasRef} aria-hidden="true" style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', display: 'block' }} />;
}
