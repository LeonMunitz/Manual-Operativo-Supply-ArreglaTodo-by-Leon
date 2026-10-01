import json
import os

with open('/home/leondon-pc/Desktop/Manual_Operativo_Supply_ArreglaTodo/assets/datos_solicitudes_auditadas.json', 'r', encoding='utf-8') as f:
    initial_data = json.load(f)

json_str = json.dumps(initial_data, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sistema de Auditoría & Clavos - ArreglaTodo</title>
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
      --primary-glow: rgba(255, 107, 53, 0.2);
      --accent: #00b4d8;
      --accent-glow: rgba(0, 180, 216, 0.2);
      --success: #10b981;
      --success-bg: rgba(16, 185, 129, 0.14);
      --warning: #f59e0b;
      --warning-bg: rgba(245, 158, 11, 0.14);
      --danger: #ef4444;
      --danger-bg: rgba(239, 68, 68, 0.18);
      --purple: #8b5cf6;
      --purple-bg: rgba(139, 92, 246, 0.14);
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

    /* Header */
    header {{
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }}

    .logo-area {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .badge-villano {{
      background: linear-gradient(135deg, #ef4444, #ff6b35);
      color: white;
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1px;
      padding: 4px 10px;
      border-radius: 20px;
      box-shadow: 0 0 12px rgba(239, 68, 68, 0.4);
    }}

    .logo-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #fff;
    }}

    .header-actions {{
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
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
      box-shadow: 0 0 15px var(--primary-glow);
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

    .btn-success {{
      background: var(--success);
      color: white;
    }}
    .btn-success:hover {{
      filter: brightness(1.1);
    }}

    .btn-danger {{
      background: var(--danger);
      color: white;
    }}

    .btn-gold {{
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: white;
      border-color: #fbbf24;
    }}
    .btn-gold:hover {{
      box-shadow: 0 0 15px rgba(251, 191, 36, 0.3);
    }}

    /* Main Container */
    .container {{
      max-width: 1600px;
      width: 100%;
      margin: 0 auto;
      padding: 20px 24px;
      flex: 1;
    }}

    /* Maximizer Hero Section */
    .hero-maximizer {{
      background: linear-gradient(135deg, #161e2e 0%, #1a1528 50%, #1e131d 100%);
      border: 1px solid var(--border-light);
      border-radius: 14px;
      padding: 20px 24px;
      margin-bottom: 24px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 24px;
      position: relative;
      overflow: hidden;
    }}

    .hero-maximizer::before {{
      content: '';
      position: absolute;
      top: -50px;
      right: -50px;
      width: 200px;
      height: 200px;
      background: radial-gradient(circle, rgba(255, 107, 53, 0.15) 0%, transparent 70%);
      pointer-events: none;
    }}

    .maximizer-left {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .maximizer-title-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}

    .maximizer-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-light);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .stats-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 16px;
    }}

    .stat-box {{
      background: rgba(10, 13, 20, 0.7);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 12px;
      text-align: center;
    }}

    .stat-label {{
      font-size: 0.75rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }}

    .stat-val {{
      font-size: 1.6rem;
      font-weight: 800;
      color: #fff;
    }}

    .stat-val.rate {{
      color: var(--accent);
    }}

    .stat-val.usd {{
      color: var(--success);
      text-shadow: 0 0 10px rgba(16, 185, 129, 0.3);
    }}

    .stat-val.clavos {{
      color: var(--gold);
    }}

    .progress-container {{
      background: rgba(10, 13, 20, 0.8);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 14px 16px;
    }}

    .progress-header {{
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      margin-bottom: 8px;
    }}

    .progress-track {{
      background: #243047;
      height: 12px;
      border-radius: 6px;
      overflow: hidden;
      position: relative;
    }}

    .progress-fill {{
      background: linear-gradient(90deg, var(--accent) 0%, var(--success) 100%);
      height: 100%;
      border-radius: 6px;
      transition: width 0.4s ease;
      width: 0%;
    }}

    .progress-next-tip {{
      margin-top: 8px;
      font-size: 0.82rem;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .progress-next-tip strong {{
      color: var(--gold);
    }}

    /* Maximizer Right (Scale reference & controls) */
    .maximizer-right {{
      background: rgba(10, 13, 20, 0.5);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .scale-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .scale-list {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      font-size: 0.78rem;
    }}

    .scale-item {{
      display: flex;
      justify-content: space-between;
      padding: 4px 8px;
      border-radius: 4px;
      background: rgba(255,255,255,0.02);
    }}

    .scale-item.active {{
      background: rgba(16, 185, 129, 0.2);
      border: 1px solid var(--success);
      font-weight: 700;
      color: #fff;
    }}

    .scale-item.next {{
      background: rgba(251, 191, 36, 0.15);
      border: 1px dashed var(--gold);
      color: var(--gold);
    }}

    /* Status Counters Strip */
    .status-strip {{
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      gap: 12px;
      margin-bottom: 24px;
    }}

    .kpi-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 12px;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s ease;
      position: relative;
    }}

    .kpi-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      border-color: var(--border-light);
    }}

    .kpi-card.active {{
      border-color: var(--accent);
      background: var(--bg-card-hover);
      box-shadow: 0 0 10px var(--accent-glow);
    }}

    .kpi-card-title {{
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 4px;
    }}

    .kpi-card-num {{
      font-size: 1.5rem;
      font-weight: 800;
      line-height: 1;
    }}

    /* Card Status Color Themes matching screenshot */
    .kpi-pendientes {{ border-top: 3px solid #f87171; }}
    .kpi-pendientes .kpi-card-title {{ color: #f87171; }}
    .kpi-enviadas {{ border-top: 3px solid #fbbf24; }}
    .kpi-enviadas .kpi-card-title {{ color: #fbbf24; }}
    .kpi-aceptadas {{ border-top: 3px solid #34d399; }}
    .kpi-aceptadas .kpi-card-title {{ color: #34d399; }}
    .kpi-pago-pendiente {{ border-top: 3px solid #c084fc; }}
    .kpi-pago-pendiente .kpi-card-title {{ color: #c084fc; }}
    .kpi-completadas {{ border-top: 3px solid #60a5fa; }}
    .kpi-completadas .kpi-card-title {{ color: #60a5fa; }}
    .kpi-canceladas {{ border-top: 3px solid #f472b6; }}
    .kpi-canceladas .kpi-card-title {{ color: #f472b6; }}
    .kpi-clavos {{ border-top: 3px solid #eab308; background: rgba(234, 179, 8, 0.05); }}
    .kpi-clavos .kpi-card-title {{ color: #eab308; }}
    .kpi-conflicto {{ border-top: 3px solid #ef4444; background: rgba(239, 68, 68, 0.08); }}
    .kpi-conflicto .kpi-card-title {{ color: #ef4444; }}

    /* Pulsing Conflict Animation */
    .pulse-danger {{
      animation: pulseRed 2s infinite;
    }}
    @keyframes pulseRed {{
      0% {{ box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.5); }}
      70% {{ box-shadow: 0 0 0 8px rgba(239, 68, 68, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }}
    }}

    /* Main Tab Navigation */
    .tabs-nav {{
      display: flex;
      gap: 4px;
      border-bottom: 1px solid var(--border-color);
      margin-bottom: 20px;
    }}

    .tab-btn {{
      padding: 10px 18px;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-muted);
      background: transparent;
      border: none;
      border-bottom: 3px solid transparent;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}

    .tab-btn:hover {{
      color: var(--text-main);
      background: rgba(255,255,255,0.02);
    }}

    .tab-btn.active {{
      color: var(--primary);
      border-bottom-color: var(--primary);
      background: rgba(255, 107, 53, 0.05);
    }}

    .tab-badge {{
      background: #243047;
      color: #fff;
      font-size: 0.72rem;
      padding: 2px 7px;
      border-radius: 12px;
      font-weight: 700;
    }}

    .tab-badge.badge-danger {{
      background: var(--danger);
    }}

    .tab-badge.badge-gold {{
      background: var(--gold);
      color: #000;
    }}

    /* Filter Controls Toolbar */
    .toolbar {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 14px 18px;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .search-box {{
      flex: 1;
      min-width: 250px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px 12px 8px 36px;
      color: var(--text-main);
      font-size: 0.88rem;
    }}

    .search-input:focus {{
      outline: none;
      border-color: var(--accent);
      box-shadow: 0 0 8px var(--accent-glow);
    }}

    .search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 0.9rem;
    }}

    .filters-group {{
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }}

    .select-filter {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px 12px;
      color: var(--text-main);
      font-size: 0.85rem;
      cursor: pointer;
    }}

    .select-filter:focus {{
      outline: none;
      border-color: var(--accent);
    }}

    /* Table Styling */
    .table-container {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      overflow-x: auto;
      box-shadow: 0 4px 16px rgba(0,0,0,0.2);
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
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-color);
      font-weight: 700;
      white-space: nowrap;
    }}

    td {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-color);
      vertical-align: middle;
    }}

    tr:hover td {{
      background: rgba(255,255,255,0.02);
    }}

    /* Conflict & Clavo Row Highlights */
    tr.row-conflict td {{
      background: rgba(239, 68, 68, 0.16) !important;
      border-top: 1px solid #ef4444;
      border-bottom: 1px solid #ef4444;
    }}

    tr.row-clavo td {{
      background: rgba(234, 179, 8, 0.08) !important;
    }}

    .badge-id {{
      font-family: monospace;
      font-weight: 700;
      font-size: 0.85rem;
      color: var(--primary-light);
    }}

    .badge-rubro {{
      background: #1f2b42;
      color: #93c5fd;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.78rem;
      font-weight: 600;
      border: 1px solid #2e4368;
    }}

    .phone-cell {{
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }}

    .btn-copy-phone {{
      background: #1f2b42;
      color: #93c5fd;
      border: 1px solid #2e4368;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .btn-copy-phone:hover {{
      background: #253754;
      color: #fff;
      border-color: var(--accent);
    }}
    .btn-copy-phone.copied {{
      background: var(--success);
      color: #fff;
      border-color: var(--success);
    }}

    .btn-copy {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 3px 6px;
      border-radius: 4px;
      font-size: 0.72rem;
      cursor: pointer;
    }}
    .btn-copy:hover {{
      color: #fff;
      border-color: var(--border-light);
    }}

    .status-select {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
    }}

    .check-cell {{
      text-align: center;
      min-width: 90px;
    }}

    .custom-checkbox {{
      width: 18px;
      height: 18px;
      cursor: pointer;
      accent-color: var(--primary);
    }}

    .custom-checkbox.clavo-box {{
      accent-color: var(--gold);
    }}

    .custom-checkbox.noclavo-box {{
      accent-color: var(--accent);
    }}

    .fundamento-input {{
      width: 100%;
      min-width: 280px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 6px 10px;
      color: var(--text-main);
      font-size: 0.83rem;
      transition: all 0.2s ease;
    }}

    .fundamento-input:focus {{
      outline: none;
      border-color: var(--primary);
      background: #111723;
    }}

    .conflict-warning-tag {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: #ef4444;
      color: white;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      margin-left: 6px;
      text-transform: uppercase;
    }}

    /* Dossier / Report View */
    .dossier-container {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 30px;
    }}

    .dossier-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 20px;
      margin-bottom: 24px;
    }}

    .dossier-title {{
      font-size: 1.6rem;
      font-weight: 800;
      color: #fff;
    }}

    .dossier-subtitle {{
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-top: 4px;
    }}

    .dossier-actions {{
      display: flex;
      gap: 10px;
    }}

    .dossier-summary-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 30px;
    }}

    .dossier-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 16px;
      text-align: center;
    }}

    .dossier-box-title {{
      font-size: 0.78rem;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 700;
    }}

    .dossier-box-num {{
      font-size: 2rem;
      font-weight: 800;
      color: #fff;
      margin-top: 6px;
    }}

    /* Modal Styling */
    .modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.75);
      backdrop-filter: blur(4px);
      z-index: 200;
      align-items: center;
      justify-content: center;
    }}

    .modal-overlay.open {{
      display: flex;
    }}

    .modal-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-light);
      border-radius: 14px;
      width: 90%;
      max-width: 700px;
      max-height: 90vh;
      overflow-y: auto;
      padding: 24px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.6);
    }}

    .modal-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .close-modal {{
      background: none;
      border: none;
      color: var(--text-dim);
      font-size: 1.5rem;
      cursor: pointer;
    }}
    .close-modal:hover {{
      color: #fff;
    }}

    .textarea-paste {{
      width: 100%;
      height: 250px;
      background: var(--bg-base);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px;
      color: var(--text-main);
      font-family: monospace;
      font-size: 0.85rem;
      resize: vertical;
      margin-bottom: 16px;
    }}

    .textarea-paste:focus {{
      outline: none;
      border-color: var(--accent);
    }}

    .form-group {{
      margin-bottom: 16px;
    }}

    .form-group label {{
      display: block;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 6px;
      font-weight: 600;
    }}

    .form-input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px 12px;
      color: #fff;
      font-size: 0.9rem;
    }}

    /* Toast Notification */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--bg-card);
      border: 1px solid var(--border-light);
      padding: 12px 20px;
      border-radius: 10px;
      font-size: 0.88rem;
      font-weight: 600;
      color: #fff;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 300;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .toast.show {{
      transform: translateY(0);
      opacity: 1;
    }}

    .toast-success {{ border-left: 4px solid var(--success); }}
    .toast-info {{ border-left: 4px solid var(--accent); }}
    .toast-warning {{ border-left: 4px solid var(--warning); }}

    /* Print media styling */
    @media print {{
      header, .hero-maximizer, .status-strip, .tabs-nav, .toolbar, .dossier-actions, .toast {{
        display: none !important;
      }}
      body, .container, .dossier-container {{
        background: #fff !important;
        color: #000 !important;
        padding: 0 !important;
      }}
      .dossier-box {{
        border: 1px solid #ccc !important;
        background: #f9f9f9 !important;
      }}
      .dossier-box-title, .dossier-subtitle {{
        color: #555 !important;
      }}
      .dossier-box-num, .dossier-title {{
        color: #000 !important;
      }}
      table {{
        border: 1px solid #ddd !important;
      }}
      th {{
        background: #eee !important;
        color: #000 !important;
        border-bottom: 2px solid #333 !important;
      }}
      td {{
        border-bottom: 1px solid #ddd !important;
        color: #111 !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Header Navigation -->
  <header>
    <div class="logo-area">
      <span class="badge-villano">Auditoría Supply</span>
      <div class="logo-title">Seguimiento de Solicitudes & Clavos</div>
    </div>
    <div class="header-actions">
      <a href="index.html" class="btn btn-secondary" title="Volver al Manual">📖 Manual Operativo</a>
      <a href="reporte.html" class="btn btn-gold" title="Abrir Reporte Ejecutivo para Jefes" style="background: linear-gradient(135deg, #f59e0b, #d97706); color:white; border-color:#fbbf24;">📊 Reporte para Jefes</a>
      <button class="btn btn-primary" onclick="openPasteModal()">📋 Pegar Texto Directo</button>
      <button class="btn btn-secondary" onclick="exportJSON()">💾 Exportar Backup</button>
      <button class="btn btn-secondary" onclick="exportCSV()">📊 Exportar Excel</button>
      <button class="btn btn-secondary" onclick="document.getElementById('importFile').click()">📥 Importar</button>
      <input type="file" id="importFile" style="display:none;" accept=".json" onchange="importJSON(event)">
      <button class="btn btn-secondary" onclick="openSettingsModal()" title="Configuración de Base">⚙️</button>
    </div>
  </header>

  <div class="container">

    <!-- Hero Maximizer: Calculador de Comisiones en Tiempo Real -->
    <div class="hero-maximizer">
      <div class="maximizer-left">
        <div class="maximizer-title-row">
          <div class="maximizer-title">
            <span>🎯 Calculadora de Incentivo & Tasa de Conversión</span>
          </div>
          <button class="btn btn-secondary" style="padding: 4px 10px; font-size: 0.75rem;" onclick="openSettingsModal()">⚙️ Configurar Base</button>
        </div>

        <div class="stats-highlight-grid">
          <div class="stat-box">
            <div class="stat-label">Total Mes Válido</div>
            <div class="stat-val" id="statTotalValido">581</div>
            <div style="font-size:0.72rem; color:var(--text-dim);" id="statBaseDeduccion">Base: 581 - 0 clavos</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Convertidas</div>
            <div class="stat-val" id="statConvertidas">192</div>
            <div style="font-size:0.72rem; color:var(--text-dim);" id="statConvertidasDetalle">Acep + Comp</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">% Conversión</div>
            <div class="stat-val rate" id="statTasaConversion">33.05%</div>
            <div style="font-size:0.72rem; color:var(--text-dim);" id="statTasaIncremento">Base inicial: 33.05%</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Incentivo Actual</div>
            <div class="stat-val usd" id="statIncentivoUSD">$150 USD</div>
            <div style="font-size:0.72rem; color:var(--text-dim);" id="statTramoNombre">Tramo 32% - 35.4%</div>
          </div>
        </div>

        <!-- Progress to Next Tier -->
        <div class="progress-container">
          <div class="progress-header">
            <span id="progressCurrentStatus">Progreso hacia el siguiente escalón</span>
            <span id="progressTargetText">Meta: 35.5% ($200 USD)</span>
          </div>
          <div class="progress-track">
            <div class="progress-fill" id="progressFillBar" style="width: 30%;"></div>
          </div>
          <div class="progress-next-tip">
            <span id="progressTipClavos">Te faltan <strong>41 clavos aprobados</strong> para alcanzar el 35.5% y cobrar <strong>$200 USD (+50 USD)</strong>.</span>
            <span style="font-size: 0.75rem; color: var(--accent);" id="progressProximoPremio">Próximo salto: +$50 USD</span>
          </div>
        </div>
      </div>

      <!-- Reference Scale Box -->
      <div class="maximizer-right">
        <div class="scale-title">
          <span>Escala Oficial de Comisiones</span>
          <span style="font-size: 0.72rem; color: var(--gold);">WhatsApp Ref.</span>
        </div>
        <div class="scale-list">
          <div class="scale-item" id="tier-0"><span>&lt; 32.0%</span> <strong>0 USD</strong></div>
          <div class="scale-item active" id="tier-1"><span>32.0% a 35.4%</span> <strong>150 USD</strong></div>
          <div class="scale-item next" id="tier-2"><span>35.5% a 38.9%</span> <strong>200 USD</strong></div>
          <div class="scale-item" id="tier-3"><span>39.0% a 42.4%</span> <strong>250 USD</strong></div>
          <div class="scale-item" id="tier-4"><span>42.5% a 46.0%</span> <strong>300 USD</strong></div>
          <div class="scale-item" id="tier-5"><span>Cada +3.5% adicional</span> <strong>+50 USD</strong></div>
        </div>
        <div style="margin-top: 8px; font-size: 0.7rem; color: var(--text-dim); text-align: center;">
          * Cada clavo detectado y aprobado reduce el denominador y eleva la conversión.
        </div>
      </div>
    </div>

    <!-- Status KPI Cards (Matching screenshot 2026-09-30_21-00.png) -->
    <div class="status-strip">
      <div class="kpi-card kpi-pendientes" onclick="filterByStateCard('Pendientes')">
        <div class="kpi-card-title">Pendientes</div>
        <div class="kpi-card-num" id="kpiPendientes">3</div>
      </div>
      <div class="kpi-card kpi-enviadas" onclick="filterByStateCard('Enviadas')">
        <div class="kpi-card-title">Enviadas</div>
        <div class="kpi-card-num" id="kpiEnviadas">251</div>
      </div>
      <div class="kpi-card kpi-aceptadas" onclick="filterByStateCard('Aceptadas')">
        <div class="kpi-card-title">Aceptadas</div>
        <div class="kpi-card-num" id="kpiAceptadas">73</div>
      </div>
      <div class="kpi-card kpi-pago-pendiente" onclick="filterByStateCard('Pago Pendiente')">
        <div class="kpi-card-title">Pago Pendiente</div>
        <div class="kpi-card-num" id="kpiPagoPendiente">19</div>
      </div>
      <div class="kpi-card kpi-completadas" onclick="filterByStateCard('Completadas')">
        <div class="kpi-card-title">Completadas</div>
        <div class="kpi-card-num" id="kpiCompletadas">119</div>
      </div>
      <div class="kpi-card kpi-canceladas" onclick="filterByStateCard('Canceladas')">
        <div class="kpi-card-title">Canceladas</div>
        <div class="kpi-card-num" id="kpiCanceladas">116</div>
      </div>
      <div class="kpi-card kpi-clavos" onclick="filterByCondition('clavos')">
        <div class="kpi-card-title">📌 Clavos</div>
        <div class="kpi-card-num" id="kpiClavos">0</div>
      </div>
      <div class="kpi-card kpi-conflicto" id="kpiConflictoCard" onclick="switchTab('conflicto')">
        <div class="kpi-card-title">⚠️ A Revisar</div>
        <div class="kpi-card-num" id="kpiConflicto">0</div>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" id="tabBtn-gestion" onclick="switchTab('gestion')">
        📋 Gestión y Auditoría <span class="tab-badge" id="badgeTotalSolicitudes">389</span>
      </button>
      <button class="tab-btn" id="tabBtn-conflicto" onclick="switchTab('conflicto')">
        ⚠️ A Revisar (Jefe) <span class="tab-badge badge-danger" id="badgeConflictoTab">0</span>
      </button>
      <button class="tab-btn" id="tabBtn-dossier" onclick="switchTab('dossier')">
        ⚖️ Dossier de Clavos (Para Jefe) <span class="tab-badge badge-gold" id="badgeDossierClavos">0</span>
      </button>
      <button class="tab-btn" id="tabBtn-historial" onclick="switchTab('historial')">
        📑 Historial de Lotes / Reportes
      </button>
    </div>

    <!-- TAB 1: Gestión y Auditoría (Tabla Principal) -->
    <div id="tabContent-gestion">
      <div class="toolbar">
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input type="text" class="search-input" id="tableSearch" placeholder="Buscar por ID, Cliente, Rubro, Teléfono o Fundamento..." oninput="applyFilters()">
        </div>
        <div class="filters-group">
          <select class="select-filter" id="filterRubro" onchange="applyFilters()">
            <option value="">Todos los Rubros</option>
          </select>
          <select class="select-filter" id="filterEstado" onchange="applyFilters()">
            <option value="">Todos los Estados</option>
            <option value="Pendientes">Pendientes</option>
            <option value="Enviadas">Enviadas</option>
            <option value="Aceptadas">Aceptadas</option>
            <option value="Pago Pendiente">Pago Pendiente</option>
            <option value="Completadas">Completadas</option>
            <option value="Canceladas">Canceladas</option>
          </select>
          <select class="select-filter" id="filterClavoCond" onchange="applyFilters()">
            <option value="">Todos (Clavos y No Clavos)</option>
            <option value="clavos">Solo Clavos Marcados</option>
            <option value="noclavo">Solo "No es Clavo"</option>
            <option value="conflicto">Solo Conflictos (Doble Check)</option>
            <option value="sinmarcar">Sin Marcar</option>
          </select>
          <button class="btn btn-secondary" onclick="resetFilters()">↺ Limpiar Filtros</button>
        </div>
      </div>

      <div style="margin-bottom: 10px; display: flex; justify-content: space-between; font-size: 0.82rem; color: var(--text-muted);">
        <span id="filteredCountInfo">Mostrando 389 solicitudes</span>
        <span>Tip: Marca los dos checks a la vez para enviar el caso directamente a <strong>A Revisar por Jefe</strong> en rojo.</span>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th style="width: 75px;">ID</th>
              <th style="width: 170px;">Cliente</th>
              <th style="width: 140px;">Rubro</th>
              <th style="width: 170px;">Teléfono</th>
              <th style="width: 150px;">Estado</th>
              <th class="check-cell" title="Si solo está marcado, no cuenta">No es Clavo</th>
              <th class="check-cell" title="Si solo está marcado, se descuenta de la base">Es Clavo</th>
              <th>Fundamento / Qué pasó (Texto Libre)</th>
              <th style="width: 70px; text-align: center;">Acción</th>
            </tr>
          </thead>
          <tbody id="solicitudesTableBody">
            <!-- Rows rendered dynamically -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 2: A Revisar (Jefe) -->
    <div id="tabContent-conflicto" style="display:none;">
      <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; border-radius: 10px; padding: 18px 24px; margin-bottom: 20px;">
        <h3 style="color: #ef4444; margin-bottom: 6px;">⚠️ Panel de Casos a Revisar por el Jefe</h3>
        <p style="font-size: 0.88rem; color: var(--text-main);">
          En esta vista se aíslan automáticamente todas las solicitudes donde se marcaron <strong>ambos casilleros (No es Clavo y Es Clavo)</strong> a la vez, o que requieren arbitraje directo de tu jefe. Con los botones rápidos tu jefe puede aprobar el clavo o descartarlo con un solo clic.
        </p>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th style="width: 80px;">ID</th>
              <th style="width: 180px;">Cliente</th>
              <th style="width: 140px;">Rubro</th>
              <th style="width: 160px;">Teléfono</th>
              <th style="width: 150px;">Estado</th>
              <th>Fundamento / Detalle Registrado</th>
              <th style="width: 230px; text-align: center;">Resolución Directa del Jefe</th>
            </tr>
          </thead>
          <tbody id="conflictTableBody">
            <!-- Conflict rows rendered dynamically -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 3: Dossier de Clavos para el Jefe -->
    <div id="tabContent-dossier" style="display:none;">
      <div class="dossier-container">
        <div class="dossier-header">
          <div>
            <div class="dossier-title">Informe Formal de Deducción de Clavos</div>
            <div class="dossier-subtitle">Fundamentación de Solicitudes Inválidas y Ajuste de Base Mensual</div>
          </div>
          <div class="dossier-actions">
            <button class="btn btn-secondary" onclick="window.print()">🖨️ Imprimir / Guardar PDF</button>
            <button class="btn btn-primary" onclick="copyDossierSummary()">📋 Copiar Resumen</button>
          </div>
        </div>

        <div class="dossier-summary-grid">
          <div class="dossier-box">
            <div class="dossier-box-title">Total Solicitudes Inicial</div>
            <div class="dossier-box-num" id="dossierTotalBase">581</div>
          </div>
          <div class="dossier-box">
            <div class="dossier-box-title">Clavos Auditados a Deducir</div>
            <div class="dossier-box-num" style="color: var(--gold);" id="dossierTotalClavos">-0</div>
          </div>
          <div class="dossier-box">
            <div class="dossier-box-title">Base Neta Aprobada</div>
            <div class="dossier-box-num" style="color: var(--accent);" id="dossierBaseAprobada">581</div>
          </div>
          <div class="dossier-box">
            <div class="dossier-box-title">Tasa de Conversión Final</div>
            <div class="dossier-box-num" style="color: var(--success);" id="dossierTasaFinal">33.05%</div>
          </div>
        </div>

        <h4 style="margin-bottom: 14px; color: var(--primary-light);">Detalle de Clavos Justificados para Aprobación</h4>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width: 80px;">ID</th>
                <th style="width: 180px;">Cliente</th>
                <th style="width: 140px;">Rubro</th>
                <th style="width: 160px;">Teléfono</th>
                <th style="width: 140px;">Estado</th>
                <th>Justificación Inobjetable (Fundamento)</th>
              </tr>
            </thead>
            <tbody id="dossierTableBody">
              <!-- Clavos rows rendered dynamically -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB 4: Historial de Reportes / Lotes -->
    <div id="tabContent-historial" style="display:none;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px;">
        <div>
          <h3 style="color: #fff;">Historial de Lotes y Reportes Mensuales</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted);">Guarda una foto o snapshot del mes analizado para tener constancia de comisiones pasadas.</p>
        </div>
        <button class="btn btn-gold" onclick="saveCurrentBatchSnapshot()">📸 Guardar Snapshot de este Mes</button>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Fecha Guardado</th>
              <th>Nombre del Lote</th>
              <th>Base Inicial</th>
              <th>Clavos Aprobados</th>
              <th>Base Neta</th>
              <th>Convertidas</th>
              <th>Conversión Final</th>
              <th>Incentivo Cobrado</th>
              <th style="text-align: center;">Acciones</th>
            </tr>
          </thead>
          <tbody id="historyTableBody">
            <!-- History rows rendered dynamically -->
          </tbody>
        </table>
      </div>
    </div>

  </div>

  <!-- MODAL: Pegar Texto Directo con Limpieza Inteligente -->
  <div class="modal-overlay" id="modalPaste">
    <div class="modal-card">
      <div class="modal-title">
        <span>📋 Pegar Texto Directo con Limpieza Automática</span>
        <button class="close-modal" onclick="closePasteModal()">&times;</button>
      </div>
      <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 12px;">
        Pega aquí el texto copiado de tu sistema o archivo. El limpiador inteligente extraerá IDs (#12345), clientes, rubros y teléfonos, omitiendo automáticamente fechas (`09-30`), tiempos transcurridos (`hace 10h`), y emoticones.
      </p>
      <textarea class="textarea-paste" id="pasteRawText" placeholder="Ejemplo:
Pendientes
#19715
Diego
Vidriería
📞 59896339883
🕐 hace 19d
09-11
ℹ️ Más info..."></textarea>
      
      <div class="form-group">
        <label>Modo de Importación:</label>
        <select class="form-input" id="pasteImportMode">
          <option value="replace">Reemplazar todas las solicitudes actuales</option>
          <option value="append">Agregar al final de las solicitudes existentes</option>
        </select>
      </div>

      <div style="display: flex; justify-content: flex-end; gap: 10px;">
        <button class="btn btn-secondary" onclick="closePasteModal()">Cancelar</button>
        <button class="btn btn-primary" onclick="processPastedText()">Procesar y Limpiar Texto</button>
      </div>
    </div>
  </div>

  <!-- MODAL: Configuración de Base Mensual -->
  <div class="modal-overlay" id="modalSettings">
    <div class="modal-card" style="max-width: 500px;">
      <div class="modal-title">
        <span>⚙️ Configurar Base Mensual para Comisiones</span>
        <button class="close-modal" onclick="closeSettingsModal()">&times;</button>
      </div>
      <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 16px;">
        Ajusta los números globales del mes para que la tasa de conversión y el cobro de incentivos se calculen con exactitud matemática.
      </p>

      <div class="form-group">
        <label>Total Solicitudes del Mes (Denominador Base):</label>
        <input type="number" class="form-input" id="settingTotalMes" value="581">
      </div>
      <div class="form-group">
        <label>Solicitudes Convertidas (Aceptadas + Completadas):</label>
        <input type="number" class="form-input" id="settingConvertidas" value="193">
      </div>
      <div class="form-group">
        <label>Aceptadas del Mes (informativo):</label>
        <input type="number" class="form-input" id="settingAceptadas" value="73">
      </div>
      <div class="form-group">
        <label>Completadas del Mes (informativo):</label>
        <input type="number" class="form-input" id="settingCompletadas" value="119">
      </div>

      <div style="display: flex; justify-content: space-between; margin-top: 24px;">
        <button class="btn btn-danger" onclick="resetToInitialDefaults()">↺ Restaurar Datos Iniciales</button>
        <div style="display: flex; gap: 8px;">
          <button class="btn btn-secondary" onclick="closeSettingsModal()">Cancelar</button>
          <button class="btn btn-primary" onclick="saveSettings()">Guardar Cambios</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div class="toast" id="toastMessage">Guardado automáticamente</div>

  <!-- APPLICATION JAVASCRIPT LOGIC -->
  <script>
    // Embedded Initial Data (parsed from Untitled document.txt)
    const INITIAL_RECORDS = {json_str};

    // Application State
    let AppState = {{
      records: [],
      monthlySettings: {{
        totalMes: 581,
        convertidas: 193,
        aceptadas: 73,
        completadas: 119
      }},
      historySnapshots: []
    }};

    // Commission Scale (from official WhatsApp table)
    const COMMISSION_TIERS = [
      {{ id: 'tier-0', min: 0, max: 31.999, usd: 0, label: 'Menos de 32%' }},
      {{ id: 'tier-1', min: 32.0, max: 35.499, usd: 150, label: '32% a 35.4%' }},
      {{ id: 'tier-2', min: 35.5, max: 38.999, usd: 200, label: '35.5% a 38.9%' }},
      {{ id: 'tier-3', min: 39.0, max: 42.499, usd: 250, label: '39% a 42.4%' }},
      {{ id: 'tier-4', min: 42.5, max: 46.0, usd: 300, label: '42.5% a 46%' }}
    ];

    // Current View / Active Tab
    let currentTab = 'gestion';

    // Initialize App on Load
    window.addEventListener('DOMContentLoaded', () => {{
      loadState();
      populateRubrosFilter();
      renderAll();
    }});

    // Load from LocalStorage or Fallback to Initial Data
    function loadState() {{
      try {{
        const savedRecords = localStorage.getItem('arreglatodo_auditoria_records');
        const savedSettings = localStorage.getItem('arreglatodo_auditoria_settings');
        const savedHistory = localStorage.getItem('arreglatodo_auditoria_history');

        if (savedRecords) {{
          AppState.records = JSON.parse(savedRecords);
        }} else {{
          AppState.records = JSON.parse(JSON.stringify(INITIAL_RECORDS));
        }}

        if (savedSettings) {{
          AppState.monthlySettings = JSON.parse(savedSettings);
        }}

        if (savedHistory) {{
          AppState.historySnapshots = JSON.parse(savedHistory);
        }}
      }} catch (e) {{
        console.error('Error loading state:', e);
        AppState.records = JSON.parse(JSON.stringify(INITIAL_RECORDS));
      }}
    }}

    // Auto-save State to LocalStorage
    function persistState(showToastNotice = true) {{
      try {{
        localStorage.setItem('arreglatodo_auditoria_records', JSON.stringify(AppState.records));
        localStorage.setItem('arreglatodo_auditoria_settings', JSON.stringify(AppState.monthlySettings));
        localStorage.setItem('arreglatodo_auditoria_history', JSON.stringify(AppState.historySnapshots));
        if (showToastNotice) {{
          showToast('Guardado automáticamente en el navegador', 'success');
        }}
      }} catch (e) {{
        console.error('Error saving state:', e);
      }}
    }}

    // Render Everything
    function renderAll() {{
      updateCalculators();
      renderTable();
      renderConflicts();
      renderDossier();
      renderHistory();
      updateRubroFilterOptions();
    }}

    // Calculate Conversion, Tiers & Incentives
    function updateCalculators() {{
      let clavosValidosCount = 0;
      let conflictCount = 0;
      const statusCounts = {{
        'Pendientes': 0,
        'Enviadas': 0,
        'Aceptadas': AppState.monthlySettings.aceptadas || 73,
        'Pago Pendiente': 0,
        'Completadas': AppState.monthlySettings.completadas || 119,
        'Canceladas': 0
      }};

      AppState.records.forEach(r => {{
        // Conflict Check (both checkboxes marked)
        if (r.noEsClavo && r.esClavo) {{
          conflictCount++;
        }} else if (r.esClavo) {{
          clavosValidosCount++;
        }}

        if (statusCounts[r.estado] !== undefined) {{
          // for loaded records
          if (r.estado !== 'Aceptadas' && r.estado !== 'Completadas') {{
            statusCounts[r.estado]++;
          }}
        }}
      }});

      // KPIs
      document.getElementById('kpiPendientes').innerText = statusCounts['Pendientes'];
      document.getElementById('kpiEnviadas').innerText = statusCounts['Enviadas'];
      document.getElementById('kpiAceptadas').innerText = statusCounts['Aceptadas'];
      document.getElementById('kpiPagoPendiente').innerText = statusCounts['Pago Pendiente'];
      document.getElementById('kpiCompletadas').innerText = statusCounts['Completadas'];
      document.getElementById('kpiCanceladas').innerText = statusCounts['Canceladas'];
      document.getElementById('kpiClavos').innerText = clavosValidosCount;
      document.getElementById('kpiConflicto').innerText = conflictCount;

      // Pulsing conflict indicator
      const confCard = document.getElementById('kpiConflictoCard');
      if (conflictCount > 0) {{
        confCard.classList.add('pulse-danger');
      }} else {{
        confCard.classList.remove('pulse-danger');
      }}

      // Badges in tabs
      document.getElementById('badgeTotalSolicitudes').innerText = AppState.records.length;
      document.getElementById('badgeConflictoTab').innerText = conflictCount;
      document.getElementById('badgeDossierClavos').innerText = clavosValidosCount;

      // Mathematical formulas
      const totalBase = AppState.monthlySettings.totalMes;
      const convertidas = AppState.monthlySettings.convertidas;
      const baseValida = Math.max(1, totalBase - clavosValidosCount);
      const conversionRate = (convertidas / baseValida) * 100;
      const initialRate = (convertidas / totalBase) * 100;
      const rateIncrement = conversionRate - initialRate;

      // Update Hero Metrics
      document.getElementById('statTotalValido').innerText = baseValida;
      document.getElementById('statBaseDeduccion').innerText = `Base: ${{totalBase}} - ${{clavosValidosCount}} clavos`;
      document.getElementById('statConvertidas').innerText = convertidas;
      document.getElementById('statTasaConversion').innerText = `${{conversionRate.toFixed(2)}}%`;
      document.getElementById('statTasaIncremento').innerText = rateIncrement > 0 ? `+${{rateIncrement.toFixed(2)}}% gracias a clavos` : 'Sin variación';

      // Calculate USD Incentive and Next Tier Target
      const incentiveInfo = calculateIncentive(conversionRate, totalBase, convertidas, clavosValidosCount);
      document.getElementById('statIncentivoUSD').innerText = `$${{incentiveInfo.usd}} USD`;
      document.getElementById('statTramoNombre').innerText = incentiveInfo.tramoName;

      // Update Progress Bar to Next Tier
      document.getElementById('progressFillBar').style.width = `${{incentiveInfo.progressPercent}}%`;
      document.getElementById('progressTargetText').innerText = `Meta: ${{incentiveInfo.nextThreshold}}% ($${{incentiveInfo.nextUSD}} USD)`;
      
      if (incentiveInfo.neededClavos > 0) {{
        document.getElementById('progressTipClavos').innerHTML = `Te faltan <strong>${{incentiveInfo.neededClavos}} clavos más</strong> para alcanzar el ${{incentiveInfo.nextThreshold}}% y cobrar <strong>$${{incentiveInfo.nextUSD}} USD (+50 USD)</strong>.`;
      }} else {{
        document.getElementById('progressTipClavos').innerHTML = `<strong>¡Excelente! Ya superaste este tramo y estás maximizando comisiones.</strong>`;
      }}

      // Highlight active scale tier in sidebar
      updateScaleHighlight(incentiveInfo.activeTierId, incentiveInfo.nextTierId);
    }}

    // Calculate incentive based on official image rules
    function calculateIncentive(rate, totalBase, convertidas, currentClavos) {{
      let usd = 0;
      let tramoName = 'Menos de 32%';
      let activeTierId = 'tier-0';
      let nextTierId = 'tier-1';
      let nextThreshold = 32.0;
      let nextUSD = 150;
      let prevThreshold = 0;

      if (rate < 32.0) {{
        usd = 0;
        tramoName = 'Menos de 32%';
        activeTierId = 'tier-0';
        nextTierId = 'tier-1';
        nextThreshold = 32.0;
        nextUSD = 150;
        prevThreshold = 0;
      }} else if (rate >= 32.0 && rate <= 35.4999) {{
        usd = 150;
        tramoName = 'Tramo 32% - 35.4%';
        activeTierId = 'tier-1';
        nextTierId = 'tier-2';
        nextThreshold = 35.5;
        nextUSD = 200;
        prevThreshold = 32.0;
      }} else if (rate >= 35.5 && rate <= 38.9999) {{
        usd = 200;
        tramoName = 'Tramo 35.5% - 38.9%';
        activeTierId = 'tier-2';
        nextTierId = 'tier-3';
        nextThreshold = 39.0;
        nextUSD = 250;
        prevThreshold = 35.5;
      }} else if (rate >= 39.0 && rate <= 42.4999) {{
        usd = 250;
        tramoName = 'Tramo 39% - 42.4%';
        activeTierId = 'tier-3';
        nextTierId = 'tier-4';
        nextThreshold = 42.5;
        nextUSD = 300;
        prevThreshold = 39.0;
      }} else if (rate >= 42.5 && rate <= 46.0) {{
        usd = 300;
        tramoName = 'Tramo 42.5% - 46%';
        activeTierId = 'tier-4';
        nextTierId = 'tier-5';
        nextThreshold = 49.5;
        nextUSD = 350;
        prevThreshold = 42.5;
      }} else {{
        // Over 46%: each +3.5% is +50 USD
        const extraSteps = Math.floor((rate - 46.0) / 3.5) + 1;
        usd = 300 + (extraSteps * 50);
        tramoName = `Superior a 46% (+${{extraSteps * 50}} USD)`;
        activeTierId = 'tier-5';
        nextTierId = 'tier-5';
        prevThreshold = 46.0 + ((extraSteps - 1) * 3.5);
        nextThreshold = +(46.0 + (extraSteps * 3.5)).toFixed(1);
        nextUSD = usd + 50;
      }}

      // Calculate Clavos needed for next threshold:
      // nextThreshold / 100 = convertidas / (totalBase - targetClavos)
      // (totalBase - targetClavos) = convertidas / (nextThreshold / 100)
      // targetClavos = totalBase - (convertidas / (nextThreshold / 100))
      let neededClavos = 0;
      if (nextThreshold > rate) {{
        const targetDenominator = convertidas / (nextThreshold / 100);
        const targetTotalClavos = Math.ceil(totalBase - targetDenominator);
        neededClavos = Math.max(0, targetTotalClavos - currentClavos);
      }}

      // Progress bar percentage within current tier
      const range = nextThreshold - prevThreshold;
      const progressWithin = rate - prevThreshold;
      let progressPercent = range > 0 ? Math.min(100, Math.max(0, (progressWithin / range) * 100)) : 100;

      return {{
        usd,
        tramoName,
        activeTierId,
        nextTierId,
        nextThreshold,
        nextUSD,
        neededClavos,
        progressPercent: progressPercent.toFixed(1)
      }};
    }}

    function updateScaleHighlight(activeId, nextId) {{
      for (let i = 0; i <= 5; i++) {{
        const el = document.getElementById(`tier-${{i}}`);
        if (el) {{
          el.className = 'scale-item';
          if (`tier-${{i}}` === activeId) {{
            el.classList.add('active');
          }} else if (`tier-${{i}}` === nextId) {{
            el.classList.add('next');
          }}
        }}
      }}
    }}

    // Render Main Table
    function renderTable() {{
      const tbody = document.getElementById('solicitudesTableBody');
      const searchTerm = document.getElementById('tableSearch').value.toLowerCase().trim();
      const rubroFilter = document.getElementById('filterRubro').value;
      const estadoFilter = document.getElementById('filterEstado').value;
      const clavoCond = document.getElementById('filterClavoCond').value;

      let visibleCount = 0;
      let html = '';

      AppState.records.forEach((record, index) => {{
        // Apply Filters
        const matchesSearch = !searchTerm || 
          record.id.toLowerCase().includes(searchTerm) ||
          record.nombre.toLowerCase().includes(searchTerm) ||
          record.rubro.toLowerCase().includes(searchTerm) ||
          record.telefono.toLowerCase().includes(searchTerm) ||
          record.fundamento.toLowerCase().includes(searchTerm);

        const matchesRubro = !rubroFilter || record.rubro === rubroFilter;
        const matchesEstado = !estadoFilter || record.estado === estadoFilter;

        let matchesClavo = true;
        const isConflict = record.noEsClavo && record.esClavo;
        if (clavoCond === 'clavos') matchesClavo = record.esClavo && !record.noEsClavo;
        else if (clavoCond === 'noclavo') matchesClavo = record.noEsClavo && !record.esClavo;
        else if (clavoCond === 'conflicto') matchesClavo = isConflict;
        else if (clavoCond === 'sinmarcar') matchesClavo = !record.noEsClavo && !record.esClavo;

        if (matchesSearch && matchesRubro && matchesEstado && matchesClavo) {{
          visibleCount++;
          const rowClass = isConflict ? 'row-conflict' : (record.esClavo ? 'row-clavo' : '');
          const waLink = record.telefono ? `https://wa.me/${{cleanPhone(record.telefono)}}` : '#';

          html += `
            <tr class="${{rowClass}}" id="row-${{record.id}}">
              <td>
                <span class="badge-id">#${{record.id}}</span>
                ${{isConflict ? '<span class="conflict-warning-tag">⚠️ Conflicto</span>' : ''}}
              </td>
              <td><strong>${{escapeHtml(record.nombre || 'Sin nombre')}}</strong></td>
              <td><span class="badge-rubro">${{escapeHtml(record.rubro || 'General')}}</span></td>
              <td>
                <div class="phone-cell">
                  <span style="font-family: monospace; font-size: 0.86rem;">${{escapeHtml(record.telefono || '—')}}</span>
                  ${{record.telefono ? `
                    <button class="btn-copy-phone" onclick="copyPhoneNumber(this, '${{cleanPhone(record.telefono)}}')" title="Copiar número directamente">📋 Copiar</button>
                  ` : ''}}
                </div>
              </td>
              <td>
                <select class="status-select" onchange="updateRecordStatus(${{index}}, this.value)">
                  <option value="Pendientes" ${{record.estado === 'Pendientes' ? 'selected' : ''}}>Pendientes</option>
                  <option value="Enviadas" ${{record.estado === 'Enviadas' ? 'selected' : ''}}>Enviadas</option>
                  <option value="Aceptadas" ${{record.estado === 'Aceptadas' ? 'selected' : ''}}>Aceptadas</option>
                  <option value="Pago Pendiente" ${{record.estado === 'Pago Pendiente' ? 'selected' : ''}}>Pago Pendiente</option>
                  <option value="Completadas" ${{record.estado === 'Completadas' ? 'selected' : ''}}>Completadas</option>
                  <option value="Canceladas" ${{record.estado === 'Canceladas' ? 'selected' : ''}}>Canceladas</option>
                </select>
              </td>
              <td class="check-cell">
                <input type="checkbox" class="custom-checkbox noclavo-box" 
                  ${{record.noEsClavo ? 'checked' : ''}} 
                  onchange="toggleNoEsClavo(${{index}}, this.checked)">
              </td>
              <td class="check-cell">
                <input type="checkbox" class="custom-checkbox clavo-box" 
                  ${{record.esClavo ? 'checked' : ''}} 
                  onchange="toggleEsClavo(${{index}}, this.checked)">
              </td>
              <td>
                <input type="text" class="fundamento-input" 
                  placeholder="Justifica por qué es clavo o qué pasó (ej. Fuera de radio, nunca cotizó)..." 
                  value="${{escapeHtml(record.fundamento || '')}}" 
                  onchange="updateRecordFundamento(${{index}}, this.value)">
              </td>
              <td style="text-align: center;">
                <button class="btn-copy" style="color: var(--danger);" onclick="deleteRecord(${{index}})" title="Eliminar fila">&times;</button>
              </td>
            </tr>
          `;
        }}
      }});

      tbody.innerHTML = html || '<tr><td colspan="9" style="text-align:center; padding: 24px; color: var(--text-dim);">No se encontraron solicitudes con los filtros aplicados.</td></tr>';
      document.getElementById('filteredCountInfo').innerText = `Mostrando ${{visibleCount}} de ${{AppState.records.length}} solicitudes`;
    }}

    // Checkbox Toggles & Realtime Calculations
    function toggleNoEsClavo(index, checked) {{
      AppState.records[index].noEsClavo = checked;
      persistState(false);
      renderAll();
    }}

    function toggleEsClavo(index, checked) {{
      AppState.records[index].esClavo = checked;
      persistState(false);
      renderAll();
    }}

    function updateRecordStatus(index, newStatus) {{
      AppState.records[index].estado = newStatus;
      persistState(false);
      renderAll();
    }}

    function updateRecordFundamento(index, text) {{
      AppState.records[index].fundamento = text.trim();
      persistState(false);
      renderDossier();
    }}

    function deleteRecord(index) {{
      if (confirm(`¿Eliminar la solicitud #${{AppState.records[index].id}}?`)) {{
        AppState.records.splice(index, 1);
        persistState(true);
        renderAll();
      }}
    }}

    // Render Conflict View (Tab 2)
    function renderConflicts() {{
      const tbody = document.getElementById('conflictTableBody');
      const conflicts = AppState.records.filter(r => r.noEsClavo && r.esClavo);

      let html = '';
      conflicts.forEach(r => {{
        const globalIndex = AppState.records.findIndex(x => x.id === r.id);
        const waLink = r.telefono ? `https://wa.me/${{cleanPhone(r.telefono)}}` : '#';

        html += `
          <tr class="row-conflict">
            <td><span class="badge-id">#${{r.id}}</span></td>
            <td><strong>${{escapeHtml(r.nombre)}}</strong></td>
            <td><span class="badge-rubro">${{escapeHtml(r.rubro)}}</span></td>
            <td>
              <div class="phone-cell">
                <span style="font-family: monospace; font-size: 0.86rem;">${{escapeHtml(r.telefono || '—')}}</span>
                ${{r.telefono ? `
                  <button class="btn-copy-phone" onclick="copyPhoneNumber(this, '${{cleanPhone(r.telefono)}}')" title="Copiar número directamente">📋 Copiar</button>
                ` : ''}}
              </div>
            </td>
            <td><span class="badge-rubro" style="background:#243047; color:#fff;">${{r.estado}}</span></td>
            <td>
              <input type="text" class="fundamento-input" value="${{escapeHtml(r.fundamento)}}" 
                onchange="updateRecordFundamento(${{globalIndex}}, this.value)">
            </td>
            <td style="text-align: center; white-space: nowrap;">
              <button class="btn btn-gold" style="padding: 4px 10px; font-size: 0.78rem;" onclick="resolveConflictAsClavo(${{globalIndex}})">✅ Aprobar como Clavo</button>
              <button class="btn btn-secondary" style="padding: 4px 10px; font-size: 0.78rem;" onclick="resolveConflictAsNoClavo(${{globalIndex}})">❌ Descartar Clavo</button>
            </td>
          </tr>
        `;
      }});

      tbody.innerHTML = html || '<tr><td colspan="7" style="text-align:center; padding: 24px; color: var(--text-muted);">🎉 No hay casos en conflicto pendientes de revisión.</td></tr>';
    }}

    function resolveConflictAsClavo(index) {{
      AppState.records[index].noEsClavo = false;
      AppState.records[index].esClavo = true;
      persistState(true);
      renderAll();
      showToast(`Solicitud #${{AppState.records[index].id}} aprobada como clavo`, 'success');
    }}

    function resolveConflictAsNoClavo(index) {{
      AppState.records[index].noEsClavo = true;
      AppState.records[index].esClavo = false;
      persistState(true);
      renderAll();
      showToast(`Solicitud #${{AppState.records[index].id}} descartada como clavo`, 'info');
    }}

    // Render Dossier View (Tab 3)
    function renderDossier() {{
      const tbody = document.getElementById('dossierTableBody');
      const clavos = AppState.records.filter(r => r.esClavo && !r.noEsClavo);

      const totalBase = AppState.monthlySettings.totalMes;
      const clavosCount = clavos.length;
      const baseAprobada = Math.max(1, totalBase - clavosCount);
      const convertidas = AppState.monthlySettings.convertidas;
      const tasaFinal = ((convertidas / baseAprobada) * 100).toFixed(2);

      document.getElementById('dossierTotalBase').innerText = totalBase;
      document.getElementById('dossierTotalClavos').innerText = `-${{clavosCount}}`;
      document.getElementById('dossierBaseAprobada').innerText = baseAprobada;
      document.getElementById('dossierTasaFinal').innerText = `${{tasaFinal}}%`;

      let html = '';
      clavos.forEach(r => {{
        html += `
          <tr>
            <td><span class="badge-id">#${{r.id}}</span></td>
            <td><strong>${{escapeHtml(r.nombre)}}</strong></td>
            <td><span class="badge-rubro">${{escapeHtml(r.rubro)}}</span></td>
            <td>${{escapeHtml(r.telefono)}}</td>
            <td>${{r.estado}}</td>
            <td>${{escapeHtml(r.fundamento || 'Clavo registrado y justificado para deducción mensual.')}}</td>
          </tr>
        `;
      }});

      tbody.innerHTML = html || '<tr><td colspan="6" style="text-align:center; padding: 24px; color: var(--text-dim);">No hay clavos marcados actualmente. Marca "Es Clavo" en la tabla para sumarlos aquí.</td></tr>';
    }}

    // Render History (Tab 4)
    function renderHistory() {{
      const tbody = document.getElementById('historyTableBody');
      let html = '';

      AppState.historySnapshots.forEach((snap, idx) => {{
        html += `
          <tr>
            <td>${{snap.fecha}}</td>
            <td><strong>${{escapeHtml(snap.nombre)}}</strong></td>
            <td>${{snap.baseInicial}}</td>
            <td style="color: var(--gold); font-weight:700;">${{snap.clavos}}</td>
            <td>${{snap.baseNeta}}</td>
            <td>${{snap.convertidas}}</td>
            <td style="color: var(--accent); font-weight:700;">${{snap.tasaConversion}}%</td>
            <td style="color: var(--success); font-weight:700;">$${{snap.usd}} USD</td>
            <td style="text-align: center;">
              <button class="btn btn-secondary" style="padding: 2px 8px; font-size: 0.75rem;" onclick="deleteSnapshot(${{idx}})">Eliminar</button>
            </td>
          </tr>
        `;
      }});

      tbody.innerHTML = html || '<tr><td colspan="9" style="text-align:center; padding: 24px; color: var(--text-dim);">No hay snapshots guardados en el historial aún.</td></tr>';
    }}

    function saveCurrentBatchSnapshot() {{
      const name = prompt('Nombre descriptivo para este lote (ej: Septiembre 2026 - Cierre Oficial):', `Lote ${{new Date().toLocaleDateString('es-UY')}}`);
      if (!name) return;

      const clavosCount = AppState.records.filter(r => r.esClavo && !r.noEsClavo).length;
      const totalBase = AppState.monthlySettings.totalMes;
      const baseNeta = Math.max(1, totalBase - clavosCount);
      const convertidas = AppState.monthlySettings.convertidas;
      const tasa = ((convertidas / baseNeta) * 100).toFixed(2);
      const incentiveInfo = calculateIncentive(parseFloat(tasa), totalBase, convertidas, clavosCount);

      AppState.historySnapshots.unshift({{
        fecha: new Date().toLocaleString('es-UY'),
        nombre: name,
        baseInicial: totalBase,
        clavos: clavosCount,
        baseNeta: baseNeta,
        convertidas: convertidas,
        tasaConversion: tasa,
        usd: incentiveInfo.usd,
        recordsSnapshot: JSON.parse(JSON.stringify(AppState.records))
      }});

      persistState(true);
      renderHistory();
      showToast('Snapshot guardado en el historial', 'success');
    }}

    function deleteSnapshot(index) {{
      if (confirm('¿Eliminar este registro histórico?')) {{
        AppState.historySnapshots.splice(index, 1);
        persistState(true);
        renderHistory();
      }}
    }}

    // Filter Helpers
    function applyFilters() {{
      renderTable();
    }}

    function filterByStateCard(estado) {{
      document.getElementById('filterEstado').value = estado;
      document.getElementById('filterClavoCond').value = '';
      switchTab('gestion');
      applyFilters();
    }}

    function filterByCondition(cond) {{
      document.getElementById('filterClavoCond').value = cond;
      document.getElementById('filterEstado').value = '';
      switchTab('gestion');
      applyFilters();
    }}

    function resetFilters() {{
      document.getElementById('tableSearch').value = '';
      document.getElementById('filterRubro').value = '';
      document.getElementById('filterEstado').value = '';
      document.getElementById('filterClavoCond').value = '';
      applyFilters();
    }}

    function populateRubrosFilter() {{
      updateRubroFilterOptions();
    }}

    function updateRubroFilterOptions() {{
      const select = document.getElementById('filterRubro');
      const currentVal = select.value;
      const rubros = new Set();
      AppState.records.forEach(r => {{
        if (r.rubro) rubros.add(r.rubro.trim());
      }});

      let html = '<option value="">Todos los Rubros</option>';
      Array.from(rubros).sort().forEach(rub => {{
        html += `<option value="${{escapeHtml(rub)}}" ${{rub === currentVal ? 'selected' : ''}}>${{escapeHtml(rub)}}</option>`;
      }});
      select.innerHTML = html;
    }}

    // Tab Navigation Switcher
    function switchTab(tab) {{
      currentTab = tab;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(`tabBtn-${{tab}}`).classList.add('active');

      document.getElementById('tabContent-gestion').style.display = tab === 'gestion' ? 'block' : 'none';
      document.getElementById('tabContent-conflicto').style.display = tab === 'conflicto' ? 'block' : 'none';
      document.getElementById('tabContent-dossier').style.display = tab === 'dossier' ? 'block' : 'none';
      document.getElementById('tabContent-historial').style.display = tab === 'historial' ? 'block' : 'none';
    }}

    // Smart Text Parser Modal
    function openPasteModal() {{
      document.getElementById('modalPaste').classList.add('open');
      document.getElementById('pasteRawText').value = '';
      document.getElementById('pasteRawText').focus();
    }}

    function closePasteModal() {{
      document.getElementById('modalPaste').classList.remove('open');
    }}

    function processPastedText() {{
      const text = document.getElementById('pasteRawText').value;
      if (!text.trim()) {{
        alert('Por favor pega el texto antes de procesar.');
        return;
      }}

      const parsed = parseRawInputText(text);
      if (parsed.length === 0) {{
        alert('No se detectaron solicitudes válidas con formato #ID. Revisa el texto pegado.');
        return;
      }}

      const mode = document.getElementById('pasteImportMode').value;
      if (mode === 'replace') {{
        AppState.records = parsed;
      }} else {{
        AppState.records = AppState.records.concat(parsed);
      }}

      persistState(true);
      closePasteModal();
      renderAll();
      showToast(`¡Se procesaron y limpiaron ${{parsed.length}} solicitudes con éxito!`, 'success');
    }}

    // Intelligent Text Cleaning & Parsing Algorithm
    function parseRawInputText(rawText) {{
      const lines = rawText.split('\\n').map(l => l.trim());
      const records = [];
      let currentSection = 'Pendientes';

      let i = 0;
      while (i < lines.length) {{
        let line = lines[i];
        if (!line) {{ i++; continue; }}

        const lower = line.toLowerCase();
        if (['pendientes', 'enviadas', 'canceladas', 'pago pendiente', 'aceptadas', 'completadas'].includes(lower)) {{
          currentSection = lower === 'pago pendiente' ? 'Pago Pendiente' : line.charAt(0).toUpperCase() + line.slice(1);
          i++;
          continue;
        }}

        // Match #12345 ID format
        if (line.startsWith('#') && line.length > 1 && /^#\\d+$/.test(line)) {{
          const reqId = line.replace('#', '').trim();
          let nombre = '';
          let rubro = '';
          let telefonos = [];
          let obs = [];

          i++;
          while (i < lines.length) {{
            let sub = lines[i];
            if (!sub) {{ i++; continue; }}

            if (sub.startsWith('#') && /^#\\d+$/.test(sub)) break;
            if (['pendientes', 'enviadas', 'canceladas', 'pago pendiente', 'aceptadas', 'completadas'].includes(sub.toLowerCase())) break;

            // Filter out noise: icons, dates, elapsed times
            if (['🔥 Urgentes', '🕐 Recientes', 'ℹ️ Más info'].includes(sub)) {{ i++; continue; }}
            if (/^\\d+\\s+mes$/i.test(sub)) {{ i++; continue; }}
            if (sub.startsWith('🕐') || sub.includes('hace ')) {{ i++; continue; }}
            if (/^\\d{{2}}-\\d{{2}}$/.test(sub)) {{ i++; continue; }}

            // Match phone
            if (sub.startsWith('📞') || /^(\\+?\\d{{8,15}})$/.test(sub.replace(/\\s+/g, ''))) {{
              const p = sub.replace('📞', '').trim();
              if (p && !telefonos.includes(p)) telefonos.push(p);
              i++;
              continue;
            }}

            if (!nombre) {{
              nombre = sub;
            }} else if (!rubro) {{
              rubro = sub;
            }} else {{
              obs.push(sub);
            }}
            i++;
          }}

          records.push({{
            id: reqId,
            nombre: nombre || 'Sin nombre',
            rubro: rubro || 'General',
            telefono: telefonos.join(' / '),
            estado: currentSection,
            noEsClavo: false,
            esClavo: false,
            fundamento: obs.join(' ').trim()
          }});
          continue;
        }}
        i++;
      }}

      return records;
    }}

    // Settings Modal
    function openSettingsModal() {{
      document.getElementById('settingTotalMes').value = AppState.monthlySettings.totalMes;
      document.getElementById('settingConvertidas').value = AppState.monthlySettings.convertidas;
      document.getElementById('settingAceptadas').value = AppState.monthlySettings.aceptadas || 73;
      document.getElementById('settingCompletadas').value = AppState.monthlySettings.completadas || 119;
      document.getElementById('modalSettings').classList.add('open');
    }}

    function closeSettingsModal() {{
      document.getElementById('modalSettings').classList.remove('open');
    }}

    function saveSettings() {{
      const total = parseInt(document.getElementById('settingTotalMes').value) || 581;
      const convertidas = parseInt(document.getElementById('settingConvertidas').value) || 193;
      const aceptadas = parseInt(document.getElementById('settingAceptadas').value) || 73;
      const completadas = parseInt(document.getElementById('settingCompletadas').value) || 119;

      AppState.monthlySettings = {{
        totalMes: total,
        convertidas: convertidas,
        aceptadas: aceptadas,
        completadas: completadas
      }};

      persistState(true);
      closeSettingsModal();
      renderAll();
      showToast('Configuración mensual actualizada', 'success');
    }}

    function resetToInitialDefaults() {{
      if (confirm('¿Restaurar las 389 solicitudes originales del mes actual?')) {{
        AppState.records = JSON.parse(JSON.stringify(INITIAL_RECORDS));
        AppState.monthlySettings = {{
          totalMes: 581,
          convertidas: 193,
          aceptadas: 73,
          completadas: 119
        }};
        persistState(true);
        closeSettingsModal();
        renderAll();
        showToast('Datos iniciales restaurados con éxito', 'info');
      }}
    }}

    // Export JSON Backup
    function exportJSON() {{
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(AppState, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", `auditoria_solicitudes_${{new Date().toISOString().slice(0,10)}}.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
      showToast('Backup JSON exportado', 'success');
    }}

    // Import JSON Backup
    function importJSON(event) {{
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {{
        try {{
          const imported = JSON.parse(e.target.result);
          if (Array.isArray(imported)) {{
            AppState.records = imported;
          }} else if (imported.records) {{
            AppState = imported;
          }}
          persistState(true);
          renderAll();
          showToast('Archivo importado con éxito', 'success');
        }} catch (err) {{
          alert('Error al leer el archivo JSON: ' + err.message);
        }}
      }};
      reader.readAsText(file);
      event.target.value = '';
    }}

    // Export CSV / Excel
    function exportCSV() {{
      let csv = "ID,Cliente,Rubro,Telefono,Estado,NoEsClavo,EsClavo,EsConflicto,Fundamento\\n";
      AppState.records.forEach(r => {{
        const isConflict = r.noEsClavo && r.esClavo ? 'SI' : 'NO';
        const clavo = r.esClavo && !r.noEsClavo ? 'SI' : 'NO';
        const noClavo = r.noEsClavo && !r.esClavo ? 'SI' : 'NO';
        csv += `"${{r.id}}","${{escapeCSV(r.nombre)}}","${{escapeCSV(r.rubro)}}","${{escapeCSV(r.telefono)}}","${{r.estado}}","${{noClavo}}","${{clavo}}","${{isConflict}}","${{escapeCSV(r.fundamento)}}"\\n`;
      }});

      const blob = new Blob(["\\ufeff" + csv], {{ type: 'text/csv;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.setAttribute("href", url);
      link.setAttribute("download", `solicitudes_auditoria_${{new Date().toISOString().slice(0,10)}}.csv`);
      document.body.appendChild(link);
      link.click();
      link.remove();
      showToast('Planilla CSV/Excel exportada', 'success');
    }}

    // Copy Dossier Summary to Clipboard (Slack / WhatsApp ready)
    function copyDossierSummary() {{
      const clavos = AppState.records.filter(r => r.esClavo && !r.noEsClavo);
      const totalBase = AppState.monthlySettings.totalMes;
      const baseAprobada = Math.max(1, totalBase - clavos.length);
      const convertidas = AppState.monthlySettings.convertidas;
      const tasa = ((convertidas / baseAprobada) * 100).toFixed(2);
      const inc = calculateIncentive(parseFloat(tasa), totalBase, convertidas, clavos.length);

      let text = `*RESUMEN DE AUDITORÍA Y DEDUCCIÓN DE CLAVOS - ARREGLATODO*\\n`;
      text += `📅 Fecha: ${{new Date().toLocaleDateString('es-UY')}}\\n`;
      text += `📊 Solicitudes Base: ${{totalBase}}\\n`;
      text += `📌 Clavos Justificados a Deducir: ${{clavos.length}}\\n`;
      text += `✅ Base Válida Neta: ${{baseAprobada}}\\n`;
      text += `🎯 Solicitudes Convertidas: ${{convertidas}}\\n`;
      text += `📈 Tasa de Conversión Resultante: *${{tasa}}%*\\n`;
      text += `💰 Tramo de Incentivo Aplicable: *${{inc.tramoName}} ($${{inc.usd}} USD)*\\n\\n`;
      text += `*DETALLE DE CLAVOS JUSTIFICADOS:*\\n`;

      clavos.forEach((c, idx) => {{
        text += `${{idx + 1}}. #${{c.id}} - ${{c.nombre}} (${{c.rubro}}): ${{c.fundamento || 'Clavo comprobado'}}\\n`;
      }});

      navigator.clipboard.writeText(text).then(() => {{
        showToast('¡Resumen copiado para WhatsApp o Slack!', 'success');
      }}).catch(() => {{
        alert('Copiado al portapapeles');
      }});
    }}

    // Utility Helpers
    function cleanPhone(phone) {{
      return phone.replace(/[^0-9]/g, '');
    }}

    function escapeHtml(text) {{
      if (!text) return '';
      return String(text)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }}

    function escapeCSV(text) {{
      if (!text) return '';
      return String(text).replace(/"/g, '""');
    }}

    function copyPhoneNumber(btn, phone) {{
      navigator.clipboard.writeText(phone).then(() => {{
        const prev = btn.innerHTML;
        btn.innerHTML = '✅ Copiado!';
        btn.classList.add('copied');
        showToast(`Número copiado: ${{phone}}`, 'success');
        setTimeout(() => {{
          btn.innerHTML = prev;
          btn.classList.remove('copied');
        }}, 1400);
      }}).catch(() => {{
        showToast(`Copiado: ${{phone}}`, 'info');
      }});
    }}

    function copyText(str) {{
      navigator.clipboard.writeText(str).then(() => {{
        showToast(`Copiado: ${{str}}`, 'info');
      }});
    }}

    function showToast(msg, type = 'info') {{
      const toast = document.getElementById('toastMessage');
      toast.innerText = msg;
      toast.className = `toast show toast-${{type}}`;
      setTimeout(() => {{
        toast.className = 'toast';
      }}, 3200);
    }}
  </script>
</body>
</html>
'''

output_file = '/home/leondon-pc/Desktop/Manual_Operativo_Supply_ArreglaTodo/auditoria.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f'Successfully generated {output_file} ({os.path.getsize(output_file)} bytes)!')
