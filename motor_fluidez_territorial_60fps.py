# -*- coding: utf-8 -*-
"""
motor_fluidez_territorial_60fps.py — ESTUDIO TERRITORIAL INTEGRAL A 60 FPS (9 MÓDULOS + LECTURA VIVA + HOJA MECÁNICA)
Asignatura: Desarrollo y Gestión Territorial — Universidad de Los Lagos (Prof. Claudio Mancilla)
Renderiza en el navegador (HTML5 SVG + JavaScript sin lag de servidor):
  1) Von Thünen: Editor libre de ecuaciones LR(d) + Gradiente 2D + Mapa de Anillos Concéntricos.
  2) Alfred Weber: Triángulo Locacional, Índice de Materiales (IM), Weiszfeld e Isodápana Crítica.
  3) Paul Krugman (1991): Bifurcación Centro-Periferia, Umbral τ* y Macrocefalia Regional.
  4) Perroux, Myrdal y Hirschman: Multiplicador en 5 Rondas y Balanza Spread vs. Backwash.
  5) Christaller (Umbral/Alcance) + Granovetter (Vínculos Fuertes vs. Débiles y Lock-in).
  6) Disparidades REAT y OT: Curva de Lorenz, Gini, Entropía de Theil y Primacía Urbana (IP4).
  7) Redes Empresariales (Dini 2010): Animación 60 FPS de 7 topologías, Densidad D y Gradiente GC.
  8) Hoja de Entrenamiento Mecánico Territorial: 16 Fórmulas Puras + 6 Esqueletos SVG + Modo Ciego.
"""

import streamlit.components.v1 as components


HTML_TERRITORIAL_60FPS = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<style>
  * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; }
  body { margin: 0; padding: 0; background: #F8FAFC; color: #0F172A; }
  .wrap { max-width: 1240px; margin: 0 auto; padding: 4px 4px 14px 4px; }
  .top-tabs {
    display: flex; gap: 6px; margin-bottom: 11px; flex-wrap: wrap;
    background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 8px;
  }
  .tab-btn {
    border: 1px solid #CBD5E1; background: #F8FAFC; color: #334155;
    padding: 6px 11px; border-radius: 6px; font-weight: 700; font-size: 12px;
    cursor: pointer; transition: all 0.14s ease;
  }
  .tab-btn:hover { border-color: #1D4ED8; color: #1D4ED8; background: #EFF6FF; }
  .tab-btn.active { background: #0F172A; color: #FFFFFF; border-color: #0F172A; }
  .panel { display: none; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 14px 16px; }
  .panel.active { display: block; }
  .sec-title {
    font-size: 13px; font-weight: 700; color: #1E3A8A;
    background: #DBEAFE; border-left: 4px solid #1D4ED8;
    padding: 7px 12px; border-radius: 4px; margin-bottom: 10px;
    display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;
  }
  .btn-bar { display: flex; gap: 6px; flex-wrap: wrap; }
  .act-btn {
    border: 1px solid #94A3B8; background: #FFFFFF; color: #0F172A;
    padding: 5px 10px; border-radius: 5px; font-size: 11.5px; font-weight: 700; cursor: pointer;
  }
  .act-btn:hover { background: #EFF6FF; border-color: #1D4ED8; color: #1D4ED8; }
  .act-btn.primary { background: #1D4ED8; color: #FFFFFF; border-color: #1D4ED8; }
  .act-btn.primary:hover { background: #1E40AF; }
  .sliders-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(185px, 1fr)); gap: 10px; margin-bottom: 11px; }
  .sl-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px; padding: 8px 10px; }
  .sl-head { display: flex; justify-content: space-between; font-size: 11.5px; font-weight: 700; color: #1E293B; margin-bottom: 4px; gap: 4px; }
  .sl-val { color: #1D4ED8; font-family: Consolas, monospace; white-space: nowrap; }
  .sl-delta { font-size: 10.5px; font-weight: 700; margin-left: 4px; }
  .d-up { color: #15803D; }
  .d-down { color: #DC2626; }
  .d-eq { color: #64748B; }
  input[type="range"] { width: 100%; accent-color: #1D4ED8; cursor: pointer; margin: 2px 0; }
  .kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 8px; margin-bottom: 10px; }
  .kpi { background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 3px solid #0F172A; border-radius: 5px; padding: 7px 10px; }
  .kpi-lbl { font-size: 11px; color: #475569; font-weight: 600; }
  .kpi-val { font-size: 14.5px; font-weight: 800; color: #0F172A; font-family: Consolas, monospace; margin-top: 2px; }
  .kpi-sub { font-size: 11px; color: #334155; margin-top: 1px; }
  .svg-box { width: 100%; border: 1px solid #E2E8F0; border-radius: 6px; background: #FFFFFF; overflow: hidden; }
  svg { width: 100%; height: auto; display: block; }
  .legend-bar {
    display: flex; gap: 14px; flex-wrap: wrap; font-size: 11.5px; color: #334155;
    margin-top: 8px; padding: 6px 10px; background: #F8FAFC; border-radius: 5px; border: 1px solid #E2E8F0;
  }
  .leg-item { display: inline-flex; align-items: center; gap: 5px; font-weight: 600; }
  .sw { width: 12px; height: 12px; border-radius: 2px; display: inline-block; }
  .sw-line { width: 16px; height: 3px; display: inline-block; }
  .enun-box {
    background: #FFFFFF; border: 1px solid #CBD5E1; border-left: 4px solid #0F172A;
    border-radius: 6px; padding: 9px 13px; margin-bottom: 10px; font-size: 12.1px; line-height: 1.46; color: #1E293B;
  }
  .enun-box summary {
    cursor: pointer; font-weight: 800; color: #0F172A; font-size: 12.3px; list-style: none;
    display: flex; justify-content: space-between; align-items: center;
  }
  .enun-box summary::-webkit-details-marker { display: none; }
  .enun-badge { font-size: 10.5px; font-weight: 700; color: #1E3A8A; background: #DBEAFE; padding: 2px 8px; border-radius: 10px; }
  .enun-body { margin-top: 7px; border-top: 1px dashed #CBD5E1; padding-top: 7px; }
  .eq-editor-bar {
    display: grid; grid-template-columns: 1fr 1fr 1fr auto; gap: 8px; align-items: end;
    background: #F1F5F9; border: 1px solid #CBD5E1; border-radius: 6px; padding: 9px 11px; margin-bottom: 10px;
  }
  @media (max-width: 820px) { .eq-editor-bar { grid-template-columns: 1fr; } }
  .eq-field label { display: block; font-size: 11px; font-weight: 700; color: #1E293B; margin-bottom: 3px; }
  .eq-input {
    width: 100%; padding: 6px 9px; border: 1px solid #94A3B8; border-radius: 5px;
    font-family: Consolas, monospace; font-size: 12px; font-weight: 700; color: #0F172A; background: #FFFFFF;
  }
  .eq-input:focus { outline: 2px solid #1D4ED8; border-color: #1D4ED8; }
  .eq-err { font-size: 11px; font-weight: 700; color: #DC2626; margin-top: 4px; display: none; }
  .sol-box {
    margin-top: 8px; background: #F8FAFC; border: 1px solid #CBD5E1; border-left: 4px solid #15803D;
    border-radius: 6px; padding: 9px 12px; font-size: 12px; line-height: 1.48; color: #0F172A;
    font-family: Consolas, monospace;
  }
  .sol-box b { color: #1E3A8A; }

  /* === HOJA DE ENTRENAMIENTO MECÁNICO === */
  .mec-toolbar {
    display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;
    background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 6px; padding: 8px 12px; margin-bottom: 10px;
  }
  .mec-filters { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px; }
  .flt-btn {
    border: 1px solid #CBD5E1; background: #FFFFFF; color: #334155;
    padding: 4px 10px; border-radius: 14px; font-size: 11.5px; font-weight: 700; cursor: pointer;
  }
  .flt-btn.active { background: #1E293B; color: #FFFFFF; border-color: #1E293B; }
  .pill-score {
    background: #0F172A; color: #FFFFFF; padding: 5px 11px; border-radius: 14px;
    font-size: 12px; font-weight: 700; font-family: Consolas, monospace;
  }
  .mec-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px; margin-bottom: 14px; }
  @media (max-width: 780px) { .mec-grid { grid-template-columns: 1fr; } }
  .f-card {
    border: 1px solid #CBD5E1; border-left: 3.5px solid #1E293B; border-radius: 6px;
    background: #FFFFFF; padding: 9px 11px; transition: border-color 0.15s ease;
  }
  .f-card.mastered { border-left-color: #15803D; background: #F0FDF4; }
  .f-head { display: flex; justify-content: space-between; align-items: center; gap: 6px; margin-bottom: 5px; }
  .f-title { font-size: 12px; font-weight: 800; color: #0F172A; }
  .f-cat { font-size: 10px; font-weight: 700; color: #475569; background: #E2E8F0; padding: 2px 6px; border-radius: 4px; }
  .chk-btn {
    border: 1px solid #94A3B8; background: #FFFFFF; color: #475569; width: 22px; height: 22px;
    border-radius: 4px; font-size: 12px; font-weight: 800; cursor: pointer; line-height: 1; padding: 0;
  }
  .f-card.mastered .chk-btn { background: #15803D; color: #FFFFFF; border-color: #15803D; }
  .f-body {
    background: #F8FAFC; border: 1px dashed #CBD5E1; border-radius: 4px; padding: 7px 9px;
    cursor: pointer; min-height: 44px; display: flex; flex-direction: column; justify-content: center;
  }
  .f-eq {
    font-family: "Cambria Math", "Times New Roman", Georgia, serif;
    font-size: 14.5px; font-weight: 700; color: #0F172A; letter-spacing: 0.2px;
    display: flex; align-items: center; flex-wrap: wrap; gap: 4px;
  }
  .f-rule { font-size: 11px; color: #334155; margin-top: 5px; line-height: 1.32; }
  .frac { display: inline-flex; flex-direction: column; align-items: center; vertical-align: middle; margin: 0 2px; font-size: 0.88em; line-height: 1.1; }
  .frac .num { border-bottom: 1.4px solid #0F172A; padding: 0 3px 1px 3px; text-align: center; }
  .frac .den { padding: 1px 3px 0 3px; text-align: center; }
  .blind-cover { display: none; font-size: 11.5px; font-weight: 700; color: #1D4ED8; text-align: center; padding: 4px 0; }
  .blind-mode .f-card:not(.revealed) .f-eq,
  .blind-mode .f-card:not(.revealed) .f-rule { display: none; }
  .blind-mode .f-card:not(.revealed) .blind-cover { display: block; }
  .skel-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; }
  @media (max-width: 860px) { .skel-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
  @media (max-width: 560px) { .skel-grid { grid-template-columns: 1fr; } }
  .s-card { border: 1px solid #CBD5E1; border-radius: 6px; background: #FFFFFF; padding: 8px 9px; cursor: pointer; }
  .s-title { font-size: 11.5px; font-weight: 800; color: #0F172A; margin-bottom: 4px; }
  .s-sub { font-size: 10.5px; color: #475569; margin-top: 4px; line-height: 1.3; }
  .blind-mode .s-card:not(.revealed) .sk-lbl { opacity: 0; }
  .blind-mode .s-card:not(.revealed) .s-sub { visibility: hidden; }

  /* === MAPA TEÓRICO Y LECTURA VIVA (PESTAÑA 9) === */
  .map-detail-card {
    margin-top: 9px; background: #F8FAFC; border: 1px solid #CBD5E1; border-left: 4px solid #1D4ED8;
    border-radius: 6px; padding: 10px 13px; font-size: 12.2px; line-height: 1.48; color: #0F172A;
  }
  .map-detail-head {
    display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;
    margin-bottom: 6px; padding-bottom: 6px; border-bottom: 1px dashed #CBD5E1;
  }
  .map-detail-title { font-size: 13px; font-weight: 800; color: #1E3A8A; }
  .jump-btn {
    border: 1px solid #1D4ED8; background: #EFF6FF; color: #1E3A8A;
    padding: 4px 9px; border-radius: 5px; font-size: 11px; font-weight: 700; cursor: pointer;
  }
  .jump-btn:hover { background: #1D4ED8; color: #FFFFFF; }
  .lec-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; margin-bottom: 12px; }
  @media (max-width: 820px) { .lec-grid { grid-template-columns: 1fr; } }
  .lec-card {
    border: 1px solid #CBD5E1; border-top: 3.5px solid #1E3A8A; border-radius: 6px;
    background: #FFFFFF; padding: 10px 12px; display: flex; flex-direction: column; gap: 6px;
  }
  .lec-meta { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 4px; }
  .lec-unit { font-size: 10px; font-weight: 800; color: #FFFFFF; background: #1E293B; padding: 2px 7px; border-radius: 4px; }
  .lec-src { font-size: 10.5px; font-weight: 600; color: #475569; font-family: Consolas, monospace; }
  .lec-title { font-size: 12.6px; font-weight: 800; color: #0F172A; }
  .lec-layer {
    font-size: 11.8px; line-height: 1.44; color: #1E293B; padding: 6px 9px; border-radius: 5px;
    background: #F8FAFC; border-left: 3px solid #94A3B8;
  }
  .lec-layer.l-core { border-left-color: #1D4ED8; background: #EFF6FF; }
  .lec-layer.l-bridge { border-left-color: #059669; background: #ECFDF5; }
  .lec-layer.l-trap { border-left-color: #DC2626; background: #FEF2F2; }
  .lec-layer b { color: #0F172A; }
  .qz-card {
    border: 1px solid #CBD5E1; border-left: 4px solid #334155; border-radius: 6px;
    background: #FFFFFF; padding: 9px 12px; margin-bottom: 8px;
  }
  .qz-card.ok { border-left-color: #15803D; background: #F0FDF4; }
  .qz-card.bad { border-left-color: #DC2626; background: #FEF2F2; }
  .qz-tag { font-size: 10px; font-weight: 800; color: #1E3A8A; background: #DBEAFE; padding: 2px 7px; border-radius: 4px; margin-right: 6px; }
  .qz-q { font-size: 12.2px; font-weight: 700; color: #0F172A; margin: 4px 0 7px 0; line-height: 1.42; }
  .qz-opts { display: flex; gap: 7px; flex-wrap: wrap; align-items: center; }
  .qz-btn {
    border: 1px solid #94A3B8; background: #FFFFFF; color: #0F172A;
    padding: 4px 10px; border-radius: 5px; font-size: 11.4px; font-weight: 700; cursor: pointer;
  }
  .qz-btn:hover { background: #EFF6FF; border-color: #1D4ED8; }
  .qz-btn.sel { background: #0F172A; color: #FFFFFF; border-color: #0F172A; }
  .qz-fb { font-size: 11.5px; color: #1E293B; margin-top: 7px; line-height: 1.42; display: none; border-top: 1px dashed #CBD5E1; padding-top: 6px; }
  .qz-card.answered .qz-fb { display: block; }

  @media print {
    body { background: #FFFFFF !important; }
    .top-tabs, .mec-toolbar, .mec-filters, .btn-bar, .chk-btn { display: none !important; }
    .panel { display: none !important; border: none !important; padding: 0 !important; }
    #panel-mecanica { display: block !important; }
    .sec-title { background: #F1F5F9 !important; color: #000000 !important; border-left: 3px solid #000 !important; padding: 4px 8px !important; font-size: 11px !important; }
    .mec-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 6px !important; }
    .f-card { break-inside: avoid; border: 1px solid #94A3B8 !important; padding: 5px 7px !important; }
    .blind-mode .f-card .f-eq, .blind-mode .f-card .f-rule { display: block !important; }
    .blind-mode .f-card .blind-cover { display: none !important; }
    .blind-mode .s-card .sk-lbl { opacity: 1 !important; }
    .blind-mode .s-card .s-sub { visibility: visible !important; }
    .skel-grid { grid-template-columns: repeat(3, 1fr) !important; gap: 6px !important; }
  }
</style>
</head>
<body>
<div class="wrap">
  <div class="top-tabs">
    <button class="tab-btn active" onclick="openTab('thunen', this)">1. Von Thünen y Ecuaciones LR</button>
    <button class="tab-btn" onclick="openTab('weber', this)">2. Weber (IM e Isodápana)</button>
    <button class="tab-btn" onclick="openTab('krugman', this)">3. Krugman (Centro-Periferia)</button>
    <button class="tab-btn" onclick="openTab('perroux', this)">4. Perroux, Myrdal y Hirschman</button>
    <button class="tab-btn" onclick="openTab('christaller', this)">5. Christaller y Granovetter</button>
    <button class="tab-btn" onclick="openTab('lorenz', this)">6. Lorenz, Gini, Theil e IP4</button>
    <button class="tab-btn" onclick="openTab('dini', this)">7. Redes Dini 2010 (Animado)</button>
    <button class="tab-btn" onclick="openTab('mecanica', this)">8. Hoja Mecánica (Modo Ciego)</button>
    <button class="tab-btn" onclick="openTab('lectura', this)">9. Mapa Teórico y Lectura Viva</button>
  </div>

  <!-- ====================================================================== -->
  <!-- PANEL 1: VON THÜNEN + EDITOR LIBRE DE ECUACIONES LR(d)                 -->
  <!-- ====================================================================== -->
  <div id="panel-thunen" class="panel active">
    <div class="sec-title">
      <span>VON THÜNEN A 60 FPS: RENTA LOCACIONAL LR(d) = Y(m − c) − Y·t·d, EDITOR DE ECUACIONES Y ANILLOS</span>
      <div class="btn-bar">
        <button class="act-btn primary" onclick="animarThunen()">Reproducir Baja de Flete</button>
        <button class="act-btn" onclick="fijarGhostThunen()">Fijar Fantasma</button>
        <button class="act-btn" onclick="resetThunen()">Caso Osorno</button>
      </div>
    </div>

    <details class="enun-box" open>
      <summary>
        <span>Planteamiento del Problema (Duch Brown / Prof. Claudio Mancilla — Anillos Concéntricos)</span>
        <span class="enun-badge">Enunciado y ecuaciones sincronizados en vivo</span>
      </summary>
      <div class="enun-body" id="vt-enunciado"></div>
    </details>

    <div class="eq-editor-bar">
      <div class="eq-field">
        <label>Ecuación Actividad 1 (Intensiva / Lechería):</label>
        <input id="vt-eq-1" class="eq-input" type="text" value="LR1 = 120 - 4.5*d" onkeydown="if(event.key==='Enter') aplicarEqThunen()" />
      </div>
      <div class="eq-field">
        <label>Ecuación Actividad 2 (Agroindustria):</label>
        <input id="vt-eq-2" class="eq-input" type="text" value="LR2 = 85 - 2.0*d" onkeydown="if(event.key==='Enter') aplicarEqThunen()" />
      </div>
      <div class="eq-field">
        <label>Ecuación Actividad 3 (Forestal / Extensiva):</label>
        <input id="vt-eq-3" class="eq-input" type="text" value="LR3 = 50 - 0.8*d" onkeydown="if(event.key==='Enter') aplicarEqThunen()" />
      </div>
      <button class="act-btn primary" style="height:33px;" onclick="aplicarEqThunen()">Aplicar Ecuaciones</button>
    </div>
    <div id="vt-eq-err" class="eq-err"></div>

    <div class="sliders-grid">
      <div class="sl-card">
        <div class="sl-head"><span>1. Margen Lechería (M1)</span><span><span id="vt-m1-v" class="sl-val">120</span><span id="vt-m1-d" class="sl-delta d-eq"></span></span></div>
        <input id="vt-m1" type="range" min="60" max="200" step="2" value="120" oninput="onSliderThunen()" />
      </div>
      <div class="sl-card">
        <div class="sl-head"><span>1. Flete Lechería (t1)</span><span><span id="vt-t1-v" class="sl-val">4,5</span><span id="vt-t1-d" class="sl-delta d-eq"></span></span></div>
        <input id="vt-t1" type="range" min="1.2" max="8.0" step="0.1" value="4.5" oninput="onSliderThunen()" />
      </div>
      <div class="sl-card">
        <div class="sl-head"><span>2. Margen Agroindustria (M2)</span><span><span id="vt-m2-v" class="sl-val">85</span><span id="vt-m2-d" class="sl-delta d-eq"></span></span></div>
        <input id="vt-m2" type="range" min="40" max="160" step="2" value="85" oninput="onSliderThunen()" />
      </div>
      <div class="sl-card">
        <div class="sl-head"><span>2. Flete Agroindustria (t2)</span><span><span id="vt-t2-v" class="sl-val">2,0</span><span id="vt-t2-d" class="sl-delta d-eq"></span></span></div>
        <input id="vt-t2" type="range" min="0.8" max="5.0" step="0.1" value="2.0" oninput="onSliderThunen()" />
      </div>
      <div class="sl-card">
        <div class="sl-head"><span>3. Flete Forestal (t3)</span><span><span id="vt-t3-v" class="sl-val">0,80</span><span id="vt-t3-d" class="sl-delta d-eq"></span></span></div>
        <input id="vt-t3" type="range" min="0.4" max="2.5" step="0.05" value="0.8" oninput="onSliderThunen()" />
      </div>
    </div>

    <div class="kpis">
      <div class="kpi" style="border-left-color:#DC2626;"><div class="kpi-lbl">Anillo 1: Intensiva / Lechería</div><div id="vt-k-r1" class="kpi-val">0 → 14,0 km</div><div class="kpi-sub">Corte LR1 = LR2</div></div>
      <div class="kpi" style="border-left-color:#1D4ED8;"><div class="kpi-lbl">Anillo 2: Agroindustria</div><div id="vt-k-r2" class="kpi-val">14,0 → 29,2 km</div><div class="kpi-sub">Corte LR2 = LR3</div></div>
      <div class="kpi" style="border-left-color:#059669;"><div class="kpi-lbl">Anillo 3: Forestal / Extensiva</div><div id="vt-k-r3" class="kpi-val">29,2 → 62,5 km</div><div class="kpi-sub">Frontera agrícola (LR=0)</div></div>
      <div class="kpi" style="border-left-color:#0F172A;"><div class="kpi-lbl">Movimiento vs. Fantasma</div><div id="vt-k-mov" class="kpi-val">Referencia base</div><div id="vt-k-mov2" class="kpi-sub">Mueve un margen o flete</div></div>
    </div>

    <div class="svg-box"><svg id="svg-thunen" viewBox="0 0 980 390"></svg></div>
    <div id="vt-sol" class="sol-box"></div>
  </div>

  <!-- ====================================================================== -->
  <!-- PANEL 2: WEBER (TRIÁNGULO LOCACIONAL, IM E ISODÁPANA CRÍTICA)          -->
  <!-- ====================================================================== -->
  <div id="panel-weber" class="panel">
    <div class="sec-title">
      <span>WEBER A 60 FPS: TRIÁNGULO LOCACIONAL, ÍNDICE DE MATERIALES (IM) E ISODÁPANA CRÍTICA</span>
      <div class="btn-bar">
        <button class="act-btn primary" onclick="animarWeber()">Reproducir Aumento de IM</button>
        <button class="act-btn" onclick="presetWeber(45, 35, 35, 30)">IM &gt; 1 (Aserradero)</button>
        <button class="act-btn" onclick="presetWeber(15, 15, 70, 30)">IM &lt; 1 (Bebidas/Mercado)</button>
        <button class="act-btn" onclick="presetWeber(25, 25, 45, 135)">Salto a Enclave L</button>
        <button class="act-btn" onclick="fijarGhostWeber()">Fijar Fantasma</button>
      </div>
    </div>

    <details class="enun-box" open>
      <summary>
        <span>Planteamiento Oficial (Alfred Weber — Orientación a Insumos vs. Mercado e Isodápana Crítica)</span>
        <span class="enun-badge">Fórmula: IM = (W1 + W2) / WM</span>
      </summary>
      <div class="enun-body" id="wb-enunciado"></div>
    </details>

    <div class="sliders-grid">
      <div class="sl-card"><div class="sl-head"><span>Peso MP1 Localizada (W1)</span><span id="wb-w1-v" class="sl-val">40 t</span></div><input id="wb-w1" type="range" min="5" max="80" step="1" value="40" oninput="drawWeber()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Peso MP2 Localizada (W2)</span><span id="wb-w2-v" class="sl-val">30 t</span></div><input id="wb-w2" type="range" min="5" max="80" step="1" value="30" oninput="drawWeber()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Peso Producto Final (WM)</span><span id="wb-wm-v" class="sl-val">40 t</span></div><input id="wb-wm" type="range" min="10" max="90" step="1" value="40" oninput="drawWeber()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Ahorro Laboral en Enclave L</span><span id="wb-ah-v" class="sl-val">$55 / unid</span></div><input id="wb-ah" type="range" min="0" max="180" step="5" value="55" oninput="drawWeber()" /></div>
    </div>

    <div class="kpis">
      <div class="kpi" style="border-left-color:#1D4ED8;"><div class="kpi-lbl">Índice de Materiales (IM)</div><div id="wb-k-im" class="kpi-val">1,75</div><div id="wb-k-ori" class="kpi-sub">IM &gt; 1: Insumos</div></div>
      <div class="kpi" style="border-left-color:#0F172A;"><div class="kpi-lbl">Costo Transporte Mínimo P*</div><div id="wb-k-ct" class="kpi-val">$248,1</div><div class="kpi-sub">Óptimo puro de flete</div></div>
      <div class="kpi" style="border-left-color:#EA580C;"><div class="kpi-lbl">Sobre-costo Flete hasta L</div><div id="wb-k-dl" class="kpi-val">+$98,4</div><div id="wb-k-iso" class="kpi-sub">Ahorro en L = $55</div></div>
      <div class="kpi" style="border-left-color:#15803D;"><div class="kpi-lbl">Decisión Locacional Final</div><div id="wb-k-dec" class="kpi-val">Permanecer en P*</div><div id="wb-k-dec2" class="kpi-sub">L fuera de Isodápana</div></div>
    </div>

    <div class="svg-box"><svg id="svg-weber" viewBox="0 0 980 400"></svg></div>
    <div id="wb-sol" class="sol-box"></div>
  </div>

  <!-- ====================================================================== -->
  <!-- PANEL 3: KRUGMAN (1991) — BIFURCACIÓN CENTRO-PERIFERIA Y UMBRAL τ*     -->
  <!-- ====================================================================== -->
  <div id="panel-krugman" class="panel">
    <div class="sec-title">
      <span>KRUGMAN (1991) A 60 FPS: NUEVA ECONOMÍA GEOGRÁFICA, UMBRAL τ* Y MACROCEFALIA REGIONAL</span>
      <div class="btn-bar">
        <button class="act-btn primary" onclick="animarKrugman()">Reproducir Baja de Fletes (τ: 10 → 1)</button>
        <button class="act-btn" onclick="fijarGhostKrugman()">Fijar Fantasma</button>
        <button class="act-btn" onclick="resetKrugman()">Restaurar Base</button>
      </div>
    </div>

    <details class="enun-box" open>
      <summary>
        <span>Planteamiento Conceptual (Fuerzas Centrípetas vs. Centrífugas y Punto de Bifurcación τ*)</span>
        <span class="enun-badge">Enunciado sincronizado en vivo</span>
      </summary>
      <div class="enun-body" id="kr-enunciado"></div>
    </details>

    <div class="sliders-grid">
      <div class="sl-card"><div class="sl-head"><span>Costo de Transporte (τ)</span><span><span id="kr-tau-v" class="sl-val">3,5</span><span id="kr-tau-d" class="sl-delta d-eq"></span></span></div><input id="kr-tau" type="range" min="1.0" max="10.0" step="0.1" value="3.5" oninput="drawKrugman()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Economías de Escala (1–10)</span><span id="kr-esc-v" class="sl-val">7,0</span></div><input id="kr-esc" type="range" min="1.0" max="10.0" step="0.2" value="7.0" oninput="drawKrugman()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Movilidad Laboral (1–10)</span><span id="kr-mov-v" class="sl-val">6,5</span></div><input id="kr-mov" type="range" min="1.0" max="10.0" step="0.2" value="6.5" oninput="drawKrugman()" /></div>
    </div>

    <div class="kpis">
      <div class="kpi" style="border-left-color:#D97706;"><div class="kpi-lbl">Umbral Crítico (τ*)</div><div id="kr-k-ust" class="kpi-val">5,43</div><div class="kpi-sub">Bifurcación espacial</div></div>
      <div class="kpi" style="border-left-color:#1D4ED8;"><div class="kpi-lbl">Cuota Capital Regional</div><div id="kr-k-cen" class="kpi-val">89,1%</div><div id="kr-k-reg" class="kpi-sub">Aglomeración</div></div>
      <div class="kpi" style="border-left-color:#64748B;"><div class="kpi-lbl">Cuota Periferia</div><div id="kr-k-per" class="kpi-val">10,9%</div><div id="kr-k-per2" class="kpi-sub">vs simetría (50%)</div></div>
      <div class="kpi" style="border-left-color:#DC2626;"><div class="kpi-lbl">Fuerza Predominante</div><div id="kr-k-fza" class="kpi-val">Centrípeta →</div><div id="kr-k-fza2" class="kpi-sub">τ ≤ τ*</div></div>
    </div>

    <div class="svg-box"><svg id="svg-krugman" viewBox="0 0 980 385"></svg></div>
  </div>

  <!-- ====================================================================== -->
  <!-- PANEL 4: PERROUX, MYRDAL Y HIRSCHMAN (MULTIPLICADOR 5 RONDAS 60 FPS)   -->
  <!-- ====================================================================== -->
  <div id="panel-perroux" class="panel">
    <div class="sec-title">
      <span>PERROUX, MYRDAL Y HIRSCHMAN A 60 FPS: POLOS DE CRECIMIENTO, ENCADENAMIENTOS Y SPREAD VS. BACKWASH</span>
      <div class="btn-bar">
        <button class="act-btn primary" onclick="presetPerroux('pymemad')">Clúster PymeMad Biobío</button>
        <button class="act-btn" onclick="presetPerroux('lacteo')">Complejo Lácteo Osorno</button>
        <button class="act-btn" onclick="presetPerroux('enclave')">Enclave Extractivo</button>
        <button class="act-btn" onclick="fijarGhostPerroux()">Fijar Fantasma</button>
      </div>
    </div>

    <details class="enun-box" open>
      <summary>
        <span>Planteamiento Teórico (Multiplicador de Hirschman y Causalidad Acumulativa de Myrdal)</span>
        <span class="enun-badge">Fórmula: M_H = 1 / [1 − (b + f)]</span>
      </summary>
      <div class="enun-body" id="px-enunciado"></div>
    </details>

    <div class="sliders-grid">
      <div class="sl-card"><div class="sl-head"><span>Inversión Motriz I0 (MM$)</span><span id="px-i0-v" class="sl-val">$1.000 MM</span></div><input id="px-i0" type="range" min="200" max="5000" step="100" value="1000" oninput="drawPerroux()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Encaden. Hacia Atrás (b)</span><span id="px-b-v" class="sl-val">0,35</span></div><input id="px-b" type="range" min="0.05" max="0.45" step="0.01" value="0.35" oninput="drawPerroux()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Encaden. Hacia Adelante (f)</span><span id="px-f-v" class="sl-val">0,25</span></div><input id="px-f" type="range" min="0.05" max="0.45" step="0.01" value="0.25" oninput="drawPerroux()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Proporción Difusión Spread (%)</span><span id="px-sp-v" class="sl-val">65%</span></div><input id="px-sp" type="range" min="5" max="95" step="5" value="65" oninput="drawPerroux()" /></div>
    </div>

    <div class="kpis">
      <div class="kpi" style="border-left-color:#1D4ED8;"><div class="kpi-lbl">Multiplicador Hirschman (M_H)</div><div id="px-k-mh" class="kpi-val">2,50x</div><div id="px-k-ret" class="kpi-sub">Retención local: 60%</div></div>
      <div class="kpi" style="border-left-color:#0F172A;"><div class="kpi-lbl">Producción Total Inducida</div><div id="px-k-tot" class="kpi-val">$2.500 MM</div><div id="px-k-ind" class="kpi-sub">+$1.500 MM indirectos</div></div>
      <div class="kpi" style="border-left-color:#15803D;"><div class="kpi-lbl">Efecto Difusión (Spread)</div><div id="px-k-sp" class="kpi-val">+$975 MM</div><div class="kpi-sub">Compras a comunas vecinas</div></div>
      <div class="kpi" style="border-left-color:#DC2626;"><div class="kpi-lbl">Saldo Neto Periferia (Myrdal)</div><div id="px-k-sal" class="kpi-val">+$660 MM</div><div id="px-k-diag" class="kpi-sub">Polo Integrador</div></div>
    </div>

    <div class="svg-box"><svg id="svg-perroux" viewBox="0 0 980 370"></svg></div>
    <div id="px-sol" class="sol-box"></div>
  </div>

  <!-- ====================================================================== -->
  <!-- PANEL 5: CHRISTALLER (UMBRAL/ALCANCE) + GRANOVETTER (VÍNCULOS DÉBILES) -->
  <!-- ====================================================================== -->
  <div id="panel-christaller" class="panel">
    <div class="sec-title">
      <span>CHRISTALLER (1933) A 60 FPS: UMBRAL DE DEMANDA Y ALCANCE ESPACIAL DE LUGARES CENTRALES</span>
      <div class="btn-bar">
        <button class="act-btn primary" onclick="presetChris(120000, 90)">Orden Superior (Hospital/Univ.)</button>
        <button class="act-btn" onclick="presetChris(30000, 45)">Orden Intermedio (Banco/CFT)</button>
        <button class="act-btn" onclick="presetChris(5000, 15)">Orden Inferior (CESFAM/Farmacia)</button>
      </div>
    </div>

    <div class="sliders-grid">
      <div class="sl-card"><div class="sl-head"><span>Población Área Influencia</span><span id="ch-pob-v" class="sl-val">37.000 hab.</span></div><input id="ch-pob" type="range" min="2000" max="220000" step="1000" value="37000" oninput="drawChrisGran()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Umbral Mínimo (Threshold)</span><span id="ch-umb-v" class="sl-val">30.000 hab.</span></div><input id="ch-umb" type="range" min="2000" max="180000" step="1000" value="30000" oninput="drawChrisGran()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Alcance Máximo (Range km)</span><span id="ch-alc-v" class="sl-val">45 km</span></div><input id="ch-alc" type="range" min="5" max="130" step="1" value="45" oninput="drawChrisGran()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Distancia Vial Localidades (km)</span><span id="ch-dst-v" class="sl-val">35 km</span></div><input id="ch-dst" type="range" min="2" max="130" step="1" value="35" oninput="drawChrisGran()" /></div>
    </div>
    <div id="ch-diag" class="sol-box" style="margin-top:0;margin-bottom:10px;"></div>

    <div class="sec-title">
      <span>GRANOVETTER (1973) A 60 FPS: VÍNCULOS FUERTES INTRALOCALES VS. PUENTES DÉBILES EXTRALOCALES (LOCK-IN)</span>
      <div class="btn-bar">
        <button class="act-btn" onclick="presetGran(9, 1)">Red Endogámica (Lock-in)</button>
        <button class="act-btn primary" onclick="presetGran(8, 7)">SPL Innovador con Puentes I+D</button>
      </div>
    </div>

    <div class="sliders-grid" style="grid-template-columns: 1fr 1fr;">
      <div class="sl-card"><div class="sl-head"><span>Vínculos Fuertes Locales (Cohesión PyMEs)</span><span id="gr-f-v" class="sl-val">8 / 10</span></div><input id="gr-f" type="range" min="1" max="10" step="1" value="8" oninput="drawChrisGran()" /></div>
      <div class="sl-card"><div class="sl-head"><span>Vínculos Débiles Externos (Puentes ULagos/INIA/CORFO)</span><span id="gr-d-v" class="sl-val">6 / 10</span></div><input id="gr-d" type="range" min="0" max="10" step="1" value="6" oninput="drawChrisGran()" /></div>
    </div>

    <div class="kpis">
      <div class="kpi" style="border-left-color:#1D4ED8;"><div class="kpi-lbl">Cohesión Interna Local</div><div id="gr-k-coh" class="kpi-val">80 / 100</div><div class="kpi-sub">Confianza horizontal</div></div>
      <div class="kpi" style="border-left-color:#15803D;"><div class="kpi-lbl">Acceso a Innovación (Info no redund.)</div><div id="gr-k-inn" class="kpi-val">85 / 100</div><div class="kpi-sub">Puentes externos activos</div></div>
      <div class="kpi" style="border-left-color:#DC2626;"><div class="kpi-lbl">Riesgo de Bloqueo (Lock-in)</div><div id="gr-k-lck" class="kpi-val">8%</div><div id="gr-k-lck2" class="kpi-sub">Red abierta</div></div>
      <div class="kpi" style="border-left-color:#0F172A;"><div class="kpi-lbl">Desempeño SPL Global</div><div id="gr-k-spl" class="kpi-val">80,4 pts</div><div class="kpi-sub">Balance cohesión + puentes</div></div>
    </div>

    <div class="svg-box"><svg id="svg-gran" viewBox="0 0 980 320"></svg></div>
  </div>

  <!-- ====================================================================== -->
  <!-- PANEL 6: LORENZ, GINI, THEIL Y PRIMACÍA URBANA (IP4 ESCALA 0–3)        -->
  <!-- ====================================================================== -->
  <div id="panel-lorenz" class="panel">
    <div class="sec-title">
      <span>DISPARIDADES REAT Y OT A 60 FPS: CURVA DE LORENZ, GINI, ENTROPÍA DE THEIL Y PRIMACÍA URBANA (IP4)</span>
      <div class="btn-bar">
        <button class="act-btn primary" onclick="presetLorenz('lagos')">Los Lagos (Censo 2024)</button>
        <button class="act-btn" onclick="presetLorenz('biobio')">Biobío (Censo 2024)</button>
        <button class="act-btn" onclick="presetLorenz('mancilla')">Ejemplo Mancilla (Lám. 12)</button>
        <button class="act-btn" onclick="fijarGhostLorenz()">Fijar Fantasma</button>
      </div>
    </div>

    <details class="enun-box" open>
      <summary>
        <span>Planteamiento Integrado Unidades 3 y 5 (Concentración Espacial, Desigualdad y Primacía Urbana)</span>
        <span class="enun-badge">Fórmulas: IP4 = P1/(P2+P3+P4) · T = ∑ si·ln(n·si)</span>
      </summary>
      <div class="enun-body" id="lz-enunciado"></div>
    </details>

    <div class="sliders-grid">
      <div class="sl-card"><div class="sl-head"><span id="lz-l1">P1: Puerto Montt</span><span id="lz-p1-v" class="sl-val">275.473</span></div><input id="lz-p1" type="range" min="1000" max="600000" step="1000" value="275473" oninput="drawLorenz()" /></div>
      <div class="sl-card"><div class="sl-head"><span id="lz-l2">P2: Osorno</span><span id="lz-p2-v" class="sl-val">174.998</span></div><input id="lz-p2" type="range" min="500" max="350000" step="500" value="174998" oninput="drawLorenz()" /></div>
      <div class="sl-card"><div class="sl-head"><span id="lz-l3">P3: Puerto Varas</span><span id="lz-p3-v" class="sl-val">50.010</span></div><input id="lz-p3" type="range" min="100" max="250000" step="500" value="50010" oninput="drawLorenz()" /></div>
      <div class="sl-card"><div class="sl-head"><span id="lz-l4">P4: Castro</span><span id="lz-p4-v" class="sl-val">48.632</span></div><input id="lz-p4" type="range" min="50" max="200000" step="500" value="48632" oninput="drawLorenz()" /></div>
    </div>

    <div class="kpis">
      <div class="kpi" style="border-left-color:#1D4ED8;"><div class="kpi-lbl">Índice Primacía (IP4)</div><div id="lz-k-ip4" class="kpi-val">1,007</div><div id="lz-k-ip2" class="kpi-sub">IP2 = 1,574</div></div>
      <div class="kpi" style="border-left-color:#D97706;"><div class="kpi-lbl">Estandarización OT (0–3)</div><div id="lz-k-cat" class="kpi-val">Valor 2: Concentrada</div><div class="kpi-sub">06 OT 2024.pdf</div></div>
      <div class="kpi" style="border-left-color:#DC2626;"><div class="kpi-lbl">Índice de Gini (G)</div><div id="lz-k-gini" class="kpi-val">0,432</div><div id="lz-k-dgini" class="kpi-sub">ΔG vs Fantasma: 0,000</div></div>
      <div class="kpi" style="border-left-color:#7C3AED;"><div class="kpi-lbl">Entropía de Theil (T)</div><div id="lz-k-theil" class="kpi-val">0,312</div><div id="lz-k-cuota" class="kpi-sub">Cuota P1: 50,2%</div></div>
    </div>

    <div class="svg-box"><svg id="svg-lorenz" viewBox="0 0 980 385"></svg></div>
  </div>

  <!-- ====================================================================== -->
  <!-- PANEL 7: REDES EMPRESARIALES DE DINI (2010) A 60 FPS                   -->
  <!-- ====================================================================== -->
  <div id="panel-dini" class="panel">
    <div class="sec-title">
      <span>REDES EMPRESARIALES DE DINI (2010) A 60 FPS: ARMADO ANIMADO, DENSIDAD D Y GRADIENTE GC</span>
      <div class="btn-bar">
        <button class="act-btn primary" onclick="animarDini()">Play: Armar Vínculo a Vínculo</button>
        <button class="act-btn" onclick="completarDini()">Ver Red Completa</button>
      </div>
    </div>

    <div class="mec-filters">
      <button class="flt-btn active" onclick="setTopologiaDini('simetrica', this)">1. Simétrica (Pares)</button>
      <button class="flt-btn" onclick="setTopologiaDini('liderazgo', this)">2. Con Liderazgo (Estrella)</button>
      <button class="flt-btn" onclick="setTopologiaDini('jerarquica', this)">3. Jerárquica (Pirámide)</button>
      <button class="flt-btn" onclick="setTopologiaDini('red_redes', this)">4. Red de Redes (Diag. 3)</button>
      <button class="flt-btn" onclick="setTopologiaDini('aviones', this)">5. Prod. Aviones (Diag. 4)</button>
      <button class="flt-btn" onclick="setTopologiaDini('osorno', this)">6. Red Láctea Osorno (C4)</button>
      <button class="flt-btn" onclick="setTopologiaDini('pymemad', this)">7. Clúster PymeMad Biobío (C4)</button>
    </div>

    <details class="enun-box" open>
      <summary>
        <span>Tipología Dini (2010, CEPAL — 04 SPL.pdf pág. 14) y Diagnóstico Estructural</span>
        <span class="enun-badge">Fórmulas: D = 2L/[n(n−1)] · GC = ∑(kmax−ki)/[(n−1)(n−2)]</span>
      </summary>
      <div class="enun-body" id="dn-enunciado"></div>
    </details>

    <div class="sl-card" style="margin-bottom:10px;">
      <div class="sl-head"><span>Paso de Construcción (Vínculos Activos L)</span><span id="dn-step-v" class="sl-val">0 / 0</span></div>
      <input id="dn-step" type="range" min="0" max="16" step="1" value="16" oninput="drawDini()" />
    </div>

    <div class="kpis">
      <div class="kpi" style="border-left-color:#0F172A;"><div class="kpi-lbl">Actores (n) y Vínculos (L)</div><div id="dn-k-nl" class="kpi-val">n=8 | L=16</div><div id="dn-k-lmax" class="kpi-sub">Máx posible: 28</div></div>
      <div class="kpi" style="border-left-color:#1D4ED8;"><div class="kpi-lbl">Densidad de la Red (D)</div><div id="dn-k-den" class="kpi-val">57,1%</div><div class="kpi-sub">D = 2L / [n(n−1)]</div></div>
      <div class="kpi" style="border-left-color:#15803D;"><div class="kpi-lbl">Grado Máximo y Promedio</div><div id="dn-k-k" class="kpi-val">k_máx=4 | k̄=4,0</div><div class="kpi-sub">Conexiones por nodo</div></div>
      <div class="kpi" style="border-left-color:#DC2626;"><div class="kpi-lbl">Gradiente Concentración (GC)</div><div id="dn-k-gc" class="kpi-val">0,0%</div><div id="dn-k-gcd" class="kpi-sub">Simétrica (0%) ↔ Líder (100%)</div></div>
    </div>

    <div class="svg-box"><svg id="svg-dini" viewBox="0 0 980 390"></svg></div>
  </div>

  <!-- ====================================================================== -->
  <!-- PANEL 8: HOJA DE ENTRENAMIENTO MECÁNICO TERRITORIAL (MODO CIEGO)       -->
  <!-- ====================================================================== -->
  <div id="panel-mecanica" class="panel">
    <div class="sec-title">
      <span>HOJA DE ENTRENAMIENTO MECÁNICO — DESARROLLO Y GESTIÓN TERRITORIAL (ULAGOS 2026)</span>
      <div class="btn-bar">
        <button id="btn-modo-copia" class="act-btn primary" onclick="setModoMec(false)">Modo Copia (Todo Visible)</button>
        <button id="btn-modo-ciego" class="act-btn" onclick="setModoMec(true)">Modo Ciego (Autoevaluación)</button>
        <button class="act-btn" onclick="resetDominadas()">Reiniciar ✓</button>
        <button class="act-btn" onclick="window.print()">Imprimir / Guardar PDF (Carta)</button>
      </div>
    </div>

    <div class="mec-toolbar">
      <div style="font-size:12px;color:#334155;">
        <b>Método de cuaderno:</b> copia cada fórmula y esqueleto varias veces; luego activa <b>Modo Ciego</b>, escríbelos sin mirar y haz clic en cada recuadro para comprobar y marcar <b>✓</b>.
      </div>
      <span id="mec-score" class="pill-score">Dominadas: 0 / 16</span>
    </div>

    <div class="mec-filters">
      <button class="flt-btn active" onclick="filtrarMec('all', this)">Todas (16)</button>
      <button class="flt-btn" onclick="filtrarMec('loc', this)">I. Localización y Polos (4)</button>
      <button class="flt-btn" onclick="filtrarMec('ilpes', this)">II. Análisis Regional ILPES/MADE (5)</button>
      <button class="flt-btn" onclick="filtrarMec('reat', this)">III. Disparidades REAT (4)</button>
      <button class="flt-btn" onclick="filtrarMec('ot', this)">IV. Redes Dini y Ordenamiento OT (3)</button>
    </div>

    <div id="mec-container">
      <div class="mec-grid" id="mec-formulas-grid"></div>
      <div class="sec-title" style="margin-top:6px;">
        <span>ESQUELETOS DE GRÁFICAS PARA COPIAR A MANO EN CUADERNO (6 DIAGRAMAS CLAVE DE EXAMEN)</span>
        <span style="font-size:11px;font-weight:600;color:#334155;">En Modo Ciego, haz clic en cada gráfico para revelar las etiquetas</span>
      </div>
      <div class="skel-grid" id="mec-skel-grid"></div>
    </div>
  </div>

  <!-- ====================================================================== -->
  <!-- PANEL 9: MAPA CAUSAL TEÓRICO, LECTURA EN 3 CAPAS Y QUIZ INTER-UNIDADES -->
  <!-- ====================================================================== -->
  <div id="panel-lectura" class="panel">
    <div class="sec-title">
      <span>MAPA CAUSAL INTERACTIVO (UNIDADES 1–5): CÓMO SE CONECTA TODA LA TEORÍA DEL RAMO</span>
      <div class="btn-bar">
        <button class="act-btn primary" onclick="activarEscenarioMapa('fletes')">Cadena A: Baja de Fletes (τ↓)</button>
        <button class="act-btn" onclick="activarEscenarioMapa('cluster')">Cadena B: Política Clúster / SPL</button>
        <button class="act-btn" onclick="activarEscenarioMapa('prot')">Cadena C: Planificación PROT + OT</button>
        <button class="act-btn" onclick="selectUnidadMapa('U1')">Ver Todo Libre</button>
      </div>
    </div>

    <div class="svg-box"><svg id="svg-mapa-teoria" viewBox="0 0 980 315"></svg></div>
    <div id="mapa-detail-box" class="map-detail-card"></div>

    <div class="sec-title" style="margin-top:14px;">
      <span>LECTURA GUIADA EN 3 CAPAS POR AUTOR Y BIBLIOGRAFÍA OFICIAL (SIN MUROS DE TEXTO)</span>
      <div class="btn-bar">
        <button id="cap-btn-core" class="act-btn primary" onclick="setCapaLectura('core')">Capa 1: Idea Central</button>
        <button id="cap-btn-bridge" class="act-btn" onclick="setCapaLectura('bridge')">Capa 2: Puentes Inter-Unidades</button>
        <button id="cap-btn-trap" class="act-btn" onclick="setCapaLectura('trap')">Capa 3: Trampas de Control</button>
        <button id="cap-btn-all" class="act-btn" onclick="setCapaLectura('all')">Ver las 3 Capas</button>
      </div>
    </div>

    <div class="mec-filters">
      <button class="flt-btn active" onclick="filtrarLectura('all', this)">Todos los Autores (6)</button>
      <button class="flt-btn" onclick="filtrarLectura('U1', this)">U1: Localización y Polos (2)</button>
      <button class="flt-btn" onclick="filtrarLectura('U2', this)">U2: ILPES / Silva Lira (1)</button>
      <button class="flt-btn" onclick="filtrarLectura('U3', this)">U3: REAT / Markov (1)</button>
      <button class="flt-btn" onclick="filtrarLectura('U4', this)">U4: Dini / Cadenas / ELITE (1)</button>
      <button class="flt-btn" onclick="filtrarLectura('U5', this)">U5: OT / Rondinelli / PROT (1)</button>
    </div>

    <div class="lec-grid" id="lec-cards-grid"></div>

    <div class="sec-title" style="margin-top:14px;">
      <span>ENTRENADOR DE CONTROL DE LECTURA CRUZADO (10 PREGUNTAS QUE RELACIONAN UNIDADES)</span>
      <div class="btn-bar">
        <span id="qz-score" class="pill-score">Aciertos: 0 / 10</span>
        <button class="act-btn" onclick="toggleSoloErradasQz(this)">Ver Solo Pendientes / Erradas</button>
        <button class="act-btn" onclick="resetQuizLectura()">Reiniciar Control</button>
      </div>
    </div>
    <div id="qz-list"></div>
  </div>
</div>

<script>
const NS = "http://www.w3.org/2000/svg";
function fmtInt(n) { return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); }
function fmtDec(n, d=1) {
  const s = Number(n).toFixed(d).split(".");
  return s[0].replace(/\B(?=(\d{3})+(?!\d))/g, ".") + (d > 0 ? "," + s[1] : "");
}
function el(tag, attrs, parent) {
  const node = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs || {})) node.setAttribute(k, v);
  if (parent) parent.appendChild(node);
  return node;
}
function addDefs(svg) {
  const defs = el("defs", {}, svg);
  const colors = [["arr-red", "#DC2626"], ["arr-blue", "#1D4ED8"], ["arr-green", "#15803D"], ["arr-orange", "#EA580C"], ["arr-dark", "#0F172A"]];
  for (const [id, col] of colors) {
    const m = el("marker", { id, viewBox: "0 0 10 10", refX: "8", refY: "5", markerWidth: "7", markerHeight: "7", orient: "auto-start-reverse" }, defs);
    el("path", { d: "M 0 1 L 10 5 L 0 9 z", fill: col }, m);
  }
}
function drawArrow(svg, x1, y1, x2, y2, color, markerId, label, lx, ly, anchor="middle") {
  const dist = Math.hypot(x2 - x1, y2 - y1);
  if (dist < 6) return;
  el("line", { x1, y1, x2, y2, stroke: color, "stroke-width": "2.6", "marker-end": `url(#${markerId})` }, svg);
  if (label) {
    const bgW = Math.max(52, label.length * 6.5 + 10);
    const rx = anchor === "middle" ? lx - bgW / 2 : (anchor === "start" ? lx - 4 : lx - bgW + 4);
    el("rect", { x: rx, y: ly - 12, width: bgW, height: 17, rx: 4, fill: "rgba(255,255,255,0.94)", stroke: color, "stroke-width": "1" }, svg);
    const t = el("text", { x: lx, y: ly, fill: color, "font-size": "10.8", "font-weight": "700", "text-anchor": anchor }, svg);
    t.textContent = label;
  }
}
function setDelta(id, diff, dec=1) {
  const node = document.getElementById(id);
  if (!node) return;
  if (Math.abs(diff) < 1e-4) { node.textContent = ""; node.className = "sl-delta d-eq"; return; }
  node.textContent = `(${diff > 0 ? "↑ +" : "↓ -"}${fmtDec(Math.abs(diff), dec)})`;
  node.className = "sl-delta " + (diff > 0 ? "d-up" : "d-down");
}
function openTab(name, btn) {
  document.querySelectorAll(".panel").forEach(p => p.classList.remove("active"));
  document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
  document.getElementById("panel-" + name).classList.add("active");
  btn.classList.add("active");
  if (name === "thunen") drawThunen();
  if (name === "weber") drawWeber();
  if (name === "krugman") drawKrugman();
  if (name === "perroux") drawPerroux();
  if (name === "christaller") drawChrisGran();
  if (name === "lorenz") drawLorenz();
  if (name === "dini") drawDini();
  if (name === "mecanica") renderMecanica();
  if (name === "lectura") { drawMapaTeoria(); renderLecturaCards(); renderQuizLectura(); }
}
function jumpToTab(name) {
  const btns = Array.from(document.querySelectorAll(".top-tabs .tab-btn"));
  const target = btns.find(b => (b.getAttribute("onclick") || "").includes("'" + name + "'"));
  if (target) {
    openTab(name, target);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
}

// ============================================================================
// 1. VON THÜNEN + PARSER LIBRE DE ECUACIONES LR(d)
// ============================================================================
let stateVt = { m1: 120, t1: 4.5, m2: 85, t2: 2.0, m3: 50, t3: 0.8 };
let ghostVt = { m1: 120, t1: 4.5, m2: 85, t2: 2.0, m3: 50, t3: 0.8 };
let animVtId = null;

function parseRentEq(raw) {
  let s = String(raw || "").replace(/,/g, ".").replace(/−/g, "-").replace(/\s+/g, "");
  if (s.includes("=")) s = s.split("=").pop();
  s = s.replace(/\*/g, "").replace(/[dDxX]/g, "d");
  const toks = s.match(/[+-]?[^+-]+/g);
  if (!toks) return null;
  let m = 0, slope = 0, hasD = false;
  for (const tk of toks) {
    if (tk.includes("d")) {
      hasD = true;
      const c = tk.replace("d", "");
      if (c === "" || c === "+") slope += 1;
      else if (c === "-") slope -= 1;
      else { const v = parseFloat(c); if (!Number.isFinite(v)) return null; slope += v; }
    } else {
      const v = parseFloat(tk);
      if (!Number.isFinite(v)) return null;
      m += v;
    }
  }
  if (!hasD || slope >= 0 || m <= 0) return null;
  return { m, t: Math.abs(slope) };
}
function syncEqInputsVt() {
  document.getElementById("vt-eq-1").value = `LR1 = ${stateVt.m1} - ${stateVt.t1}*d`;
  document.getElementById("vt-eq-2").value = `LR2 = ${stateVt.m2} - ${stateVt.t2}*d`;
  document.getElementById("vt-eq-3").value = `LR3 = ${stateVt.m3} - ${stateVt.t3}*d`;
}
function aplicarEqThunen() {
  const err = document.getElementById("vt-eq-err");
  err.style.display = "none";
  const r1 = parseRentEq(document.getElementById("vt-eq-1").value);
  const r2 = parseRentEq(document.getElementById("vt-eq-2").value);
  const r3 = parseRentEq(document.getElementById("vt-eq-3").value);
  if (!r1 || !r2 || !r3) {
    err.textContent = "Formato esperado: lineal con pendiente negativa en d (ej: LR1 = 120 - 4.5*d).";
    err.style.display = "block";
    return;
  }
  fijarGhostThunen();
  stateVt = { m1: r1.m, t1: r1.t, m2: r2.m, t2: r2.t, m3: r3.m, t3: r3.t };
  document.getElementById("vt-m1").max = Math.max(200, Math.ceil(r1.m * 1.4));
  document.getElementById("vt-m1").value = r1.m;
  document.getElementById("vt-t1").max = Math.max(8, Math.ceil(r1.t * 1.5));
  document.getElementById("vt-t1").value = r1.t;
  document.getElementById("vt-m2").max = Math.max(160, Math.ceil(r2.m * 1.4));
  document.getElementById("vt-m2").value = r2.m;
  document.getElementById("vt-t2").value = r2.t;
  document.getElementById("vt-t3").value = r3.t;
  drawThunen();
}
function onSliderThunen() {
  stateVt.m1 = +document.getElementById("vt-m1").value;
  stateVt.t1 = +document.getElementById("vt-t1").value;
  stateVt.m2 = +document.getElementById("vt-m2").value;
  stateVt.t2 = +document.getElementById("vt-t2").value;
  stateVt.t3 = +document.getElementById("vt-t3").value;
  syncEqInputsVt();
  drawThunen();
}
function fijarGhostThunen() {
  ghostVt = { ...stateVt };
  drawThunen();
}
function resetThunen() {
  if (animVtId) cancelAnimationFrame(animVtId);
  stateVt = { m1: 120, t1: 4.5, m2: 85, t2: 2.0, m3: 50, t3: 0.8 };
  ghostVt = { ...stateVt };
  document.getElementById("vt-m1").value = 120;
  document.getElementById("vt-t1").value = 4.5;
  document.getElementById("vt-m2").value = 85;
  document.getElementById("vt-t2").value = 2.0;
  document.getElementById("vt-t3").value = 0.8;
  syncEqInputsVt();
  drawThunen();
}
function animarThunen() {
  if (animVtId) cancelAnimationFrame(animVtId);
  stateVt.t1 = 6.0;
  document.getElementById("vt-t1").value = 6.0;
  fijarGhostThunen();
  const t0 = performance.now(), dur = 1700;
  function step(now) {
    const u = Math.min(1, (now - t0) / dur);
    const ease = 1 - Math.pow(1 - u, 3);
    stateVt.t1 = +(6.0 - 3.4 * ease).toFixed(2);
    document.getElementById("vt-t1").value = stateVt.t1;
    syncEqInputsVt();
    drawThunen();
    if (u < 1) animVtId = requestAnimationFrame(step);
  }
  animVtId = requestAnimationFrame(step);
}
function calcRadiosThunen(s) {
  let r1 = 0, r2 = 0, r3 = 0;
  const maxScan = Math.max(70, (s.m3 / s.t3) * 1.1, (s.m2 / s.t2) * 1.1, (s.m1 / s.t1) * 1.1);
  for (let d = 0; d <= maxScan; d += 0.2) {
    const l1 = Math.max(0, s.m1 - s.t1 * d);
    const l2 = Math.max(0, s.m2 - s.t2 * d);
    const l3 = Math.max(0, s.m3 - s.t3 * d);
    const mx = Math.max(l1, l2, l3);
    if (mx <= 0) break;
    if (l1 >= l2 && l1 >= l3) { r1 = d; r2 = Math.max(r2, d); r3 = Math.max(r3, d); }
    else if (l2 >= l1 && l2 >= l3) { r2 = d; r3 = Math.max(r3, d); }
    else { r3 = d; }
  }
  return { r1, r2, r3, maxScan };
}
function drawThunen() {
  const s = stateVt;
  document.getElementById("vt-m1-v").textContent = fmtDec(s.m1, 0);
  document.getElementById("vt-t1-v").textContent = fmtDec(s.t1, 1);
  document.getElementById("vt-m2-v").textContent = fmtDec(s.m2, 0);
  document.getElementById("vt-t2-v").textContent = fmtDec(s.t2, 1);
  document.getElementById("vt-t3-v").textContent = fmtDec(s.t3, 2);
  setDelta("vt-m1-d", s.m1 - ghostVt.m1, 0);
  setDelta("vt-t1-d", s.t1 - ghostVt.t1, 1);
  setDelta("vt-m2-d", s.m2 - ghostVt.m2, 0);
  setDelta("vt-t2-d", s.t2 - ghostVt.t2, 1);
  setDelta("vt-t3-d", s.t3 - ghostVt.t3, 2);

  const cur = calcRadiosThunen(s), gho = calcRadiosThunen(ghostVt);
  const d12 = Math.abs(s.t1 - s.t2) > 1e-4 ? (s.m1 - s.m2) / (s.t1 - s.t2) : 0;
  const d23 = Math.abs(s.t2 - s.t3) > 1e-4 ? (s.m2 - s.m3) / (s.t2 - s.t3) : 0;
  const d30 = s.m3 / s.t3;

  document.getElementById("vt-enunciado").innerHTML =
    `En una llanura homogénea alrededor de un mercado urbano central compiten tres actividades con rentas locacionales: ` +
    `<b>LR<sub>1</sub>(d) = ${fmtDec(s.m1,0)} − ${fmtDec(s.t1,1)}·d</b> (Lechería/Hortalizas), ` +
    `<b>LR<sub>2</sub>(d) = ${fmtDec(s.m2,0)} − ${fmtDec(s.t2,1)}·d</b> (Agroindustria) y ` +
    `<b>LR<sub>3</sub>(d) = ${fmtDec(s.m3,0)} − ${fmtDec(s.t3,2)}·d</b> (Forestal/Extensiva). ` +
    `Determine los radios de transición de los anillos concéntricos y el límite agrícola donde la renta se hace cero.`;

  document.getElementById("vt-sol").innerHTML =
    `<b>Cortes exactos:</b> LR1=LR2 ⇒ d<sub>12</sub> = (${fmtDec(s.m1,0)}−${fmtDec(s.m2,0)})/(${fmtDec(s.t1,1)}−${fmtDec(s.t2,1)}) = <b>${fmtDec(Math.max(0,d12),1)} km</b> | ` +
    `LR2=LR3 ⇒ d<sub>23</sub> = (${fmtDec(s.m2,0)}−${fmtDec(s.m3,0)})/(${fmtDec(s.t2,1)}−${fmtDec(s.t3,2)}) = <b>${fmtDec(Math.max(0,d23),1)} km</b> | ` +
    `Frontera LR3=0 ⇒ d<sub>máx</sub> = ${fmtDec(s.m3,0)}/${fmtDec(s.t3,2)} = <b>${fmtDec(d30,1)} km</b>`;

  document.getElementById("vt-k-r1").textContent = `0 → ${fmtDec(cur.r1, 1)} km`;
  document.getElementById("vt-k-r2").textContent = `${fmtDec(cur.r1, 1)} → ${fmtDec(cur.r2, 1)} km`;
  document.getElementById("vt-k-r3").textContent = `${fmtDec(cur.r2, 1)} → ${fmtDec(cur.r3, 1)} km`;
  const dr1 = cur.r1 - gho.r1;
  document.getElementById("vt-k-mov").textContent = Math.abs(dr1) >= 0.3 ? `${dr1 > 0 ? "→ +" : "← -"}${fmtDec(Math.abs(dr1), 1)} km` : "En fantasma";
  document.getElementById("vt-k-mov2").textContent = Math.abs(dr1) >= 0.3 ? (dr1 > 0 ? "Anillo 1 se expande" : "Anillo 1 se contrae") : "Mueve un parámetro";

  const svg = document.getElementById("svg-thunen");
  svg.innerHTML = "";
  addDefs(svg);
  const M = { l: 55, r: 420, t: 30, b: 44 }, W = 980, H = 390;
  const maxD = Math.max(70, Math.ceil(cur.r3 * 1.12 / 10) * 10);
  const maxR = Math.max(175, Math.max(s.m1, s.m2, s.m3) * 1.15);
  const sx = d => M.l + (d / maxD) * (W - M.l - M.r);
  const sy = r => H - M.b - (r / maxR) * (H - M.t - M.b);

  for (let i = 0; i <= 4; i++) {
    const yv = (maxR / 4) * i, dv = (maxD / 5) * i;
    el("line", { x1: M.l, y1: sy(yv), x2: W - M.r, y2: sy(yv), stroke: "#E2E8F0" }, svg);
    const ty = el("text", { x: M.l - 8, y: sy(yv) + 4, fill: "#475569", "font-size": "11", "text-anchor": "end" }, svg);
    ty.textContent = fmtInt(yv);
  }
  for (let i = 0; i <= 5; i++) {
    const dv = (maxD / 5) * i;
    el("line", { x1: sx(dv), y1: M.t, x2: sx(dv), y2: H - M.b, stroke: "#F1F5F9" }, svg);
    const tx = el("text", { x: sx(dv), y: H - M.b + 16, fill: "#475569", "font-size": "11", "text-anchor": "middle" }, svg);
    tx.textContent = fmtInt(dv) + " km";
  }
  el("line", { x1: M.l, y1: H - M.b, x2: W - M.r, y2: H - M.b, stroke: "#334155", "stroke-width": "1.5" }, svg);
  el("line", { x1: M.l, y1: M.t, x2: M.l, y2: H - M.b, stroke: "#334155", "stroke-width": "1.5" }, svg);

  if (cur.r1 > 0.2) el("polygon", { points: `${sx(0)},${sy(0)} ${sx(cur.r1)},${sy(0)} ${sx(cur.r1)},${sy(Math.max(0, s.m1 - s.t1 * cur.r1))} ${sx(0)},${sy(s.m1)}`, fill: "rgba(220,38,38,0.18)" }, svg);
  if (cur.r2 > cur.r1 + 0.2) el("polygon", { points: `${sx(cur.r1)},${sy(0)} ${sx(cur.r2)},${sy(0)} ${sx(cur.r2)},${sy(Math.max(0, s.m2 - s.t2 * cur.r2))} ${sx(cur.r1)},${sy(Math.max(0, s.m2 - s.t2 * cur.r1))}`, fill: "rgba(29,78,216,0.16)" }, svg);
  if (cur.r3 > cur.r2 + 0.2) el("polygon", { points: `${sx(cur.r2)},${sy(0)} ${sx(cur.r3)},${sy(0)} ${sx(cur.r2)},${sy(Math.max(0, s.m3 - s.t3 * cur.r2))}`, fill: "rgba(5,150,105,0.16)" }, svg);

  if (Math.abs(s.m1 - ghostVt.m1) > 0.5 || Math.abs(s.t1 - ghostVt.t1) > 0.05) {
    el("line", { x1: sx(0), y1: sy(ghostVt.m1), x2: sx(Math.min(maxD, ghostVt.m1 / ghostVt.t1)), y2: sy(Math.max(0, ghostVt.m1 - ghostVt.t1 * maxD)), stroke: "#94A3B8", "stroke-width": "1.6", "stroke-dasharray": "5,4" }, svg);
  }
  const drawRL = (m, t, col) => {
    const dz = Math.min(maxD, m / t);
    el("line", { x1: sx(0), y1: sy(m), x2: sx(dz), y2: sy(Math.max(0, m - t * dz)), stroke: col, "stroke-width": "2.6" }, svg);
  };
  drawRL(s.m1, s.t1, "#DC2626");
  drawRL(s.m2, s.t2, "#1D4ED8");
  drawRL(s.m3, s.t3, "#059669");

  if (Math.abs(dr1) >= 0.4) {
    drawArrow(svg, sx(gho.r1), sy(maxR * 0.84), sx(cur.r1), sy(maxR * 0.84), dr1 > 0 ? "#15803D" : "#DC2626", dr1 > 0 ? "arr-green" : "arr-red",
      `${dr1 > 0 ? "→ +" : "← -"}${fmtDec(Math.abs(dr1), 1)} km`, (sx(gho.r1) + sx(cur.r1)) / 2, sy(maxR * 0.91));
  }

  // Mapa concéntrico derecho
  const cx = 775, cy = 200, maxPixR = 152;
  const sr = km => (Math.min(km, maxD) / maxD) * maxPixR;
  const tMap = el("text", { x: cx, y: 24, fill: "#0F172A", "font-size": "12", "font-weight": "700", "text-anchor": "middle" }, svg);
  tMap.textContent = "Mapa Espacial de Anillos Concéntricos";
  el("circle", { cx, cy, r: sr(cur.r3), fill: "rgba(5,150,105,0.22)", stroke: "#059669", "stroke-width": "1.8" }, svg);
  el("circle", { cx, cy, r: sr(cur.r2), fill: "rgba(29,78,216,0.24)", stroke: "#1D4ED8", "stroke-width": "1.8" }, svg);
  el("circle", { cx, cy, r: sr(cur.r1), fill: "rgba(220,38,38,0.28)", stroke: "#DC2626", "stroke-width": "2" }, svg);
  if (Math.abs(dr1) >= 0.4) {
    el("circle", { cx, cy, r: sr(gho.r1), fill: "none", stroke: "#64748B", "stroke-width": "1.6", "stroke-dasharray": "5,4" }, svg);
    drawArrow(svg, cx + sr(gho.r1), cy, cx + sr(cur.r1), cy, dr1 > 0 ? "#15803D" : "#DC2626", dr1 > 0 ? "arr-green" : "arr-red", "", cx, cy);
  }
  el("circle", { cx, cy, r: 8, fill: "#0F172A" }, svg);
  const tCen = el("text", { x: cx, y: cy + 21, fill: "#0F172A", "font-size": "11", "font-weight": "800", "text-anchor": "middle" }, svg);
  tCen.textContent = "Mercado";
}

// ============================================================================
// 2. WEBER (TRIÁNGULO LOCACIONAL, IM E ISODÁPANA CRÍTICA)
// ============================================================================
const WB_M1 = { x: 180, y: 78, name: "MP1 (Bosque/Predio)" };
const WB_M2 = { x: 180, y: 325, name: "MP2 (Insumo 2)" };
const WB_MK = { x: 700, y: 202, name: "Mercado (Ciudad)" };
const WB_L  = { x: 525, y: 86,  name: "Enclave Laboral L" };
let ghostWb = { w1: 40, w2: 30, wm: 40, ah: 55 };
let animWbId = null;

function solveWeber(w1, w2, wm) {
  const pts = [[WB_M1.x, WB_M1.y, w1], [WB_M2.x, WB_M2.y, w2], [WB_MK.x, WB_MK.y, wm]];
  let x = (WB_M1.x * w1 + WB_M2.x * w2 + WB_MK.x * wm) / (w1 + w2 + wm);
  let y = (WB_M1.y * w1 + WB_M2.y * w2 + WB_MK.y * wm) / (w1 + w2 + wm);
  for (let it = 0; it < 35; it++) {
    let nx = 0, ny = 0, den = 0;
    for (const [px, py, w] of pts) {
      const d = Math.max(4, Math.hypot(x - px, y - py));
      nx += (w * px) / d; ny += (w * py) / d; den += w / d;
    }
    x = nx / den; y = ny / den;
  }
  const costFn = (px, py) => (w1 * Math.hypot(px - WB_M1.x, py - WB_M1.y) + w2 * Math.hypot(px - WB_M2.x, py - WB_M2.y) + wm * Math.hypot(px - WB_MK.x, py - WB_MK.y)) / 100;
  return { x, y, costMin: costFn(x, y), costAtL: costFn(WB_L.x, WB_L.y), costFn };
}
function fijarGhostWeber() {
  ghostWb = { w1: +document.getElementById("wb-w1").value, w2: +document.getElementById("wb-w2").value, wm: +document.getElementById("wb-wm").value, ah: +document.getElementById("wb-ah").value };
  drawWeber();
}
function presetWeber(w1, w2, wm, ah) {
  if (animWbId) cancelAnimationFrame(animWbId);
  fijarGhostWeber();
  document.getElementById("wb-w1").value = w1;
  document.getElementById("wb-w2").value = w2;
  document.getElementById("wb-wm").value = wm;
  document.getElementById("wb-ah").value = ah;
  drawWeber();
}
function animarWeber() {
  if (animWbId) cancelAnimationFrame(animWbId);
  document.getElementById("wb-w1").value = 12; document.getElementById("wb-w2").value = 12; document.getElementById("wb-wm").value = 70; document.getElementById("wb-ah").value = 45;
  fijarGhostWeber();
  const t0 = performance.now(), dur = 1800;
  function step(now) {
    const u = Math.min(1, (now - t0) / dur);
    const ease = 1 - Math.pow(1 - u, 3);
    document.getElementById("wb-w1").value = Math.round(12 + 43 * ease);
    document.getElementById("wb-w2").value = Math.round(12 + 38 * ease);
    document.getElementById("wb-wm").value = Math.round(70 - 40 * ease);
    drawWeber();
    if (u < 1) animWbId = requestAnimationFrame(step);
  }
  animWbId = requestAnimationFrame(step);
}
function drawWeber() {
  const w1 = +document.getElementById("wb-w1").value, w2 = +document.getElementById("wb-w2").value;
  const wm = +document.getElementById("wb-wm").value, ah = +document.getElementById("wb-ah").value;
  document.getElementById("wb-w1-v").textContent = w1 + " t";
  document.getElementById("wb-w2-v").textContent = w2 + " t";
  document.getElementById("wb-wm-v").textContent = wm + " t";
  document.getElementById("wb-ah-v").textContent = "$" + ah + " / unid";

  const im = (w1 + w2) / wm;
  const opt = solveWeber(w1, w2, wm), gOpt = solveWeber(ghostWb.w1, ghostWb.w2, ghostWb.wm);
  const extraCostL = opt.costAtL - opt.costMin;
  const convieneL = ah > extraCostL && ah > 0;

  document.getElementById("wb-enunciado").innerHTML =
    `Una industria utiliza dos materias primas localizadas de pesos <b>W<sub>1</sub> = ${w1} t</b> y <b>W<sub>2</sub> = ${w2} t</b> para elaborar un producto final de <b>W<sub>M</sub> = ${wm} t</b>. ` +
    `Existe además un enclave laboral <b>L</b> que ofrece un ahorro salarial de <b>$${ah}/unidad</b>. Determine el Índice de Materiales (IM), la ubicación óptima P* y si conviene desviarse hacia L.`;

  document.getElementById("wb-sol").innerHTML =
    `<b>IM</b> = (${w1}+${w2})/${wm} = <b>${fmtDec(im,2)}</b> (${im > 1.05 ? "IM > 1 ⇒ pérdida de peso, atracción hacia insumos" : (im < 0.95 ? "IM < 1 ⇒ ganancia de peso, atracción hacia mercado" : "IM ≈ 1 ⇒ equilibrio")}) | ` +
    `<b>Isodápana Crítica:</b> Sobre-costo flete hacia L = <b>+$${fmtDec(extraCostL,1)}</b> vs. Ahorro salarial = <b>$${ah}</b> ⇒ <b>${convieneL ? "CONVIENE DESVIAR A L (Ahorro neto +$" + fmtDec(ah - extraCostL,1) + ")" : "PERMANECER EN P*"}</b>`;

  document.getElementById("wb-k-im").textContent = fmtDec(im, 2);
  document.getElementById("wb-k-ori").textContent = im > 1.05 ? "IM > 1: Insumos" : (im < 0.95 ? "IM < 1: Mercado" : "IM ≈ 1: Intermedio");
  document.getElementById("wb-k-ct").textContent = "$" + fmtDec(opt.costMin, 1);
  document.getElementById("wb-k-dl").textContent = "+$" + fmtDec(extraCostL, 1);
  document.getElementById("wb-k-iso").textContent = `Ahorro L = $${ah}`;
  document.getElementById("wb-k-dec").textContent = convieneL ? "DESVIAR A L" : "PERMANECER EN P*";
  document.getElementById("wb-k-dec2").textContent = convieneL ? `Neto: +$${fmtDec(ah - extraCostL, 1)}/unid` : "L fuera de isodápana";

  const svg = document.getElementById("svg-weber");
  svg.innerHTML = "";
  addDefs(svg);
  el("polygon", { points: `${WB_M1.x},${WB_M1.y} ${WB_M2.x},${WB_M2.y} ${WB_MK.x},${WB_MK.y}`, fill: "#F8FAFC", stroke: "#CBD5E1", "stroke-width": "2" }, svg);

  if (ah > 2) {
    const isoPts = [];
    for (let k = 0; k < 48; k++) {
      const ang = (k / 48) * Math.PI * 2;
      let lo = 0, hi = 420;
      for (let b = 0; b < 14; b++) {
        const mid = (lo + hi) / 2;
        if (opt.costFn(opt.x + Math.cos(ang) * mid, opt.y + Math.sin(ang) * mid) - opt.costMin < ah) lo = mid; else hi = mid;
      }
      isoPts.push(`${(opt.x + Math.cos(ang) * lo).toFixed(1)},${(opt.y + Math.sin(ang) * lo).toFixed(1)}`);
    }
    el("polygon", { points: isoPts.join(" "), fill: convieneL ? "rgba(21,128,61,0.14)" : "rgba(234,88,12,0.10)", stroke: convieneL ? "#15803D" : "#EA580C", "stroke-width": "2", "stroke-dasharray": "6,4" }, svg);
  }
  const drawPull = (vx, vy, w, col) => {
    const dx = vx - opt.x, dy = vy - opt.y, dist = Math.hypot(dx, dy);
    if (dist < 10) return;
    el("line", { x1: opt.x, y1: opt.y, x2: vx, y2: vy, stroke: "#CBD5E1", "stroke-dasharray": "3,3" }, svg);
    const len = Math.min(dist - 12, 26 + w * 1.1);
    drawArrow(svg, opt.x, opt.y, opt.x + (dx / dist) * len, opt.y + (dy / dist) * len, col, col === "#1D4ED8" ? "arr-blue" : "arr-dark", "", 0, 0);
  };
  drawPull(WB_M1.x, WB_M1.y, w1, "#1D4ED8");
  drawPull(WB_M2.x, WB_M2.y, w2, "#1D4ED8");
  drawPull(WB_MK.x, WB_MK.y, wm, "#0F172A");

  if (Math.hypot(opt.x - gOpt.x, opt.y - gOpt.y) > 8) {
    el("circle", { cx: gOpt.x, cy: gOpt.y, r: 6, fill: "#94A3B8" }, svg);
    drawArrow(svg, gOpt.x, gOpt.y, opt.x, opt.y, "#DC2626", "arr-red", "Movimiento P*", (gOpt.x + opt.x) / 2, (gOpt.y + opt.y) / 2 - 12);
  }
  if (convieneL) drawArrow(svg, opt.x, opt.y, WB_L.x, WB_L.y, "#15803D", "arr-green", "Salto óptimo → L", (opt.x + WB_L.x) / 2 + 12, (opt.y + WB_L.y) / 2 - 10, "start");

  const drawNode = (pt, col, sub, anchor="middle", dy=-14) => {
    el("circle", { cx: pt.x, cy: pt.y, r: 9, fill: col, stroke: "#FFFFFF", "stroke-width": "2" }, svg);
    const t = el("text", { x: pt.x, y: pt.y + dy, fill: "#0F172A", "font-size": "11.5", "font-weight": "700", "text-anchor": anchor }, svg);
    t.textContent = `${pt.name} ${sub}`;
  };
  drawNode(WB_M1, "#1D4ED8", `(${w1}t)`, "middle", -14);
  drawNode(WB_M2, "#1D4ED8", `(${w2}t)`, "middle", 22);
  drawNode(WB_MK, "#0F172A", `(${wm}t)`, "start", 4);
  drawNode(WB_L, convieneL ? "#15803D" : "#EA580C", `(-$${ah})`, "start", -12);
  el("circle", { cx: opt.x, cy: opt.y, r: 8.5, fill: "#DC2626", stroke: "#FFFFFF", "stroke-width": "2" }, svg);
  const tP = el("text", { x: opt.x, y: opt.y + 22, fill: "#DC2626", "font-size": "12", "font-weight": "800", "text-anchor": "middle" }, svg);
  tP.textContent = "P* (Fábrica)";
}

// ============================================================================
// 3. KRUGMAN (1991) — CENTRO-PERIFERIA Y UMBRAL τ*
// ============================================================================
let ghostKr = { tau: 3.5, esc: 7.0, mov: 6.5 };
let animKrId = null;

function calcKrugman(tau, esc, mov) {
  const ust = 0.45 * esc + 0.35 * mov;
  const pres = (ust - tau) * 1.45;
  let cen = Math.min(95, Math.max(50, 50 + 43 / (1 + Math.exp(-pres))));
  return { ust, cen, per: 100 - cen };
}
function fijarGhostKrugman() { ghostKr = { tau: +document.getElementById("kr-tau").value, esc: +document.getElementById("kr-esc").value, mov: +document.getElementById("kr-mov").value }; drawKrugman(); }
function resetKrugman() {
  if (animKrId) cancelAnimationFrame(animKrId);
  document.getElementById("kr-tau").value = 3.5; document.getElementById("kr-esc").value = 7.0; document.getElementById("kr-mov").value = 6.5;
  ghostKr = { tau: 3.5, esc: 7.0, mov: 6.5 }; drawKrugman();
}
function animarKrugman() {
  if (animKrId) cancelAnimationFrame(animKrId);
  document.getElementById("kr-tau").value = 9.5; fijarGhostKrugman();
  const t0 = performance.now(), dur = 2100;
  function step(now) {
    const u = Math.min(1, (now - t0) / dur);
    const ease = 1 - Math.pow(1 - u, 2.5);
    document.getElementById("kr-tau").value = (9.5 - 8.2 * ease).toFixed(2);
    drawKrugman();
    if (u < 1) animKrId = requestAnimationFrame(step);
  }
  animKrId = requestAnimationFrame(step);
}
function drawKrugman() {
  const tau = +document.getElementById("kr-tau").value, esc = +document.getElementById("kr-esc").value, mov = +document.getElementById("kr-mov").value;
  document.getElementById("kr-tau-v").textContent = fmtDec(tau, 1);
  document.getElementById("kr-esc-v").textContent = fmtDec(esc, 1);
  document.getElementById("kr-mov-v").textContent = fmtDec(mov, 1);
  setDelta("kr-tau-d", tau - ghostKr.tau, 1);

  const cur = calcKrugman(tau, esc, mov), gho = calcKrugman(ghostKr.tau, ghostKr.esc, ghostKr.mov);
  const aglom = tau <= cur.ust;

  document.getElementById("kr-enunciado").innerHTML =
    `En una economía de dos regiones (<b>Capital Regional</b> y <b>Periferia</b>) con economías de escala = <b>${fmtDec(esc,1)}</b> y movilidad laboral = <b>${fmtDec(mov,1)}</b>, ` +
    `el umbral crítico de bifurcación se ubica en <b>τ* = ${fmtDec(cur.ust,2)}</b>. Con un costo de transporte actual de <b>τ = ${fmtDec(tau,1)}</b>, ` +
    `predominan las fuerzas <b>${aglom ? "centrípetas (aglomeración hacia el centro: " + fmtDec(cur.cen,1) + "%)" : "centrífugas (equilibrio disperso entre regiones)"}</b>.`;

  document.getElementById("kr-k-ust").textContent = fmtDec(cur.ust, 2);
  document.getElementById("kr-k-cen").textContent = fmtDec(cur.cen, 1) + "%";
  document.getElementById("kr-k-reg").textContent = aglom ? "Aglomeración" : "Equilibrio Disperso";
  document.getElementById("kr-k-per").textContent = fmtDec(cur.per, 1) + "%";
  document.getElementById("kr-k-per2").textContent = `${fmtDec(cur.per - 50, 1)} pp vs 50%`;
  document.getElementById("kr-k-fza").textContent = aglom ? "Centrípeta →" : "Centrífuga ↔";
  document.getElementById("kr-k-fza2").textContent = aglom ? "τ ≤ τ* (Macrocefalia)" : "τ > τ* (Protege periferia)";

  const svg = document.getElementById("svg-krugman");
  svg.innerHTML = "";
  addDefs(svg);
  const M = { l: 55, r: 440, t: 28, b: 46 }, W = 980, H = 385;
  const sx = t => M.l + ((t - 1) / 9) * (W - M.l - M.r);
  const sy = c => H - M.b - ((c - 45) / 55) * (H - M.t - M.b);

  for (let c = 50; c <= 100; c += 10) {
    el("line", { x1: M.l, y1: sy(c), x2: W - M.r, y2: sy(c), stroke: "#E2E8F0" }, svg);
    const t = el("text", { x: M.l - 8, y: sy(c) + 4, fill: "#475569", "font-size": "11", "text-anchor": "end" }, svg);
    t.textContent = c + "%";
  }
  for (let t = 1; t <= 10; t += 1) {
    const tx = el("text", { x: sx(t), y: H - M.b + 16, fill: "#475569", "font-size": "11", "text-anchor": "middle" }, svg);
    tx.textContent = "τ=" + t;
  }
  el("line", { x1: M.l, y1: H - M.b, x2: W - M.r, y2: H - M.b, stroke: "#334155", "stroke-width": "1.5" }, svg);
  el("line", { x1: M.l, y1: M.t, x2: M.l, y2: H - M.b, stroke: "#334155", "stroke-width": "1.5" }, svg);
  el("line", { x1: sx(cur.ust), y1: M.t, x2: sx(cur.ust), y2: H - M.b, stroke: "#D97706", "stroke-width": "2", "stroke-dasharray": "6,4" }, svg);
  const tUst = el("text", { x: sx(cur.ust) + 5, y: M.t + 14, fill: "#B45309", "font-size": "11", "font-weight": "700" }, svg);
  tUst.textContent = `τ* = ${fmtDec(cur.ust, 1)}`;

  const pts = [];
  for (let t = 1; t <= 10.01; t += 0.15) pts.push(`${sx(t).toFixed(1)},${sy(calcKrugman(t, esc, mov).cen).toFixed(1)}`);
  el("polyline", { points: pts.join(" "), fill: "none", stroke: "#1D4ED8", "stroke-width": "2.8" }, svg);

  if (Math.hypot(sx(tau) - sx(ghostKr.tau), sy(cur.cen) - sy(gho.cen)) > 10) {
    el("circle", { cx: sx(ghostKr.tau), cy: sy(gho.cen), r: 5.5, fill: "#94A3B8" }, svg);
    drawArrow(svg, sx(ghostKr.tau), sy(gho.cen), sx(tau), sy(cur.cen), "#DC2626", "arr-red", `${cur.cen >= gho.cen ? "↑ +" : "↓ -"}${fmtDec(Math.abs(cur.cen - gho.cen), 1)} pp`, (sx(ghostKr.tau) + sx(tau)) / 2, (sy(gho.cen) + sy(cur.cen)) / 2 - 12);
  }
  el("circle", { cx: sx(tau), cy: sy(cur.cen), r: 7, fill: "#DC2626", stroke: "#FFFFFF", "stroke-width": "2" }, svg);

  const xCen = 665, xPer = 880, yMid = 200;
  const rCen = 28 + (cur.cen / 100) * 56, rPer = 22 + (cur.per / 100) * 56;
  el("circle", { cx: xCen, cy: yMid, r: rCen, fill: "rgba(29,78,216,0.22)", stroke: "#1D4ED8", "stroke-width": "2.4" }, svg);
  el("circle", { cx: xPer, cy: yMid, r: rPer, fill: "rgba(100,116,139,0.22)", stroke: "#475569", "stroke-width": "2" }, svg);
  const mkT = (x, y, txt, sz, col) => { const n = el("text", { x, y, fill: col, "font-size": sz, "font-weight": "800", "text-anchor": "middle" }, svg); n.textContent = txt; };
  mkT(xCen, yMid - 4, "Capital Regional", 11.5, "#1E3A8A");
  mkT(xCen, yMid + 14, fmtDec(cur.cen, 1) + "%", 14, "#1D4ED8");
  mkT(xPer, yMid - 4, "Periferia", 11.5, "#334155");
  mkT(xPer, yMid + 14, fmtDec(cur.per, 1) + "%", 13.5, "#475569");
  if (aglom) {
    drawArrow(svg, xPer - rPer - 6, yMid - 14, xCen + rCen + 8, yMid - 14, "#DC2626", "arr-red", "Aglomeración (Backwash)", 775, yMid - 42);
    drawArrow(svg, xPer - rPer - 6, yMid + 14, xCen + rCen + 8, yMid + 14, "#DC2626", "arr-red", "", 0, 0);
  } else {
    drawArrow(svg, xCen + rCen + 8, yMid, xPer - rPer - 8, yMid, "#15803D", "arr-green", "Equilibrio Disperso", 775, yMid - 20);
  }
}

// ============================================================================
// 4. PERROUX, MYRDAL Y HIRSCHMAN (5 RONDAS + SPREAD VS. BACKWASH A 60 FPS)
// ============================================================================
let ghostPx = 2500;
function fijarGhostPerroux() {
  const i0 = +document.getElementById("px-i0").value;
  const p = Math.min(0.88, +document.getElementById("px-b").value + +document.getElementById("px-f").value);
  ghostPx = i0 / (1 - p);
  drawPerroux();
}
function presetPerroux(tipo) {
  fijarGhostPerroux();
  if (tipo === "pymemad") { document.getElementById("px-i0").value = 1000; document.getElementById("px-b").value = 0.35; document.getElementById("px-f").value = 0.25; document.getElementById("px-sp").value = 65; }
  else if (tipo === "lacteo") { document.getElementById("px-i0").value = 1200; document.getElementById("px-b").value = 0.40; document.getElementById("px-f").value = 0.22; document.getElementById("px-sp").value = 70; }
  else { document.getElementById("px-i0").value = 1000; document.getElementById("px-b").value = 0.12; document.getElementById("px-f").value = 0.08; document.getElementById("px-sp").value = 25; }
  drawPerroux();
}
function drawPerroux() {
  const i0 = +document.getElementById("px-i0").value;
  const b = +document.getElementById("px-b").value;
  const f = +document.getElementById("px-f").value;
  const spPct = +document.getElementById("px-sp").value;
  document.getElementById("px-i0-v").textContent = `$${fmtInt(i0)} MM`;
  document.getElementById("px-b-v").textContent = fmtDec(b, 2);
  document.getElementById("px-f-v").textContent = fmtDec(f, 2);
  document.getElementById("px-sp-v").textContent = spPct + "%";

  const prop = Math.min(0.88, b + f);
  const mh = 1 / (1 - prop);
  const tot = i0 * mh;
  const ind = tot - i0;
  const spread = ind * (spPct / 100);
  const backwash = ind * ((100 - spPct) / 100) * 0.6;
  const saldo = spread - backwash;

  document.getElementById("px-enunciado").innerHTML =
    `Una industria motriz (<b>Perroux</b>) inyecta <b>I<sub>0</sub> = $${fmtInt(i0)} MM</b> en un polo regional con encadenamientos hacia atrás <b>b = ${fmtDec(b,2)}</b> y hacia adelante <b>f = ${fmtDec(f,2)}</b>. ` +
    `De los efectos indirectos inducidos, el <b>${spPct}%</b> se difunde hacia comunas vecinas (<i>Spread</i>) mientras el resto genera atracción/absorción de factores hacia el centro (<i>Backwash</i>).`;

  document.getElementById("px-k-mh").textContent = fmtDec(mh, 2) + "x";
  document.getElementById("px-k-ret").textContent = `Retención b+f = ${fmtDec(prop * 100, 0)}%`;
  document.getElementById("px-k-tot").textContent = `$${fmtInt(tot)} MM`;
  document.getElementById("px-k-ind").textContent = `+$${fmtInt(ind)} MM indirectos`;
  document.getElementById("px-k-sp").textContent = `+$${fmtInt(spread)} MM`;
  document.getElementById("px-k-sal").textContent = `${saldo >= 0 ? "+" : "-"}$${fmtInt(Math.abs(saldo))} MM`;
  document.getElementById("px-k-diag").textContent = saldo >= 0 ? "Polo Integrador (Spread > Backwash)" : "Enclave Extractivo (Backwash)";

  document.getElementById("px-sol").innerHTML =
    `<b>Multiplicador:</b> M<sub>H</sub> = 1 / [1 − (${fmtDec(b,2)}+${fmtDec(f,2)})] = <b>${fmtDec(mh,2)}x</b> ⇒ Producción Total = <b>$${fmtInt(tot)} MM</b> | ` +
    `<b>Myrdal:</b> Spread ($${fmtInt(spread)}M) − Backwash ($${fmtInt(backwash)}M) = <b>${saldo >= 0 ? "+" : "-"}$${fmtInt(Math.abs(saldo))} MM</b>`;

  const svg = document.getElementById("svg-perroux");
  svg.innerHTML = "";
  addDefs(svg);

  // Izquierda: 5 rondas acumuladas
  const rondas = [], acum = [];
  let ac = 0;
  for (let r = 0; r < 5; r++) {
    const val = i0 * Math.pow(prop, r);
    ac += val;
    rondas.push(val); acum.push(ac);
  }
  const M = { l: 64, r: 360, t: 30, b: 46 }, W = 980, H = 370;
  const maxY = Math.max(tot, ghostPx) * 1.15;
  const sy = v => H - M.b - (v / maxY) * (H - M.t - M.b);
  for (let i = 0; i <= 4; i++) {
    const yv = (maxY / 4) * i;
    el("line", { x1: M.l, y1: sy(yv), x2: W - M.r, y2: sy(yv), stroke: "#E2E8F0" }, svg);
    const t = el("text", { x: M.l - 8, y: sy(yv) + 4, fill: "#475569", "font-size": "11", "text-anchor": "end" }, svg);
    t.textContent = "$" + fmtInt(yv) + "M";
  }
  el("line", { x1: M.l, y1: H - M.b, x2: W - M.r, y2: H - M.b, stroke: "#334155", "stroke-width": "1.5" }, svg);

  const slotW = (W - M.l - M.r) / 5, bw = slotW * 0.56;
  const linePts = [];
  for (let r = 0; r < 5; r++) {
    const x0 = M.l + r * slotW + (slotW - bw) / 2;
    el("rect", { x: x0, y: sy(acum[r]), width: bw, height: Math.max(2, sy(0) - sy(acum[r])), fill: "#1D4ED8", opacity: "0.24", stroke: "#1D4ED8", rx: 3 }, svg);
    el("rect", { x: x0, y: sy(rondas[r]), width: bw, height: Math.max(2, sy(0) - sy(rondas[r])), fill: "#1D4ED8", rx: 3 }, svg);
    linePts.push(`${x0 + bw / 2},${sy(acum[r])}`);
    const tl = el("text", { x: x0 + bw / 2, y: H - M.b + 17, fill: "#1E293B", "font-size": "11", "font-weight": "700", "text-anchor": "middle" }, svg);
    tl.textContent = `Ronda ${r + 1}`;
    const tv = el("text", { x: x0 + bw / 2, y: sy(acum[r]) - 6, fill: "#0F172A", "font-size": "10.5", "font-weight": "800", "text-anchor": "middle" }, svg);
    tv.textContent = `$${fmtInt(acum[r])}M`;
  }
  el("polyline", { points: linePts.join(" "), fill: "none", stroke: "#0F172A", "stroke-width": "2.4" }, svg);

  // Derecha: Balanza Myrdal (Spread vs Backwash vs Saldo)
  const bx0 = 670, bSlot = 95, bw2 = 58;
  const maxB = Math.max(spread, backwash, Math.abs(saldo), 200) * 1.25;
  const syB = v => 295 - (v / maxB) * 220;
  const tM = el("text", { x: 805, y: 26, fill: "#0F172A", "font-size": "12", "font-weight": "700", "text-anchor": "middle" }, svg);
  tM.textContent = "Balance Myrdal: Spread vs. Backwash";
  el("line", { x1: 650, y1: 295, x2: 955, y2: 295, stroke: "#334155", "stroke-width": "1.5" }, svg);

  const itemsB = [
    { lbl: "Spread (+)", val: spread, col: "#15803D" },
    { lbl: "Backwash (−)", val: backwash, col: "#DC2626" },
    { lbl: "Saldo Neto", val: Math.abs(saldo), col: saldo >= 0 ? "#1D4ED8" : "#991B1B", sign: saldo >= 0 ? "+" : "-" },
  ];
  itemsB.forEach((it, k) => {
    const x = bx0 + k * bSlot;
    el("rect", { x, y: syB(it.val), width: bw2, height: Math.max(2, 295 - syB(it.val)), fill: it.col, rx: 4 }, svg);
    const tv = el("text", { x: x + bw2 / 2, y: syB(it.val) - 6, fill: it.col, "font-size": "11", "font-weight": "800", "text-anchor": "middle" }, svg);
    tv.textContent = `${it.sign || ""}$${fmtInt(it.val)}M`;
    const tl = el("text", { x: x + bw2 / 2, y: 314, fill: "#1E293B", "font-size": "11", "font-weight": "700", "text-anchor": "middle" }, svg);
    tl.textContent = it.lbl;
  });
}

// ============================================================================
// 5. CHRISTALLER (UMBRAL/ALCANCE) + GRANOVETTER (VÍNCULOS DÉBILES A 60 FPS)
// ============================================================================
function presetChris(umb, alc) {
  document.getElementById("ch-umb").value = umb;
  document.getElementById("ch-alc").value = alc;
  drawChrisGran();
}
function presetGran(f, d) {
  document.getElementById("gr-f").value = f;
  document.getElementById("gr-d").value = d;
  drawChrisGran();
}
function drawChrisGran() {
  const pob = +document.getElementById("ch-pob").value;
  const umb = +document.getElementById("ch-umb").value;
  const alc = +document.getElementById("ch-alc").value;
  const dst = +document.getElementById("ch-dst").value;

  document.getElementById("ch-pob-v").textContent = fmtInt(pob) + " hab.";
  document.getElementById("ch-umb-v").textContent = fmtInt(umb) + " hab.";
  document.getElementById("ch-alc-v").textContent = alc + " km";
  document.getElementById("ch-dst-v").textContent = dst + " km";

  const okU = pob >= umb, okA = alc >= dst;
  const cob = (pob / Math.max(1, umb)) * 100;
  let diagC = "";
  if (okU && okA) diagC = `<span style="color:#15803D;font-weight:800;">✓ VIABLE (Cumple Umbral y Alcance):</span> Demanda cubre <b>${fmtDec(cob,1)}%</b> del umbral mínimo y el alcance (${alc} km) supera la distancia vial (${dst} km).`;
  else if (!okU && okA) diagC = `<span style="color:#DC2626;font-weight:800;">✗ DÉFICIT DE UMBRAL:</span> Faltan <b>${fmtInt(umb - pob)} hab.</b> de masa crítica (solo cubre ${fmtDec(cob,1)}%). Requiere asociar comunas vecinas.`;
  else if (okU && !okA) diagC = `<span style="color:#EA580C;font-weight:800;">⚠ FUERA DE ALCANCE ESPACIAL:</span> Hay masa crítica, pero los usuarios están a <b>${dst} km &gt; ${alc} km</b> de alcance máximo.`;
  else diagC = `<span style="color:#DC2626;font-weight:800;">✗ NO FACTIBLE:</span> No alcanza umbral mínimo ni cobertura territorial; el servicio debe concentrarse en un Lugar Central de orden superior.`;
  document.getElementById("ch-diag").innerHTML = diagC;

  // Granovetter 60 FPS
  const f = +document.getElementById("gr-f").value;
  const d = +document.getElementById("gr-d").value;
  document.getElementById("gr-f-v").textContent = `${f} / 10`;
  document.getElementById("gr-d-v").textContent = `${d} / 10`;

  const coh = f * 10;
  const inn = Math.min(100, d * 11.5 + f * 2);
  const lck = Math.max(0, f * 10 - d * 12);
  const spl = 0.45 * coh + 0.55 * inn - 0.30 * lck;

  document.getElementById("gr-k-coh").textContent = `${fmtInt(coh)} / 100`;
  document.getElementById("gr-k-inn").textContent = `${fmtInt(inn)} / 100`;
  document.getElementById("gr-k-lck").textContent = `${fmtInt(lck)}%`;
  document.getElementById("gr-k-lck2").textContent = lck > 40 ? "Red endogámica (Lock-in)" : "Puentes externos activos";
  document.getElementById("gr-k-spl").textContent = `${fmtDec(spl, 1)} pts`;

  const svg = document.getElementById("svg-gran");
  svg.innerHTML = "";
  const locNames = ["PyME 1", "PyME 2", "PyME 3", "PyME 4", "Gremio Local"];
  const extNames = ["Univ. ULagos", "Centro I+D INIA", "Comprador Ext.", "Prov. Tecnología", "CORFO / Fomento"];
  const locPts = locNames.map((nm, i) => {
    const a = (i / 5) * Math.PI * 2 - Math.PI / 2;
    return { x: 255 + 115 * Math.cos(a), y: 165 + 100 * Math.sin(a), nm };
  });
  const extPts = extNames.map((nm, i) => ({ x: 755 + (i % 2 === 0 ? 0 : 28), y: 52 + i * 56, nm }));

  const pFuertes = [[0,1],[1,2],[2,3],[3,4],[4,0],[0,2],[1,3],[2,4],[0,3],[1,4]];
  const pDebiles = [[4,0],[0,1],[1,2],[2,3],[4,4],[3,1],[0,0],[2,2],[1,3],[3,4]];

  // Enlaces fuertes (azul sólido)
  for (let i = 0; i < f; i++) {
    const [u, v] = pFuertes[i];
    el("line", { x1: locPts[u].x, y1: locPts[u].y, x2: locPts[v].x, y2: locPts[v].y, stroke: "#1D4ED8", "stroke-width": "2.6" }, svg);
  }
  // Enlaces débiles puente (rojo punteado)
  for (let i = 0; i < d; i++) {
    const [u, v] = pDebiles[i];
    el("line", { x1: locPts[u].x, y1: locPts[u].y, x2: extPts[v].x, y2: extPts[v].y, stroke: "#DC2626", "stroke-width": "2.2", "stroke-dasharray": "6,4" }, svg);
  }
  locPts.forEach(p => {
    el("circle", { cx: p.x, cy: p.y, r: 11, fill: "#1D4ED8", stroke: "#FFFFFF", "stroke-width": "2" }, svg);
    const t = el("text", { x: p.x, y: p.y - 15, fill: "#0F172A", "font-size": "11", "font-weight": "700", "text-anchor": "middle" }, svg);
    t.textContent = p.nm;
  });
  extPts.forEach(p => {
    el("circle", { cx: p.x, cy: p.y, r: 10, fill: "#DC2626", stroke: "#FFFFFF", "stroke-width": "2" }, svg);
    const t = el("text", { x: p.x + 15, y: p.y + 4, fill: "#991B1B", "font-size": "11", "font-weight": "700" }, svg);
    t.textContent = p.nm;
  });
  const tl1 = el("text", { x: 255, y: 24, fill: "#1E3A8A", "font-size": "12", "font-weight": "800", "text-anchor": "middle" }, svg);
  tl1.textContent = "Clúster Comunal (Vínculos Fuertes)";
  const tl2 = el("text", { x: 785, y: 24, fill: "#991B1B", "font-size": "12", "font-weight": "800", "text-anchor": "middle" }, svg);
  tl2.textContent = "Ecosistema Externo (Puentes Débiles)";
}

// ============================================================================
// 6. LORENZ, GINI, THEIL Y PRIMACÍA URBANA (IP4 ESCALA 0–3)
// ============================================================================
let ghostLz = [275473, 174998, 50010, 48632];
function presetLorenz(caso) {
  fijarGhostLorenz();
  const s1 = document.getElementById("lz-p1"), s2 = document.getElementById("lz-p2"), s3 = document.getElementById("lz-p3"), s4 = document.getElementById("lz-p4");
  if (caso === "lagos") {
    s1.max = 600000; s2.max = 350000; s3.max = 250000; s4.max = 200000;
    s1.value = 275473; s2.value = 174998; s3.value = 50010; s4.value = 48632;
    document.getElementById("lz-l1").textContent = "P1: Puerto Montt"; document.getElementById("lz-l2").textContent = "P2: Osorno";
    document.getElementById("lz-l3").textContent = "P3: Puerto Varas"; document.getElementById("lz-l4").textContent = "P4: Castro";
  } else if (caso === "biobio") {
    s1.max = 600000; s2.max = 350000; s3.max = 250000; s4.max = 200000;
    s1.value = 230375; s2.value = 219441; s3.value = 150992; s4.value = 147322;
    document.getElementById("lz-l1").textContent = "P1: Concepción"; document.getElementById("lz-l2").textContent = "P2: Los Ángeles";
    document.getElementById("lz-l3").textContent = "P3: San Pedro Paz"; document.getElementById("lz-l4").textContent = "P4: Talcahuano";
  } else {
    s1.max = 20000; s2.max = 10000; s3.max = 5000; s4.max = 5000;
    s1.value = 5520; s2.value = 4541; s3.value = 122; s4.value = 50;
    document.getElementById("lz-l1").textContent = "P1: Villa Esperanza"; document.getElementById("lz-l2").textContent = "P2: El Rincón";
    document.getElementById("lz-l3").textContent = "P3: Pueblo Nuevo"; document.getElementById("lz-l4").textContent = "P4: El Quebradero";
  }
  drawLorenz();
}
function fijarGhostLorenz() {
  ghostLz = [+document.getElementById("lz-p1").value, +document.getElementById("lz-p2").value, +document.getElementById("lz-p3").value, +document.getElementById("lz-p4").value];
  drawLorenz();
}
function calcLorenz(arr) {
  const ord = [...arr].sort((a, b) => a - b);
  const tot = ord.reduce((s, v) => s + v, 0) || 1;
  const n = ord.length;
  const pts = [{ p: 0, q: 0 }];
  let acc = 0, areaTrap = 0, theil = 0;
  for (let i = 0; i < n; i++) {
    const qPrev = acc / tot;
    acc += ord[i];
    const qCur = acc / tot;
    pts.push({ p: (i + 1) / n, q: qCur });
    areaTrap += (1 / n) * (qPrev + qCur);
    const si = ord[i] / tot;
    if (si > 0) theil += si * Math.log(n * si);
  }
  return { pts, gini: Math.max(0, 1 - areaTrap), theil: Math.max(0, theil), tot };
}
function drawLorenz() {
  const arr = [+document.getElementById("lz-p1").value, +document.getElementById("lz-p2").value, +document.getElementById("lz-p3").value, +document.getElementById("lz-p4").value];
  document.getElementById("lz-p1-v").textContent = fmtInt(arr[0]);
  document.getElementById("lz-p2-v").textContent = fmtInt(arr[1]);
  document.getElementById("lz-p3-v").textContent = fmtInt(arr[2]);
  document.getElementById("lz-p4-v").textContent = fmtInt(arr[3]);

  const desc = [...arr].sort((a, b) => b - a);
  const ip4 = desc[0] / Math.max(1, desc[1] + desc[2] + desc[3]);
  const ip2 = desc[0] / Math.max(1, desc[1]);
  const cur = calcLorenz(arr), gho = calcLorenz(ghostLz);

  let catTxt = "Valor 0: Muy Dispersa";
  if (ip4 >= 1.50) catTxt = "Valor 3: Alt. Concentrada";
  else if (ip4 >= 1.00) catTxt = "Valor 2: Concentrada";
  else if (ip4 >= 0.65) catTxt = "Valor 1: Dispersa";

  document.getElementById("lz-enunciado").innerHTML =
    `Las cuatro mayores ciudades de la región concentran poblaciones de <b>P<sub>1</sub> = ${fmtInt(desc[0])}</b>, <b>P<sub>2</sub> = ${fmtInt(desc[1])}</b>, ` +
    `<b>P<sub>3</sub> = ${fmtInt(desc[2])}</b> y <b>P<sub>4</sub> = ${fmtInt(desc[3])} hab.</b> Calcule el Índice de Primacía <b>IP<sub>4</sub> = ${fmtDec(ip4,3)}</b> (${catTxt}), ` +
    `el Índice de Gini por trapecios (<b>G = ${fmtDec(cur.gini,3)}</b>) y la Entropía de Theil (<b>T = ${fmtDec(cur.theil,3)}</b>).`;

  document.getElementById("lz-k-ip4").textContent = fmtDec(ip4, 3);
  document.getElementById("lz-k-ip2").textContent = `IP2 (P1/P2) = ${fmtDec(ip2, 3)}`;
  document.getElementById("lz-k-cat").textContent = catTxt;
  document.getElementById("lz-k-gini").textContent = fmtDec(cur.gini, 3);
  const dg = cur.gini - gho.gini;
  document.getElementById("lz-k-dgini").textContent = `ΔG vs Fantasma: ${dg >= 0 ? "+" : "-"}${fmtDec(Math.abs(dg), 3)}`;
  document.getElementById("lz-k-theil").textContent = fmtDec(cur.theil, 3);
  document.getElementById("lz-k-cuota").textContent = `Cuota P1: ${fmtDec((desc[0] / cur.tot) * 100, 1)}%`;

  const svg = document.getElementById("svg-lorenz");
  svg.innerHTML = "";
  addDefs(svg);
  const M = { l: 64, r: 460, t: 28, b: 46 }, W = 980, H = 385;
  const sx = p => M.l + p * (W - M.l - M.r);
  const sy = q => H - M.b - q * (H - M.t - M.b);

  for (let v = 0; v <= 1.001; v += 0.25) {
    el("line", { x1: M.l, y1: sy(v), x2: W - M.r, y2: sy(v), stroke: "#E2E8F0" }, svg);
    el("line", { x1: sx(v), y1: M.t, x2: sx(v), y2: H - M.b, stroke: "#F1F5F9" }, svg);
    const ty = el("text", { x: M.l - 8, y: sy(v) + 4, fill: "#475569", "font-size": "11", "text-anchor": "end" }, svg);
    ty.textContent = Math.round(v * 100) + "%";
    const tx = el("text", { x: sx(v), y: H - M.b + 16, fill: "#475569", "font-size": "11", "text-anchor": "middle" }, svg);
    tx.textContent = Math.round(v * 100) + "%";
  }
  el("line", { x1: M.l, y1: H - M.b, x2: W - M.r, y2: H - M.b, stroke: "#334155", "stroke-width": "1.5" }, svg);
  el("line", { x1: M.l, y1: M.t, x2: M.l, y2: H - M.b, stroke: "#334155", "stroke-width": "1.5" }, svg);
  el("line", { x1: sx(0), y1: sy(0), x2: sx(1), y2: sy(1), stroke: "#64748B", "stroke-width": "1.8", "stroke-dasharray": "6,4" }, svg);
  el("polygon", { points: cur.pts.map(pt => `${sx(pt.p)},${sy(pt.q)}`).join(" ") + ` ${sx(0)},${sy(0)}`, fill: "rgba(220,38,38,0.16)" }, svg);
  if (Math.abs(dg) > 0.004) {
    el("polyline", { points: gho.pts.map(pt => `${sx(pt.p)},${sy(pt.q)}`).join(" "), fill: "none", stroke: "#94A3B8", "stroke-width": "2", "stroke-dasharray": "4,4" }, svg);
    drawArrow(svg, sx(gho.pts[3].p), sy(gho.pts[3].q), sx(cur.pts[3].p), sy(cur.pts[3].q), dg > 0 ? "#DC2626" : "#15803D", dg > 0 ? "arr-red" : "arr-green", dg > 0 ? "↑ Mayor Gini" : "↓ Menor Gini", sx(cur.pts[3].p) - 46, (sy(gho.pts[3].q) + sy(cur.pts[3].q)) / 2);
  }
  el("polyline", { points: cur.pts.map(pt => `${sx(pt.p)},${sy(pt.q)}`).join(" "), fill: "none", stroke: "#DC2626", "stroke-width": "2.8" }, svg);
  cur.pts.forEach(pt => el("circle", { cx: sx(pt.p), cy: sy(pt.q), r: 4.5, fill: "#DC2626" }, svg));

  // Termómetro IP4 derecho
  const bx = 575, bw = 370, by = 185, bh = 32, maxIP = 2.4;
  const sip = v => bx + (Math.min(v, maxIP) / maxIP) * bw;
  const tBar = el("text", { x: bx + bw / 2, y: 120, fill: "#0F172A", "font-size": "12.5", "font-weight": "700", "text-anchor": "middle" }, svg);
  tBar.textContent = "Escala Estandarizada de Primacía IP4 (06 OT 2024.pdf)";
  for (const [a, b, bg, fg, lbl] of [[0,0.65,"#DCFCE7","#166534","0: Muy Disp."],[0.65,1.00,"#DBEAFE","#1E40AF","1: Disp."],[1.00,1.50,"#FEF3C7","#92400E","2: Conc."],[1.50,maxIP,"#FEE2E2","#991B1B","3: Macrocefalia"]]) {
    el("rect", { x: sip(a), y: by, width: sip(b) - sip(a), height: bh, fill: bg, stroke: "#CBD5E1" }, svg);
    const tl = el("text", { x: (sip(a) + sip(b)) / 2, y: by + bh + 18, fill: fg, "font-size": "10.5", "font-weight": "700", "text-anchor": "middle" }, svg);
    tl.textContent = lbl;
  }
  const gDesc = [...ghostLz].sort((a, b) => b - a);
  const gIp4 = gDesc[0] / Math.max(1, gDesc[1] + gDesc[2] + gDesc[3]);
  if (Math.abs(ip4 - gIp4) > 0.02) {
    drawArrow(svg, sip(gIp4), by - 20, sip(ip4), by - 20, ip4 > gIp4 ? "#DC2626" : "#15803D", ip4 > gIp4 ? "arr-red" : "arr-green", `IP4: ${fmtDec(ip4, 2)}`, (sip(gIp4) + sip(ip4)) / 2, by - 30);
  }
  el("circle", { cx: sip(ip4), cy: by + bh / 2, r: 8, fill: "#0F172A", stroke: "#FFFFFF", "stroke-width": "2" }, svg);
}

// ============================================================================
// 7. REDES EMPRESARIALES DE DINI (2010) A 60 FPS
// ============================================================================
const TOPOS_DINI = {
  simetrica: {
    desc: "<b>Red Simétrica (Dini, 2010 — Diagrama 2):</b> Cooperación horizontal entre pares con grado nodal homogéneo. <b>Gradiente GC = 0%</b>.",
    nodes: Array.from({length: 8}, (_, i) => ({ nm: `PyME ${i+1}`, x: 265 + 145 * Math.cos(i * Math.PI / 4), y: 195 + 135 * Math.sin(i * Math.PI / 4) })),
    edges: [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,0],[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,0],[7,1]]
  },
  liderazgo: {
    desc: "<b>Red con Liderazgo (Dini, 2010 — Diagrama 2):</b> Estructura radial tipo estrella. Un nodo ancla centraliza todos los acuerdos. <b>Gradiente GC = 100%</b>.",
    nodes: [{ nm: "Empresa Líder", x: 265, y: 195 }, ...Array.from({length: 7}, (_, i) => ({ nm: `PyME ${i+1}`, x: 265 + 145 * Math.cos(i * 2 * Math.PI / 7), y: 195 + 135 * Math.sin(i * 2 * Math.PI / 7) }))],
    edges: [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]]
  },
  jerarquica: {
    desc: "<b>Red Jerárquica (Dini, 2010 — Diagrama 2):</b> Subcontratación escalonada por niveles (Matriz → Contratistas → Talleres) sin vínculos horizontales en la base.",
    nodes: [
      { nm: "Matriz Ancla", x: 265, y: 55 }, { nm: "Contratista 1A", x: 160, y: 175 }, { nm: "Contratista 1B", x: 370, y: 175 },
      { nm: "Taller 2A", x: 95, y: 310 }, { nm: "Taller 2B", x: 210, y: 310 }, { nm: "Taller 2C", x: 320, y: 310 }, { nm: "Proveedor 2D", x: 435, y: 310 }
    ],
    edges: [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
  },
  red_redes: {
    desc: "<b>Red de Redes (Dini, 2010 — Diagrama 3):</b> Tres clústeres locales (Osorno, Pto. Montt, Valdivia) cohesionados cuyos nodos puente se articulan entre sí.",
    nodes: [
      { nm: "Líder Osorno", x: 165, y: 135 }, { nm: "O1", x: 95, y: 70 }, { nm: "O2", x: 85, y: 175 }, { nm: "O3", x: 160, y: 215 },
      { nm: "Líder P.Montt", x: 370, y: 135 }, { nm: "M1", x: 445, y: 75 }, { nm: "M2", x: 455, y: 175 }, { nm: "M3", x: 365, y: 215 },
      { nm: "Líder Valdivia", x: 265, y: 285 }, { nm: "V1", x: 195, y: 345 }, { nm: "V2", x: 335, y: 345 }, { nm: "V3", x: 265, y: 225 }
    ],
    edges: [[0,4],[4,8],[0,8],[0,1],[0,2],[0,3],[4,5],[4,6],[4,7],[6,7],[8,9],[8,10],[8,11]]
  },
  aviones: {
    desc: "<b>Red de Redes en Producción de Aviones (Dini, 2010 — Diagrama 4):</b> Una gran ensambladora central coordina a los líderes de subsistemas (Motores, Aviónica, Fuselaje).",
    nodes: [
      { nm: "ENSAMBLADORA", x: 265, y: 195 },
      { nm: "Líder Motores", x: 135, y: 125 }, { nm: "Turb.A", x: 65, y: 68 }, { nm: "Turb.B", x: 60, y: 165 },
      { nm: "Líder Aviónica", x: 395, y: 125 }, { nm: "Soft.A", x: 465, y: 68 }, { nm: "Radar", x: 470, y: 165 },
      { nm: "Líder Fuselaje", x: 265, y: 305 }, { nm: "Aleac.", x: 185, y: 350 }, { nm: "Cabina", x: 345, y: 350 }
    ],
    edges: [[0,1],[0,4],[0,7],[1,2],[1,3],[4,5],[4,6],[7,8],[7,9],[8,9]]
  },
  osorno: {
    desc: "<b>Caso Control 4 — Red Láctea-Quesera de Osorno:</b> Articulación multilateral liderada por <i>Aproleche</i> y <i>Cooprinsem</i> conectada a plantas ancla (<i>Nestlé, Watt's</i>) e <i>INIA Remehue</i>.",
    nodes: [
      { nm: "Aproleche", x: 265, y: 155 }, { nm: "Cooprinsem", x: 225, y: 235 }, { nm: "INIA", x: 120, y: 90 }, { nm: "Lech.Matthei", x: 90, y: 215 },
      { nm: "Q.Las Ánimas", x: 145, y: 325 }, { nm: "Láct.Osorno", x: 315, y: 330 }, { nm: "Nestlé", x: 425, y: 115 }, { nm: "Watt's", x: 440, y: 235 }, { nm: "DeLaval", x: 345, y: 65 }
    ],
    edges: [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[2,3],[3,6],[3,7],[4,5],[6,8],[7,8]]
  },
  pymemad: {
    desc: "<b>Caso Control 4 — Clúster Forestal-Maderero PymeMad (Biobío):</b> El gremio <i>PymeMad</i> coordina aserraderos y plantas de remanufactura CLT para compras y certificación estructural.",
    nodes: [
      { nm: "Gremio PymeMad", x: 265, y: 195 }, { nm: "Aserradero 1", x: 130, y: 105 }, { nm: "Aserradero 2", x: 115, y: 260 },
      { nm: "Remanuf. CLT", x: 265, y: 335 }, { nm: "Prov. Forestal", x: 265, y: 55 }, { nm: "Logística", x: 410, y: 280 },
      { nm: "Planta Ancla", x: 420, y: 130 }, { nm: "Centro I+D", x: 365, y: 65 }
    ],
    edges: [[0,1],[0,2],[0,3],[0,4],[0,6],[0,7],[1,2],[1,3],[1,4],[2,3],[3,5],[3,6],[3,7],[4,5],[4,6],[5,6],[6,7]]
  }
};
let diniKey = "simetrica";
let animDnId = null;

function setTopologiaDini(key, btn) {
  if (animDnId) cancelAnimationFrame(animDnId);
  diniKey = key;
  btn.parentElement.querySelectorAll(".flt-btn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");
  const maxE = TOPOS_DINI[key].edges.length;
  const sl = document.getElementById("dn-step");
  sl.max = maxE; sl.value = maxE;
  drawDini();
}
function completarDini() {
  if (animDnId) cancelAnimationFrame(animDnId);
  const sl = document.getElementById("dn-step");
  sl.value = sl.max;
  drawDini();
}
function animarDini() {
  if (animDnId) cancelAnimationFrame(animDnId);
  const maxE = TOPOS_DINI[diniKey].edges.length;
  const t0 = performance.now(), dur = Math.max(1200, maxE * 130);
  function step(now) {
    const u = Math.min(1, (now - t0) / dur);
    document.getElementById("dn-step").value = Math.round(u * maxE);
    drawDini();
    if (u < 1) animDnId = requestAnimationFrame(step);
  }
  animDnId = requestAnimationFrame(step);
}
function drawDini() {
  const topo = TOPOS_DINI[diniKey];
  const n = topo.nodes.length, maxE = topo.edges.length;
  const kStep = Math.min(maxE, +document.getElementById("dn-step").value);
  document.getElementById("dn-step-v").textContent = `${kStep} / ${maxE} vínculos`;
  document.getElementById("dn-enunciado").innerHTML = topo.desc;

  const deg = new Array(n).fill(0);
  const actEdges = topo.edges.slice(0, kStep);
  actEdges.forEach(([u, v]) => { deg[u]++; deg[v]++; });

  const lMax = (n * (n - 1)) / 2;
  const den = lMax > 0 ? (kStep / lMax) * 100 : 0;
  const kMax = Math.max(...deg);
  const kAvg = deg.reduce((s, v) => s + v, 0) / n;
  const gc = n > 2 ? (deg.reduce((s, v) => s + (kMax - v), 0) / ((n - 1) * (n - 2))) * 100 : 0;

  document.getElementById("dn-k-nl").textContent = `n=${n} | L=${kStep}`;
  document.getElementById("dn-k-lmax").textContent = `Máx posible: ${lMax}`;
  document.getElementById("dn-k-den").textContent = fmtDec(den, 1) + "%";
  document.getElementById("dn-k-k").textContent = `k_máx=${kMax} | k̄=${fmtDec(kAvg, 1)}`;
  document.getElementById("dn-k-gc").textContent = fmtDec(gc, 1) + "%";
  document.getElementById("dn-k-gcd").textContent = gc < 15 ? "Red Simétrica" : (gc > 68 ? "Red con Liderazgo Fuerte" : "Red Jerárquica / Policéntrica");

  const svg = document.getElementById("svg-dini");
  svg.innerHTML = "";
  // Izquierda: Grafo SVG
  actEdges.forEach(([u, v], idx) => {
    const isLast = idx === kStep - 1;
    el("line", { x1: topo.nodes[u].x, y1: topo.nodes[u].y, x2: topo.nodes[v].x, y2: topo.nodes[v].y, stroke: isLast ? "#DC2626" : "#64748B", "stroke-width": isLast ? "3.4" : "2.1" }, svg);
  });
  topo.nodes.forEach((nd, i) => {
    const r = 10 + deg[i] * 2.2;
    const isHub = deg[i] === kMax && kMax > 0;
    el("circle", { cx: nd.x, cy: nd.y, r, fill: isHub ? "#DC2626" : "#1D4ED8", stroke: "#FFFFFF", "stroke-width": "2" }, svg);
    const t = el("text", { x: nd.x, y: nd.y - r - 4, fill: "#0F172A", "font-size": "10.5", "font-weight": "700", "text-anchor": "middle" }, svg);
    t.textContent = `${nd.nm} (k=${deg[i]})`;
  });

  // Derecha: Curva de Gradiente Nodal (k_i ordenado de mayor a menor)
  const ord = topo.nodes.map((nd, i) => ({ nm: nd.nm, k: deg[i] })).sort((a, b) => b.k - a.k);
  const bx = 545, bwTot = 410, by = 330, bhMax = 250;
  const maxKPlot = Math.max(4, kMax);
  const slot = bwTot / n, bw = Math.min(34, slot * 0.65);
  const tTit = el("text", { x: bx + bwTot / 2, y: 28, fill: "#0F172A", "font-size": "12", "font-weight": "700", "text-anchor": "middle" }, svg);
  tTit.textContent = "Gradiente de Concentración Nodal (k_i ordenado)";
  el("line", { x1: bx, y1: by, x2: bx + bwTot, y2: by, stroke: "#334155", "stroke-width": "1.5" }, svg);

  const lPts = [];
  ord.forEach((o, i) => {
    const x0 = bx + i * slot + (slot - bw) / 2;
    const h = (o.k / maxKPlot) * bhMax;
    el("rect", { x: x0, y: by - h, width: bw, height: Math.max(2, h), fill: i === 0 && o.k > 0 ? "#DC2626" : "#2563EB", rx: 3 }, svg);
    lPts.push(`${x0 + bw / 2},${by - h}`);
    const tv = el("text", { x: x0 + bw / 2, y: by - h - 5, fill: "#0F172A", "font-size": "10.5", "font-weight": "800", "text-anchor": "middle" }, svg);
    tv.textContent = o.k;
    const tl = el("text", { x: x0 + bw / 2, y: by + 14, fill: "#334155", "font-size": "9.2", "font-weight": "700", "text-anchor": "middle" }, svg);
    tl.textContent = o.nm.slice(0, 7);
  });
  if (lPts.length > 1) el("polyline", { points: lPts.join(" "), fill: "none", stroke: "#DC2626", "stroke-width": "2.2", "stroke-dasharray": "4,3" }, svg);
}

// ============================================================================
// 8. HOJA DE ENTRENAMIENTO MECÁNICO TERRITORIAL (16 FÓRMULAS + 6 ESQUELETOS)
// ============================================================================
const FORMULAS_TERR = [
  { id: 1, cat: "loc", tag: "Von Thünen", title: "1. Renta Locacional y Anillos",
    eq: `LR(d) = Y(m − c) − Y·t·d`,
    rule: "Pendiente negativa (-Y·t). Las actividades con mayor flete/margen ocupan el anillo más cercano al mercado urbano." },
  { id: 2, cat: "loc", tag: "Weber", title: "2. Índice de Materiales (IM) e Isodápana",
    eq: `IM = <span class="frac"><span class="num">Peso MP Localizadas</span><span class="den">Peso Producto Final</span></span>`,
    rule: "IM > 1 → cerca de insumos (pérdida de peso). IM < 1 → cerca del mercado. Desvío a L solo si cae dentro de la isodápana crítica." },
  { id: 3, cat: "loc", tag: "Krugman", title: "3. Nueva Economía Geográfica (Precio y τ*)",
    eq: `p*(x) = <span class="frac"><span class="num">a·W(x)</span><span class="den">ρ</span></span> &nbsp;|&nbsp; τ ≤ τ* ⇒ Aglomeración`,
    rule: "Si el costo de transporte τ cae bajo el umbral crítico τ*, las fuerzas centrípetas (escala + mercado local) disparan la macrocefalia." },
  { id: 4, cat: "loc", tag: "Hirschman", title: "4. Polos (Perroux/Hirschman/Myrdal) y Christaller",
    eq: `M<sub>H</sub> = <span class="frac"><span class="num">1</span><span class="den">1 − (b + f)</span></span> &nbsp;|&nbsp; Pob ≥ Umbral ∧ Alcance ≥ Dist`,
    rule: "Saldo periferia = Spread − Backwash. En Christaller un servicio es viable si supera el Umbral demográfico dentro de su Alcance (km)." },

  { id: 5, cat: "ilpes", tag: "ILPES 59", title: "5. Cociente de Localización (Qij)",
    eq: `Q<sub>ij</sub> = <span class="frac"><span class="num">V<sub>ij</sub> / ∑<sub>i</sub> V<sub>ij</sub></span><span class="den">∑<sub>j</sub> V<sub>ij</sub> / ∑<sub>i</sub>∑<sub>j</sub> V<sub>ij</sub></span></span>`,
    rule: "Qij > 1 indica especialización relativa de la comuna j en el sector i (sector básico exportador)." },
  { id: 6, cat: "ilpes", tag: "ILPES 59", title: "6. Coeficiente de Especialización (Qr)",
    eq: `Q<sub>r</sub> = <span class="frac"><span class="num">1</span><span class="den">2</span></span> ∑<sub>i</sub> |P<sub>ij</sub> − P<sub>i</sub>|`,
    rule: "Rango [0, 1]. Cercano a 0 = estructura diversificada (igual a la región); cercano a 1 = alta especialización comunal." },
  { id: 7, cat: "ilpes", tag: "ILPES 59", title: "7. Coeficiente de Reestructuración (CRr)",
    eq: `CR<sub>r</sub> = <span class="frac"><span class="num">1</span><span class="den">2</span></span> ∑<sub>i</sub> |P<sub>ij,t</sub> − P<sub>ij,0</sub>|`,
    rule: "Rango [0, 1]. Mide cuánto cambió la composición sectorial de una comuna entre el año inicial t0 y el final tf." },
  { id: 8, cat: "ilpes", tag: "Tiebout", title: "8. Base Económica Exportadora y Multiplicador",
    eq: `X<sub>ij</sub> = V<sub>ij</sub> − <span class="frac"><span class="num">V<sub>ij</sub></span><span class="den">Q<sub>ij</sub></span></span> (∀Q<sub>ij</sub>&gt;1) &nbsp;|&nbsp; M<sub>j</sub> = <span class="frac"><span class="num">V<sub>j</sub></span><span class="den">X<sub>j</sub></span></span>`,
    rule: "Xj es el excedente exportable de la comuna. Mj indica cuánta actividad total genera cada $1 de base exportadora." },
  { id: 9, cat: "ilpes", tag: "MADE", title: "9. Shift & Share Clásico y Modificado (Stilwell)",
    eq: `ET<sub>j</sub> = EE<sub>j</sub> + ED<sub>j</sub> &nbsp;|&nbsp; EM<sub>j</sub> = EI<sub>j</sub> − EE<sub>j</sub> ; ERM<sub>j</sub> = ET<sub>j</sub> − EI<sub>j</sub>`,
    rule: "EE = composición sectorial; ED = competitividad local. 6 tipologías de Boisier (clásico) y 14 tipologías de Stilwell (modificado)." },

  { id: 10, cat: "reat", tag: "REAT", title: "10. Convergencia Sigma (σ) y Beta Absoluta (β)",
    eq: `<span class="frac"><span class="num">1</span><span class="den">T</span></span>ln(<span class="frac"><span class="num">Y<sub>i,t</sub></span><span class="den">Y<sub>i,0</sub></span></span>) = α + β·ln(Y<sub>i,0</sub>) + ε<sub>i</sub>`,
    rule: "β < 0 y p < 0,05 confirma Convergencia Beta. Velocidad λ = −ln(1 + βT)/T y Semivida t(1/2) = ln(2)/λ." },
  { id: 11, cat: "reat", tag: "REAT", title: "11. Curva de Lorenz e Índice de Gini (Trapecios)",
    eq: `G = 1 − ∑<sub>i=1..n</sub> (p<sub>i</sub> − p<sub>i-1</sub>)(q<sub>i</sub> + q<sub>i-1</sub>) &nbsp;|&nbsp; G* = G·<span class="frac"><span class="num">N</span><span class="den">N−1</span></span>`,
    rule: "G = 0 equidad perfecta; G → 1 concentración absoluta. A mayor alejamiento de la diagonal de 45°, mayor desigualdad." },
  { id: 12, cat: "reat", tag: "REAT", title: "12. Índice de Entropía de Theil (T)",
    eq: `T = ∑<sub>i=1..n</sub> s<sub>i</sub> · ln(n · s<sub>i</sub>)`,
    rule: "Rango [0, ln(n)]. Su gran ventaja sobre el Gini es ser perfectamente descomponible en desigualdad Entre-regiones + Intra-región." },
  { id: 13, cat: "reat", tag: "REAT", title: "13. Concentración: HHI y Hannah-Kay (HKα)",
    eq: `HHI = ∑ s<sub>i</sub><sup>2</sup> &nbsp;|&nbsp; HK<sub>α</sub> = (∑ s<sub>i</sub><sup>α</sup>)<sup>1/(1−α)</sup>`,
    rule: "HHI ∈ [1/n, 1]. En la convención de número equivalente, HKα indica cuántas comunas de igual tamaño replican la concentración." },

  { id: 14, cat: "ot", tag: "Dini 2010", title: "14. Densidad de Red y Gradiente de Concentración",
    eq: `D = <span class="frac"><span class="num">2L</span><span class="den">n(n − 1)</span></span> &nbsp;|&nbsp; GC<sub>red</sub> = <span class="frac"><span class="num">∑(k<sub>máx</sub> − k<sub>i</sub>)</span><span class="den">(n−1)(n−2)</span></span>`,
    rule: "Diagonal principal A_ii = 0. En red dirigida D = L/[n(n−1)]. GC = 0% (Red Simétrica) ↔ GC = 100% (Red Estrella/Liderazgo)." },
  { id: 15, cat: "ot", tag: "OT 2024", title: "15. Índice de Primacía Urbana (IP4) y Zipf",
    eq: `IP<sub>4</sub> = <span class="frac"><span class="num">P<sub>1</sub></span><span class="den">P<sub>2</sub> + P<sub>3</sub> + P<sub>4</sub></span></span> &nbsp;|&nbsp; P<sub>r</sub> = <span class="frac"><span class="num">P<sub>1</sub></span><span class="den">r</span></span>`,
    rule: "Escala Mancilla (0–3): <0,65 Muy Disp.(0) · 0,65–1,00 Disp.(1) · 1,00–1,50 Conc.(2) · ≥1,50 Macrocefalia(3)." },
  { id: 16, cat: "ot", tag: "Rondinelli", title: "16. Escalograma de Guttman y Centralidad Rondinelli",
    eq: `W<sub>k</sub> = <span class="frac"><span class="num">100</span><span class="den">f<sub>k</sub></span></span> &nbsp;|&nbsp; IC<sub>i</sub> = ∑<sub>k</sub> X<sub>ik</sub> · W<sub>k</sub>`,
    rule: "X_ik ∈ {0,1}. Variables deben discriminar entre comunas (si todas tienen 1, reemplazar). Servicios más raros otorgan mayor peso Wk." }
];

const ESQUELETOS_TERR = [
  {
    title: "1. Von Thünen (Gradiente LR y Anillos)",
    sub: "Mayor pendiente = anillo interior; los cortes LR1=LR2 y LR2=LR3 fijan los radios.",
    svg: `<svg viewBox="0 0 260 150">
      <line x1="22" y1="128" x2="148" y2="128" stroke="#0F172A" stroke-width="1.5"/><line x1="22" y1="16" x2="22" y2="128" stroke="#0F172A" stroke-width="1.5"/>
      <line x1="22" y1="26" x2="78" y2="128" stroke="#DC2626" stroke-width="2"/><line x1="22" y1="58" x2="112" y2="128" stroke="#1D4ED8" stroke-width="2"/>
      <line x1="22" y1="90" x2="144" y2="128" stroke="#059669" stroke-width="2"/>
      <circle cx="206" cy="76" r="46" fill="rgba(5,150,105,0.18)" stroke="#059669"/><circle cx="206" cy="76" r="30" fill="rgba(29,78,216,0.20)" stroke="#1D4ED8"/>
      <circle cx="206" cy="76" r="15" fill="rgba(220,38,38,0.24)" stroke="#DC2626"/><circle cx="206" cy="76" r="3" fill="#0F172A"/>
      <g class="sk-lbl" font-size="9" font-weight="700">
        <text x="10" y="24">LR</text><text x="142" y="142">d</text><text x="48" y="45" fill="#DC2626">LR1</text><text x="86" y="76" fill="#1D4ED8">LR2</text><text x="122" y="106" fill="#059669">LR3</text>
        <text x="206" y="140" text-anchor="middle">Anillos 1-2-3</text>
      </g>
    </svg>`
  },
  {
    title: "2. Triángulo de Weber + Isodápana",
    sub: "IM>1 atrae P* a MP1/MP2; desvío a L solo si L cae dentro de la curva punteada.",
    svg: `<svg viewBox="0 0 260 150">
      <polygon points="48,26 48,128 214,78" fill="#F8FAFC" stroke="#94A3B8" stroke-width="1.6"/>
      <circle cx="114" cy="78" r="44" fill="rgba(21,128,61,0.12)" stroke="#15803D" stroke-width="1.6" stroke-dasharray="4,3"/>
      <circle cx="48" cy="26" r="5" fill="#1D4ED8"/><circle cx="48" cy="128" r="5" fill="#1D4ED8"/><circle cx="214" cy="78" r="5" fill="#0F172A"/>
      <circle cx="114" cy="78" r="5" fill="#DC2626"/><circle cx="146" cy="46" r="5" fill="#EA580C"/>
      <g class="sk-lbl" font-size="9" font-weight="700">
        <text x="26" y="22" fill="#1D4ED8">MP1</text><text x="26" y="142" fill="#1D4ED8">MP2</text><text x="218" y="82">M</text>
        <text x="106" y="96" fill="#DC2626">P*</text><text x="154" y="46" fill="#EA580C">L</text><text x="118" y="138" fill="#15803D">Isodápana</text>
      </g>
    </svg>`
  },
  {
    title: "3. Bifurcación de Krugman (τ*)",
    sub: "Al bajar τ bajo τ* la participación del centro salta de 50% a aglomeración.",
    svg: `<svg viewBox="0 0 260 150">
      <line x1="28" y1="128" x2="244" y2="128" stroke="#0F172A" stroke-width="1.5"/><line x1="28" y1="16" x2="28" y2="128" stroke="#0F172A" stroke-width="1.5"/>
      <line x1="136" y1="18" x2="136" y2="128" stroke="#D97706" stroke-width="1.8" stroke-dasharray="4,3"/>
      <path d="M 34 28 C 95 30, 120 55, 136 74 C 152 93, 175 112, 240 116" fill="none" stroke="#1D4ED8" stroke-width="2.4"/>
      <g class="sk-lbl" font-size="9" font-weight="700">
        <text x="6" y="28">100%</text><text x="8" y="120">50%</text><text x="140" y="28" fill="#B45309">τ*</text>
        <text x="48" y="50" fill="#DC2626">Aglomeración</text><text x="166" y="102" fill="#15803D">Dispersión</text><text x="234" y="142">τ</text>
      </g>
    </svg>`
  },
  {
    title: "4. Cuadrantes de Silva Lira (2×2)",
    sub: "Eje X: Nivel per cápita vs prom. reg.; Eje Y: Crec. anual vs prom. reg.",
    svg: `<svg viewBox="0 0 260 150">
      <rect x="26" y="18" width="214" height="108" fill="#FFFFFF" stroke="#94A3B8"/>
      <line x1="133" y1="18" x2="133" y2="126" stroke="#1D4ED8" stroke-width="1.6" stroke-dasharray="4,3"/>
      <line x1="26" y1="72" x2="240" y2="72" stroke="#DC2626" stroke-width="1.6" stroke-dasharray="4,3"/>
      <g class="sk-lbl" font-size="9" font-weight="700" text-anchor="middle">
        <text x="80" y="48" fill="#1D4ED8">II. Emergente (-,+)</text><text x="186" y="48" fill="#15803D">I. Dinámica (+,+)</text>
        <text x="80" y="102" fill="#DC2626">IV. Retroceso (-,-)</text><text x="186" y="102" fill="#B45309">III. Estancada (+,-)</text>
        <text x="133" y="142">Nivel per cápita (X)</text>
      </g>
    </svg>`
  },
  {
    title: "5. Curva de Lorenz y Gini",
    sub: "Diagonal 45° = equidad perfecta; área sombreada = desigualdad (G = 2A).",
    svg: `<svg viewBox="0 0 260 150">
      <line x1="34" y1="128" x2="224" y2="128" stroke="#0F172A" stroke-width="1.5"/><line x1="34" y1="18" x2="34" y2="128" stroke="#0F172A" stroke-width="1.5"/>
      <line x1="34" y1="128" x2="224" y2="18" stroke="#64748B" stroke-width="1.6" stroke-dasharray="5,3"/>
      <path d="M 34 128 Q 160 122 224 18 L 34 128 Z" fill="rgba(220,38,38,0.18)" stroke="#DC2626" stroke-width="2"/>
      <g class="sk-lbl" font-size="9" font-weight="700">
        <text x="108" y="64" fill="#475569">45° Equidad</text><text x="132" y="104" fill="#DC2626">Área A (G=2A)</text>
        <text x="205" y="142">p_i %</text><text x="8" y="26">q_i %</text>
      </g>
    </svg>`
  },
  {
    title: "6. Redes Dini: Simétrica vs. Liderazgo",
    sub: "Izq: todos igual k (GC=0%). Der: nodo líder central (GC=100%).",
    svg: `<svg viewBox="0 0 260 150">
      <polygon points="62,36 96,60 84,104 40,104 28,60" fill="none" stroke="#1D4ED8" stroke-width="1.8"/>
      <circle cx="62" cy="36" r="5" fill="#1D4ED8"/><circle cx="96" cy="60" r="5" fill="#1D4ED8"/><circle cx="84" cy="104" r="5" fill="#1D4ED8"/><circle cx="40" cy="104" r="5" fill="#1D4ED8"/><circle cx="28" cy="60" r="5" fill="#1D4ED8"/>
      <line x1="194" y1="74" x2="194" y2="34" stroke="#DC2626" stroke-width="1.8"/><line x1="194" y1="74" x2="232" y2="62" stroke="#DC2626" stroke-width="1.8"/>
      <line x1="194" y1="74" x2="218" y2="108" stroke="#DC2626" stroke-width="1.8"/><line x1="194" y1="74" x2="170" y2="108" stroke="#DC2626" stroke-width="1.8"/><line x1="194" y1="74" x2="156" y2="62" stroke="#DC2626" stroke-width="1.8"/>
      <circle cx="194" cy="74" r="8" fill="#DC2626"/><circle cx="194" cy="34" r="4.5" fill="#0F172A"/><circle cx="232" cy="62" r="4.5" fill="#0F172A"/><circle cx="218" cy="108" r="4.5" fill="#0F172A"/><circle cx="170" cy="108" r="4.5" fill="#0F172A"/><circle cx="156" cy="62" r="4.5" fill="#0F172A"/>
      <g class="sk-lbl" font-size="9" font-weight="700" text-anchor="middle">
        <text x="62" y="138" fill="#1D4ED8">Simétrica (GC=0%)</text><text x="194" y="138" fill="#DC2626">Liderazgo (GC=100%)</text>
      </g>
    </svg>`
  }
];

let mecBlind = false, mecFilter = "all", mecMastered = new Set(), mecBuilt = false;
function renderMecanica() {
  const fGrid = document.getElementById("mec-formulas-grid"), sGrid = document.getElementById("mec-skel-grid");
  if (!fGrid || !sGrid) return;
  fGrid.innerHTML = "";
  FORMULAS_TERR.filter(f => mecFilter === "all" || f.cat === mecFilter).forEach(item => {
    const card = document.createElement("div");
    card.className = "f-card" + (mecMastered.has(item.id) ? " mastered" : "");
    card.innerHTML = `
      <div class="f-head">
        <div><span class="f-cat">${item.tag}</span> <span class="f-title">${item.title}</span></div>
        <button class="chk-btn" title="Marcar dominada" onclick="toggleMastered(${item.id}, event)">✓</button>
      </div>
      <div class="f-body" onclick="this.parentElement.classList.toggle('revealed')">
        <div class="blind-cover">Haz clic para revelar y comprobar tu cuaderno</div>
        <div class="f-eq">${item.eq}</div>
        <div class="f-rule">${item.rule}</div>
      </div>`;
    fGrid.appendChild(card);
  });
  if (!mecBuilt) {
    sGrid.innerHTML = "";
    ESQUELETOS_TERR.forEach(sk => {
      const sc = document.createElement("div");
      sc.className = "s-card";
      sc.onclick = function() { this.classList.toggle("revealed"); };
      sc.innerHTML = `<div class="s-title">${sk.title}</div>${sk.svg}<div class="s-sub">${sk.sub}</div>`;
      sGrid.appendChild(sc);
    });
    mecBuilt = true;
  }
  document.getElementById("mec-score").textContent = `Dominadas: ${mecMastered.size} / ${FORMULAS_TERR.length}`;
}
function setModoMec(isBlind) {
  mecBlind = isBlind;
  const cont = document.getElementById("mec-container");
  cont.classList.toggle("blind-mode", isBlind);
  document.getElementById("btn-modo-copia").classList.toggle("primary", !isBlind);
  document.getElementById("btn-modo-ciego").classList.toggle("primary", isBlind);
  cont.querySelectorAll(".f-card, .s-card").forEach(n => n.classList.remove("revealed"));
}
function filtrarMec(cat, btn) {
  mecFilter = cat;
  btn.parentElement.querySelectorAll(".flt-btn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");
  renderMecanica();
}
function toggleMastered(id, ev) {
  ev.stopPropagation();
  if (mecMastered.has(id)) mecMastered.delete(id); else mecMastered.add(id);
  renderMecanica();
}
function resetDominadas() { mecMastered.clear(); renderMecanica(); }

drawThunen();
drawWeber();
drawKrugman();
drawPerroux();
drawChrisGran();
drawLorenz();

// ============================================================================
// 9. MAPA CAUSAL TEÓRICO, LECTURA EN 3 CAPAS Y QUIZ CRUZADO (60 FPS)
// ============================================================================
const MAPA_UNIDADES = {
  U1: {
    id: "U1", x: 130, y: 95, w: 205, h: 74, col: "#1D4ED8",
    lbl: "U1. LOCALIZACIÓN Y POLOS",
    sub: "Von Thünen · Weber · Krugman\nPerroux · Myrdal · Christaller",
    explica: "Explica por qué las actividades económicas NO se distribuyen de forma homogénea en el espacio: costos de transporte (t, τ), economías de escala, pérdida de peso (IM) y polos motrices generan anillos productivos y concentración en núcleos.",
    puentes: "<b>→ Hacia U2:</b> la localización de plantas crea especialización sectorial medible con Q<sub>ij</sub> &gt; 1 y Base Exportadora (X<sub>j</sub>). <b>→ Hacia U3:</b> cuando τ ≤ τ* (Krugman) o Backwash &gt; Spread (Myrdal), se amplían las disparidades (Gini/Theil). <b>→ Hacia U5:</b> el umbral y alcance de Christaller fundamentan la jerarquía de centros urbanos de Rondinelli.",
    jumps: [["thunen", "Abrir Von Thünen"], ["weber", "Abrir Weber"], ["krugman", "Abrir Krugman"], ["perroux", "Abrir Perroux/Myrdal"], ["christaller", "Abrir Christaller"]]
  },
  U2: {
    id: "U2", x: 490, y: 78, w: 215, h: 74, col: "#0F766E",
    lbl: "U2. ANÁLISIS REGIONAL ILPES",
    sub: "Manual 59 (Lira & Quiroga)\nQij · Qr · Xj/Mj · Silva Lira · MADE",
    explica: "Traduce la geografía productiva en indicadores empíricos sobre matrices Sector × Comuna (SII 2014–2024): detecta rubros exportadores (Q<sub>ij</sub> &gt; 1), diversificación (Q<sub>r</sub>), cambio estructural (CR<sub>r</sub>) y descompone el crecimiento en Efecto Estructural (EE) y Competitividad Local (ED).",
    puentes: "<b>← Desde U1:</b> un polo motriz (Perroux) eleva el multiplicador básico M<sub>j</sub>. <b>→ Hacia U3:</b> los Cuadrantes de Silva Lira (Emergentes vs. Estancadas) anticipan si habrá Convergencia β. <b>→ Hacia U4:</b> un Efecto Diferencial positivo (ED<sub>j</sub> &gt; 0) refleja competitividad local impulsada por redes y Upgrading.",
    jumps: [["mecanica", "Ver Fórmulas ILPES/MADE"]]
  },
  U3: {
    id: "U3", x: 850, y: 95, w: 205, h: 74, col: "#B91C1C",
    lbl: "U3. DISPARIDADES (REAT)",
    sub: "Convergencia σ y β · Lorenz/Gini\nTheil · HHI / HKα · Markov",
    explica: "Evalúa si las brechas entre territorios se cierran o se amplían en el tiempo: Convergencia Sigma (cae dispersión σ), Convergencia Beta (rezagados crecen más rápido, β &lt; 0), desigualdad (Gini y Theil descomponible), concentración (HHI, HK<sub>α</sub>) y transiciones de largo plazo (Markov).",
    puentes: "<b>← Desde U1 y U2:</b> la macrocefalia de Krugman o el estancamiento estructural (Tipo IV Boisier) elevan el Gini y el HHI. <b>→ Hacia U5:</b> alta desigualdad territorial justifica políticas de descentralización y Ordenamiento Territorial (PROT).",
    jumps: [["lorenz", "Abrir Lorenz, Gini y Theil"]]
  },
  U4: {
    id: "U4", x: 300, y: 245, w: 235, h: 74, col: "#7C3AED",
    lbl: "U4. SPL, REDES Y CADENAS",
    sub: "Dini (2010) · Schmitz · Granovetter\nPadilla & Oddone · ELITE (Boisier)",
    explica: "Aporta la palanca territorial para competir desde las PyMEs: pasar de empresas aisladas a Red Empresarial → Clúster → SPL, combinando vínculos fuertes (confianza) con vínculos débiles (innovación/I+D), escalamiento (Upgrading) y gobernanza interinstitucional (ELITE).",
    puentes: "<b>→ Hacia U1 y U2:</b> la cooperación horizontal (Aproleche, PymeMad) eleva los encadenamientos locales (b + f) y mejora el Efecto Diferencial (ED<sub>j</sub>). <b>→ Hacia U3:</b> el Upgrading de comunas intermedias impulsa convergencia regional.",
    jumps: [["dini", "Abrir Redes Dini 2010"], ["christaller", "Abrir Granovetter"]]
  },
  U5: {
    id: "U5", x: 685, y: 245, w: 235, h: 74, col: "#B45309",
    lbl: "U5. ORDENAMIENTO OT / PROT",
    sub: "Primacía IP4 · Ley de Zipf\nGuttman/Rondinelli · Aislamiento · PROT",
    explica: "Ordena el sistema de asentamientos humanos y resuelve conflictos de uso del suelo (Sistemas Costero, Urbano, Rural y Cuencas) mediante diagnóstico de macrocefalia (IP<sub>4</sub>), jerarquía de servicios (Guttman/Rondinelli) y conectividad vial (Matriz de Aislamiento 0/1).",
    puentes: "<b>← Desde U1 y U3:</b> traduce la aglomeración de Krugman y el Gini en Primacía Urbana (IP<sub>4</sub> escala 0–3). <b>→ Hacia U1 y U4:</b> reducir el aislamiento vial y dotar equipamiento intermedio amplía el alcance (Christaller) y fortalece el entorno del SPL.",
    jumps: [["lorenz", "Abrir Primacía IP4"], ["mecanica", "Abrir Hoja Mecánica"]]
  }
};

const MAPA_EDGES = [
  { a: "U1", b: "U2", lbl: "Especialización Qij" },
  { a: "U2", b: "U3", lbl: "Silva Lira → β/σ" },
  { a: "U1", b: "U3", lbl: "τ ≤ τ* → Gini↑" },
  { a: "U4", b: "U2", lbl: "Upgrading → EDj+" },
  { a: "U4", b: "U1", lbl: "Encadenam. b+f" },
  { a: "U3", b: "U5", lbl: "Brecha → OT/PROT" },
  { a: "U5", b: "U1", lbl: "Rondinelli/Umbral" },
  { a: "U4", b: "U5", lbl: "SPL + Gobernanza" }
];

const ESCENARIOS_MAPA = {
  fletes: {
    titulo: "Cadena A: Shock de Baja en Costos de Transporte (τ ↓)",
    nodes: ["U1", "U3", "U5"],
    edges: [["U1", "U3"], ["U3", "U5"], ["U5", "U1"]],
    texto: "<b>1) En U1 (Krugman):</b> al caer τ por debajo del umbral crítico τ*, se disparan las fuerzas centrípetas y las empresas se aglomeran en la capital regional (<i>Backwash</i>). " +
           "<b>2) En U3 (REAT):</b> aumenta la dispersión σ, la Curva de Lorenz se curva hacia abajo (suben Gini, Theil y HHI) y aparece divergencia. " +
           "<b>3) En U5 (OT):</b> el Índice de Primacía IP<sub>4</sub> salta al tramo ≥ 1,50 (Valor 3: Macrocefalia), exigiendo políticas PROT de reequilibrio hacia ciudades intermedias.",
    jumps: [["krugman", "Probar τ ↓ en Krugman"], ["lorenz", "Ver IP4 y Gini subir"]]
  },
  cluster: {
    titulo: "Cadena B: Política de Clúster, Puentes I+D y Upgrading (SPL)",
    nodes: ["U4", "U2", "U3"],
    edges: [["U4", "U2"], ["U2", "U3"]],
    texto: "<b>1) En U4 (Dini + Granovetter + Padilla/Oddone):</b> un gremio articulador (ej. PymeMad o Aproleche) abre vínculos débiles con universidades/I+D, evita el <i>lock-in</i> y ejecuta Upgrading de proceso y producto. " +
           "<b>2) En U2 (ILPES/MADE):</b> la comuna mejora su competitividad local (Efecto Diferencial ED<sub>j</sub> &gt; 0) y pasa a Cuadrante II (Emergente) o I (Dinámica) en Silva Lira. " +
           "<b>3) En U3 (REAT):</b> el mayor crecimiento de comunas no capitales empuja la pendiente β &lt; 0 (Convergencia Beta).",
    jumps: [["dini", "Probar Red Dini"], ["christaller", "Probar Puentes Granovetter"]]
  },
  prot: {
    titulo: "Cadena C: Planificación PROT + Reducción de Aislamiento Vial",
    nodes: ["U5", "U1", "U4"],
    edges: [["U5", "U1"], ["U4", "U5"], ["U4", "U1"]],
    texto: "<b>1) En U5 (OT/PROT):</b> el diagnóstico de Rondinelli/Guttman y la Matriz de Aislamiento detectan comunas con déficit de servicios intermedios y baja conectividad (índice alto de 1s). " +
           "<b>2) En U1 (Christaller + Von Thünen):</b> pavimentar rutas y dotar equipamiento intermedio amplía el alcance (km) y reduce el flete rural (t<sub>1</sub>), expandiendo los anillos productivos de mayor valor. " +
           "<b>3) En U4 (SPL):</b> el territorio consolidado habilita encadenamientos locales sostenibles sin conflictos de uso del suelo.",
    jumps: [["thunen", "Probar Baja Flete Von Thünen"], ["christaller", "Probar Umbral/Alcance"]]
  }
};

let mapaActivoUnidad = "U1";
let mapaEscenarioKey = null;

function selectUnidadMapa(uKey) {
  mapaEscenarioKey = null;
  mapaActivoUnidad = uKey;
  drawMapaTeoria();
}
function activarEscenarioMapa(escKey) {
  mapaEscenarioKey = escKey;
  drawMapaTeoria();
}
function drawMapaTeoria() {
  const svg = document.getElementById("svg-mapa-teoria");
  const box = document.getElementById("mapa-detail-box");
  if (!svg || !box) return;
  svg.innerHTML = "";
  addDefs(svg);

  const esc = mapaEscenarioKey ? ESCENARIOS_MAPA[mapaEscenarioKey] : null;
  const activeNodes = new Set(esc ? esc.nodes : [mapaActivoUnidad]);

  // Dibujar aristas causales
  MAPA_EDGES.forEach(ed => {
    const na = MAPA_UNIDADES[ed.a], nb = MAPA_UNIDADES[ed.b];
    let isHot = false;
    if (esc) {
      isHot = esc.edges.some(([x, y]) => (x === ed.a && y === ed.b) || (x === ed.b && y === ed.a));
    } else {
      isHot = (ed.a === mapaActivoUnidad || ed.b === mapaActivoUnidad);
    }
    const dx = nb.x - na.x, dy = nb.y - na.y, dist = Math.hypot(dx, dy) || 1;
    const x1 = na.x + (dx / dist) * 58, y1 = na.y + (dy / dist) * 32;
    const x2 = nb.x - (dx / dist) * 62, y2 = nb.y - (dy / dist) * 34;

    el("line", {
      x1, y1, x2, y2,
      stroke: isHot ? "#DC2626" : "#CBD5E1",
      "stroke-width": isHot ? "2.8" : "1.5",
      "stroke-dasharray": isHot ? "" : "4,3",
      "marker-end": isHot ? "url(#arr-red)" : ""
    }, svg);

    const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
    if (isHot) {
      const bw = Math.max(76, ed.lbl.length * 6.2 + 10);
      el("rect", { x: mx - bw / 2, y: my - 9, width: bw, height: 16, rx: 4, fill: "#FFFFFF", stroke: "#DC2626", "stroke-width": "1" }, svg);
      const tl = el("text", { x: mx, y: my + 3, fill: "#991B1B", "font-size": "9.8", "font-weight": "700", "text-anchor": "middle" }, svg);
      tl.textContent = ed.lbl;
    }
  });

  // Dibujar nodos interactivos clicables
  Object.values(MAPA_UNIDADES).forEach(nd => {
    const isSel = activeNodes.has(nd.id);
    const g = el("g", { style: "cursor:pointer;", onclick: `selectUnidadMapa('${nd.id}')` }, svg);
    el("rect", {
      x: nd.x - nd.w / 2, y: nd.y - nd.h / 2, width: nd.w, height: nd.h, rx: 9,
      fill: isSel ? nd.col : "#FFFFFF",
      stroke: isSel ? "#0F172A" : nd.col,
      "stroke-width": isSel ? "2.6" : "1.8",
      opacity: esc && !isSel ? "0.45" : "1"
    }, g);

    const t1 = el("text", { x: nd.x, y: nd.y - 12, fill: isSel ? "#FFFFFF" : nd.col, "font-size": "11.5", "font-weight": "800", "text-anchor": "middle" }, g);
    t1.textContent = nd.lbl;
    nd.sub.split("\n").forEach((ln, k) => {
      const ts = el("text", { x: nd.x, y: nd.y + 6 + k * 14, fill: isSel ? "#F1F5F9" : "#334155", "font-size": "10", "font-weight": "600", "text-anchor": "middle" }, g);
      ts.textContent = ln;
    });
  });

  // Render detalle inferior
  if (esc) {
    const btnsHtml = esc.jumps.map(([tb, lbl]) => `<button class="jump-btn" onclick="jumpToTab('${tb}')">${lbl} →</button>`).join(" ");
    box.innerHTML = `
      <div class="map-detail-head">
        <span class="map-detail-title">${esc.titulo}</span>
        <div class="btn-bar">${btnsHtml}</div>
      </div>
      <div>${esc.texto}</div>`;
  } else {
    const u = MAPA_UNIDADES[mapaActivoUnidad];
    const btnsHtml = u.jumps.map(([tb, lbl]) => `<button class="jump-btn" onclick="jumpToTab('${tb}')">${lbl} →</button>`).join(" ");
    box.innerHTML = `
      <div class="map-detail-head">
        <span class="map-detail-title">${u.lbl} (Haz clic en cualquier otra unidad del diagrama para cambiar el foco)</span>
        <div class="btn-bar">${btnsHtml}</div>
      </div>
      <div><b>Lógica central:</b> ${u.explica}</div>
      <div style="margin-top:5px;"><b>Interrelación con el resto del ramo:</b> ${u.puentes}</div>`;
  }
}

const FICHAS_LECTURA = [
  {
    unit: "U1", src: "La_teoria_de_la_localizacion.pdf (Duch Brown)",
    title: "1. Teoría Clásica y Nueva Economía Geográfica (Von Thünen, Weber, Christaller, Krugman)",
    core: "<b>Idea central:</b> La distancia cuesta dinero. Von Thünen ordena el uso del suelo rural en anillos según renta locacional LR(d); Weber minimiza el flete industrial con el Índice de Materiales (IM) y evalúa desvíos salariales con la Isodápana Crítica; Christaller define la jerarquía de ciudades por Umbral y Alcance; Krugman (1991) formaliza la competencia imperfecta y muestra que bajar τ bajo τ* dispara la aglomeración Centro-Periferia.",
    bridge: "<b>Puente inter-unidades:</b> Es la causa teórica de lo que luego mides empíricamente en U2 (especialización Q<sub>ij</sub>), U3 (concentración Gini/HHI) y U5 (macrocefalia IP<sub>4</sub> y centralidad de Rondinelli).",
    trap: "<b>Trampas de control:</b> (1) En Weber, si IM &gt; 1 (pierde peso al procesar, ej. madera/leche en polvo) se ubica cerca de insumos; si IM &lt; 1 (gana peso con insumos ubicuos, ej. bebidas) se ubica cerca del mercado. (2) Desviarse a un enclave laboral barato L solo conviene si L cae <i>dentro</i> de la isodápana crítica (ahorro salarial &gt; sobrecosto de flete)."
  },
  {
    unit: "U1", src: "Perroux (1955) · Myrdal (1957) · Hirschman (1958)",
    title: "2. Polos de Crecimiento, Causalidad Acumulativa y Encadenamientos",
    core: "<b>Idea central:</b> El crecimiento no surge parejo en todos lados sino en <i>polos motrices</i> (Perroux). Su impacto regional depende de los encadenamientos hacia atrás (proveedores b) y hacia adelante (procesamiento f) de Hirschman, y del balance neto entre difusión hacia comunas vecinas (<i>Spread</i>) versus absorción de talento y capital (<i>Backwash</i>) de Myrdal.",
    bridge: "<b>Puente inter-unidades:</b> Si un polo tiene bajo b + f opera como enclave y genera divergencia en U3; para volverlo polo integrador se requieren redes de proveedores y Upgrading de U4.",
    trap: "<b>Trampas de control:</b> No confundir un proyecto grande con un polo integrador: si la industria importa sus insumos y se lleva los excedentes (Backwash &gt; Spread), profundiza la desigualdad intercomunal en lugar de generar convergencia."
  },
  {
    unit: "U2", src: "Manual 59 ILPES (Lira & Quiroga) · Silva Lira (2005)",
    title: "3. Técnicas de Análisis Regional (Matrices SII, Qij, Base Exportadora y MADE)",
    core: "<b>Idea central:</b> A partir de matrices Sector × Comuna (t<sub>0</sub> y t<sub>f</sub>), Q<sub>ij</sub> &gt; 1 identifica vocación exportadora; Q<sub>r</sub> mide especialización y CR<sub>r</sub> reestructuración; Tiebout estima el excedente exportable X<sub>j</sub> y su multiplicador M<sub>j</sub> = V<sub>j</sub>/X<sub>j</sub>; Silva Lira clasifica territorios en 4 cuadrantes (Dinámica, Emergente, Estancada, En retroceso); y Shift &amp; Share separa Efecto Estructural (EE) de Efecto Diferencial (ED).",
    bridge: "<b>Puente inter-unidades:</b> Las comunas del Cuadrante II de Silva Lira (Emergentes: bajo nivel inicial y alto crecimiento) son el motor empírico de la Convergencia Beta (U3). El ED<sub>j</sub> &gt; 0 suele correlacionarse con clústeres activos (U4).",
    trap: "<b>Trampas de control:</b> (1) Q<sub>r</sub> y CR<sub>r</sub> siempre van entre 0 y 1 (multiplicando por 1/2 para no contar doble). (2) En MADE Clásico existen 6 tipologías de Boisier, mientras que en MADE Modificado (EM<sub>j</sub> = EI<sub>j</sub> − EE<sub>j</sub>; ERM<sub>j</sub> = ET<sub>j</sub> − EI<sub>j</sub>) existen 14 tipologías de Stilwell (1969)."
  },
  {
    unit: "U3", src: "Motor REAT · Figueroa & Herrero (2003) · CASEN",
    title: "4. Disparidades, Convergencia (σ y β), Desigualdad (Gini/Theil) y Markov",
    core: "<b>Idea central:</b> Convergencia Beta ocurre cuando territorios pobres crecen más rápido (β &lt; 0 en OLS); Convergencia Sigma cuando cae la dispersión transversal (σ<sub>t</sub> &lt; σ<sub>0</sub>). Gini mide desigualdad global desde la Curva de Lorenz; Theil mide entropía y se descompone aditivamente; HHI y Hannah-Kay (HK<sub>α</sub>) miden concentración; Markov proyecta la distribución ergódica de largo plazo.",
    bridge: "<b>Puente inter-unidades:</b> Responde si los polos (U1) y la reestructuración sectorial (U2) cerraron o abrieron las brechas territoriales, dando la línea base cuantitativa para justificar intervenciones OT (U5).",
    trap: "<b>Trampas de control:</b> (1) La Convergencia Beta es condición <i>necesaria pero NO suficiente</i> para que exista Convergencia Sigma (choques aleatorios pueden mantener alta la dispersión σ). (2) Para analizar desigualdad 'entre regiones' vs. 'dentro de regiones' se usa Theil, no Gini. (3) En Base1 (n=7), β es negativo pero con p=0,420 no es estadísticamente significativo al 5%."
  },
  {
    unit: "U4", src: "04 SPL.pdf (Dini 2010) · Granovetter · Padilla & Oddone · Boisier",
    title: "5. Redes Empresariales, Clúster, SPL, Cadenas de Valor y Sistema ELITE",
    core: "<b>Idea central:</b> Dini (2010) ordena la articulación en 3 círculos concéntricos: Red Empresarial (cooperación voluntaria entre pares) ⊂ Clúster (masa crítica sectorial localizada) ⊂ SPL (actores productivos + instituciones del territorio). Granovetter destaca los vínculos débiles para traer innovación; Padilla &amp; Oddone plantean Upgrading (proceso, producto, funcional); Boisier (ELITE) evalúa poder e interacción institucional.",
    bridge: "<b>Puente inter-unidades:</b> Es la dimensión institucional y microeconómica que transforma una aglomeración pasiva (U1) en competitividad genuina (ED<sub>j</sub> &gt; 0 en U2), como los casos PymeMad Biobío y Red Láctea Osorno.",
    trap: "<b>Trampas de control (Control 4):</b> (1) En matrices UCINET la diagonal principal es siempre 0 (A<sub>ii</sub> = 0); en red no dirigida D = 2L/[n(n−1)] y en dirigida D = L/[n(n−1)]. (2) Entrevista obligatoria a 3 personas de organizaciones distintas cubriendo mínimo 2 eslabones (1 gremio + 2 empresas). (3) Regla de oro del Prof. Mancilla: NO sugerir que debe existir un clúster ni usar la palabra 'debilidades' (preguntar por desafíos o aspectos por fortalecer)."
  },
  {
    unit: "U5", src: "06 OT 2024.pdf · Unidad 5 OT · PROT SUBDERE-CEPAL (2011)",
    title: "6. Ordenamiento Territorial: Primacía IP4, Guttman/Rondinelli, Aislamiento y PROT",
    core: "<b>Idea central:</b> El Ordenamiento Territorial diagnostica la red de asentamientos con Primacía Urbana (IP<sub>4</sub> = P<sub>1</sub>/[P<sub>2</sub>+P<sub>3</sub>+P<sub>4</sub>] en escala 0–3), jerarquía funcional con Escalograma de Guttman / Rondinelli (peso inverso W<sub>k</sub> = 100/f<sub>k</sub>) y conectividad vial con Matriz de Aislamiento (0 = asfalto directo, 1 = sin conexión directa). El PROT articula 4 sistemas: Costero, Urbano, Rural y Cuencas.",
    bridge: "<b>Puente inter-unidades:</b> Cierra el ciclo del ramo: conecta la densidad de servicios de Christaller (U1) y la concentración poblacional/económica (U3) con instrumentos públicos reales (PROT, PLADECO, LGUC, Ley 19.175 LOCGAR).",
    trap: "<b>Trampas de control (Control 5):</b> (1) En la Escala de Guttman (Top 10 comunas más pobladas y mínimo 7 variables), las variables DEBEN discriminar entre comunas: si todas tienen 1, debes reemplazar la variable. (2) En Rondinelli, mientras más escaso es un equipamiento (menor frecuencia f<sub>k</sub>), MAYOR peso de centralidad W<sub>k</sub> aporta. (3) En Matriz de Aislamiento, 0 es bueno (conectada directamente) y 1 indica aislamiento."
  }
];

let capaLecturaActiva = "core";
let filtroLecturaUnit = "all";

function setCapaLectura(capa) {
  capaLecturaActiva = capa;
  ["core", "bridge", "trap", "all"].forEach(k => {
    const b = document.getElementById("cap-btn-" + k);
    if (b) b.classList.toggle("primary", k === capa);
  });
  renderLecturaCards();
}
function filtrarLectura(unit, btn) {
  filtroLecturaUnit = unit;
  btn.parentElement.querySelectorAll(".flt-btn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");
  renderLecturaCards();
}
function renderLecturaCards() {
  const grid = document.getElementById("lec-cards-grid");
  if (!grid) return;
  grid.innerHTML = "";
  FICHAS_LECTURA.filter(f => filtroLecturaUnit === "all" || f.unit === filtroLecturaUnit).forEach(f => {
    const card = document.createElement("div");
    card.className = "lec-card";
    let layersHtml = "";
    if (capaLecturaActiva === "core" || capaLecturaActiva === "all") layersHtml += `<div class="lec-layer l-core">${f.core}</div>`;
    if (capaLecturaActiva === "bridge" || capaLecturaActiva === "all") layersHtml += `<div class="lec-layer l-bridge">${f.bridge}</div>`;
    if (capaLecturaActiva === "trap" || capaLecturaActiva === "all") layersHtml += `<div class="lec-layer l-trap">${f.trap}</div>`;
    card.innerHTML = `
      <div class="lec-meta"><span class="lec-unit">${f.unit}</span><span class="lec-src">${f.src}</span></div>
      <div class="lec-title">${f.title}</div>
      ${layersHtml}`;
    grid.appendChild(card);
  });
}

const QUIZ_LECTURA_DATA = [
  {
    tag: "U1 ↔ U5",
    q: "Si una mejora vial reduce el costo de transporte τ por debajo del umbral crítico τ* en el modelo de Krugman (1991), ¿qué tendencia cabría esperar en el Índice de Primacía (IP4) y en la Curva de Lorenz?",
    opts: ["Disminuyen IP4 y Gini (dispersión automática)", "Aumentan IP4 y Gini (mayor aglomeración en el centro)", "No cambia la distribución espacial"],
    ans: 1,
    why: "Al caer τ ≤ τ* predominan las fuerzas centrípetas (economías de escala + mercado local), concentrando producción y población en la capital regional, lo que eleva IP4 y aleja la Curva de Lorenz de la diagonal (Duch Brown / Krugman 1991)."
  },
  {
    tag: "U1 Weber",
    q: "Una planta procesadora de madera aserrada o leche en polvo tiene un Índice de Materiales IM = 1,85 y existe un enclave laboral barato L fuera de su Isodápana Crítica. ¿Dónde debe ubicarse?",
    opts: ["Cerca de las materias primas en P* (no salta a L)", "En el enclave laboral L para ahorrar salarios", "Pegada al mercado consumidor porque IM > 1"],
    ans: 0,
    why: "Como IM > 1 (pérdida de peso en el proceso), P* se orienta a los insumos. Como L queda FUERA de la Isodápana Crítica, el sobrecosto de transporte hacia L supera el ahorro salarial, por lo que permanece en P* (Duch Brown, Sec. 1.2)."
  },
  {
    tag: "U2 ↔ U3",
    q: "Una comuna ubicada en el Cuadrante II de Silva Lira (Emergente: bajo PIB per cápita inicial y tasa de crecimiento superior al promedio regional) aporta evidencia en favor de:",
    opts: ["Divergencia absoluta (β > 0)", "Macrocefalia urbana (IP4 ≥ 1,50)", "Convergencia Beta (β < 0)"],
    ans: 2,
    why: "La Convergencia Beta ocurre precisamente cuando las economías que parten rezagadas (bajo nivel inicial) crecen proporcionalmente más rápido que el promedio, cerrando la brecha (Silva Lira 2005 / Motor REAT)."
  },
  {
    tag: "U3 REAT",
    q: "Verdadero o Falso: Si en una regresión transversal regional encontramos Convergencia Beta estadísticamente significativa (β < 0), eso garantiza automáticamente que exista Convergencia Sigma (σ_t < σ_0).",
    opts: ["Verdadero", "Falso"],
    ans: 1,
    why: "Falso: En econometría regional (REAT / Barro y Sala-i-Martin), la Convergencia Beta es condición necesaria pero NO suficiente para Convergencia Sigma, ya que choques aleatorios pueden sostener o ampliar la dispersión transversal."
  },
  {
    tag: "U3 Desigualdad",
    q: "Si el GORE necesita descomponer exactamente cuánto de la desigualdad total de ingresos se explica 'entre provincias' y cuánto 'dentro de cada provincia', ¿qué indicador debe elegir?",
    opts: ["Índice de Gini estándar (G)", "Índice de Primacía IP2", "Índice de Entropía de Theil (T)"],
    ans: 2,
    why: "La principal ventaja analítica de la Entropía de Theil frente al Gini es su perfecta descomponibilidad aditiva en componente inter-grupal (entre territorios) e intra-grupal (dentro de cada territorio)."
  },
  {
    tag: "U4 Dini / Granovetter",
    q: "Un clúster local tiene 100% de vínculos fuertes internos entre sus 6 PyMEs, pero cero vínculos débiles con universidades, centros I+D o compradores externos. Según Granovetter (1973), ¿cuál es su principal riesgo?",
    opts: ["Exceso de competencia desleal por baja cohesión", "Bloqueo cognitivo (lock-in) por información redundante", "Pérdida inmediata de densidad D = 0%"],
    ans: 1,
    why: "Sin vínculos débiles externos que operen como puentes hacia nueva tecnología y mercados, las redes altamente endogámicas caen en bloqueo cognitivo (lock-in) y repiten información redundante."
  },
  {
    tag: "U4 Control 4",
    q: "En el protocolo de entrevistas del Taller de Redes y Cadenas de Valor (Control 4, Prof. Mancilla), ¿cuál de estas prácticas es INCORRECTA?",
    opts: ["Entrevistar a 3 actores de organizaciones distintas cubriendo mínimo 2 eslabones (1 gremio + 2 empresas)", "Preguntar por 'desafíos' o 'aspectos por fortalecer' y validar el esquema de la cadena", "Sugerir al entrevistado que debe existir un clúster y preguntarle por sus 'debilidades'"],
    ans: 2,
    why: "Regla explícita de cátedra ('Unidad 5. Redes y Cadena de Valor.dcx.pdf'): no se debe inducir la existencia de un clúster ni usar la palabra 'debilidades', sino consultar por desafíos o aspectos por fortalecer."
  },
  {
    tag: "U4 Dini 2010",
    q: "En una red no dirigida de n = 6 empresas con L = 5 vínculos todos conectados a una única empresa ancla (estrella), ¿qué valores toman la Densidad (D) y el Gradiente de Concentración (GC)?",
    opts: ["D = 33,3% y GC = 100% (Red con Liderazgo)", "D = 100% y GC = 0% (Red Simétrica)", "D = 50,0% y GC = 50% (Red Jerárquica)"],
    ans: 0,
    why: "D = 2L/[n(n−1)] = 10/30 = 33,3%. Como el líder tiene k_max = 5 y las otras 5 empresas tienen k_i = 1, ∑(5−k_i) = 20 y (n−1)(n−2) = 5×4 = 20 ⇒ GC = 20/20 = 100% (04 SPL.pdf, pág. 14)."
  },
  {
    tag: "U5 Guttman / Rondinelli",
    q: "Al construir tu Escala de Guttman / Matriz de Rondinelli para las 10 comunas más pobladas, notas que la variable 'Escuela Básica' tiene valor 1 en las 10 comunas. ¿Qué debes hacer según la pauta de cátedra?",
    opts: ["Mantenerla porque otorga el mayor peso Wk = 100/f_k", "Reemplazar esa variable por un equipamiento que sí discrimine entre comunas", "Asignarle peso 0 pero dejarla como indicador principal de jerarquía"],
    ans: 1,
    why: "En el Escalograma de Guttman ('06 OT 2024.pdf' / Control 5), las variables elegidas deben discriminar jerárquicamente entre comunas; si todas tienen valor 1 no aporta diferenciación y debe reemplazarse."
  },
  {
    tag: "U5 Aislamiento",
    q: "En la Matriz de Aislamiento Comunal del Control 5 (0 = conexión directa asfaltada; 1 = sin conexión directa), una comuna con Índice de Aislamiento = 22% frente a otra con 78% indica que:",
    opts: ["La primera está más aislada porque tiene menos unos", "Ambas tienen el mismo nivel de centralidad funcional", "La primera está mejor conectada (es un nodo más accesible en la red vial)"],
    ans: 2,
    why: "Como el valor 0 marca conexión directa y el 1 marca ausencia de conexión directa, un menor porcentaje de 1s refleja mayor accesibilidad y menor aislamiento territorial."
  }
];

let qzAnswers = {};
let qzSoloPend = false;

function toggleSoloErradasQz(btn) {
  qzSoloPend = !qzSoloPend;
  btn.classList.toggle("primary", qzSoloPend);
  renderQuizLectura();
}
function responderQuizLectura(idx, optIdx) {
  qzAnswers[idx] = optIdx;
  renderQuizLectura();
}
function resetQuizLectura() {
  qzAnswers = {};
  qzSoloPend = false;
  renderQuizLectura();
}
function renderQuizLectura() {
  const wrap = document.getElementById("qz-list");
  if (!wrap) return;
  wrap.innerHTML = "";
  let okCount = 0;
  QUIZ_LECTURA_DATA.forEach((item, idx) => {
    const uAns = qzAnswers[idx];
    const isAns = uAns !== undefined;
    const isOk = isAns && uAns === item.ans;
    if (isOk) okCount++;
    if (qzSoloPend && isOk) return;

    const card = document.createElement("div");
    card.className = "qz-card" + (isAns ? (" answered " + (isOk ? "ok" : "bad")) : "");
    const btns = item.opts.map((op, oi) =>
      `<button class="qz-btn ${uAns === oi ? "sel" : ""}" onclick="responderQuizLectura(${idx}, ${oi})">${op}</button>`
    ).join("");
    const badgeRes = isAns ? `<span style="font-size:11.5px;font-weight:800;color:${isOk ? "#15803D" : "#DC2626"};">${isOk ? "✓ Correcto" : "✗ Revisar"}</span>` : "";
    card.innerHTML = `
      <div><span class="qz-tag">${item.tag}</span> <span style="font-size:11px;color:#475569;font-weight:700;">Pregunta ${idx + 1}</span></div>
      <div class="qz-q">${item.q}</div>
      <div class="qz-opts">${btns}${badgeRes}</div>
      <div class="qz-fb"><b>Fundamento teórico de cátedra:</b> ${item.why}</div>`;
    wrap.appendChild(card);
  });
  document.getElementById("qz-score").textContent = `Aciertos: ${okCount} / ${QUIZ_LECTURA_DATA.length}`;
}

drawDini();
renderMecanica();
drawMapaTeoria();
renderLecturaCards();
renderQuizLectura();
</script>
</body>
</html>
"""


def renderizar_laboratorio_fluido_territorial():
    """Renderiza el Estudio Territorial Integral a 60 FPS (8 módulos) sin recarga de servidor."""
    components.html(HTML_TERRITORIAL_60FPS, height=1180, scrolling=True)
