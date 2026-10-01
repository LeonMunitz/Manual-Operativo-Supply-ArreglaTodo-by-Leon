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
      z-index: 100;
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

    /* Quantitative Analytics Section */
    .analytics-section {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 36px;
    }}

    .chart-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 24px;
    }}

    .chart-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 12px;
    }}

    .chart-card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .chart-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .bar-row {{
      cursor: pointer;
      padding: 6px 8px;
      border-radius: 6px;
      transition: background 0.15s ease;
    }}
    .bar-row:hover {{
      background: rgba(255,255,255,0.03);
    }}
    .bar-row.active {{
      background: rgba(0, 180, 216, 0.12);
      border-left: 3px solid var(--accent);
    }}

    .bar-info {{
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      margin-bottom: 5px;
    }}

    .bar-track {{
      background: #1e293b;
      height: 8px;
      border-radius: 4px;
      overflow: hidden;
    }}

    .bar-fill {{
      height: 100%;
      border-radius: 4px;
      transition: width 0.6s ease;
    }}

    .fill-supply {{ background: linear-gradient(90deg, #f59e0b, #d97706); }}
    .fill-emergencia {{ background: linear-gradient(90deg, #ef4444, #b91c1c); }}
    .fill-pago {{ background: linear-gradient(90deg, #8b5cf6, #6d28d9); }}
    .fill-incompatible {{ background: linear-gradient(90deg, #64748b, #475569); }}
    .fill-error {{ background: linear-gradient(90deg, #ec4899, #be185d); }}
    .fill-invalido {{ background: linear-gradient(90deg, #06b6d4, #0891b2); }}

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

    /* Print Formatting */
    @media print {{
      header, .header-actions, .table-toolbar, .btn, .filter-pills {{
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
      .kpi-num, .chart-card-title, .conflicts-title, .scope-title {{
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

    <!-- Analytics Section (Breakdown by Rubro and Motive) -->
    <div class="analytics-section">
      
      <!-- By Rubro Chart -->
      <div class="chart-card">
        <div class="chart-card-header">
          <div class="chart-card-title">
            <span>📦 Concentración de Clavos por Rubro</span>
          </div>
          <span style="font-size: 0.75rem; color: var(--text-dim);">Haz clic para filtrar abajo</span>
        </div>
        <div class="chart-list" id="rubroChartList">
          <!-- Rendered via JS -->
        </div>
      </div>

      <!-- By Motive Chart -->
      <div class="chart-card">
        <div class="chart-card-header">
          <div class="chart-card-title">
            <span>🔍 Causa Raíz de No Conversión (Motivos)</span>
          </div>
          <span style="font-size: 0.75rem; color: var(--text-dim);">Estandarización Operativa</span>
        </div>
        <div class="chart-list" id="motivoChartList">
          <!-- Rendered via JS -->
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
          Decisiones requeridas de Dirección / Oportunidades de Negocio
        </span>
      </div>

      <div class="conflicts-grid">

        <!-- Card 1: B2B / Corporativo -->
        <div class="conflict-group-card">
          <div class="conflict-group-title">
            <span>🏢 Cuentas Corporativas & Grandes Clientes</span>
          </div>
          <div class="conflict-item">
            <div class="conflict-item-top">
              <span class="conflict-id">#19719</span>
              <span class="conflict-client">MONICA VALLARINO (Riogas) • Jardinería</span>
            </div>
            <div class="conflict-desc">"Sector de compras de Riogas. Preocupados por costos de gestión repetitivos, quizás se pueda hacer un avance con un precio preferencial."</div>
          </div>
          <div class="conflict-item">
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
          <div class="conflict-item">
            <div class="conflict-item-top">
              <span class="conflict-id">#19567</span>
              <span class="conflict-client">Gustavo Laborde • Carpintería</span>
            </div>
            <div class="conflict-desc">"Esta venta se cayó por el servicio fallido de Progreso."</div>
          </div>
          <div class="conflict-item">
            <div class="conflict-item-top">
              <span class="conflict-id">#19684</span>
              <span class="conflict-client">Paula Viola • Limpieza</span>
            </div>
            <div class="conflict-desc">"Acá se cotizó, pero luego se cambió el precio; hay que hablar este tema, porque hay un precio por zona y se debe respetar."</div>
          </div>
          <div class="conflict-item">
            <div class="conflict-item-top">
              <span class="conflict-id">#19973</span>
              <span class="conflict-client">Alicia • Aire acondicionado</span>
            </div>
            <div class="conflict-desc">"La atención fue pésima y reenviar audios de los proveedores así porque sí es un error."</div>
          </div>
          <div class="conflict-item">
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
          <div class="conflict-item">
            <div class="conflict-item-top">
              <span class="conflict-id">#20009</span>
              <span class="conflict-client">Vanina Grunberg • Jardinería</span>
            </div>
            <div class="conflict-desc">"Contactar hoy para tratar de remontar."</div>
          </div>
          <div class="conflict-item">
            <div class="conflict-item-top">
              <span class="conflict-id">#20022</span>
              <span class="conflict-client">Ignacio • Construcción</span>
            </div>
            <div class="conflict-desc">"Contactar para coordinar, quizás se pueda."</div>
          </div>
          <div class="conflict-item">
            <div class="conflict-item-top">
              <span class="conflict-id">#19877</span>
              <span class="conflict-client">Karina • Jardinería</span>
            </div>
            <div class="conflict-desc">"Para contactar el 07/10."</div>
          </div>
          <div class="conflict-item">
            <div class="conflict-item-top">
              <span class="conflict-id">#19834</span>
              <span class="conflict-client">Avalon • Carpintería</span>
            </div>
            <div class="conflict-desc">"Tratar de enviar cotización, está a nombre de Pablo Leva, seguro es la que falta de Álvaro."</div>
          </div>
          <div class="conflict-item">
            <div class="conflict-item-top">
              <span class="conflict-id">#19885 & #19975</span>
              <span class="conflict-client">Carmen Barbe / Paula Maciel</span>
            </div>
            <div class="conflict-desc">"Esperando por Germán / Hacer seguimiento a cotización."</div>
          </div>
          <div class="conflict-item">
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
          <div class="conflict-item">
            <div class="conflict-item-top">
              <span class="conflict-id">#19528</span>
              <span class="conflict-client">Bessie • Carpintería</span>
            </div>
            <div class="conflict-desc">"La venta se cayó por el pago adelantado."</div>
          </div>
          <div class="conflict-item">
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

  <script>
    const CLAVOS = {clavos_json};
    const CONFLICTOS = {conflictos_json};

    let activeFilter = 'all';

    window.addEventListener('DOMContentLoaded', () => {{
      renderRubroChart();
      renderMotivoChart();
      renderTable();
    }});

    // Render Rubro Breakdown Chart
    function renderRubroChart() {{
      const counts = {{}};
      CLAVOS.forEach(c => {{
        counts[c.rubro] = (counts[c.rubro] || 0) + 1;
      }});

      const sorted = Object.entries(counts).sort((a,b) => b[1] - a[1]);
      const max = sorted[0][1];
      const container = document.getElementById('rubroChartList');

      let html = '';
      sorted.forEach(([rubro, cnt]) => {{
        const pct = ((cnt / CLAVOS.length) * 100).toFixed(1);
        const widthPct = ((cnt / max) * 100).toFixed(1);
        html += `
          <div class="bar-row" onclick="setFilter('${{rubro}}')">
            <div class="bar-info">
              <span><strong>${{rubro}}</strong></span>
              <span style="color:var(--text-muted);">${{cnt}} clavos (${{pct}}%)</span>
            </div>
            <div class="bar-track">
              <div class="bar-fill" style="width: ${{widthPct}}%; background: var(--primary);"></div>
            </div>
          </div>
        `;
      }});
      container.innerHTML = html;
    }}

    // Render Motivo Breakdown Chart
    function renderMotivoChart() {{
      const counts = {{
        'Falla de Supply / Opciones Insuficientes': {{ cnt: 0, class: 'fill-supply' }},
        'Emergencia sin Cobertura': {{ cnt: 0, class: 'fill-emergencia' }},
        'Fricción de Pago Adelantado': {{ cnt: 0, class: 'fill-pago' }},
        'Servicio Incompatible / Fuera de Regla': {{ cnt: 0, class: 'fill-incompatible' }},
        'Error Administrativo / Duplicada': {{ cnt: 0, class: 'fill-error' }},
        'Lead No Calificado (Inquilino/Curioso)': {{ cnt: 0, class: 'fill-invalido' }}
      }};

      CLAVOS.forEach(c => {{
        const cat = c.categoriaClavo || 'Falla de Supply / Opciones Insuficientes';
        if (counts[cat]) counts[cat].cnt++;
        else counts['Falla de Supply / Opciones Insuficientes'].cnt++;
      }});

      const sorted = Object.entries(counts).sort((a,b) => b[1].cnt - a[1].cnt);
      const max = sorted[0][1].cnt;
      const container = document.getElementById('motivoChartList');

      let html = '';
      sorted.forEach(([cat, data]) => {{
        const cnt = data.cnt;
        const pct = ((cnt / CLAVOS.length) * 100).toFixed(1);
        const widthPct = ((cnt / max) * 100).toFixed(1);
        html += `
          <div class="bar-row" onclick="setFilter('${{cat}}')">
            <div class="bar-info">
              <span><strong>${{cat}}</strong></span>
              <span style="color:var(--text-muted);">${{cnt}} casos (${{pct}}%)</span>
            </div>
            <div class="bar-track">
              <div class="bar-fill ${{data.class}}" style="width: ${{widthPct}}%;"></div>
            </div>
          </div>
        `;
      }});
      container.innerHTML = html;
    }}

    // Filter Logic
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

    // Render Table
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
              <td><span class="badge-rubro">${{escapeHtml(c.rubro)}}</span></td>
              <td><span class="badge-cat ${{catClass}}">${{c.categoriaClavo}}</span></td>
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
