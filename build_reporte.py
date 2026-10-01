import json
import os

with open('/home/leondon-pc/Desktop/Manual_Operativo_Supply_ArreglaTodo/assets/datos_solicitudes_auditadas.json', 'r', encoding='utf-8') as f:
    all_records = json.load(f)

clavos = [r for r in all_records if r.get('esClavo') and not r.get('noEsClavo')]
conflictos = [r for r in all_records if r.get('noEsClavo') and r.get('esClavo')]

clavos_json = json.dumps(clavos, ensure_ascii=False)
conflictos_json = json.dumps(conflictos, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reporte Ejecutivo: Auditoría Operativa & No Conversión | ArreglaTodo</title>
  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    :root {{
      --bg-base: #0a0d14;
      --bg-surface: #121722;
      --bg-card: #182030;
      --bg-card-hover: #1f2b42;
      --border-color: #243047;
      --border-light: #334466;
      --primary: #ff6b35;
      --primary-light: #ff8c5a;
      --accent: #00b4d8;
      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
      --purple: #8b5cf6;
      --gold: #fbbf24;
      --pink: #ec4899;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font);
      background-color: var(--bg-base);
      color: var(--text-main);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Top Executive Header */
    header {{
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      padding: 16px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 90;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }}

    .logo-container {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .badge-reporte {{
      background: linear-gradient(135deg, #ff6b35, #ef4444);
      color: white;
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1px;
      padding: 4px 12px;
      border-radius: 20px;
      box-shadow: 0 0 10px rgba(239, 68, 68, 0.3);
    }}

    .header-titles h1 {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #fff;
    }}

    .header-titles p {{
      font-size: 0.82rem;
      color: var(--text-muted);
    }}

    .header-actions {{
      display: flex;
      gap: 10px;
      align-items: center;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.2s ease;
      text-decoration: none;
    }}

    .btn-primary {{
      background: var(--primary);
      color: white;
      border-color: var(--primary-light);
    }}
    .btn-primary:hover {{
      background: var(--primary-light);
      box-shadow: 0 0 12px rgba(255, 107, 53, 0.3);
    }}

    .btn-secondary {{
      background: var(--bg-card);
      color: var(--text-main);
      border-color: var(--border-color);
    }}
    .btn-secondary:hover {{
      background: var(--bg-card-hover);
      border-color: var(--border-light);
    }}

    .btn-gold {{
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: white;
      border-color: #fbbf24;
    }}

    .container {{
      max-width: 1440px;
      width: 100%;
      margin: 0 auto;
      padding: 28px 32px 60px;
      flex: 1;
    }}

    /* Methodology / Scope Alert Box */
    .scope-box {{
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
      border: 1px solid #3b82f6;
      border-left: 5px solid #3b82f6;
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 28px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    }}

    .scope-title {{
      font-size: 1rem;
      font-weight: 700;
      color: #60a5fa;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }}

    .scope-content {{
      font-size: 0.88rem;
      color: #cbd5e1;
      line-height: 1.6;
    }}

    .scope-content strong {{
      color: #fff;
    }}

    .scope-tags {{
      display: flex;
      gap: 8px;
      margin-top: 12px;
      flex-wrap: wrap;
    }}

    .scope-pill {{
      font-size: 0.75rem;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 6px;
      background: rgba(59, 130, 246, 0.15);
      border: 1px solid rgba(59, 130, 246, 0.3);
      color: #93c5fd;
    }}

    /* Financial Impact Grid */
    .balance-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr) 1.4fr;
      gap: 16px;
      margin-bottom: 32px;
    }}

    .kpi-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      text-align: center;
      position: relative;
    }}

    .kpi-label {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      margin-bottom: 6px;
    }}

    .kpi-num {{
      font-size: 2.2rem;
      font-weight: 800;
      line-height: 1.1;
      color: #fff;
    }}

    .kpi-subtext {{
      font-size: 0.75rem;
      color: var(--text-dim);
      margin-top: 6px;
    }}

    .hero-card {{
      background: linear-gradient(135deg, #1e1b4b 0%, #172554 100%);
      border: 1px solid #4f46e5;
      box-shadow: 0 0 25px rgba(79, 70, 229, 0.25);
    }}

    .hero-card .kpi-label {{
      color: #a5b4fc;
    }}

    .hero-card .kpi-num {{
      color: #38bdf8;
      text-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
    }}

    .incentive-badge {{
      display: inline-block;
      background: #10b981;
      color: white;
      font-size: 0.78rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 20px;
      margin-top: 6px;
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);
    }}

    /* Interactive Charts Section */
    .charts-container {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 36px;
    }}

    .chart-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      position: relative;
    }}

    .chart-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 12px;
    }}

    .chart-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .chart-hint {{
      font-size: 0.75rem;
      color: var(--accent);
      background: rgba(0, 180, 216, 0.1);
      padding: 3px 8px;
      border-radius: 6px;
      border: 1px solid rgba(0, 180, 216, 0.2);
    }}

    .chart-canvas-wrapper {{
      position: relative;
      flex: 1;
      min-height: 320px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* Special Conflicts Section (15 Double Check) */
    .conflicts-section {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 26px 30px;
      margin-bottom: 36px;
    }}

    .conflicts-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 14px;
    }}

    .conflicts-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #f87171;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .conflicts-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 18px;
    }}

    .conflict-group-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 18px;
    }}

    .conflict-group-title {{
      font-size: 0.92rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 12px;
      border-bottom: 1px solid rgba(255,255,255,0.06);
      padding-bottom: 8px;
    }}

    .conflict-item {{
      background: rgba(10, 13, 20, 0.5);
      border: 1px solid rgba(255,255,255,0.04);
      border-radius: 6px;
      padding: 10px 12px;
      margin-bottom: 8px;
      font-size: 0.83rem;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .conflict-item:hover {{
      background: rgba(255,255,255,0.04);
      border-color: var(--border-light);
    }}

    .conflict-item:last-child {{
      margin-bottom: 0;
    }}

    .conflict-item-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 4px;
    }}

    .conflict-id {{
      font-family: monospace;
      font-weight: 700;
      color: var(--primary-light);
    }}

    .conflict-client {{
      font-weight: 600;
      color: #fff;
    }}

    .conflict-desc {{
      color: #cbd5e1;
      font-style: italic;
    }}

    /* Evidence Table Section */
    .table-section {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 26px 30px;
    }}

    .table-toolbar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      flex-wrap: wrap;
      gap: 14px;
    }}

    .search-input {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px 14px;
      color: #fff;
      font-size: 0.88rem;
      min-width: 320px;
    }}
    .search-input:focus {{
      outline: none;
      border-color: var(--accent);
    }}

    .filter-pills {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .filter-btn {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .filter-btn:hover, .filter-btn.active {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      text-align: left;
    }}

    th {{
      background: #151c2a;
      color: var(--text-muted);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-color);
      font-weight: 700;
      white-space: nowrap;
    }}

    td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-color);
      vertical-align: middle;
    }}

    tr:hover td {{
      background: rgba(255,255,255,0.02);
    }}

    .badge-rubro {{
      background: #1f2b42;
      color: #93c5fd;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
    }}

    .badge-cat {{
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      display: inline-block;
      white-space: nowrap;
    }}

    .cat-supply {{ background: rgba(245, 158, 11, 0.18); color: #fbbf24; border: 1px solid #d97706; }}
    .cat-emergencia {{ background: rgba(239, 68, 68, 0.18); color: #f87171; border: 1px solid #dc2626; }}
    .cat-pago {{ background: rgba(139, 92, 246, 0.18); color: #c084fc; border: 1px solid #7c3aed; }}
    .cat-incompatible {{ background: rgba(100, 116, 139, 0.2); color: #cbd5e1; border: 1px solid #475569; }}
    .cat-error {{ background: rgba(236, 72, 153, 0.18); color: #f472b6; border: 1px solid #db2777; }}
    .cat-invalido {{ background: rgba(6, 182, 212, 0.18); color: #67e8f9; border: 1px solid #0891b2; }}

    /* =========================================
       SLIDING SIDE DRAWER (INTERACTION PANEL)
       ========================================= */
    .drawer-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(4px);
      z-index: 200;
      opacity: 0;
      visibility: hidden;
      transition: all 0.25s ease;
    }}
    .drawer-overlay.open {{
      opacity: 1;
      visibility: visible;
    }}

    .side-drawer {{
      position: fixed;
      top: 0;
      right: 0;
      width: 520px;
      max-width: 92vw;
      height: 100vh;
      background: var(--bg-surface);
      border-left: 1px solid var(--border-light);
      box-shadow: -10px 0 40px rgba(0, 0, 0, 0.7);
      transform: translateX(100%);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 210;
      display: flex;
      flex-direction: column;
    }}
    .side-drawer.open {{
      transform: translateX(0);
    }}

    .drawer-header {{
      padding: 20px 24px;
      background: #151c2a;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
    }}

    .drawer-badge {{
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 3px 8px;
      border-radius: 6px;
      margin-bottom: 6px;
      background: var(--primary-glow);
      color: var(--primary-light);
      border: 1px solid rgba(255, 107, 53, 0.3);
    }}

    .drawer-header h2 {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #fff;
    }}

    .drawer-header p {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .drawer-close {{
      background: rgba(255,255,255,0.06);
      border: none;
      color: var(--text-muted);
      font-size: 1.5rem;
      line-height: 1;
      cursor: pointer;
      width: 36px;
      height: 36px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s ease;
    }}
    .drawer-close:hover {{
      background: rgba(255,255,255,0.12);
      color: #fff;
    }}

    .drawer-body {{
      padding: 24px;
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 22px;
    }}

    .drawer-section-title {{
      font-size: 0.88rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    /* Cross Distribution Cards */
    .cross-item {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 10px 14px;
      margin-bottom: 8px;
    }}

    .cross-item-header {{
      display: flex;
      justify-content: space-between;
      font-size: 0.84rem;
      font-weight: 600;
      margin-bottom: 6px;
    }}

    .cross-track {{
      background: #111723;
      height: 6px;
      border-radius: 3px;
      overflow: hidden;
    }}
    .cross-fill {{
      height: 100%;
      background: var(--accent);
      border-radius: 3px;
    }}

    /* Drawer Request Cards */
    .req-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 14px;
      margin-bottom: 10px;
      transition: border-color 0.15s ease;
    }}
    .req-card:hover {{
      border-color: var(--border-light);
    }}

    .req-card-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}

    .req-card-id {{
      font-family: monospace;
      font-weight: 700;
      color: var(--primary-light);
    }}

    .req-card-name {{
      font-weight: 700;
      color: #fff;
      font-size: 0.9rem;
    }}

    .req-card-desc {{
      font-size: 0.85rem;
      color: #cbd5e1;
      background: rgba(10, 13, 20, 0.4);
      padding: 8px 10px;
      border-radius: 6px;
      margin-top: 8px;
      border-left: 3px solid var(--primary);
      line-height: 1.45;
    }}

    .drawer-footer {{
      padding: 16px 24px;
      background: #151c2a;
      border-top: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      gap: 12px;
    }}

    /* Print Formatting */
    @media print {{
      header, .header-actions, .table-toolbar, .btn, .filter-pills, .drawer-overlay, .side-drawer, .chart-hint {{
        display: none !important;
      }}
      body, .container, .kpi-card, .chart-card, .conflicts-section, .table-section {{
        background: #fff !important;
        color: #000 !important;
        box-shadow: none !important;
      }}
      .kpi-card, .chart-card, .conflicts-section, .table-section, .scope-box {{
        border: 1px solid #cbd5e1 !important;
        margin-bottom: 20px !important;
      }}
      .kpi-num, .chart-title, .conflicts-title, .scope-title {{
        color: #000 !important;
      }}
      .hero-card {{
        background: #f8fafc !important;
        border: 2px solid #4f46e5 !important;
      }}
      .hero-card .kpi-num {{
        color: #1e40af !important;
      }}
      .scope-content {{
        color: #334155 !important;
      }}
      th {{
        background: #f1f5f9 !important;
        color: #0f172a !important;
        border-bottom: 2px solid #000 !important;
      }}
      td {{
        color: #1e293b !important;
        border-bottom: 1px solid #e2e8f0 !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Executive Header -->
  <header>
    <div class="logo-container">
      <span class="badge-reporte">Dirección Supply</span>
      <div class="header-titles">
        <h1>Informe Ejecutivo: Auditoría Operativa & No Conversión</h1>
        <p>Cierre Oficial • Análisis de Clavos, Deducción de Base y Conversión Real</p>
      </div>
    </div>
    <div class="header-actions">
      <a href="auditoria.html" class="btn btn-secondary">🔍 Ver Auditoría Operativa</a>
      <button class="btn btn-primary" onclick="copyExecutiveSummary()">📋 Copiar Resumen</button>
      <button class="btn btn-secondary" onclick="window.print()">🖨️ Imprimir / Guardar PDF</button>
    </div>
  </header>

  <div class="container">

    <!-- Methodology & Scope Alert Box -->
    <div class="scope-box">
      <div class="scope-title">
        <span>📌 Declaración de Alcance, Horario & Criterio Estratégico de Auditoría</span>
      </div>
      <div class="scope-content">
        Por razones operativas y límites estrictos de horario de cierre, el presente informe se enfocó tácticamente en las solicitudes de <strong>mayor criticidad histórica y probabilidad de anomalías (Canceladas, Carpintería, Vidriería, Emergencias, Armado de Muebles)</strong>.
        <br><br>
        <strong>Quedaron excluidas de revisión en esta fase:</strong>
        <ul style="margin: 6px 0 6px 20px;">
          <li>Todas las solicitudes <strong>Aceptadas</strong> (destacando que se identificó y sumó la <strong>#19994 de Construcción</strong> cerrada con Anthony que figuraba pendiente en sistema), <strong>Completadas</strong> y <strong>Pago Pendiente</strong>.</li>
          <li>Las solicitudes <strong>Enviadas</strong> de los rubros <strong>Limpieza</strong>, <strong>Pintura</strong> y <strong>Sanitaria</strong>.</li>
        </ul>
        <strong>Conclusión de Alcance:</strong> Los <strong>66 clavos documentados constituyen un piso mínimo comprobado</strong>. De completarse la auditoría sobre las solicitudes enviadas pendientes de Limpieza, Pintura y Sanitaria, el volumen de solicitudes no válidas aumentará proporcionalmente.
      </div>
      <div class="scope-tags">
        <span class="scope-pill">Foco Crítico Realizado</span>
        <span class="scope-pill">193 Solicitudes Convertidas</span>
        <span class="scope-pill">Piso Conservador de 66 Clavos</span>
        <span class="scope-pill">15 Casos Estratégicos a Informar</span>
      </div>
    </div>

    <!-- Financial & Conversion Balance Cards -->
    <div class="balance-grid">
      <div class="kpi-card">
        <div class="kpi-label">Base Mensual Inicial</div>
        <div class="kpi-num">581</div>
        <div class="kpi-subtext">Total solicitudes cargadas</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Clavos Comprobados</div>
        <div class="kpi-num" style="color: var(--gold);">-66</div>
        <div class="kpi-subtext">A deducir formalmente</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Base Válida Neta</div>
        <div class="kpi-num" style="color: var(--accent);">515</div>
        <div class="kpi-subtext">Denominador depurado</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Convertidas Totales</div>
        <div class="kpi-num" style="color: var(--success);">193</div>
        <div class="kpi-subtext">Incluye #19994 (Anthony)</div>
      </div>
      <div class="kpi-card hero-card">
        <div class="kpi-label">Tasa de Conversión Real</div>
        <div class="kpi-num">37.48%</div>
        <div class="incentive-badge">Tramo Oficial: $200 USD</div>
        <div class="kpi-subtext" style="color: #93c5fd; margin-top: 6px;">
          +4.26% sobre tasa inicial (33.22%). A solo 20 clavos del tramo $250 USD.
        </div>
      </div>
    </div>

    <!-- Interactive Charts Section (Chart.js) -->
    <div class="charts-container">
      
      <!-- Donut Chart: Motivos -->
      <div class="chart-card">
        <div class="chart-header">
          <div class="chart-title">
            <span>🍩 Causas Raíz de No Conversión (Motivos)</span>
          </div>
          <span class="chart-hint">Haz clic en una porción para ver detalles ➔</span>
        </div>
        <div class="chart-canvas-wrapper">
          <canvas id="motivosDonutChart"></canvas>
        </div>
      </div>

      <!-- Horizontal Bar Chart: Rubros -->
      <div class="chart-card">
        <div class="chart-header">
          <div class="chart-title">
            <span>📊 Concentración de Clavos por Rubro</span>
          </div>
          <span class="chart-hint">Haz clic en una barra para ver detalles ➔</span>
        </div>
        <div class="chart-canvas-wrapper">
          <canvas id="rubrosBarChart"></canvas>
        </div>
      </div>

    </div>

    <!-- Special Section: 15 Conflict Cases for Boss Review -->
    <div class="conflicts-section">
      <div class="conflicts-header">
        <div class="conflicts-title">
          <span>⚠️ Casos Estratégicos a Informar & Resolver (15 Doble Check)</span>
        </div>
        <span style="font-size: 0.82rem; color: var(--text-muted);">
          Haz clic en cualquier caso para abrir el desglose
        </span>
      </div>

      <div class="conflicts-grid">

        <!-- Card 1: B2B / Corporativo -->
        <div class="conflict-group-card">
          <div class="conflict-group-title">
            <span>🏢 Cuentas Corporativas & Grandes Clientes</span>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19719')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19719</span>
              <span class="conflict-client">MONICA VALLARINO (Riogas) • Jardinería</span>
            </div>
            <div class="conflict-desc">"Sector de compras de Riogas. Preocupados por costos de gestión repetitivos, quizás se pueda hacer un avance con un precio preferencial."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19922')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19922</span>
              <span class="conflict-client">ANII • Carpintería</span>
            </div>
            <div class="conflict-desc">"Hacer seguimiento Agencia Nacional de Investigación e Innovación."</div>
          </div>
        </div>

        <!-- Card 2: Fallas Operativas -->
        <div class="conflict-group-card">
          <div class="conflict-group-title">
            <span>🛠️ Fallas Operativas Internas a Corregir</span>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19567')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19567</span>
              <span class="conflict-client">Gustavo Laborde • Carpintería</span>
            </div>
            <div class="conflict-desc">"Esta venta se cayó por el servicio fallido de Progreso."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19684')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19684</span>
              <span class="conflict-client">Paula Viola • Limpieza</span>
            </div>
            <div class="conflict-desc">"Acá se cotizó, pero luego se cambió el precio; hay que hablar este tema, porque hay un precio por zona y se debe respetar."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19973')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19973</span>
              <span class="conflict-client">Alicia • Aire acondicionado</span>
            </div>
            <div class="conflict-desc">"La atención fue pésima y reenviar audios de los proveedores así porque sí es un error."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19618')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19618</span>
              <span class="conflict-client">Naty • Limpieza</span>
            </div>
            <div class="conflict-desc">"Interesada sin respuesta, posible fuga por canal secundario."</div>
          </div>
        </div>

        <!-- Card 3: Leads Rescatables -->
        <div class="conflict-group-card">
          <div class="conflict-group-title">
            <span>📞 Leads Rescatables en Seguimiento Activo</span>
          </div>
          <div class="conflict-item" onclick="openConflictModal('20009')">
            <div class="conflict-item-top">
              <span class="conflict-id">#20009</span>
              <span class="conflict-client">Vanina Grunberg • Jardinería</span>
            </div>
            <div class="conflict-desc">"Contactar hoy para tratar de remontar."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('20022')">
            <div class="conflict-item-top">
              <span class="conflict-id">#20022</span>
              <span class="conflict-client">Ignacio • Construcción</span>
            </div>
            <div class="conflict-desc">"Contactar para coordinar, quizás se pueda."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19877')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19877</span>
              <span class="conflict-client">Karina • Jardinería</span>
            </div>
            <div class="conflict-desc">"Para contactar el 07/10."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19834')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19834</span>
              <span class="conflict-client">Avalon • Carpintería</span>
            </div>
            <div class="conflict-desc">"Tratar de enviar cotización, está a nombre de Pablo Leva, seguro es la que falta de Álvaro."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19885')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19885</span>
              <span class="conflict-client">Carmen Barbe • Carpintería</span>
            </div>
            <div class="conflict-desc">"Esperando por Germán."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19975')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19975</span>
              <span class="conflict-client">Paula Maciel • Electricidad</span>
            </div>
            <div class="conflict-desc">"Hacer seguimiento a cotización."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19563')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19563</span>
              <span class="conflict-client">María Eugenia Burgos • Limpieza</span>
            </div>
            <div class="conflict-desc">"Agendar para fines de octubre hacer un recordatorio."</div>
          </div>
        </div>

        <!-- Card 4: Fricción Política Cobro -->
        <div class="conflict-group-card">
          <div class="conflict-group-title">
            <span>💳 Fricción por Política de Pago Adelantado</span>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19528')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19528</span>
              <span class="conflict-client">Bessie • Carpintería</span>
            </div>
            <div class="conflict-desc">"La venta se cayó por el pago adelantado."</div>
          </div>
          <div class="conflict-item" onclick="openConflictModal('19547')">
            <div class="conflict-item-top">
              <span class="conflict-id">#19547</span>
              <span class="conflict-client">Annia Gaitán • Carpintería</span>
            </div>
            <div class="conflict-desc">"La venta se cayó por el pago adelantado."</div>
          </div>
        </div>

      </div>
    </div>

    <!-- Evidence Table Section -->
    <div class="table-section">
      <div class="table-toolbar">
        <div>
          <h3 style="color:#fff; margin-bottom: 4px;">Auditoría Detallada de los 66 Clavos Justificados</h3>
          <p style="font-size: 0.82rem; color: var(--text-muted);" id="tableCountText">Mostrando 66 clavos</p>
        </div>
        <input type="text" class="search-input" id="tableSearch" placeholder="🔍 Buscar por ID, cliente, rubro, o motivo..." oninput="filterTable()">
      </div>

      <div class="filter-pills" id="filterPillsContainer" style="margin-bottom: 18px;">
        <button class="filter-btn active" onclick="setFilter('all')">Todos (66)</button>
        <button class="filter-btn" onclick="setFilter('Carpintería')">Carpintería (20)</button>
        <button class="filter-btn" onclick="setFilter('Sanitaria')">Sanitaria (11)</button>
        <button class="filter-btn" onclick="setFilter('Vidriería')">Vidriería (7)</button>
        <button class="filter-btn" onclick="setFilter('Armado de muebles')">Armado de muebles (6)</button>
        <button class="filter-btn" onclick="setFilter('Limpieza')">Limpieza (5)</button>
        <button class="filter-btn" onclick="setFilter('Electricidad')">Electricidad (4)</button>
        <button class="filter-btn" onclick="setFilter('Falla de Supply')">Falla de Supply</button>
        <button class="filter-btn" onclick="setFilter('Emergencia')">Emergencias</button>
        <button class="filter-btn" onclick="setFilter('Pago Adelantado')">Pago Adelantado</button>
      </div>

      <div style="overflow-x: auto;">
        <table>
          <thead>
            <tr>
              <th style="width: 80px;">ID</th>
              <th style="width: 170px;">Cliente</th>
              <th style="width: 140px;">Rubro</th>
              <th style="width: 220px;">Causa Raíz Estandarizada</th>
              <th>Fundamento Inobjetable (Descripción Real)</th>
              <th style="width: 110px;">Estado</th>
            </tr>
          </thead>
          <tbody id="evidenceTableBody">
            <!-- Rendered by JS -->
          </tbody>
        </table>
      </div>
    </div>

  </div>

  <!-- SLIDING SIDE DRAWER -->
  <div class="drawer-overlay" id="drawerOverlay" onclick="closeDrawer()"></div>
  <aside class="side-drawer" id="sideDrawer">
    <div class="drawer-header">
      <div>
        <span class="drawer-badge" id="drawerBadge">Rubro</span>
        <h2 id="drawerTitle">Carpintería</h2>
        <p id="drawerSubtitle">20 clavos detectados (30.3% del total)</p>
      </div>
      <button class="drawer-close" onclick="closeDrawer()">&times;</button>
    </div>
    
    <div class="drawer-body">
      <!-- Cross Breakdown Card -->
      <div class="drawer-section">
        <div class="drawer-section-title" id="drawerCrossTitle">📊 Desglose Cruzado</div>
        <div id="drawerCrossList">
          <!-- Rendered via JS -->
        </div>
      </div>

      <!-- Request List -->
      <div class="drawer-section">
        <div class="drawer-section-title" id="drawerRequestsTitle">📋 Solicitudes del Segmento</div>
        <div id="drawerCardsList">
          <!-- Rendered via JS -->
        </div>
      </div>
    </div>

    <div class="drawer-footer">
      <button class="btn btn-secondary" onclick="filterMainTableFromDrawer()">🔍 Filtrar en Tabla Principal</button>
      <button class="btn btn-primary" onclick="copyDrawerDetails()">📋 Copiar este Grupo</button>
    </div>
  </aside>

  <script>
    const CLAVOS = {clavos_json};
    const CONFLICTOS = {conflictos_json};

    let activeFilter = 'all';
    let currentDrawerData = null;

    let donutChartInstance = null;
    let barChartInstance = null;

    window.addEventListener('DOMContentLoaded', () => {{
      initDonutChart();
      initBarChart();
      renderTable();

      // Keyboard Esc close drawer
      window.addEventListener('keydown', (e) => {{
        if (e.key === 'Escape') closeDrawer();
      }});
    }});

    // =========================================
    // CHART.JS INITIALIZATION WITH ONCLICK
    // =========================================
    function initDonutChart() {{
      const motiveCounts = {{
        'Falla de Supply / Opciones Insuficientes': 0,
        'Emergencia sin Cobertura': 0,
        'Servicio Incompatible / Fuera de Regla': 0,
        'Fricción de Pago Adelantado': 0,
        'Error Administrativo / Duplicada': 0,
        'Lead No Calificado (Inquilino/Curioso)': 0
      }};

      CLAVOS.forEach(c => {{
        const cat = c.categoriaClavo || 'Falla de Supply / Opciones Insuficientes';
        if (motiveCounts[cat] !== undefined) motiveCounts[cat]++;
        else motiveCounts['Falla de Supply / Opciones Insuficientes']++;
      }});

      const labels = Object.keys(motiveCounts);
      const data = Object.values(motiveCounts);
      const colors = ['#f59e0b', '#ef4444', '#64748b', '#8b5cf6', '#ec4899', '#06b6d4'];

      const ctx = document.getElementById('motivosDonutChart').getContext('2d');
      donutChartInstance = new Chart(ctx, {{
        type: 'doughnut',
        data: {{
          labels: labels,
          datasets: [{{
            data: data,
            backgroundColor: colors,
            borderColor: '#121722',
            borderWidth: 3,
            hoverOffset: 12
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          cutout: '62%',
          plugins: {{
            legend: {{
              position: 'bottom',
              labels: {{
                color: '#cbd5e1',
                font: {{ family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto', size: 11 }},
                boxWidth: 12,
                padding: 14
              }}
            }},
            tooltip: {{
              backgroundColor: '#182030',
              titleColor: '#fff',
              bodyColor: '#cbd5e1',
              borderColor: '#334466',
              borderWidth: 1,
              padding: 12,
              callbacks: {{
                label: function(context) {{
                  const val = context.parsed;
                  const pct = ((val / CLAVOS.length) * 100).toFixed(1);
                  return ` ${{val}} casos (${{pct}}%) • Clic para ver detalle`;
                }}
              }}
            }}
          }},
          onClick: (evt, activeEls) => {{
            if (activeEls.length > 0) {{
              const index = activeEls[0].index;
              const motiveName = labels[index];
              openDrawer('motivo', motiveName);
            }}
          }}
        }}
      }});
    }}

    function initBarChart() {{
      const rubroCounts = {{}};
      CLAVOS.forEach(c => {{
        rubroCounts[c.rubro] = (rubroCounts[c.rubro] || 0) + 1;
      }});

      const sorted = Object.entries(rubroCounts).sort((a,b) => b[1] - a[1]);
      const labels = sorted.map(x => x[0]);
      const data = sorted.map(x => x[1]);

      const ctx = document.getElementById('rubrosBarChart').getContext('2d');
      barChartInstance = new Chart(ctx, {{
        type: 'bar',
        data: {{
          labels: labels,
          datasets: [{{
            data: data,
            backgroundColor: 'rgba(255, 107, 53, 0.85)',
            hoverBackgroundColor: '#ff6b35',
            borderRadius: 6,
            borderSkipped: false
          }}]
        }},
        options: {{
          indexAxis: 'y',
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              backgroundColor: '#182030',
              titleColor: '#fff',
              bodyColor: '#cbd5e1',
              borderColor: '#334466',
              borderWidth: 1,
              padding: 12,
              callbacks: {{
                label: function(context) {{
                  const val = context.parsed.x;
                  const pct = ((val / CLAVOS.length) * 100).toFixed(1);
                  return ` ${{val}} clavos (${{pct}}%) • Clic para ver detalle`;
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              grid: {{ color: 'rgba(255, 255, 255, 0.05)' }},
              ticks: {{ color: '#94a3b8', font: {{ size: 10 }} }}
            }},
            y: {{
              grid: {{ display: false }},
              ticks: {{ color: '#f1f5f9', font: {{ weight: 600, size: 11 }} }}
            }}
          }},
          onClick: (evt, activeEls) => {{
            if (activeEls.length > 0) {{
              const index = activeEls[0].index;
              const rubroName = labels[index];
              openDrawer('rubro', rubroName);
            }}
          }}
        }}
      }});
    }}

    // =========================================
    // SLIDING DRAWER LOGIC (DRILL-DOWN)
    // =========================================
    function openDrawer(type, name) {{
      currentDrawerData = {{ type, name }};
      const overlay = document.getElementById('drawerOverlay');
      const drawer = document.getElementById('sideDrawer');

      const badge = document.getElementById('drawerBadge');
      const title = document.getElementById('drawerTitle');
      const subtitle = document.getElementById('drawerSubtitle');
      const crossTitle = document.getElementById('drawerCrossTitle');
      const crossList = document.getElementById('drawerCrossList');
      const requestsTitle = document.getElementById('drawerRequestsTitle');
      const cardsList = document.getElementById('drawerCardsList');

      let matching = [];
      let crossCounts = {{}};

      if (type === 'rubro') {{
        badge.innerText = 'Rubro Seleccionado';
        title.innerText = name;
        matching = CLAVOS.filter(c => c.rubro.toLowerCase() === name.toLowerCase());
        const pct = ((matching.length / CLAVOS.length) * 100).toFixed(1);
        subtitle.innerText = `${{matching.length}} clavos justificados (${{pct}}% del total de clavos)`;
        crossTitle.innerText = `🔍 ¿Qué causas golpean a ${{name}}?`;

        matching.forEach(c => {{
          const m = c.categoriaClavo || 'Falla de Supply / Opciones Insuficientes';
          crossCounts[m] = (crossCounts[m] || 0) + 1;
        }});
      }} else {{
        badge.innerText = 'Causa Raíz Seleccionada';
        title.innerText = name;
        matching = CLAVOS.filter(c => (c.categoriaClavo || '').toLowerCase() === name.toLowerCase());
        const pct = ((matching.length / CLAVOS.length) * 100).toFixed(1);
        subtitle.innerText = `${{matching.length}} casos documentados (${{pct}}% de las pérdidas)`;
        crossTitle.innerText = `📦 ¿Qué rubros sufren más por este motivo?`;

        matching.forEach(c => {{
          crossCounts[c.rubro] = (crossCounts[c.rubro] || 0) + 1;
        }});
      }}

      // Render Cross List
      const sortedCross = Object.entries(crossCounts).sort((a,b) => b[1] - a[1]);
      let crossHtml = '';
      sortedCross.forEach(([key, count]) => {{
        const cPct = ((count / matching.length) * 100).toFixed(1);
        crossHtml += `
          <div class="cross-item">
            <div class="cross-item-header">
              <span>${{key}}</span>
              <span style="color:var(--accent); font-weight:700;">${{count}} (${{cPct}}%)</span>
            </div>
            <div class="cross-track">
              <div class="cross-fill" style="width: ${{cPct}}%;"></div>
            </div>
          </div>
        `;
      }});
      crossList.innerHTML = crossHtml;

      // Render Individual Requests
      requestsTitle.innerText = `📋 Solicitudes Individuales (${{matching.length}})`;
      let cardsHtml = '';
      matching.forEach(c => {{
        cardsHtml += `
          <div class="req-card">
            <div class="req-card-top">
              <span class="req-card-id">#${{c.id}}</span>
              <span class="badge-rubro">${{c.rubro}}</span>
            </div>
            <div class="req-card-name">${{escapeHtml(c.nombre)}}</div>
            <div style="font-size: 0.78rem; color: var(--gold); margin-top:2px;">
              ${{c.categoriaClavo}}
            </div>
            <div class="req-card-desc">
              "${{escapeHtml(c.fundamento || 'Clavo comprobado para deducción de base.')}}"
            </div>
          </div>
        `;
      }});
      cardsList.innerHTML = cardsHtml;

      overlay.classList.add('open');
      drawer.classList.add('open');
    }}

    function closeDrawer() {{
      document.getElementById('drawerOverlay').classList.remove('open');
      document.getElementById('sideDrawer').classList.remove('open');
    }}

    function filterMainTableFromDrawer() {{
      if (currentDrawerData) {{
        setFilter(currentDrawerData.name);
        closeDrawer();
        document.querySelector('.table-section').scrollIntoView({{ behavior: 'smooth' }});
      }}
    }}

    function copyDrawerDetails() {{
      if (!currentDrawerData) return;
      const {{ type, name }} = currentDrawerData;
      const matching = type === 'rubro' ? 
        CLAVOS.filter(c => c.rubro.toLowerCase() === name.toLowerCase()) :
        CLAVOS.filter(c => (c.categoriaClavo || '').toLowerCase() === name.toLowerCase());

      let text = `*DESGLOSE AUDITADO: ${{name.toUpperCase()}} (${{matching.length}} CASOS)*\\n\\n`;
      matching.forEach((c, idx) => {{
        text += `${{idx + 1}}. #${{c.id}} • ${{c.nombre}} (${{c.rubro}}): ${{c.fundamento}}\\n`;
      }});

      navigator.clipboard.writeText(text).then(() => {{
        alert(`¡Detalles de ${{name}} copiados al portapapeles!`);
      }});
    }}

    // Conflict Click Modal / Drilldown
    function openConflictModal(id) {{
      const item = CONFLICTOS.find(c => c.id === id);
      if (!item) return;

      const badge = document.getElementById('drawerBadge');
      const title = document.getElementById('drawerTitle');
      const subtitle = document.getElementById('drawerSubtitle');
      const crossTitle = document.getElementById('drawerCrossTitle');
      const crossList = document.getElementById('drawerCrossList');
      const requestsTitle = document.getElementById('drawerRequestsTitle');
      const cardsList = document.getElementById('drawerCardsList');

      badge.innerText = 'Caso Estratégico (Doble Check)';
      title.innerText = `#${{item.id}} - ${{item.nombre}}`;
      subtitle.innerText = `Rubro: ${{item.rubro}} • Estado: ${{item.estado}}`;
      crossTitle.innerText = `🎯 Resolución Requerida`;
      crossList.innerHTML = `
        <div class="cross-item">
          <div style="font-size:0.85rem; color:#f87171; font-weight:700;">Requiere decisión del jefe</div>
          <div style="font-size:0.82rem; color:var(--text-muted); margin-top:4px;">
            Este caso tiene ambos casilleros marcados. Si el jefe lo aprueba como clavo, se descuenta de la base y aporta a comisiones.
          </div>
        </div>
      `;

      requestsTitle.innerText = `Detalle y Fundamento Registrado`;
      cardsList.innerHTML = `
        <div class="req-card" style="border-left: 3px solid #ef4444;">
          <div class="req-card-top">
            <span class="req-card-id">#${{item.id}}</span>
            <span class="badge-rubro">${{item.rubro}}</span>
          </div>
          <div class="req-card-name">${{escapeHtml(item.nombre)}}</div>
          <div class="req-card-desc" style="font-size: 0.9rem; color:#fff;">
            "${{escapeHtml(item.fundamento)}}"
          </div>
        </div>
      `;

      document.getElementById('drawerOverlay').classList.add('open');
      document.getElementById('sideDrawer').classList.add('open');
    }}

    // =========================================
    // TABLE FILTER & SEARCH
    // =========================================
    function setFilter(filt) {{
      activeFilter = filt;
      document.querySelectorAll('.filter-btn').forEach(btn => {{
        btn.classList.toggle('active', btn.innerText.includes(filt) || (filt === 'all' && btn.innerText.includes('Todos')));
      }});
      renderTable();
    }}

    function filterTable() {{
      renderTable();
    }}

    function renderTable() {{
      const tbody = document.getElementById('evidenceTableBody');
      const search = document.getElementById('tableSearch').value.toLowerCase().trim();

      let visible = 0;
      let html = '';

      CLAVOS.forEach(c => {{
        const matchesFilter = activeFilter === 'all' || 
          c.rubro.toLowerCase().includes(activeFilter.toLowerCase()) || 
          c.categoriaClavo.toLowerCase().includes(activeFilter.toLowerCase());

        const matchesSearch = !search ||
          c.id.includes(search) ||
          c.nombre.toLowerCase().includes(search) ||
          c.rubro.toLowerCase().includes(search) ||
          c.fundamento.toLowerCase().includes(search) ||
          c.categoriaClavo.toLowerCase().includes(search);

        if (matchesFilter && matchesSearch) {{
          visible++;
          const catClass = getCatClass(c.categoriaClavo);
          html += `
            <tr>
              <td><span style="font-family: monospace; font-weight:700; color:var(--primary-light);">#${{c.id}}</span></td>
              <td><strong>${{escapeHtml(c.nombre)}}</strong></td>
              <td><span class="badge-rubro" style="cursor:pointer;" onclick="openDrawer('rubro', '${{c.rubro}}')">${{escapeHtml(c.rubro)}}</span></td>
              <td><span class="badge-cat ${{catClass}}" style="cursor:pointer;" onclick="openDrawer('motivo', '${{c.categoriaClavo}}')">${{c.categoriaClavo}}</span></td>
              <td>${{escapeHtml(c.fundamento)}}</td>
              <td><span style="font-size: 0.78rem; color: var(--text-dim);">${{c.estado}}</span></td>
            </tr>
          `;
        }}
      }});

      tbody.innerHTML = html || '<tr><td colspan="6" style="text-align:center; padding: 24px; color: var(--text-muted);">No se encontraron solicitudes con el criterio seleccionado.</td></tr>';
      document.getElementById('tableCountText').innerText = `Mostrando ${{visible}} de ${{CLAVOS.length}} clavos justificados`;
    }}

    function getCatClass(cat) {{
      if (cat.includes('Supply')) return 'cat-supply';
      if (cat.includes('Emergencia')) return 'cat-emergencia';
      if (cat.includes('Pago')) return 'cat-pago';
      if (cat.includes('Incompatible')) return 'cat-incompatible';
      if (cat.includes('Error')) return 'cat-error';
      return 'cat-invalido';
    }}

    function escapeHtml(text) {{
      if (!text) return '';
      return String(text).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }}

    // Copy Executive Summary for Slack / WhatsApp
    function copyExecutiveSummary() {{
      let msg = `*REPORTE EJECUTIVO DE AUDITORÍA OPERATIVA & NO CONVERSIÓN*\\n`;
      msg += `📅 Cierre Mensual Oficial | ArreglaTodo\\n\\n`;
      msg += `*1. BALANCE Y TASA DE CONVERSIÓN REAL:*\\n`;
      msg += `• Solicitudes Iniciales Cargadas: 581\\n`;
      msg += `• Clavos Auditados Comprobados: -66\\n`;
      msg += `• Base Válida Depurada: *515*\\n`;
      msg += `• Solicitudes Convertidas: *193* (incluye #19994 cerrada con Anthony)\\n`;
      msg += `• Tasa de Conversión Real Resultante: *37.48%* (vs 33.22% sin deducción)\\n`;
      msg += `• Tramo Oficial de Comisiones: *35.5% a 38.9% ($200 USD)*\\n\\n`;
      msg += `*2. CAUSA RAÍZ DE NO CONVERSIÓN:*\\n`;
      msg += `• Falla de Supply / Falta de Opciones: 30 casos (45.5%)\\n`;
      msg += `• Emergencias sin Cobertura Inmediata: 13 casos (19.7%)\\n`;
      msg += `• Servicios Incompatibles / Fuera de Regla: 6 casos (9.1%)\\n`;
      msg += `• Fricción por Pago Adelantado: 6 casos (9.1%)\\n`;
      msg += `• Errores Administrativos / Duplicadas: 6 casos (9.1%)\\n`;
      msg += `• Leads No Calificados (Inquilinos/Curiosos): 5 casos (7.6%)\\n\\n`;
      msg += `*3. CASOS ESTRATÉGICOS A RESOLVER (15 Doble Check):*\\n`;
      msg += `• Riogas (#19719) y ANII (#19922) pendientes de propuesta B2B.\\n`;
      msg += `• Falla en servicio Progreso (#19567) y control de precios por zona (#19684).\\n`;
      msg += `• 7 leads en seguimiento activo con potencial de rescate.\\n\\n`;
      msg += `*4. ALCANCE METODOLÓGICO:*\\n`;
      msg += `Se priorizó el foco crítico en Canceladas, Carpintería, Vidriería y Emergencias. Quedaron sin auditar las Enviadas de Limpieza, Pintura y Sanitaria, por lo que 66 clavos representa un piso conservador.\\n\\n`;
      msg += `🔗 Ver tablero completo interactivo:\\nhttps://leonmunitz.github.io/Manual-Operativo-Supply-ArreglaTodo-by-Leon/reporte.html`;

      navigator.clipboard.writeText(msg).then(() => {{
        alert('¡Resumen ejecutivo copiado al portapapeles!');
      }}).catch(() => {{
        alert('Copiado');
      }});
    }}
  </script>
</body>
</html>
'''

output_file = '/home/leondon-pc/Desktop/Manual_Operativo_Supply_ArreglaTodo/reporte.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f'Successfully created {output_file} ({os.path.getsize(output_file)} bytes)!')
