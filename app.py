import streamlit as st
import pandas as pd
from pathlib import Path
import html as ihtml

# =========================================
# CONFIG
# =========================================
st.set_page_config(
    page_title="Panel de Oportunidades",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
# =========================================
# CSS GENERAL
# =========================================
st.markdown("""
<style>






#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}




.filters-box {
    background: #f1f3f7;
    padding: 26px 28px;
    border-radius: 16px;
    margin-top: 18px;
    margin-bottom: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}

div[data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within {
    border: 1px solid #2d4de2 !important;
    box-shadow: 0 0 0 2px rgba(45, 77, 226, 0.15);
}




/* TEXTO DEL VALOR SELECCIONADO */
div[data-testid="stSelectbox"] [data-baseweb="select"] span {
    color: #1f2a44 !important;  /* oscuro elegante */
    font-weight: 600 !important;
}






div[data-testid="stSelectbox"] [data-baseweb="select"] > div:hover {
    border: 1px solid #cfd6e6 !important;
}




div[data-testid="stSelectbox"] label {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    margin-bottom: 6px !important;
}






/* CAJA DEL SELECT */
div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
    background: #ffffff !important;
    border-radius: 12px !important;
    border: 1px solid #e3e7ef !important;
    min-height: 52px !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

/* TEXTO */
div[data-testid="stSelectbox"] span {
    color: #5b6178 !important;
    font-size: 15px !important;
}

.block-container {
    padding-top: 0 !important;
    padding-bottom: 1.2rem !important;
    padding-left: 1.2rem !important;
    padding-right: 1.2rem !important;
    max-width: 100% !important;
}

.stApp {
    background: linear-gradient(180deg, #16004a 0%, #2a1393 100%);
}

html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

.topbar {
    width: 100%;
    max-width: 100%;
    margin: 0;
    background: linear-gradient(90deg, #032a84 0%, #0b47c2 100%);
    color: white;
    border-radius: 0;
    padding: 22px 34px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: none;
}


.main-shell {
    width: 100%;
    max-width: 1460px;
    margin: 14px auto 24px auto;
    overflow: hidden;
}

.brand-wrap {
    display: flex;
    align-items: center;
    gap: 14px;
}

.brand-icon {
    font-size: 34px;
}

.brand-title {
    font-size: 21px;
    font-weight: 800;
    line-height: 1.0;
}

.nav-wrap {
    display: flex;
    gap: 34px;
    align-items: center;
}

.nav-item {
    color: white;
    font-size: 17px;
    font-weight: 700;
    position: relative;
}

.nav-item.active::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -10px;
    width: 100%;
    height: 2px;
    background: #e87222;
    border-radius: 10px;
}

.user-wrap {
    display: flex;
    align-items: center;
    gap: 14px;
    color: white;
    font-size: 16px;
    font-weight: 700;
}

.user-badge {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #f6d8c2;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border: 2px solid rgba(255,255,255,0.65);
}

.dashboard-body {
    width: 100%;
    max-width: 100%;
    margin: 0;
    background: transparent;
    padding: 22px;
    border-radius: 0;
    box-shadow: none;
}



.kpi-card {
    border-radius: 16px;
    padding: 18px 20px;
    color: white;
    min-height: 92px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.12);
}

.kpi-blue {
    background: linear-gradient(90deg, #2d4de2 0%, #3d59d3 100%);
}

.kpi-blue2 {
    background: linear-gradient(90deg, #2e43d4 0%, #4052d7 100%);
}

.kpi-orange {
    background: linear-gradient(90deg, #e87222 0%, #f0b349 100%);
}

.kpi-navy {
    background: linear-gradient(90deg, #141414 0%, #232a74 100%);
}

.kpi-top {
    display: flex;
    align-items: center;
    gap: 12px;
}

.kpi-icon {
    width: 46px;
    height: 46px;
    border-radius: 12px;
    background: rgba(255,255,255,0.14);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
}

.kpi-title {
    font-size: 16px;
    font-weight: 700;
    opacity: 0.98;
}

.kpi-value {
    font-size: 24px;
    font-weight: 800;
    margin-top: 6px;
}

.white-box {
    background: white;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 5px 16px rgba(0,0,0,0.07);
    border: 1px solid #e9eef6;
}

.section-title {
    font-size: 22px;
    font-weight: 800;
    color: #17326a;
    margin-bottom: 16px;
}

.mini-btn {
    border: 1px solid #d6deea;
    background: white;
    color: #30466f;
    padding: 9px 16px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 14px;
    text-align: center;
}

.table-wrap {
    border: 1px solid #edf2f8;
    border-radius: 10px;
    overflow: hidden;
}

.table-header, .table-row {
    display: grid;
    grid-template-columns: 2.5fr 1.3fr 1.3fr 1fr;
    align-items: center;
}

.table-header {
    background: #eff4fa;
    color: #30415f;
    font-weight: 700;
    font-size: 15px;
}

.table-header div, .table-row div {
    padding: 15px 18px;
}

.table-row {
    border-top: 1px solid #edf1f7;
    color: #27395f;
    background: white;
    font-size: 15px;
}

.status-pill {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 8px;
    color: white;
    font-size: 13px;
    font-weight: 700;
}

.pill-blue { background: #2f53d8; }
.pill-blue2 { background: #3950b9; }
.pill-orange { background: #e8a035; }
.pill-orange2 { background: #d88c27; }
.pill-navy { background: #111111; }
.pill-gray { background: #7b88a5; }

.stat-card {
    background: white;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 5px 16px rgba(0,0,0,0.07);
    border: 1px solid #e9eef6;
    height: 100%;
}

.stat-title {
    font-size: 20px;
    font-weight: 800;
    color: #17326a;
    margin-bottom: 14px;
}

.bar-zone {
    height: 220px;
    display: flex;
    align-items: end;
    gap: 12px;
    padding: 10px 6px 0 6px;
    border-top: 1px solid #edf1f7;
}

.bar {
    width: 42px;
    border-radius: 8px 8px 0 0;
}

.bar-blue { background: #2d4de2; }
.bar-blue2 { background: #4155c9; }
.bar-blue3 { background: #8ca0ea; }
.bar-orange { background: #e87222; }
.bar-orange2 { background: #f0b349; }
.bar-navy { background: #111111; }

.legend-row {
    display: flex;
    gap: 18px;
    flex-wrap: wrap;
    margin-top: 14px;
    color: #223660;
    font-weight: 600;
    font-size: 14px;
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

.activity-list {
    list-style: none;
    padding-left: 0;
    margin: 0;
    border-top: 1px solid #edf1f7;
}

.activity-list li {
    padding: 14px 0;
    border-bottom: 1px solid #edf1f7;
    font-size: 16px;
    color: #27395f;
    line-height: 1.4;
}

.activity-list li:last-child {
    border-bottom: none;
}

.dot {
    color: #2d4de2;
    font-weight: 900;
    margin-right: 10px;
}

@media (max-width: 1100px) {
    .nav-wrap {
        display: none;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================
# CARGA DE DATOS
# =========================================
archivo = Path(__file__).parent / "data" / "APLICACION LICITACIONES.xlsx"
df = pd.read_excel(archivo)
df.columns = df.columns.str.strip()

df = df.rename(columns={
    "NUMERO DE LA LICITACIÓN": "licitacion",
    "CONVOCANTE": "convocante",
    "ESTADO": "estado",
    "TIPO": "tipo",
    "ESTATUS DE LA LICITACION": "estatus",
    "GANADA / PERDIDA": "resultado",
    "ELABORO": "elaboro",
    "FALLO": "fallo"
})

fechas_cols = [
    "PUBLICACION",
    "ENVIO DE PREGUNTAS",
    "JUNTA ACLARACIONES",
    "PROPUESTA ECONOMICA",
    "FALLO",
    "VIGENCIA LICITACION INICIO",
    "VIGENCIA LICITACION TERMINO"
]

for col in fechas_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

for col in ["tipo", "convocante", "estado", "estatus", "resultado", "elaboro", "licitacion"]:
    if col in df.columns:
        df[col] = df[col].fillna("").astype(str).str.strip()

# =========================================
# FUNCIONES
# =========================================
def limpiar(v):
    if pd.isna(v):
        return ""
    s = str(v).strip()
    if s.lower() == "nan":
        return ""
    return s

def formatear_fecha(v):
    if pd.isna(v):
        return "-"
    try:
        return pd.to_datetime(v).strftime("%d %b %Y")
    except Exception:
        return str(v)

def detectar_en_curso(row):
    extra = row.get("INFORMACIÓN DE GRAFICAS (RESULTADO)", "")
    texto = " ".join([
        limpiar(row.get("estatus", "")),
        limpiar(row.get("resultado", "")),
        limpiar(extra)
    ]).upper()
    claves = ["CURSO", "PROCESO", "EVALUACION", "EVALUACIÓN", "ABIERTA", "ACTIVA", "VIGENTE"]
    return any(k in texto for k in claves)

def detectar_ganada(row):
    extra = row.get("INFORMACIÓN DE GRAFICAS (RESULTADO)", "")
    texto = " ".join([
        limpiar(row.get("resultado", "")),
        limpiar(extra)
    ]).upper()
    return "GANAD" in texto or "ADJUDIC" in texto

def detectar_perdida(row):
    extra = row.get("INFORMACIÓN DE GRAFICAS (RESULTADO)", "")
    texto = " ".join([
        limpiar(row.get("resultado", "")),
        limpiar(extra)
    ]).upper()
    return "PERDID" in texto or "NO ADJUDIC" in texto or "DESECHAD" in texto or "CANCEL" in texto

def badge_estado(row):
    estatus = limpiar(row.get("estatus", ""))
    resultado = limpiar(row.get("resultado", ""))
    extra = limpiar(row.get("INFORMACIÓN DE GRAFICAS (RESULTADO)", ""))
    texto = " ".join([estatus, resultado, extra]).upper()

    if "GANAD" in texto or "ADJUDIC" in texto:
        return "Adjudicada", "pill-orange"
    if "PERDID" in texto or "DESECHAD" in texto or "CANCEL" in texto:
        return "Cerrada", "pill-navy"
    if "ABIERTA" in texto:
        return "Abierta", "pill-orange2"
    if "OFERTA" in texto or "COTIZ" in texto:
        return "Recepción de Ofertas", "pill-blue2"
    if "EVALU" in texto or "PROCESO" in texto or "CURSO" in texto or "VIGENTE" in texto:
        return "En Evaluación", "pill-blue"
    return "Sin estatus", "pill-gray"

# =========================================


st.markdown('<div class="main-shell">', unsafe_allow_html=True)


# HEADER
# =========================================
st.markdown("""
<div class="topbar">
<div class="brand-wrap">
<div class="brand-icon">📄</div>
<div class="brand-title">Panel de<br>Oportunidades</div>
</div>

<div class="nav-wrap">
<div class="nav-item active">Inicio</div>
<div class="nav-item">Procesos</div>
<div class="nav-item">Reportes</div>
</div>

<div class="user-wrap">
<div>🔔 Notificaciones</div>
<div class="user-badge">👩🏻</div>
<div>Usuario ▾</div>
</div>
</div>
""", unsafe_allow_html=True)

# =========================================
# ABRIR CUERPO
# =========================================
st.markdown('<div class="dashboard-body">', unsafe_allow_html=True)

# =========================================



st.markdown('<div class="filters-box">', unsafe_allow_html=True)

# FILTROS
# =========================================
f1, f2, f3, f4 = st.columns(4)

with f1:
    tipo_filtro = st.selectbox("Tipo", ["Todos"] + sorted([x for x in df["tipo"].unique().tolist() if x != ""]))

with f2:
    convocante_filtro = st.selectbox("Convocante", ["Todos"] + sorted([x for x in df["convocante"].unique().tolist() if x != ""]))

with f3:
    estado_filtro = st.selectbox("Estado", ["Todos"] + sorted([x for x in df["estado"].unique().tolist() if x != ""]))

with f4:
    elaboro_filtro = st.selectbox("Elaboró", ["Todos"] + sorted([x for x in df["elaboro"].unique().tolist() if x != ""]))

df_filtrado = df.copy()
if tipo_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo"] == tipo_filtro]
if convocante_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["convocante"] == convocante_filtro]
if estado_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["estado"] == estado_filtro]
if elaboro_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["elaboro"] == elaboro_filtro]





st.markdown('</div>', unsafe_allow_html=True)


# =========================================
# KPIS
# =========================================
procesos_totales = len(df_filtrado)
en_curso = int(df_filtrado.apply(detectar_en_curso, axis=1).sum())
ganadas = int(df_filtrado.apply(detectar_ganada, axis=1).sum())
perdidas = int(df_filtrado.apply(detectar_perdida, axis=1).sum())

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
<div class="kpi-card kpi-blue">
<div class="kpi-top">
<div class="kpi-icon">☑️</div>
<div class="kpi-title">Procesos Totales</div>
</div>
<div class="kpi-value">{procesos_totales}</div>
</div>
""", unsafe_allow_html=True)

with k2:
    st.markdown(f"""
<div class="kpi-card kpi-blue2">
<div class="kpi-top">
<div class="kpi-icon">⚖️</div>
<div class="kpi-title">En Curso</div>
</div>
<div class="kpi-value">{en_curso}</div>
</div>
""", unsafe_allow_html=True)

with k3:
    st.markdown(f"""
<div class="kpi-card kpi-orange">
<div class="kpi-top">
<div class="kpi-icon">📁</div>
<div class="kpi-title">Ganadas</div>
</div>
<div class="kpi-value">{ganadas}</div>
</div>
""", unsafe_allow_html=True)

with k4:
    st.markdown(f"""
<div class="kpi-card kpi-navy">
<div class="kpi-top">
<div class="kpi-icon">➖</div>
<div class="kpi-title">Perdidas</div>
</div>
<div class="kpi-value">{perdidas}</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)

# =========================================
# TABLA RESUMEN
# =========================================
df_tabla = df_filtrado.copy()
if "fallo" in df_tabla.columns:
    df_tabla = df_tabla.sort_values(by="fallo", ascending=True, na_position="last")
elif "PUBLICACION" in df_tabla.columns:
    df_tabla = df_tabla.sort_values(by="PUBLICACION", ascending=False, na_position="last")

df_tabla = df_tabla.head(6)

filas_html = ""
for _, row in df_tabla.iterrows():
    titulo = ihtml.escape(limpiar(row.get("licitacion", "")) or "Sin identificador")
    estado_badge, badge_class = badge_estado(row)
    referencia = ihtml.escape(limpiar(row.get("tipo", "")) or "-")
    cierre = ihtml.escape(formatear_fecha(row.get("fallo", "")))

    filas_html += f"""
<div class="table-row">
<div>{titulo}</div>
<div><span class="status-pill {badge_class}">{estado_badge}</span></div>
<div>{referencia}</div>
<div>{cierre}</div>
</div>
"""

st.markdown(f"""
<div class="white-box">
<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:18px;">
<div class="section-title" style="margin-bottom:0;">Resumen de Oportunidades</div>
<div class="mini-btn">Vista actual</div>
</div>

<div class="table-wrap">
<div class="table-header">
<div>Proceso</div>
<div>Estado</div>
<div>Referencia</div>
<div>Cierre</div>
</div>
{filas_html}
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)

# =========================================
# ESTADÍSTICAS
# =========================================
tipos_resumen = (
    df_filtrado["tipo"]
    .replace("", pd.NA)
    .dropna()
    .value_counts()
    .head(6)
)

bars_html = ""
max_val = tipos_resumen.max() if not tipos_resumen.empty else 1
colores_barras = ["bar-blue", "bar-blue2", "bar-orange", "bar-blue3", "bar-navy", "bar-orange2"]

if not tipos_resumen.empty:
    for i, (_, valor) in enumerate(tipos_resumen.items()):
        altura = max(18, int((valor / max_val) * 160))
        clase = colores_barras[i % len(colores_barras)]
        bars_html += f'<div class="bar {clase}" style="height:{altura}px;"></div>'
else:
    bars_html = '<div class="bar bar-blue" style="height:20px;"></div>'

# =========================================
# ACTIVIDADES
# =========================================
actividades = []
for _, row in df_filtrado.iterrows():
    lic = limpiar(row.get("licitacion", "")) or "Proceso sin nombre"
    for col in ["ENVIO DE PREGUNTAS", "JUNTA ACLARACIONES", "PROPUESTA ECONOMICA", "FALLO"]:
        if col in df_filtrado.columns and pd.notnull(row.get(col)):
            actividades.append({
                "licitacion": lic,
                "evento": col.replace("_", " ").title(),
                "fecha": pd.to_datetime(row.get(col), errors="coerce")
            })

df_act = pd.DataFrame(actividades)

actividad_items = ""
if not df_act.empty:
    df_act = df_act.dropna(subset=["fecha"]).sort_values("fecha").head(5)
    for _, row in df_act.iterrows():
        evento = ihtml.escape(str(row["evento"]))
        lic = ihtml.escape(str(row["licitacion"]))
        fecha = row["fecha"].strftime("%d %b %Y")
        actividad_items += f'<li><span class="dot">●</span>{evento}: “{lic}” — {fecha}</li>'
else:
    actividad_items = '<li><span class="dot">●</span>No hay actividades próximas registradas.</li>'

c1, c2 = st.columns([1.35, 1])

with c1:
    st.markdown(f"""
<div class="stat-card">
<div class="stat-title">📊 Estadísticas</div>
<div class="bar-zone">
{bars_html}
</div>
<div class="legend-row">
<div class="legend-item">
<div class="legend-color" style="background:#2d4de2;"></div>
<div>Procesos por tipo</div>
</div>
<div class="legend-item">
<div class="legend-color" style="background:#e87222;"></div>
<div>Enfoque Werfen</div>
</div>
<div class="legend-item">
<div class="legend-color" style="background:#111111;"></div>
<div>Cierre</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""
<div class="stat-card">
<div class="stat-title">Última Actividad</div>
<ul class="activity-list">
{actividad_items}
</ul>
</div>
""", unsafe_allow_html=True)

# =========================================
# CERRAR CUERPO
# =========================================
st.markdown("</div>", unsafe_allow_html=True)

# =========================================
# DETALLE OPCIONAL
# =========================================
with st.expander("Ver tabla detallada"):
    columnas_mostrar = ["tipo", "licitacion", "convocante", "estado", "estatus", "resultado", "fallo", "elaboro"]
    columnas_existentes = [c for c in columnas_mostrar if c in df_filtrado.columns]
    st.dataframe(df_filtrado[columnas_existentes], use_container_width=True)

with st.expander("Ver actividades detalladas"):
    if not df_act.empty:
        st.dataframe(df_act, use_container_width=True)
    else:
        st.info("No hay actividades registradas.")



st.markdown("</div>", unsafe_allow_html=True)  # dashboard-body
st.markdown("</div>", unsafe_allow_html=True)  # main-shell
