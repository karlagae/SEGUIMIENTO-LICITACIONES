import streamlit as st

st.set_page_config(
    page_title="Plataforma Licitaciones",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>
/* ===== Fondo general ===== */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.stApp {
    background: linear-gradient(180deg, #062a7b 0%, #0b2f86 45%, #062a7b 100%);
}

/* ===== Contenedor principal ===== */
.main-wrapper {
    max-width: 1280px;
    margin: 20px auto;
    background: #f6f8fc;
    border-radius: 0px;
    overflow: hidden;
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.20);
}

/* ===== Header ===== */
.topbar {
    background: linear-gradient(90deg, #032a84 0%, #0b47c2 100%);
    color: white;
    padding: 22px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.brand-section {
    display: flex;
    align-items: center;
    gap: 14px;
}

.brand-icon {
    font-size: 34px;
    line-height: 1;
}

.brand-title {
    font-size: 22px;
    font-weight: 700;
    line-height: 1.05;
}

.nav-center {
    display: flex;
    gap: 34px;
    align-items: center;
}

.nav-item {
    color: white;
    font-size: 18px;
    font-weight: 600;
    opacity: 0.95;
    position: relative;
}

.nav-item.active::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -8px;
    width: 100%;
    height: 2px;
    background: #f4c048;
    border-radius: 10px;
}

.nav-right {
    display: flex;
    align-items: center;
    gap: 18px;
    font-size: 17px;
    font-weight: 600;
}

.user-badge {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: #f7c59f;
    border: 2px solid rgba(255,255,255,0.7);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}

/* ===== Layout interno ===== */
.content-area {
    display: flex;
    gap: 22px;
    padding: 26px;
    background: linear-gradient(180deg, #eef3fb 0%, #f7f9fc 100%);
}

/* ===== Sidebar ===== */
.left-menu {
    width: 230px;
    background: white;
    border-radius: 14px;
    padding: 0;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    height: fit-content;
    overflow: hidden;
    border: 1px solid #e8edf5;
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
    color: #21325b;
    border-bottom: 1px solid #edf1f7;
}

.menu-item:last-child {
    border-bottom: none;
}

/* ===== Main section ===== */
.main-panel {
    flex: 1;
}

/* ===== KPI Cards ===== */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin-bottom: 26px;
}

.kpi-card {
    color: white;
    border-radius: 12px;
    padding: 18px 22px;
    display: flex;
    align-items: center;
    gap: 14px;
    min-height: 92px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
}

.kpi-icon {
    font-size: 27px;
    width: 46px;
    height: 46px;
    border-radius: 10px;
    background: rgba(255,255,255,0.15);
    display: flex;
    align-items: center;
    justify-content: center;
}

.kpi-title {
    font-size: 16px;
    font-weight: 600;
    opacity: 0.95;
    margin-bottom: 2px;
}

.kpi-value {
    font-size: 24px;
    font-weight: 800;
}

.blue-card {
    background: linear-gradient(90deg, #0a43bf 0%, #1157e6 100%);
}

.blue-dark-card {
    background: linear-gradient(90deg, #0a2f89 0%, #09306f 100%);
}

.orange-card {
    background: linear-gradient(90deg, #ef9b20 0%, #f5b73f 100%);
}

.navy-card {
    background: linear-gradient(90deg, #081d4e 0%, #10255e 100%);
}

/* ===== Bloques blancos ===== */
.white-box {
    background: white;
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
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
    border: 1px solid #d7dfea;
    color: #30466f;
    background: white;
    padding: 9px 20px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 15px;
}

/* ===== Tabla ===== */
.table-wrap {
    border: 1px solid #eef2f7;
    border-radius: 10px;
    overflow: hidden;
}

.table-header, .table-row {
    display: grid;
    grid-template-columns: 2.3fr 1.2fr 1fr 1fr;
    align-items: center;
}

.table-header {
    background: #f0f4fa;
    color: #32425f;
    font-weight: 700;
    font-size: 16px;
}

.table-header div, .table-row div {
    padding: 16px 18px;
}

.table-row {
    background: white;
    border-top: 1px solid #edf1f7;
    color: #243553;
    font-size: 16px;
}

.status-pill {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 700;
    color: white;
}

.pill-blue {
    background: #0c58dc;
}

.pill-blue2 {
    background: #2156b3;
}

.pill-orange {
    background: #f2a129;
}

.pill-orange2 {
    background: #e3911a;
}

/* ===== Bottom section ===== */
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
    margin-bottom: 18px;
}

.chart-area {
    height: 270px;
    display: flex;
    align-items: end;
    gap: 14px;
    padding: 20px 8px 10px 8px;
    border-top: 1px solid #edf1f7;
}

.bar {
    width: 38px;
    border-radius: 8px 8px 0 0;
}

.bar-blue { background: #0a43bf; }
.bar-blue2 { background: #235fcb; }
.bar-blue3 { background: #5f8fdc; }
.bar-orange { background: #f1a22b; }

.chart-legend {
    display: flex;
    gap: 22px;
    margin-top: 10px;
    font-weight: 600;
    color: #223660;
    flex-wrap: wrap;
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

/* ===== Pie decorativo ===== */
.pie-wrap {
    display: flex;
    justify-content: center;
    align-items: center;
}

.pie-chart {
    width: 170px;
    height: 170px;
    border-radius: 50%;
    background: conic-gradient(#0a43bf 0deg 250deg, #f1a22b 250deg 360deg);
    position: relative;
    box-shadow: inset 0 0 0 0 rgba(0,0,0,0.08);
}

.pie-chart::after {
    content: "";
    position: absolute;
    inset: 38px;
    background: white;
    border-radius: 50%;
}

.pie-center {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    font-weight: 800;
    color: #17326a;
    z-index: 2;
}

/* ===== Actividad ===== */
.activity-list {
    margin: 0;
    padding-left: 0;
    list-style: none;
    border-top: 1px solid #edf1f7;
}

.activity-list li {
    padding: 16px 0;
    border-bottom: 1px solid #edf1f7;
    color: #273a60;
    font-size: 17px;
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

/* ===== Responsive ===== */
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
    .kpi-grid {
        grid-template-columns: 1fr;
    }

    .table-header, .table-row {
        grid-template-columns: 1fr;
    }

    .topbar {
        flex-direction: column;
        gap: 16px;
        align-items: flex-start;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# HTML PRINCIPAL
# =========================
st.markdown("""
<div class="main-wrapper">

    <!-- Header -->
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

    <!-- Body -->
    <div class="content-area">

        <!-- Sidebar -->
        <div class="left-menu">
            <div class="menu-header">🗂️ &nbsp; Panel Principal</div>
            <div class="menu-item">📅 &nbsp; Mis Licitaciones</div>
            <div class="menu-item">🗃️ &nbsp; Historial</div>
            <div class="menu-item">✉️ &nbsp; Documentos</div>
            <div class="menu-item">⚙️ &nbsp; Configuración</div>
        </div>

        <!-- Main -->
        <div class="main-panel">

            <!-- KPIs -->
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

                <div class="kpi-card blue-dark-card">
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

            <!-- Tabla resumen -->
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

            <!-- Parte inferior -->
            <div class="bottom-grid">

                <div class="white-box">
                    <div class="box-title">📊 Estadísticas</div>

                    <div style="display:grid; grid-template-columns: 1.3fr 1fr; gap: 16px; align-items:center;">
                        <div>
                            <div class="chart-area">
                                <div class="bar bar-blue" style="height: 150px;"></div>
                                <div class="bar bar-blue2" style="height: 95px;"></div>
                                <div class="bar bar-blue" style="height: 135px;"></div>
                                <div class="bar bar-orange" style="height: 110px;"></div>
                                <div class="bar bar-blue2" style="height: 105px;"></div>
                                <div class="bar bar-blue3" style="height: 62px;"></div>
                                <div class="bar bar-blue" style="height: 42px;"></div>
                                <div class="bar bar-orange" style="height: 10px;"></div>
                            </div>

                            <div class="chart-legend">
                                <div class="legend-item">
                                    <div class="legend-color" style="background:#0a43bf;"></div>
                                    <div>Propuestas Recibidas</div>
                                </div>
                                <div class="legend-item">
                                    <div class="legend-color" style="background:#f1a22b;"></div>
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
""", unsafe_allow_html=True)
