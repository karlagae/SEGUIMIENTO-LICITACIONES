import streamlit as st
import pandas as pd
from pathlib import Path
import html as ihtml

# =========================================
# CONFIG
# =========================================
st.set_page_config(
    page_title="PANEL DE OPORTUNIDADES",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================
# CSS GENERAL
# =========================================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

.block-container {
    padding-top: 0 !important;
    padding-bottom: 1.2rem !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    max-width: 100% !important;
}

.stApp {
    background: #F5F6FA;
}

/* ---- TOPBAR ---- */
.topbar {
    width: 100%;
    background: #06038D;
    color: white;
    padding: 16px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid rgba(255,255,255,0.12);
}

.brand-wrap {
    display: flex;
    align-items: center;
    gap: 10px;
}

.brand-icon {
    width: 34px;
    height: 34px;
    background: #E87722;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
}

.brand-title {
    font-size: 16px;
    font-weight: 700;
    color: white;
    line-height: 1.2;
}

.nav-wrap {
    display: flex;
    gap: 28px;
    align-items: center;
}

.nav-item {
    color: rgba(255,255,255,0.7);
    font-size: 14px;
    font-weight: 600;
    padding-bottom: 3px;
}

.nav-item.active {
    color: white;
    border-bottom: 2px solid #E87722;
}

.user-wrap {
    display: flex;
    align-items: center;
    gap: 14px;
    color: white;
    font-size: 13px;
    font-weight: 600;
}

.notif-wrap {
    display: flex;
    align-items: center;
    gap: 5px;
    color: rgba(255,255,255,0.8);
    font-size: 13px;
}

.notif-dot {
    width: 7px;
    height: 7px;
    background: #E87722;
    border-radius: 50%;
    display: inline-block;
}

.user-badge {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: #f5d5b8;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    border: 2px solid rgba(255,255,255,0.4);
}

/* ---- BODY ---- */
.dashboard-body {
    background: #F5F6FA;
    padding: 22px 28px;
}

/* ---- FILTROS (selectbox de streamlit) ---- */
div[data-testid="stSelectbox"] label {
    color: #3d3b80 !important;
    font-weight: 700 !important;
    font-size: 11px !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 5px !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
    background: #ffffff !important;
    border-radius: 8px !important;
    border: 1px solid #E8EAF0 !important;
    min-height: 42px !important;
    box-shadow: none !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within {
    border: 1px solid #E87722 !important;
    box-shadow: 0 0 0 2px rgba(232,119,34,0.15) !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] span {
    color: #0a0850 !important;
    font-weight: 500 !important;
    font-size: 13px !important;
}

/* ---- KPI CARDS ---- */
.kpi-card {
    border-radius: 12px;
    padding: 16px 18px;
    color: white;
    min-height: 82px;
    display: flex;
    align-items: center;
    gap: 14px;
}

.kpi-total  { background: #06038D; }
.kpi-curso  { background: #2e2cbe; }
.kpi-ganadas { background: #E87722; }
.kpi-perdidas { background: #000000; }

.kpi-icon {
    width: 42px;
    height: 42px;
    border-radius: 8px;
    background: rgba(255,255,255,0.16);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
}

.kpi-label {
    font-size: 11px;
    color: rgba(255,255,255,0.82);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.kpi-value {
    font-size: 28px;
    font-weight: 800;
    color: white;
    line-height: 1.1;
    margin-top: 2px;
}

/* ---- CARD BLANCA ---- */
.card {
    background: white;
    border-radius: 12px;
    border: 1px solid #E8EAF0;
    padding: 20px;
    margin-bottom: 18px;
}

.card-title {
    font-size: 15px;
    font-weight: 700;
    color: #0a0850;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid #E8EAF0;
    padding-bottom: 12px;
}

.card-title-accent {
    width: 4px;
    height: 18px;
    background: #E87722;
    border-radius: 2px;
    flex-shrink: 0;
}

/* ---- TABLA RESUMEN ---- */
.table-wrap {
    border: 1px solid #E8EAF0;
    border-radius: 8px;
    overflow: hidden;
}

.table-header.summary-9, .table-row.summary-9 {
    display: grid;
    grid-template-columns: 1.1fr 1.8fr 1fr 1.1fr 1fr 1fr 1fr 1fr 1fr;
    align-items: center;
}

.table-header {
    background: #F0F2F9;
    color: #3d3b80;
    font-weight: 700;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.table-header div, .table-row div {
    padding: 10px 14px;
}

.table-row {
    border-top: 1px solid #E8EAF0;
    color: #0a0850;
    background: white;
    font-size: 13px;
    transition: background 0.15s;
}

.table-row:hover {
    background: #F8F9FD;
}

/* ---- BADGES ESPECIALIDAD ---- */
.badge {
    display: inline-block;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
}

.badge-lab      { background: #EEEEFF; color: #06038D; }
.badge-bs       { background: #FFF0E6; color: #a84e0a; }
.badge-cardio   { background: #E6F4FF; color: #0a5490; }
.badge-default  { background: #F0F2F9; color: #3d3b80; }

/* ---- PILLS ESTATUS ---- */
.pill {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
}

.pill-proceso    { background: #EEEEFF; color: #06038D; }
.pill-adjudicada { background: #FFF0E6; color: #a84e0a; }
.pill-cerrada    { background: #F0F0F0; color: #333333; }
.pill-abierta    { background: #E6FFE6; color: #1a6e1a; }
.pill-oferta     { background: #FFF8E6; color: #8a6000; }
.pill-sin        { background: #F0F2F9; color: #888; }

.tipo-tag {
    font-size: 11px;
    font-weight: 600;
    color: #3d3b80;
}

.integ-tag {
    font-size: 12px;
    font-weight: 600;
    color: #E87722;
}

.fecha-tag {
    font-size: 12px;
    color: #0a0850;
}

.lic-num {
    font-size: 11px;
    font-weight: 600;
    color: #06038D;
    word-break: break-all;
}

/* ---- BARRAS INTEGRADOR ---- */
.stat-card {
    background: white;
    border-radius: 12px;
    border: 1px solid #E8EAF0;
    padding: 20px;
    height: 100%;
}

.stat-title {
    font-size: 15px;
    font-weight: 700;
    color: #0a0850;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid #E8EAF0;
    padding-bottom: 12px;
}

.bar-zone {
    height: 200px;
    display: flex;
    align-items: flex-end;
    gap: 14px;
    padding: 10px 6px 0 6px;
    border-bottom: 2px solid #E8EAF0;
    overflow-x: auto;
}

.bar { border-radius: 4px 4px 0 0; }
.bar-naranja { background: #E87722; }
.bar-azul    { background: #06038D; }

/* ---- ACTIVIDADES ---- */
.activity-list {
    list-style: none;
    padding-left: 0;
    margin: 0;
}

.activity-list li {
    padding: 10px 0;
    border-bottom: 1px solid #E8EAF0;
    font-size: 12px;
    color: #0a0850;
    line-height: 1.4;
    display: flex;
    align-items: flex-start;
    gap: 8px;
}

.activity-list li:last-child { border-bottom: none; }

.dot {
    color: #E87722;
    font-weight: 900;
    font-size: 10px;
    margin-top: 2px;
    flex-shrink: 0;
}

.act-fecha {
    font-size: 11px;
    color: #3d3b80;
    margin-top: 2px;
}

@media (max-width: 1100px) {
    .nav-wrap { display: none; }
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
    "ESPECIALIDAD\nSERV.INT (LAB)\nSER.INT (BS)\nSERV.INT (CARDIO)": "especialidad",
    "DISTRIBUIDOR ACTUAL": "integrador",
    "JUNTA ACLARACIONES": "junta_aclaraciones",
    "PRESENT. TECNICA": "present_tecnica",
    "FALLO": "fallo",
    "ESTATUS DE LA LICITACION": "estatus",
    "GANADA / PERDIDA": "resultado"
})

# Fechas
for col in ["junta_aclaraciones", "fallo", "present_tecnica"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# Limpieza de texto
for col in ["tipo", "licitacion", "especialidad", "convocante", "integrador", "estatus", "resultado"]:
    if col in df.columns:
        df[col] = df[col].fillna("").astype(str).str.strip()

# =========================================
# FUNCIONES
# =========================================
def limpiar(v):
    if pd.isna(v):
        return ""
    s = str(v).strip()
    return "" if s.lower() == "nan" else s

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
    texto = " ".join([limpiar(row.get("resultado", "")), limpiar(extra)]).upper()
    return "GANAD" in texto or "ADJUDIC" in texto

def detectar_perdida(row):
    extra = row.get("INFORMACIÓN DE GRAFICAS (RESULTADO)", "")
    texto = " ".join([limpiar(row.get("resultado", "")), limpiar(extra)]).upper()
    return "PERDID" in texto or "NO ADJUDIC" in texto or "DESECHAD" in texto or "CANCEL" in texto

def badge_especialidad(esp):
    e = esp.upper()
    if "LAB" in e:
        return f'<span class="badge badge-lab">{ihtml.escape(esp) or "—"}</span>'
    if "SANGRE" in e or "BS" in e:
        return f'<span class="badge badge-bs">{ihtml.escape(esp) or "—"}</span>'
    if "CARDIO" in e:
        return f'<span class="badge badge-cardio">{ihtml.escape(esp) or "—"}</span>'
    if esp and esp != "-":
        return f'<span class="badge badge-default">{ihtml.escape(esp)}</span>'
    return '<span style="color:#aaa">—</span>'

def badge_estatus(row):
    estatus = limpiar(row.get("estatus", ""))
    resultado = limpiar(row.get("resultado", ""))
    extra = limpiar(row.get("INFORMACIÓN DE GRAFICAS (RESULTADO)", ""))
    texto = " ".join([estatus, resultado, extra]).upper()

    if "GANAD" in texto or "ADJUDIC" in texto:
        return '<span class="pill pill-adjudicada">Adjudicada</span>'
    if "PERDID" in texto or "DESECHAD" in texto or "CANCEL" in texto:
        return '<span class="pill pill-cerrada">Cerrada</span>'
    if "TERMINADA" in texto:
        return '<span class="pill pill-cerrada">Terminada</span>'
    if "ABIERTA" in texto:
        return '<span class="pill pill-abierta">Abierta</span>'
    if "OFERTA" in texto or "COTIZ" in texto:
        return '<span class="pill pill-oferta">Rec. Ofertas</span>'
    if "EVALU" in texto or "PROCESO" in texto or "CURSO" in texto or "VIGENTE" in texto:
        return '<span class="pill pill-proceso">En proceso</span>'
    return '<span class="pill pill-sin">Sin estatus</span>'

# =========================================
# TOPBAR
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
    <div class="notif-wrap"><span class="notif-dot"></span> Notificaciones</div>
    <div class="user-badge">👤</div>
    <span>Usuario ▾</span>
  </div>
</div>
""", unsafe_allow_html=True)

# =========================================
# BODY
# =========================================
st.markdown('<div class="dashboard-body">', unsafe_allow_html=True)

# =========================================
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
    integrador_filtro = st.selectbox("Integrador", ["Todos"] + sorted([x for x in df["integrador"].unique().tolist() if x != ""]))

df_filtrado = df.copy()
if tipo_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo"] == tipo_filtro]
if convocante_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["convocante"] == convocante_filtro]
if estado_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["estado"] == estado_filtro]
if integrador_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["integrador"] == integrador_filtro]

st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

# =========================================
# KPIs
# =========================================
procesos_totales = len(df_filtrado)
en_curso  = int(df_filtrado.apply(detectar_en_curso, axis=1).sum())
ganadas   = int(df_filtrado.apply(detectar_ganada, axis=1).sum())
perdidas  = int(df_filtrado.apply(detectar_perdida, axis=1).sum())

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
<div class="kpi-card kpi-total">
  <div class="kpi-icon">📋</div>
  <div><div class="kpi-label">Procesos totales</div><div class="kpi-value">{procesos_totales}</div></div>
</div>""", unsafe_allow_html=True)

with k2:
    st.markdown(f"""
<div class="kpi-card kpi-curso">
  <div class="kpi-icon">⏳</div>
  <div><div class="kpi-label">En curso</div><div class="kpi-value">{en_curso}</div></div>
</div>""", unsafe_allow_html=True)

with k3:
    st.markdown(f"""
<div class="kpi-card kpi-ganadas">
  <div class="kpi-icon">✅</div>
  <div><div class="kpi-label">Ganadas</div><div class="kpi-value">{ganadas}</div></div>
</div>""", unsafe_allow_html=True)

with k4:
    st.markdown(f"""
<div class="kpi-card kpi-perdidas">
  <div class="kpi-icon">✖️</div>
  <div><div class="kpi-label">Perdidas</div><div class="kpi-value">{perdidas}</div></div>
</div>""", unsafe_allow_html=True)

st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

# =========================================
# TABLA RESUMEN
# =========================================
df_tabla = df_filtrado.copy()
if "fallo" in df_tabla.columns:
    df_tabla = df_tabla.sort_values(by="fallo", ascending=True, na_position="last")
df_tabla = df_tabla.head(6)

filas_html = ""
for _, row in df_tabla.iterrows():
    tipo        = ihtml.escape(limpiar(row.get("tipo", "")) or "-")
    licitacion  = ihtml.escape(limpiar(row.get("licitacion", "")) or "-")
    especialidad = limpiar(row.get("especialidad", "")) or "-"
    convocante  = ihtml.escape(limpiar(row.get("convocante", "")) or "-")
    integrador  = limpiar(row.get("integrador", ""))
    junta       = ihtml.escape(formatear_fecha(row.get("junta_aclaraciones", "")))
    present     = ihtml.escape(formatear_fecha(row.get("present_tecnica", "")))
    fallo       = ihtml.escape(formatear_fecha(row.get("fallo", "")))
    estatus_html = badge_estatus(row)
    esp_html    = badge_especialidad(especialidad)
    integ_html  = f'<span class="integ-tag">{ihtml.escape(integrador)}</span>' if integrador else '<span style="color:#aaa">—</span>'

    filas_html += f"""
<div class="table-row summary-9">
  <div><span class="tipo-tag">{tipo}</span></div>
  <div><span class="lic-num">{licitacion}</span></div>
  <div>{esp_html}</div>
  <div>{convocante}</div>
  <div>{integ_html}</div>
  <div><span class="fecha-tag">{junta}</span></div>
  <div><span class="fecha-tag">{present}</span></div>
  <div><span class="fecha-tag">{fallo}</span></div>
  <div>{estatus_html}</div>
</div>
"""

st.markdown(f"""
<div class="card">
  <div class="card-title">
    <div class="card-title-accent"></div>
    Resumen de oportunidades
  </div>
  <div class="table-wrap">
    <div class="table-header summary-9">
      <div>Tipo</div>
      <div>Número licitación</div>
      <div>Especialidad</div>
      <div>Convocante</div>
      <div>Integrador</div>
      <div>Junta</div>
      <div>Present. técnica</div>
      <div>Fallo</div>
      <div>Estatus</div>
    </div>
    {filas_html}
  </div>
</div>
""", unsafe_allow_html=True)

# =========================================
# ESTADÍSTICAS + ACTIVIDADES
# =========================================
integradores_resumen = (
    df_filtrado["integrador"]
    .replace("", "Sin asignar")
    .fillna("Sin asignar")
    .value_counts()
    .head(6)
)

bars_html = ""
max_val = integradores_resumen.max() if not integradores_resumen.empty else 1
colores = ["bar-naranja", "bar-naranja", "bar-naranja", "bar-azul", "bar-azul", "bar-azul"]

if not integradores_resumen.empty:
    for i, (nombre, valor) in enumerate(integradores_resumen.items()):
        altura = max(18, int((valor / max_val) * 150))
        color_clase = colores[i % len(colores)]
        bars_html += f"""
<div style="display:flex;flex-direction:column;align-items:center;min-width:60px;flex:1">
  <div style="font-size:13px;font-weight:700;color:#0a0850;margin-bottom:4px">{valor}</div>
  <div class="bar {color_clase}" style="height:{altura}px;width:36px"></div>
  <div style="margin-top:7px;font-size:11px;text-align:center;color:#3d3b80;line-height:1.3;font-weight:600">{ihtml.escape(str(nombre))}</div>
</div>"""
else:
    bars_html = '<div style="font-size:13px;color:#aaa">Sin datos</div>'

# Actividades
actividades = []
for _, row in df_filtrado.iterrows():
    lic = limpiar(row.get("licitacion", "")) or "Proceso sin nombre"
    conv = limpiar(row.get("convocante", ""))
    integ = limpiar(row.get("integrador", ""))
    for col, label in [
        ("JUNTA ACLARACIONES", "Junta aclaraciones"),
        ("PRESENT. TECNICA",   "Present. técnica"),
        ("FALLO",              "Fallo"),
    ]:
        val = row.get(col) if col in df_filtrado.columns else None
        if val is not None and pd.notnull(val):
            actividades.append({
                "licitacion": lic,
                "evento": label,
                "convocante": conv,
                "integrador": integ,
                "fecha": pd.to_datetime(val, errors="coerce")
            })

df_act = pd.DataFrame(actividades)

actividad_items = ""
if not df_act.empty:
    df_act = df_act.dropna(subset=["fecha"]).sort_values("fecha").head(5)
    for _, row in df_act.iterrows():
        evento  = ihtml.escape(str(row["evento"]))
        lic     = ihtml.escape(str(row["licitacion"]))
        fecha   = row["fecha"].strftime("%d %b %Y")
        conv    = ihtml.escape(str(row["convocante"]))
        integ   = ihtml.escape(str(row["integrador"]))
        meta    = " · ".join(filter(None, [conv, integ if integ else ""]))
        actividad_items += f"""
<li>
  <span class="dot">●</span>
  <div>
    <div>{evento}: <strong>{lic}</strong></div>
    <div class="act-fecha">{fecha}{(' · ' + meta) if meta else ''}</div>
  </div>
</li>"""
else:
    actividad_items = '<li><span class="dot">●</span><div>No hay actividades próximas registradas.</div></li>'

c1, c2 = st.columns([1.4, 1])

with c1:
    st.markdown(f"""
<div class="stat-card">
  <div class="stat-title">
    <div class="card-title-accent"></div>
    Procesos por integrador
  </div>
  <div class="bar-zone">
    {bars_html}
  </div>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""
<div class="stat-card">
  <div class="stat-title">
    <div class="card-title-accent"></div>
    Actividades próximas
  </div>
  <ul class="activity-list">
    {actividad_items}
  </ul>
</div>
""", unsafe_allow_html=True)

# =========================================
# CIERRE BODY
# =========================================
st.markdown("</div>", unsafe_allow_html=True)

# =========================================
# EXPANDERS DETALLE
# =========================================
st.markdown("<div style='padding:0 28px 28px 28px'>", unsafe_allow_html=True)

with st.expander("Ver tabla detallada completa"):
    columnas_mostrar = ["tipo", "licitacion", "convocante", "estado", "estatus", "resultado", "fallo", "integrador"]
    columnas_existentes = [c for c in columnas_mostrar if c in df_filtrado.columns]
    st.dataframe(df_filtrado[columnas_existentes], use_container_width=True)

with st.expander("Ver actividades detalladas"):
    if not df_act.empty:
        st.dataframe(df_act, use_container_width=True)
    else:
        st.info("No hay actividades registradas.")

st.markdown("</div>", unsafe_allow_html=True)
