import os

base_dir = '/home/leondon-pc/DatosComprimidos/Escritorio/Manual_Operativo_Supply_ArreglaTodo'
html_path = os.path.join(base_dir, 'index.html')

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Manual Operativo Integral - Supply & CRM ArreglaTodo</title>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <script>mermaid.initialize({startOnLoad:true, theme:'dark', securityLevel:'loose'});</script>
  <style>
    :root {
      --bg-base: #0a0d14;
      --bg-surface: #121722;
      --bg-card: #182030;
      --bg-card-hover: #1f2b42;
      --border-color: #243047;
      --border-light: #334466;
      --primary: #ff6b35;
      --primary-light: #ff8c5a;
      --primary-dark: #d94e18;
      --primary-glow: rgba(255, 107, 53, 0.15);
      --accent: #00b4d8;
      --accent-bg: rgba(0, 180, 216, 0.12);
      --success: #10b981;
      --success-bg: rgba(16, 185, 129, 0.12);
      --warning: #f59e0b;
      --warning-bg: rgba(245, 158, 11, 0.12);
      --danger: #ef4444;
      --danger-bg: rgba(239, 68, 68, 0.14);
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --sidebar-width: 320px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg-base);
      color: var(--text-main);
      line-height: 1.6;
      display: flex;
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* SIDEBAR */
    #sidebar {
      width: var(--sidebar-width);
      background-color: var(--bg-surface);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      z-index: 100;
      transition: transform 0.3s ease;
    }

    .sidebar-header {
      padding: 24px 20px 16px;
      border-bottom: 1px solid var(--border-color);
    }

    .brand-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--primary-glow);
      color: var(--primary-light);
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      border: 1px solid rgba(255, 107, 53, 0.3);
      margin-bottom: 8px;
    }

    .sidebar-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sidebar-subtitle {
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .search-box {
      padding: 12px 18px;
      border-bottom: 1px solid var(--border-color);
    }

    .search-input {
      width: 100%;
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px 12px;
      font-size: 0.85rem;
      color: var(--text-main);
      outline: none;
      transition: all 0.2s;
    }

    .search-input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 2px var(--primary-glow);
    }

    .nav-list {
      flex: 1;
      overflow-y: auto;
      padding: 16px 12px;
      list-style: none;
    }

    .nav-group-title {
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.75px;
      color: var(--text-dim);
      font-weight: 700;
      padding: 12px 10px 6px;
    }

    .nav-item a {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding: 8px 12px;
      border-radius: 6px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 500;
      transition: all 0.2s;
    }

    .nav-item a:hover, .nav-item a.active {
      color: var(--text-main);
      background-color: var(--bg-card);
      border-left: 3px solid var(--primary);
    }

    .nav-item .badge {
      font-size: 0.7rem;
      padding: 2px 6px;
      border-radius: 4px;
      background: var(--bg-base);
      color: var(--text-dim);
    }

    /* MAIN CONTENT */
    #main-wrapper {
      margin-left: var(--sidebar-width);
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
    }

    header.top-header {
      background: linear-gradient(180deg, #161e2e 0%, var(--bg-base) 100%);
      border-bottom: 1px solid var(--border-color);
      padding: 40px 48px 30px;
    }

    .header-badge {
      background: rgba(255, 107, 53, 0.15);
      color: var(--primary);
      padding: 5px 12px;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 700;
      display: inline-block;
      margin-bottom: 12px;
      border: 1px solid rgba(255, 107, 53, 0.3);
    }

    h1.hero-title {
      font-size: 2.2rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      color: #ffffff;
      margin-bottom: 10px;
      line-height: 1.25;
    }

    p.hero-desc {
      font-size: 1.05rem;
      color: var(--text-muted);
      max-width: 880px;
      line-height: 1.6;
    }

    /* KPI METRICS */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      margin-top: 28px;
    }

    .kpi-card {
      background-color: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
    }

    .kpi-label {
      font-size: 0.78rem;
      color: var(--text-dim);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .kpi-value {
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--text-main);
      margin: 4px 0 2px;
    }

    .kpi-desc {
      font-size: 0.78rem;
      color: var(--text-muted);
    }

    /* CONTENT SECTIONS */
    .content-container {
      padding: 40px 48px 80px;
      max-width: 1280px;
      width: 100%;
    }

    .module-section {
      margin-bottom: 64px;
      scroll-margin-top: 40px;
    }

    .module-header {
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 16px;
      margin-bottom: 28px;
    }

    .module-tag {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--primary);
    }

    .module-title {
      font-size: 1.7rem;
      font-weight: 700;
      color: var(--text-main);
      margin-top: 4px;
    }

    .module-summary {
      font-size: 0.95rem;
      color: var(--text-muted);
      margin-top: 6px;
    }

    /* CARDS */
    .step-card {
      background-color: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      margin-bottom: 28px;
      overflow: hidden;
      transition: border-color 0.2s, box-shadow 0.2s;
    }

    .step-card:hover {
      border-color: var(--border-light);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }

    .step-header {
      padding: 18px 24px;
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }

    .step-header-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .step-num {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: var(--primary-glow);
      color: var(--primary-light);
      border: 1px solid rgba(255, 107, 53, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.9rem;
    }

    .step-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .step-body {
      padding: 24px;
    }

    .step-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 28px;
      align-items: start;
    }

    @media (max-width: 1024px) {
      .step-grid {
        grid-template-columns: 1fr;
      }
    }

    .step-content {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .step-content p {
      color: var(--text-muted);
      font-size: 0.93rem;
      line-height: 1.65;
    }

    .step-content strong {
      color: var(--text-main);
    }

    .rules-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-top: 4px;
    }

    .rules-list li {
      position: relative;
      padding-left: 24px;
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    .rules-list li::before {
      content: "➔";
      position: absolute;
      left: 0;
      color: var(--primary);
      font-size: 0.8rem;
    }

    /* CALLOUTS */
    .callout {
      border-radius: 8px;
      padding: 14px 18px;
      font-size: 0.88rem;
      display: flex;
      gap: 12px;
      align-items: flex-start;
      margin: 8px 0;
    }

    .callout-icon {
      font-size: 1.1rem;
      line-height: 1.3;
      flex-shrink: 0;
    }

    .callout-danger {
      background-color: var(--danger-bg);
      border: 1px solid rgba(239, 68, 68, 0.35);
      color: #fca5a5;
    }
    .callout-danger strong { color: #ffffff; }

    .callout-warning {
      background-color: var(--warning-bg);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #fde68a;
    }
    .callout-warning strong { color: #ffffff; }

    .callout-tip {
      background-color: var(--accent-bg);
      border: 1px solid rgba(0, 180, 216, 0.35);
      color: #7dd3fc;
    }
    .callout-tip strong { color: #ffffff; }

    .callout-success {
      background-color: var(--success-bg);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: #86efac;
    }
    .callout-success strong { color: #ffffff; }

    /* SCREENSHOT VIEWER */
    .screenshot-box {
      background: #000000;
      border: 1px solid var(--border-color);
      border-radius: 10px;
      overflow: hidden;
      position: relative;
      cursor: zoom-in;
      transition: transform 0.2s, border-color 0.2s;
    }

    .screenshot-box:hover {
      border-color: var(--primary);
      transform: translateY(-2px);
    }

    .screenshot-box img {
      width: 100%;
      height: auto;
      display: block;
    }

    .screenshot-badge {
      position: absolute;
      bottom: 8px;
      right: 8px;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(4px);
      color: #fff;
      font-size: 0.75rem;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* BADGES */
    .pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .pill-primary { background: var(--primary-glow); color: var(--primary-light); border: 1px solid rgba(255, 107, 53, 0.4); }
    .pill-warning { background: var(--warning-bg); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }
    .pill-danger { background: var(--danger-bg); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }
    .pill-success { background: var(--success-bg); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
    .pill-accent { background: var(--accent-bg); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
    .pill-neutral { background: #1e293b; color: #94a3b8; border: 1px solid #334155; }

    /* MERMAID CONTAINER */
    .diagram-container {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 24px;
      margin: 24px 0;
      overflow-x: auto;
    }

    /* LIGHTBOX */
    #lightbox {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(8px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 30px;
    }

    #lightbox.active {
      display: flex;
    }

    #lightbox img {
      max-width: 95%;
      max-height: 92%;
      border-radius: 8px;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8);
      border: 1px solid var(--border-color);
    }

    .lightbox-close {
      position: absolute;
      top: 20px;
      right: 24px;
      color: #fff;
      font-size: 2rem;
      cursor: pointer;
      font-weight: 300;
      line-height: 1;
      padding: 8px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 50%;
      width: 44px;
      height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    /* SCRIPT CODE BLOCK */
    .script-box {
      background: #0d121c;
      border: 1px solid #1f2b42;
      border-radius: 8px;
      padding: 14px 18px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.85rem;
      color: #93c5fd;
      position: relative;
      margin: 8px 0;
    }

    .copy-btn {
      position: absolute;
      top: 10px;
      right: 12px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.72rem;
      cursor: pointer;
    }
    .copy-btn:hover { color: var(--text-main); border-color: var(--primary); }
  </style>
</head>
<body>

  <!-- SIDEBAR NAVIGATION -->
  <aside id="sidebar">
    <div class="sidebar-header">
      <div class="brand-badge">ArreglaTodo • Manual Oficial</div>
      <div class="sidebar-title">📦 Supply & CRM</div>
      <div class="sidebar-subtitle">Protocolo Unificado Paso a Paso</div>
    </div>
    
    <div class="search-box">
      <input type="text" id="filterInput" class="search-input" placeholder="🔍 Buscar paso, regla, Gmail, n8n..." onkeyup="filterManual()">
    </div>

    <ul class="nav-list">
      <li class="nav-group-title">Visión General</li>
      <li class="nav-item"><a href="#flujo-general">🗺️ Mapa del Proceso <span class="badge">Mermaid</span></a></li>
      
      <li class="nav-group-title">Módulo 1: Reglas Críticas</li>
      <li class="nav-item"><a href="#m1-ecosistema">1.1 Ecosistema de 3 Piezas <span class="badge">Arquitectura</span></a></li>
      <li class="nav-item"><a href="#m1-alerta-n8n">1.2 Alerta n8n vs CRM <span class="badge" style="color:#ef4444">Crítico</span></a></li>
      <li class="nav-item"><a href="#m1-meta-24h">1.3 Ventana 24h & Plantillas <span class="badge">WhatsApp</span></a></li>

      <li class="nav-group-title">Módulo 2: Curado del Pipeline</li>
      <li class="nav-item"><a href="#m2-orden-trabajo">2.1 El Orden Correcto <span class="badge">Prioridad</span></a></li>
      <li class="nav-item"><a href="#m2-sin-decidir">2.2 Triaje: Sin Decidir <span class="badge">Paso 1</span></a></li>
      <li class="nav-item"><a href="#m2-completando">2.3 Completando Registro <span class="badge">Paso 2</span></a></li>
      <li class="nav-item"><a href="#m2-sin-acceso">2.4 Carga de Gmail <span class="badge">Paso 3</span></a></li>
      <li class="nav-item"><a href="#m2-seguridad-gmail">2.5 Cambio de Correo <span class="badge" style="color:#f59e0b">Antifraude</span></a></li>
      <li class="nav-item"><a href="#m2-seguimiento">2.6 Recordatorios (Días 3, 7, 10) <span class="badge">Cadencia</span></a></li>

      <li class="nav-group-title">Módulo 3: Revisión de Perfiles</li>
      <li class="nav-item"><a href="#m3-filosofia">3.1 "Corregir es Revisar" <span class="badge">Criterio</span></a></li>
      <li class="nav-item"><a href="#m3-referencias">3.2 Llamada a Referencias <span class="badge">Script</span></a></li>
      <li class="nav-item"><a href="#m3-edicion-textos">3.3 Curaduría de Datos <span class="badge">Editorial</span></a></li>
      <li class="nav-item"><a href="#m3-fotos-videos">3.4 Fotos & Videos Prohibidos <span class="badge">Regla 2 fotos</span></a></li>
      <li class="nav-item"><a href="#m3-decision">3.5 Aprobación vs Corrección <span class="badge">SLA 48h</span></a></li>

      <li class="nav-group-title">Módulo 4: Operaciones & CRM</li>
      <li class="nav-item"><a href="#m4-en-vivo">4.1 Monitoreo "En Vivo" <span class="badge">Punto Verde</span></a></li>
      <li class="nav-item"><a href="#m4-inactivos">4.2 Gestión de Inactivos <span class="badge">Retención</span></a></li>
      <li class="nav-item"><a href="#m4-cortar">4.3 Cortar Oportunidades <span class="badge">Motivo Oblig.</span></a></li>
      <li class="nav-item"><a href="#m4-crm">4.4 Operación desde el CRM <span class="badge">Atención Cliente</span></a></li>
    </ul>
  </aside>

  <!-- MAIN WRAPPER -->
  <main id="main-wrapper">
    
    <!-- TOP HEADER -->
    <header class="top-header">
      <div class="header-badge">Manual Operativo Unificado • Versión 2.0</div>
      <h1 class="hero-title">Manual Operativo Paso a Paso: Supply y CRM</h1>
      <p class="hero-desc">
        Guía integral consolidada para el equipo de Supply y Atención al Cliente de <strong>ArreglaTodo</strong>. 
        Reorganiza los 9 módulos de capacitación en un ciclo de vida orgánico: desde la captación y validación de correo, 
        el curado estricto del pipeline por orden de prioridad, la auditoría editorial y telefónica de perfiles, 
        hasta el control de distribución de ofertas entre CRM y n8n.
      </p>

      <!-- KPI SUMMARY -->
      <div class="kpi-grid">
        <div class="kpi-card">
          <span class="kpi-label">Ecosistema</span>
          <span class="kpi-value" style="color: var(--primary);">4 Bloques</span>
          <span class="kpi-desc">0 redundancias, orden 100% orgánico</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">SLA Revisión</span>
          <span class="kpi-value" style="color: var(--accent);">48 Horas</span>
          <span class="kpi-desc">Máximo para auditar perfiles nuevos</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Ventana Meta</span>
          <span class="kpi-value" style="color: var(--warning);">24 Horas</span>
          <span class="kpi-desc">Plantillas obligatorias de Utilidad</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Punto Ciego</span>
          <span class="kpi-value" style="color: var(--danger);">n8n vs CRM</span>
          <span class="kpi-desc">Exclusión automática solo a Suspendidos</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Material Visual</span>
          <span class="kpi-value" style="color: var(--success);">33 Capturas</span>
          <span class="kpi-desc">Detalle interactivo con zoom paso a paso</span>
        </div>
      </div>
    </header>

    <!-- CONTENT -->
    <div class="content-container">

      <!-- DIAGRAMA MERMAID -->
      <section id="flujo-general" class="module-section">
        <div class="module-header">
          <span class="module-tag">Mapa del Proceso</span>
          <h2 class="module-title">El Ciclo de Vida Orgánico del Prestador</h2>
          <p class="module-summary">Visión secuencial de cómo avanza un prestador desde que se registra hasta que recibe trabajos.</p>
        </div>

        <div class="diagram-container">
          <pre class="mermaid">
flowchart TD
    subgraph ONBOARDING["1. Onboarding y Acceso"]
        A["Prospecto (Tablero de Alta)"] -->|Sin correo| B["Sin Acceso"]
        B -->|Pedir Gmail por Chat / Cargar| C["Completando Registro"]
        C -->|Faltan datos| C1["Recordatorios Día 3, 7 y 10"]
        C -->|Completa los 11 pasos| D["Para Revisar (SLA 48h)"]
    end

    subgraph REVISION["2. Auditoría y Curaduría (Pestaña Revisión)"]
        D --> E["Llamada a las 2 Referencias"]
        E --> F["Curaduría Editorial (Sobre mí / Zonas)"]
        F --> G["Filtro de Fotos y Videos (Regla 2 fotos)"]
        G -->|Con observaciones| H["Con Correcciones"]
        H -->|Subsanado| D
        G -->|Aprobado| I["Falta Activar / A Prueba"]
    end

    subgraph PRODUCCION["3. Producción y Reparto"]
        I --> J["Verificado y Activo"]
        J -->|Reparto de Trabajos| K["CRM & Bot n8n"]
    end

    subgraph EXCEPCIONES["4. Gestión de Fugas y Mantenimiento"]
        J -->|Deja de trabajar| L["Inactivo (Anotar Motivo en Bot)"]
        L -->|Quiere volver| I
        L -->|Recibe ofertas indebidas| M["Cortar Oportunidades (Motivo Oblig.)"]
        J -->|Incumplimiento grave| N["Suspendido / De Baja (Bloqueo Total)"]
    end

    classDef stage fill:#182030,stroke:#243047,stroke-width:1px,color:#f1f5f9;
    classDef highlight fill:#ff6b35,stroke:#ff8c5a,stroke-width:2px,color:#fff;
    classDef alert fill:#ef4444,stroke:#f87171,stroke-width:1px,color:#fff;
    class A,B,C,C1,D,E,F,G,H,I,J,L stage;
    class M,N alert;
          </pre>
        </div>
      </section>

      <!-- ========================================================================= -->
      <!-- MODULO 1: ARQUITECTURA Y REGLAS CRÍTICAS -->
      <!-- ========================================================================= -->
      <section id="m1-ecosistema" class="module-section">
        <div class="module-header">
          <span class="module-tag">Módulo 1</span>
          <h2 class="module-title">Arquitectura del Ecosistema y Reglas Críticas</h2>
          <p class="module-summary">Comprender las piezas del sistema evita errores operativos graves que impactan en clientes y trabajadores.</p>
        </div>

        <!-- 1.1 Ecosistema -->
        <div class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">01</span>
              <h3 class="step-title">Las 3 Piezas del Sistema: CRM, Supply y el Bot n8n</h3>
            </div>
            <span class="pill pill-primary">Fundamento</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  El funcionamiento de ArreglaTodo se sostiene sobre tres componentes interconectados que deben operar en sincronía:
                </p>
                <ul class="rules-list">
                  <li><strong>supply.arreglatodo.uy (Panel de Supply):</strong> Gestión integral de prestadores, onboarding, verificación de identidad, revisión de carpetas y seguimiento directo de actividad.</li>
                  <li><strong>crm.arreglatodo.uy (CRM Comercial):</strong> Utilizado por Atención al Cliente para gestionar pedidos de presupuestos, coordinar con usuarios y despachar solicitudes a los trabajadores del rubro.</li>
                  <li><strong>Bot de Reparto Automático (n8n):</strong> Automatización en segundo plano que envía avisos de trabajos disponibles por WhatsApp a los prestadores de cada categoría según su ubicación.</li>
                </ul>
                <div class="callout callout-tip">
                  <span class="callout-icon">💡</span>
                  <div>
                    <strong>Regla de Oro Operativa:</strong> Toda la comunicación con el prestador se gestiona <strong>únicamente desde el panel de Supply</strong>. Nunca se debe escribir desde celulares personales ni WhatsApp Web, para que todo el equipo mantenga visibilidad en tiempo real del historial.
                  </div>
                </div>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/01_crm_enviar_trabajadores.jpg')">
                <img src="assets/01_crm_enviar_trabajadores.jpg" alt="CRM Enviar a Trabajadores">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 1.2 Alerta n8n -->
        <div id="m1-alerta-n8n" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">02</span>
              <h3 class="step-title">Punto Ciego Crítico: El Desfasaje entre CRM y n8n</h3>
            </div>
            <span class="pill pill-danger">Alerta de Seguridad</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Existe un desfasaje técnico vital que todo operador de Supply y Atención al Cliente debe conocer de memoria:
                </p>
                <div class="callout callout-danger">
                  <span class="callout-icon">🚨</span>
                  <div>
                    <strong>Comportamiento del Bot n8n:</strong> Hoy en día, el reparto automático de <code>n8n</code> <strong>SOLO excluye a los prestadores en estado "Suspendido"</strong>. A los prestadores <strong>"De baja"</strong>, <strong>"Inactivos"</strong> o con <strong>"Oportunidades cortadas"</strong> les pueden llegar ofertas automáticas de todas formas.
                  </div>
                </div>
                <ul class="rules-list">
                  <li><strong>Desde el CRM:</strong> El botón <em>"Seleccionar visibles"</em> es inteligente y saltea automáticamente a los suspendidos, de baja y cortados.</li>
                  <li><strong>Desde el Bot n8n:</strong> No distingue cortes manuales. Por eso, en las tarjetas de Supply verás el aviso en rojo: <code>Recibe ofertas igual (X)</code>.</li>
                  <li><strong>Procedimiento de Mitigación:</strong> Si detectás que un prestador lleva días cortado o de baja y sigue recibiendo ofertas automáticas, <strong>se debe avisar de inmediato a Máximo</strong> con el nombre del prestador.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/04_crm_alerta_n8n.jpg')">
                <img src="assets/04_crm_alerta_n8n.jpg" alt="Alerta n8n en CRM">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 1.3 Meta 24h -->
        <div id="m1-meta-24h" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">03</span>
              <h3 class="step-title">Protocolo de Mensajería: Ventana de 24 Horas y Plantillas Meta</h3>
            </div>
            <span class="pill pill-warning">Regla WhatsApp API</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Por políticas oficiales de Meta (WhatsApp Cloud API), si transcurrieron <strong>más de 24 horas</strong> desde el último mensaje recibido del prestador, la ventana de conversación queda <strong>cerrada</strong>.
                </p>
                <ul class="rules-list">
                  <li><strong>Bloqueo de texto libre:</strong> No se pueden mandar mensajes comunes ni redactados a mano. WhatsApp los rebotará.</li>
                  <li><strong>Uso obligatorio de Plantillas:</strong> Se deben utilizar exclusivamente las <strong>8 plantillas oficiales de Supply</strong> aprobadas por Meta (categoría Utilidad).</li>
                  <li><strong>Previsualización ("Ver cómo le llega"):</strong> Permite comprobar las variables (nombre, link de acceso a <code>app.arreglatodo.uy/prestador</code> y campos faltantes).</li>
                  <li><strong>Reapertura de la ventana:</strong> En cuanto el prestador responde la plantilla (aunque sea un "Ok"), la ventana de 24 horas se reabre y ya se puede volver a usar texto libre y el botón <em>"Poner en el chat"</em>.</li>
                  <li><strong>Firma institucional:</strong> Todas las plantillas salen firmadas por <strong>Máximo</strong> y salen desde la línea de trabajadores, nunca de clientes.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/05_meta_plantillas_menu.jpg')">
                <img src="assets/05_meta_plantillas_menu.jpg" alt="Menú de Plantillas Meta">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

      </section>

      <!-- ========================================================================= -->
      <!-- MODULO 2: CURADO DIARIO DEL PIPELINE -->
      <!-- ========================================================================= -->
      <section id="m2-orden-trabajo" class="module-section">
        <div class="module-header">
          <span class="module-tag">Módulo 2</span>
          <h2 class="module-title">El Curado Diario del Pipeline de Supply</h2>
          <p class="module-summary">Secuencia estricta de trabajo diario: "Se atiende primero lo que destraba a los demás".</p>
        </div>

        <div class="callout callout-tip" style="margin-bottom: 24px;">
          <span class="callout-icon">🎯</span>
          <div>
            <strong>Jerarquía de Curado Diario:</strong> El orden visual del Kanban NO es el orden cronológico de trabajo. Cada mañana se curan las columnas en el siguiente orden de impacto:
            <strong>1° Sin decidir</strong> ➔ <strong>2° Completando registro</strong> ➔ <strong>3° Sin acceso (Gmail)</strong> ➔ <strong>4° Para revisar (48h)</strong> ➔ <strong>5° Inactivos</strong>.
          </div>
        </div>

        <!-- 2.1 Sin Decidir -->
        <div id="m2-sin-decidir" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">04</span>
              <h3 class="step-title">Prioridad 1: "Sin Decidir" (El Filtro Inicial de Entrada)</h3>
            </div>
            <span class="pill pill-primary">Paso 1 del Día</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Son contactos que llegaron al sistema pero nadie resolvió si trabajarán con nosotros o no. 
                </p>
                <div class="callout callout-danger">
                  <span class="callout-icon">⛔</span>
                  <div><strong>Regla inquebrantable:</strong> <em>Hasta que no se decida, NUNCA se le escribe al prestador.</em></div>
                </div>
                <ul class="rules-list">
                  <li><strong>Opción A (Avanza):</strong> Si el perfil aplica, se arrastra la tarjeta a <strong>"A prueba"</strong> para iniciar su camino.</li>
                  <li><strong>Opción B (No aplica / Descartado):</strong> Si no encaja, se arrastra a <strong>"Inactivo"</strong> registrando obligatoriamente el motivo del descarte en el bot.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/10_pipeline_sin_decidir.jpg')">
                <img src="assets/10_pipeline_sin_decidir.jpg" alt="Columna Sin Decidir">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 2.2 Completando Registro -->
        <div id="m2-completando" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">05</span>
              <h3 class="step-title">Prioridad 2: "Completando Registro" (Máxima Velocidad de Conversión)</h3>
            </div>
            <span class="pill pill-success">Paso 2 del Día</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  ¿Por qué se trabajan segundos? <strong>Porque ya tienen Gmail y ya ingresaron: son los que más rápido terminan su ficha y quedan listos para trabajar.</strong>
                </p>
                <ul class="rules-list">
                  <li><strong>Diagnóstico de la tarjeta:</strong> Cada tarjeta dice exactamente qué datos le faltan con las palabras exactas que se le deben enviar (ej: <em>"tu cédula, zonas, fotos de trabajos, el RUT, dónde te pagamos"</em>).</li>
                  <li><strong>Si nunca entró:</strong> Se le manda el link directo de acceso a su espacio.</li>
                  <li><strong>Si ya entró:</strong> Se le recuerda puntualmente los ítems pendientes.</li>
                  <li><strong>Botón "Escribirle":</strong> Abre el chat lateral con el mensaje pre-redactado a medida. Solo se revisa y se envía.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/16_pipeline_completando_registro.jpg')">
                <img src="assets/16_pipeline_completando_registro.jpg" alt="Completando Registro">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 2.3 Sin Acceso -->
        <div id="m2-sin-acceso" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">06</span>
              <h3 class="step-title">Prioridad 3: "Sin Acceso" (Cargar el Gmail desde el Chat)</h3>
            </div>
            <span class="pill pill-accent">Paso 3 del Día</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  <strong>Sin Gmail no hay espacio de prestador.</strong> El prestador no puede ver sus trabajos, ni cargar fotos, ni ver lo que cobró si no tiene un correo vinculado.
                </p>
                <ul class="rules-list">
                  <li><strong>Volumen de trabajo:</strong> Se procesa en <strong>tandas de 15 prestadores por día</strong> para no saturar el canal.</li>
                  <li><strong>Paso 1:</strong> Solicitarle el correo electrónico por chat con el mensaje predeterminado.</li>
                  <li><strong>Paso 2:</strong> En cuanto el prestador responde su Gmail por el chat, copiarlo y pegarlo en el campo <code>Cargar su Gmail</code> de la barra lateral derecha.</li>
                  <li><strong>Paso 3:</strong> Verificar meticulosamente que no tenga errores tipográficos (una sola letra mal y no podrá entrar).</li>
                  <li><strong>Paso 4:</strong> Click en <em>"Guardar en su ficha"</em>. <strong>La tarjeta se mueve SOLA</strong> de "Sin acceso" a "Completando registro".</li>
                  <li><strong>Paso 5:</strong> Enviar el mensaje que se habilita con el link de bienvenida y sus credenciales.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/12_pipeline_cargar_gmail.jpg')">
                <img src="assets/12_pipeline_cargar_gmail.jpg" alt="Cargar Gmail desde el Chat">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 2.4 Seguridad Gmail -->
        <div id="m2-seguridad-gmail" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">07</span>
              <h3 class="step-title">Protocolo de Seguridad Antifraude: "Piden Entrar con Otro Gmail"</h3>
            </div>
            <span class="pill pill-danger">Seguridad Estricta</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Ocurre con frecuencia cuando un trabajador cambia de teléfono o cuenta de Google. 
                  <strong>Nadie entra a la ficha de otro sin validación de identidad previa.</strong>
                </p>
                <div class="callout callout-warning">
                  <span class="callout-icon">⚠️</span>
                  <div>
                    <strong>Alerta en Pestaña Revisión:</strong> Aparecerá un cartel en rojo: <code>Piden entrar a su perfil</code>. Al cambiar el correo, el anterior queda automáticamente inhabilitado.
                  </div>
                </div>
                <ul class="rules-list">
                  <li><strong>Paso 1:</strong> Escribirle SIEMPRE al WhatsApp oficial que ya figura en su ficha (nunca por WhatsApp Web ni a números nuevos no verificados).</li>
                  <li><strong>Paso 2:</strong> Preguntarle mencionando <strong>ambos correos explícitamente</strong> para confirmar cuál deja de funcionar.</li>
                  <li><strong>Paso 3:</strong> Solo cuando el prestador confirma expresamente por el canal oficial que fue él quien pidió el cambio, se ingresa a Revisión y se presiona <em>"Es quien dice ser"</em>.</li>
                  <li><strong>Si no reconoce el pedido o no contesta:</strong> NO aprobar bajo ninguna circunstancia; puede tratarse de una suplantación de identidad.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/14_pipeline_cambio_gmail_seguridad.jpg')">
                <img src="assets/14_pipeline_cambio_gmail_seguridad.jpg" alt="Validación Seguridad Cambio Gmail">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 2.5 Seguimiento -->
        <div id="m2-seguimiento" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">08</span>
              <h3 class="step-title">Cadencia de Seguimiento: Recordatorios Días 3, 7 y 10</h3>
            </div>
            <span class="pill pill-neutral">Automatización</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Si un prestador se estanca en "Completando registro" y no avanza con sus datos, el panel de chat ya tiene redactados los mensajes de seguimiento correspondientes a cada hito temporal:
                </p>
                <ul class="rules-list">
                  <li><strong>Día 3 (Recordatorio Amigable):</strong> Mensaje recordándole que su perfil está a medio completar y que sin eso no puede recibir ofertas de trabajo.</li>
                  <li><strong>Día 7 (Segundo Aviso):</strong> Notificación con llamada a la acción para destrabar el registro o consultar si tuvo alguna dificultad con las fotos/RUT.</li>
                  <li><strong>Día 10 (Ofrecer Ayuda Telefónica):</strong> <em>"Ofrecer ayuda por teléfono (día 10)"</em>. Un agente se ofrece a llamarlo para completar los datos faltantes de manera guiada en 5 minutos.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/18_pipeline_recordatorios_3_7_10.jpg')">
                <img src="assets/18_pipeline_recordatorios_3_7_10.jpg" alt="Recordatorios Días 3 7 10">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

      </section>

      <!-- ========================================================================= -->
      <!-- MODULO 3: AUDITORIA Y REVISION DE PERFILES -->
      <!-- ========================================================================= -->
      <section id="m3-filosofia" class="module-section">
        <div class="module-header">
          <span class="module-tag">Módulo 3</span>
          <h2 class="module-title">Protocolo de Auditoría y Revisión de Perfiles</h2>
          <p class="module-summary">Criterio editorial y control de calidad en la pestaña "Revisión". SLA máximo: 48 horas.</p>
        </div>

        <div class="callout callout-tip" style="margin-bottom: 24px;">
          <span class="callout-icon">💡</span>
          <div>
            <strong>Mantra de Revisión:</strong> <em>"Corregir es parte de revisar"</em>. Lo que el operador puede arreglar en 10 segundos en la pantalla (tildes, mayúsculas, zonas), <strong>se arregla ahí mismo</strong>. No se le devuelve el perfil al prestador ni se le hace perder días por detalles menores.
          </div>
        </div>

        <!-- 3.1 Referencias -->
        <div id="m3-referencias" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">09</span>
              <h3 class="step-title">Validación de Rubros: Llamada a las 2 Referencias</h3>
            </div>
            <span class="pill pill-primary">Auditoría Telefónica</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Para aprobar cualquier rubro solicitado (ej: Herrería, Pintura, Sanitaria), <strong>es obligatorio llamar por teléfono a las 2 referencias</strong> que cargó el prestador.
                </p>
                <div class="script-box">
                  <button class="copy-btn" onclick="navigator.clipboard.writeText('Hola, te llamo de ArreglaTodo. ¿Cómo fue el trabajo de [Rubro]? Del 1 al 10, ¿cómo lo calificarías? ¿Qué aspectos mejoraría? ¿Lo volverías a contratar?')">Copiar Guion</button>
                  "Hola, te llamo de ArreglaTodo. ¿Cómo fue el trabajo realizado por el prestador?<br>
                  1. Del 1 al 10, ¿cómo calificarías la calidad y puntualidad?<br>
                  2. ¿Hubo algún detalle que mejoraría?<br>
                  3. ¿Lo volverías a contratar?"
                </div>
                <ul class="rules-list">
                  <li><strong>Anotación confidencial:</strong> Anotar textualmente lo que dice cada persona en los cuadros de texto. <strong>El prestador NUNCA ve estas notas.</strong></li>
                  <li><strong>Calificación:</strong> Marcar una opción: <code>Lo recomienda</code>, <code>No lo recomienda</code> o <code>No respondió</code>.</li>
                  <li><strong>Efecto de Aprobar:</strong> Al hacer click en <em>"Aprobar Rubro"</em>, el oficio se publica en su perfil web y el bot de n8n empieza a mandarle trabajos de ese rubro.</li>
                  <li><strong>Rechazo:</strong> Si no se aprueba, se redacta el motivo (este texto <strong>SÍ</strong> lo lee el prestador).</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/20_revision_llamar_referencias.jpg')">
                <img src="assets/20_revision_llamar_referencias.jpg" alt="Llamar a Referencias">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 3.2 Curaduria Editorial -->
        <div id="m3-edicion-textos" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">10</span>
              <h3 class="step-title">Curaduría Editorial Directa (Nombre, Sobre mí y Zonas)</h3>
            </div>
            <span class="pill pill-success">Acción Inmediata</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  El formulario de revisión permite editar en vivo la información pública del profesional antes de publicarlo:
                </p>
                <ul class="rules-list">
                  <li><strong>Corrección ortográfica y de estilo:</strong> Corregir nombres en minúsculas, falta de tildes o errores gramaticales groseros.</li>
                  <li><strong>Sección "Sobre mí":</strong> Si el texto es excesivamente corto o confuso, embellecerlo manteniendo la esencia de su experiencia.</li>
                  <li><strong>Zonas de Cobertura:</strong> Verificar que las localidades y barrios seleccionados sean coherentes con su lugar de residencia.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/22_revision_editar_textos.jpg')">
                <img src="assets/22_revision_editar_textos.jpg" alt="Editar Textos del Perfil">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 3.3 Fotos y Videos -->
        <div id="m3-fotos-videos" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">11</span>
              <h3 class="step-title">Control de Fotos y Videos: La "Regla de las 2 Fotos"</h3>
            </div>
            <span class="pill pill-danger">Filtro de Contenido</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Todas las fotos y videos deben inspeccionarse en tamaño ampliado antes de dar el visto bueno:
                </p>
                <div class="callout callout-danger">
                  <span class="callout-icon">🚫</span>
                  <div>
                    <strong>Motivos de Eliminación Inmediata de Fotos:</strong>
                    Imágenes con números de teléfono, enlaces web, logotipos de otras empresas competidoras, marcas de agua o fotos bajadas de internet/stock.
                  </div>
                </div>
                <ul class="rules-list">
                  <li><strong>Borrar con motivo:</strong> Al eliminar una foto, se ingresa el motivo (ej: <em>"Tenía teléfono visible"</em>). La foto se borra del perfil público al instante y el prestador ve el motivo en su espacio.</li>
                  <li><strong>La Regla de Oro de las 2 Fotos:</strong> Si al descartar fotos prohibidas <strong>todavía le quedan al menos 2 fotos válidas</strong>, <strong>NO hace falta devolverle el perfil</strong>: se eliminan las fotos incorrectas y se continúa con la aprobación.</li>
                  <li><strong>Videos:</strong> Es obligatorio mirarlos completos hasta el final. Muchos prestadores dicen o muestran números de celular en los últimos segundos.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/23_revision_curar_fotos.jpg')">
                <img src="assets/23_revision_curar_fotos.jpg" alt="Curación de Fotos de Trabajos">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 3.4 Decision Final -->
        <div id="m3-decision" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">12</span>
              <h3 class="step-title">Decisión Final: "Aprobar y Verificar" vs. "Pedir Correcciones"</h3>
            </div>
            <span class="pill pill-primary">Cierre de Revisión</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Una vez auditados los rubros, referencias y multimedia, se toma la determinación final:
                </p>
                <ul class="rules-list">
                  <li><strong>Aprobar y Verificar:</strong>
                    Si todo cumple los estándares, se presiona el botón verde. Sale de la lista de Revisión. En el Pipeline pasa a <em>"Verificado y activo"</em> si ya está a prueba en el bot y tiene los 11 pasos; o a <em>"Completando registro"</em> si aún le resta algún dato administrativo secundario.
                    <br><small style="color:var(--text-dim);">*Nota: Aprobar NO le avisa solo al prestador; se le debe notificar por chat.</small>
                  </li>
                  <li><strong>Pedir Correcciones (Devolución):</strong>
                    Si le faltan requisitos indispensables (sin rubros aprobados no le llega nada), se redacta claramente en el recuadro <code>Pedirle correcciones</code> qué debe corregir para que lo vea en su espacio.
                  </li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/25_revision_aprobar_o_devolver.jpg')">
                <img src="assets/25_revision_aprobar_o_devolver.jpg" alt="Aprobar y Verificar o Devolver">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

      </section>

      <!-- ========================================================================= -->
      <!-- MODULO 4: OPERACIONES AVANZADAS, INACTIVOS Y CRM -->
      <!-- ========================================================================= -->
      <section id="m4-en-vivo" class="module-section">
        <div class="module-header">
          <span class="module-tag">Módulo 4</span>
          <h2 class="module-title">Operaciones Avanzadas, Retención y Control Comercial</h2>
          <p class="module-summary">Monitoreo reactivo en vivo, gestión de inactivos, corte de oportunidades y despacho en CRM.</p>
        </div>

        <!-- 4.1 En Vivo -->
        <div class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">13</span>
              <h3 class="step-title">Monitoreo en Tiempo Real: "En Vivo" y el Pulso Verde</h3>
            </div>
            <span class="pill pill-success">Conversión en Caliente</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  El sistema cuenta con un motor de eventos en tiempo real (polling silencioso cada 15 segundos sin necesidad de recargar la pantalla).
                </p>
                <div class="callout callout-tip">
                  <span class="callout-icon">🟢</span>
                  <div>
                    <strong>La Regla de Oro: "Escribile cuando está en su espacio":</strong>
                    Arriba a la derecha, el punto verde late cuando alguien estuvo en su espacio en los últimos 10 minutos. Es el momento con mayor tasa de respuesta porque tiene el celular en la mano.
                  </div>
                </div>
                <ul class="rules-list">
                  <li><strong>Avisos fijos que no se van solos:</strong> Si un prestador completó todo el registro, mandó a revisión o pidió entrar con otro correo, la tarjeta queda fija en pantalla hasta que un operador la atienda explícitamente.</li>
                  <li><strong>Campana de los últimos 50 avances:</strong> Muestra cronológicamente cada paso completado con acceso directo a <em>"Chat"</em> o <em>"Pipeline"</em> con su tarjeta resaltada.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/31_en_vivo_punto_verde.jpg')">
                <img src="assets/31_en_vivo_punto_verde.jpg" alt="Monitoreo En Vivo">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 4.2 Inactivos -->
        <div id="m4-inactivos" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">14</span>
              <h3 class="step-title">Gestión de Inactivos: Registro de Motivo y Reactivación</h3>
            </div>
            <span class="pill pill-warning">Retención</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Son prestadores que dejaron de cotizar o informaron que no pueden tomar changas por un tiempo (ej: consiguieron trabajo fijo).
                </p>
                <ul class="rules-list">
                  <li><strong>Consultar motivo:</strong> Usar el mensaje tipo <em>"Preguntarle por qué no está trabajando"</em> (o plantilla si pasaron >24h).</li>
                  <li><strong>Registro obligatorio en el Bot:</strong> En cuanto responda, escribir el motivo en el recuadro <code>Qué respondió</code> y guardar. Queda asentado con tu nombre y fecha para que ningún otro compañero vuelva a molestarlo con la misma pregunta.</li>
                  <li><strong>Proceso de Reactivación:</strong> Si el prestador escribe diciendo que quiere volver, presionar el botón verde <strong>"Quiere volver: pasar a prueba"</strong>. Vuelve a recibir oportunidades de inmediato. Si le falta el correo, se le solicita el Gmail para habilitar su acceso.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/26_inactivos_motivo_bot.jpg')">
                <img src="assets/26_inactivos_motivo_bot.jpg" alt="Gestión de Inactivos y Motivo">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 4.3 Cortar Oportunidades -->
        <div id="m4-cortar" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">15</span>
              <h3 class="step-title">Cortar Oportunidades ("Sin Oportunidades"): Cuándo y Cómo Usarlo</h3>
            </div>
            <span class="pill pill-danger">Control de Reparto</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Se utiliza cuando se necesita pausar el envío de trabajos a un prestador <strong>sin modificar su estado general ni suspenderlo</strong> (ej: tiene quejas reiteradas en análisis, sobrecarga de pedidos o vacaciones transitorias).
                </p>
                <ul class="rules-list">
                  <li><strong>Acción:</strong> Presionar el botón <code>Sin oportunidades</code> en su tarjeta del pipeline.</li>
                  <li><strong>Motivo Obligatorio:</strong> Es mandatorio ingresar la justificación en el pop-up modal. Queda registrado en el historial del bot con operador y fecha.</li>
                  <li><strong>Identificación Visual:</strong> La tarjeta queda destacada con una etiqueta negra distintiva y el botón cambia a <em>"Volver a mandarle"</em>.</li>
                  <li><strong>Filtro "Solo los que reciben ofertas":</strong> Herramienta esencial para auditar rápidamente si hay prestadores cortados que siguen filtrándose en el bot.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/28_cortar_modal_motivo.jpg')">
                <img src="assets/28_cortar_modal_motivo.jpg" alt="Modal Cortar Oportunidades">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 4.4 Operacion CRM -->
        <div id="m4-crm" class="step-card">
          <div class="step-header">
            <div class="step-header-left">
              <span class="step-num">16</span>
              <h3 class="step-title">Despacho desde el CRM (Atención al Cliente): Estados y Solicitudes</h3>
            </div>
            <span class="pill pill-primary">CRM Comercial</span>
          </div>
          <div class="step-body">
            <div class="step-grid">
              <div class="step-content">
                <p>
                  Cuando un agente de Atención al Cliente abre una solicitud de presupuesto (ej: <em>#20460 - Pintura</em>) y despliega el panel <strong>"Enviar a trabajadores"</strong>:
                </p>
                <ul class="rules-list">
                  <li><strong>Sin marca (Activo):</strong> Prestador habilitado y verificado. Se puede tildar libremente.</li>
                  <li><strong>Inactivo:</strong> Muestra la etiqueta, pero <strong>se puede tildar y le llega igual</strong> (decisión operativa: en rubros con baja oferta, los inactivos salvan pedidos).</li>
                  <li><strong>Suspendido (Grisáceo):</strong> Bloqueado totalmente. No se puede elegir. Decisión privativa de Supply.</li>
                  <li><strong>De baja (Grisáceo):</strong> Se desvinculó de la plataforma. Bloqueado.</li>
                  <li><strong>Sin oportunidades (Grisáceo):</strong> Supply le cortó los envíos con motivo explícito. Bloqueado.</li>
                  <li><strong>El botón "Seleccionar visibles":</strong> Al presionar este botón, el CRM selecciona automáticamente a los prestadores hábiles y <strong>saltea sin excepción a los suspendidos, de baja y cortados</strong>.</li>
                  <li><strong>Protocolo ante reclamo ("No me llegan trabajos"):</strong> El agente de CRM revisa la marca en esta lista. Si está bloqueado, se deriva inmediatamente a Supply indicando el nombre.</li>
                </ul>
              </div>
              <div class="screenshot-box" onclick="openLightbox('assets/03_crm_seleccionar_visibles.jpg')">
                <img src="assets/03_crm_seleccionar_visibles.jpg" alt="CRM Seleccionar Visibles">
                <span class="screenshot-badge">🔍 Click para ampliar</span>
              </div>
            </div>
          </div>
        </div>

      </section>

    </div>
  </main>

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox" onclick="closeLightbox()">
    <span class="lightbox-close">&times;</span>
    <img id="lightbox-img" src="" alt="Captura ampliada">
  </div>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // Lightbox modal functionality
    function openLightbox(src) {
      const lb = document.getElementById('lightbox');
      const img = document.getElementById('lightbox-img');
      img.src = src;
      lb.classList.add('active');
    }

    function closeLightbox() {
      const lb = document.getElementById('lightbox');
      lb.classList.remove('active');
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeLightbox();
    });

    // Real-time manual search / filter
    function filterManual() {
      const query = document.getElementById('filterInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.step-card');
      const navItems = document.querySelectorAll('.nav-item');

      cards.forEach(card => {
        const text = card.innerText.toLowerCase();
        if (text.includes(query) || query === '') {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }

    // Scroll spy for sidebar links
    window.addEventListener('scroll', () => {
      const sections = document.querySelectorAll('.module-section, .step-card');
      const scrollPos = window.scrollY + 100;

      sections.forEach(section => {
        if (section.id) {
          const top = section.offsetTop;
          const height = section.offsetHeight;
          if (scrollPos >= top && scrollPos < top + height) {
            document.querySelectorAll('.nav-item a').forEach(a => a.classList.remove('active'));
            const current = document.querySelector(`.nav-item a[href="#${section.id}"]`);
            if (current) current.classList.add('active');
          }
        }
      });
    });
  </script>
</body>
</html>
"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML successfully generated at: {html_path}")
