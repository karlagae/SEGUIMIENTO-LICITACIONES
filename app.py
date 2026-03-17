import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Plataforma Licitaciones",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Plataforma Licitaciones</title>
<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: "Segoe UI", sans-serif;
    }

    body {
        background: linear-gradient(180deg, #1b228a 0%, #241f96 100%);
        padding: 28px;
    }

    .main-wrapper {
        max-width: 1320px;
        margin: 0 auto;
        background: #f5f8fc;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 14px 30px rgba(0,0,0,0.18);
    }

    .topbar {
        background: linear-gradient(90deg, #06297e 0%, #0c45ba 100%);
        color: white;
        padding: 22px 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .brand-section {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .brand-icon {
        font-size: 34px;
    }

    .brand-title {
        font-size: 21px;
        font-weight: 700;
        line-height: 1.05;
    }

    .nav-center {
        display: flex;
        gap: 36px;
        align-items: center;
    }

    .nav-item {
        font-size: 17px;
        font-weight: 600;
        position: relative;
        opacity: 0.96;
    }

    .nav-item.active::after {
        content: "";
        position: absolute;
        left: 0;
        bottom: -8px;
        width: 100%;
        height: 2px;
        background: #f4be46;
        border-radius: 10px;
    }

    .nav-right {
        display: flex;
        align-items: center;
        gap: 16px;
        font-size: 16px;
        font-weight: 600;
    }

    .user-badge {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background: #f0c3a1;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid rgba(255,255,255,0.65);
    }

    .content-area {
        display: flex;
        gap: 24px;
        padding: 24px;
        align-items: flex-start;
        background: linear-gradient(180deg, #edf3fb 0%, #f8fbff 100%);
    }

    .left-menu {
        width: 240px;
        background: white;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #e6edf6;
        box-shadow: 0 5px 16px rgba(0,0,0,0.08);
        flex-shrink: 0;
    }

    .menu-header {
        background: #082f8f;
        color: white;
        font-weight: 700;
        padding: 16px 18px;
        font-size: 18px;
    }

    .menu-item {
        padding: 16px 18px;
        font-size: 17px;
        color: #21355e;
        border-bottom: 1px solid #edf1f7;
    }

    .menu-item:last-child {
        border-bottom: none;
    }

    .main-panel {
        flex: 1;
    }

    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 18px;
        margin-bottom: 22px;
    }

    .kpi-card {
        color: white;
        border-radius: 12px;
        padding: 18px 20px;
        display: flex;
        align-items: center;
        gap: 14px;
        min-height: 88px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.14);
    }

    .blue-card {
        background: linear-gradient(90deg, #0c46bf 0%, #0f5ae6 100%);
    }

    .orange-card {
        background: linear-gradient(90deg, #ee9d21 0%, #f5b53d 100%);
    }

    .navy-card {
        background: linear-gradient(90deg, #081b4f 0%, #10245e 100%);
    }

    .kpi-icon {
        width: 46px;
        height: 46px;
        border-radius: 10px;
        background: rgba(255,255,255,0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 23px;
    }

    .kpi-title {
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 4px;
    }

    .kpi-value {
        font-size: 24px;
        font-weight: 800;
    }

    .white-box {
        background: white;
        border-radius: 12px;
        padding: 22px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.07);
        border: 1px solid #e9eef6;
    }

    .section-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 18px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 800;
        color: #17326a;
    }

    .small-btn {
        border: 1px solid #d6deea;
        background: white;
        color: #30466f;
        padding: 9px 18px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 15px;
    }

    .table-wrap {
        border: 1px solid #edf2f8;
        border-radius: 10px;
        overflow: hidden;
    }

    .table-header,
    .table-row {
        display: grid;
        grid-template-columns: 2.3fr 1.2fr 1fr 1fr;
        align-items: center;
    }

    .table-header {
        background: #eff4fa;
        color: #30415f;
        font-weight: 700;
        font-size: 16px;
    }

    .table-header div,
    .table-row div {
        padding: 15px 18px;
    }

    .table-row {
        border-top: 1px solid #edf1f7;
        color: #27395f;
        background: white;
        font-size: 16px;
    }

    .status-pill {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 8px;
        color: white;
        font-size: 14px;
        font-weight: 700;
    }

    .pill-blue { background: #0b56d8; }
    .pill-blue2 { background: #2557b8; }
    .pill-orange { background: #f0a126; }
    .pill-orange2 { background: #e08b18; }

    .bottom-grid {
        display: grid;
        grid-template-columns: 1.35fr 1fr;
        gap: 22px;
        margin-top: 22px;
    }

    .box-title {
        font-size: 20px;
        font-weight: 800;
        color: #17326a;
        margin-bottom: 12px;
    }

    .chart-layout {
        display: grid;
        grid-template-columns: 1.35fr 1fr;
        gap: 10px;
        align-items: center;
    }

    .chart-area {
        height: 250px;
        display: flex;
        align-items: flex-end;
        gap: 12px;
        padding: 10px 8px 0 8px;
        border-top: 1px solid #edf1f7;
        margin-top: 8px;
    }

    .bar {
        width: 36px;
        border-radius: 8px 8px 0 0;
    }

    .bar-blue { background: #0a43bf; }
    .bar-blue2 { background: #2a5ebd; }
    .bar-blue3 { background: #7ca1db; }
    .bar-orange { background: #ef9d24; }

    .chart-legend {
        display: flex;
        gap: 22px;
        flex-wrap: wrap;
        margin-top: 16px;
        font-weight: 600;
        color: #223660;
    }

    .legend-item {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .legend-color {
        width: 14px;
        height: 14px;
        border-radius: 3px;
    }

    .pie-wrap {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .pie-chart {
        width: 170px;
        height: 170px;
        border-radius: 50%;
        background: conic-gradient(#0a43bf 0deg 250deg, #f1a22b 250deg 360deg);
        position: relative;
    }

    .pie-chart::after {
        content: "";
        position: absolute;
        inset: 42px;
        background: white;
        border-radius: 50%;
    }

    .pie-center {
        position: absolute;
        inset: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 2;
        font-size: 28px;
        font-weight: 800;
        color: #17326a;
    }

    .activity-list {
        list-style: none;
        padding-left: 0;
        margin: 0;
        border-top: 1px solid #edf1f7;
    }

    .activity-list li {
        padding: 16px 0;
        border-bottom: 1px solid #edf1f7;
        font-size: 17px;
        color: #27395f;
        line-height: 1.4;
    }

    .activity-list li:last-child {
        border-bottom: none;
    }

    .dot {
        color: #0a43bf;
        font-weight: 900;
        margin-right: 10px;
    }

    @media (max-width: 1100px) {
        .content-area {
            flex-direction: column;
        }

        .left-menu {
            width: 100%;
        }

        .kpi-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .bottom-grid {
            grid-template-columns: 1fr;
        }

        .nav-center {
            display: none;
        }
    }

    @media (max-width: 700px) {
        body {
            padding: 10px;
        }

        .kpi-grid {
            grid-template-columns: 1fr;
        }

        .table-header,
        .table-row {
            grid-template-columns: 1fr;
        }

        .topbar {
            flex-direction: column;
            align-items: flex-start;
            gap: 16px;
        }

        .chart-layout {
            grid-template-columns: 1fr;
        }
    }
</style>
</head>
<body>
    <div class="main-wrapper">

        <div class="topbar">
            <div class="brand-section">
                <div class="brand-icon">📄</div>
                <div class="brand-title">Plataforma<br>Licitaciones</div>
            </div>

            <div class="nav-center">
                <div class="nav-item active">Inicio</div>
                <div class="nav-item">Licitaciones</div>
                <div class="nav-item">Reportes</div>
            </div>

            <div class="nav-right">
                <div>🔔 Notificaciones</div>
                <div class="user-badge">👩🏻</div>
                <div>Usuario ▾</div>
            </div>
        </div>

        <div class="content-area">

            <div class="left-menu">
                <div class="menu-header">🗂️ Panel Principal</div>
                <div class="menu-item">📅 Mis Licitaciones</div>
                <div class="menu-item">🗃️ Historial</div>
                <div class="menu-item">✉️ Documentos</div>
                <div class="menu-item">⚙️ Configuración</div>
            </div>

            <div class="main-panel">

                <div class="kpi-grid">
                    <div class="kpi-card blue-card">
                        <div class="kpi-icon">☑️</div>
                        <div>
                            <div class="kpi-title">Licitaciones</div>
                            <div class="kpi-value">12</div>
                        </div>
                    </div>

                    <div class="kpi-card blue-card">
                        <div class="kpi-icon">⚖️</div>
                        <div>
                            <div class="kpi-title">En Evaluación</div>
                            <div class="kpi-value">8</div>
                        </div>
                    </div>

                    <div class="kpi-card orange-card">
                        <div class="kpi-icon">📁</div>
                        <div>
                            <div class="kpi-title">Adjudicadas</div>
                            <div class="kpi-value">5</div>
                        </div>
                    </div>

                    <div class="kpi-card navy-card">
                        <div class="kpi-icon">➕</div>
                        <div>
                            <div class="kpi-title">Canceladas</div>
                            <div class="kpi-value">2</div>
                        </div>
                    </div>
                </div>

                <div class="white-box">
                    <div class="section-header">
                        <div class="section-title">Resumen de Licitaciones</div>
                        <div class="small-btn">Ver todas</div>
                    </div>

                    <div class="table-wrap">
                        <div class="table-header">
                            <div>Licitación</div>
                            <div>Estado</div>
                            <div>Propuestas</div>
                            <div>Cierre</div>
                        </div>

                        <div class="table-row">
                            <div>Construcción de Edificio</div>
                            <div><span class="status-pill pill-blue">En Evaluación</span></div>
                            <div>8 Propuestas</div>
                            <div>15 Feb 2022</div>
                        </div>

                        <div class="table-row">
                            <div>Suministro de Equipos</div>
                            <div><span class="status-pill pill-blue2">Recepción de Ofertas</span></div>
                            <div>13 Propuestas</div>
                            <div>22 Feb 2022</div>
                        </div>

                        <div class="table-row">
                            <div>Servicio de Mantenimiento</div>
                            <div><span class="status-pill pill-orange">Adjudicada</span></div>
                            <div>6 Propuestas</div>
                            <div>05 Feb 2022</div>
                        </div>

                        <div class="table-row">
                            <div>Proveeduría de Materiales</div>
                            <div><span class="status-pill pill-orange2">Abierta</span></div>
                            <div>15 Propuestas</div>
                            <div>28 Feb 2022</div>
                        </div>
                    </div>
                </div>

                <div class="bottom-grid">
                    <div class="white-box">
                        <div class="box-title">📊 Estadísticas</div>

                        <div class="chart-layout">
                            <div>
                                <div class="chart-area">
                                    <div class="bar bar-blue" style="height:150px;"></div>
                                    <div class="bar bar-blue2" style="height:95px;"></div>
                                    <div class="bar bar-blue" style="height:135px;"></div>
                                    <div class="bar bar-orange" style="height:110px;"></div>
                                    <div class="bar bar-blue2" style="height:105px;"></div>
                                    <div class="bar bar-blue3" style="height:62px;"></div>
                                    <div class="bar bar-blue" style="height:40px;"></div>
                                    <div class="bar bar-orange" style="height:12px;"></div>
                                </div>

                                <div class="chart-legend">
                                    <div class="legend-item">
                                        <div class="legend-color" style="background:#0a43bf;"></div>
                                        <div>Propuestas Recibidas</div>
                                    </div>
                                    <div class="legend-item">
                                        <div class="legend-color" style="background:#ef9d24;"></div>
                                        <div>Adjudicaciones</div>
                                    </div>
                                </div>
                            </div>

                            <div class="pie-wrap">
                                <div class="pie-chart">
                                    <div class="pie-center">75%</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="white-box">
                        <div class="box-title">Última Actividad</div>
                        <ul class="activity-list">
                            <li><span class="dot">●</span>Revisión de propuestas en curso.</li>
                            <li><span class="dot">●</span>Nueva licitación añadida: “Servicio de Consultoría”.</li>
                            <li><span class="dot">●</span>Plazo extendido para recepción de ofertas.</li>
                            <li><span class="dot">●</span>Adjudicación finalizada en “Compra de Vehículos”.</li>
                        </ul>
                    </div>
                </div>

            </div>
        </div>
    </div>
</body>
</html>
"""

components.html(html_code, height=980, scrolling=True)
