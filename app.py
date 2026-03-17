import streamlit as st
import pandas as pd
from pathlib import Path
import html

st.set_page_config(
    page_title="Panel de Oportunidades",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================
# CONFIG GENERAL
# =========================================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding-top: 0rem !important;
    padding-bottom: 1rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    max-width: 100% !important;
}

.stApp {
    background: linear-gradient(180deg, #16004a 0%, #2a1393 100%);
}
</style>
""", unsafe_allow_html=True)

# =========================================
# CARGA DE DATOS
# =========================================
archivo = Path(__file__).parent / "data" / "APLICACION LICITACIONES.xlsx"
df = pd.read_excel(archivo)
df.columns = df.columns.str.strip()

# Renombrar columnas clave
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

# =========================================
# COLUMNAS DE FECHAS
# =========================================
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

# =========================================
# NORMALIZACIÓN DE TEXTO
# =========================================
for col in ["tipo", "convocante", "estado", "estatus", "resultado", "elaboro", "licitacion"]:
    if col in df.columns:
        df[col] = df[col].astype(str).replace("nan", "").fillna("")

# =========================================
# FILTROS
# =========================================
f1, f2, f3, f4 = st.columns(4)

with f1:
    tipo_filtro = st.selectbox(
        "Tipo",
        ["Todos"] + sorted([x for x in df["tipo"].dropna().unique().tolist() if str(x).strip() != ""])
    )

with f2:
    convocante_filtro = st.selectbox(
        "Convocante",
        ["Todos"] + sorted([x for x in df["convocante"].dropna().unique().tolist() if str(x).strip() != ""])
    )

with f3:
    estado_filtro = st.selectbox(
        "Estado",
        ["Todos"] + sorted([x for x in df["estado"].dropna().unique().tolist() if str(x).strip() != ""])
    )

with f4:
    elaboro_filtro = st.selectbox(
        "Elaboró",
        ["Todos"] + sorted([x for x in df["elaboro"].dropna().unique().tolist() if str(x).strip() != ""])
    )

df_filtrado = df.copy()

if tipo_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo"] == tipo_filtro]

if convocante_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["convocante"] == convocante_filtro]

if estado_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["estado"] == estado_filtro]

if elaboro_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["elaboro"] == elaboro_filtro]

# =========================================
# FUNCIONES AUXILIARES
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
        return ""
    try:
        return pd.to_datetime(v).strftime("%d %b %Y")
    except:
        return str(v)

def detectar_en_curso(row):
    texto = " ".join([
        limpiar(row.get("estatus", "")),
        limpiar(row.get("resultado", "")),
        limpiar(row.get("INFORMACIÓN DE GRAFICAS (RESULTADO)", "")) if "INFORMACIÓN DE GRAFICAS (RESULTADO)" in row else ""
    ]).upper()

    claves = ["CURSO", "PROCESO", "EVALUACION", "EVALUACIÓN", "ABIERTA", "ACTIVA", "VIGENTE"]
    return any(k in texto for k in claves)

def detectar_ganada(row):
    texto = " ".join([
        limpiar(row.get("resultado", "")),
        limpiar(row.get("INFORMACIÓN DE GRAFICAS (RESULTADO)", "")) if "INFORMACIÓN DE GRAFICAS (RESULTADO)" in row else ""
    ]).upper()
    return "GANAD" in texto or "ADJUDIC" in texto

def detectar_perdida(row):
    texto = " ".join([
        limpiar(row.get("resultado", "")),
        limpiar(row.get("INFORMACIÓN DE GRAFICAS (RESULTADO)", "")) if "INFORMACIÓN DE GRAFICAS (RESULTADO)" in row else ""
    ]).upper()
    return "PERDID" in texto or "NO ADJUDIC" in texto or "DESECHAD" in texto

def badge_estado(row):
    estatus = limpiar(row.get("estatus", ""))
    resultado = limpiar(row.get("resultado", ""))
    extra = limpiar(row.get("INFORMACIÓN DE GRAFICAS (RESULTADO)", "")) if "INFORMACIÓN DE GRAFICAS (RESULTADO)" in row else ""
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
# KPIS
# =========================================
procesos_totales = len(df_filtrado)
en_curso = int(df_filtrado.apply(detectar_en_curso, axis=1).sum())
ganadas = int(df_filtrado.apply(detectar_ganada, axis=1).sum())
perdidas = int(df_filtrado.apply(detectar_perdida, axis=1).sum())

# =========================================
# TABLA RESUMEN
# =========================================
df_tabla = df_filtrado.copy()

# ordenar por fecha de fallo si existe, si no por publicación
if "fallo" in df_tabla.columns:
    df_tabla = df_tabla.sort_values(by="fallo", ascending=True, na_position="last")
elif "PUBLICACION" in df_tabla.columns:
    df_tabla = df_tabla.sort_values(by="PUBLICACION", ascending=False, na_position="last")

df_tabla = df_tabla.head(6)

filas_html = ""

for _, row in df_tabla.iterrows():
    titulo = limpiar(row.get("licitacion", "")) or "Sin identificador"
    estado_badge, badge_class = badge_estado(row)
    propuestas = limpiar(row.get("PRESENTAR COTIZACION", ""))
    propuestas_txt = propuestas if propuestas else "-"
    cierre = formatear_fecha(row.get("fallo", "")) if "fallo" in row else ""

    filas_html += f"""
    <div class="table-row">
        <div>{html.escape(titulo)}</div>
        <div><span class="status-pill {badge_class}">{html.escape(estado_badge)}</span></div>
        <div>{html.escape(propuestas_txt)}</div>
        <div>{html.escape(cierre if cierre else "-")}</div>
    </div>
    """

# =========================================
# ACTIVIDADES PRÓXIMAS
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

if not df_act.empty:
    df_act = df_act.dropna(subset=["fecha"]).sort_values("fecha").head(5)

actividad_html = ""
if not df_act.empty:
    for _, row in df_act.iterrows():
        actividad_html += f"""
        <li><span class="dot">●</span>{html.escape(row['evento'])}: “{html.escape(row['licitacion'])}” — {row['fecha'].strftime('%d %b %Y')}</li>
        """
else:
    actividad_html = """
    <li><span class="dot">●</span>No hay actividades próximas registradas.</li>
    """

# =========================================
# ESTADÍSTICAS POR TIPO
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
        altura = max(18, int((valor / max_val) * 150))
        clase = colores_barras[i % len(colores_barras)]
        bars_html += f'<div class="bar {clase}" style="height:{altura}px;"></div>'
else:
    bars_html = '<div class="bar bar-blue" style="height:20px;"></div>'

# =========================================
# HTML DEL DASHBOARD
# =========================================
dashboard_html = f"""
<div class="main-wrapper">

    <style>
        * {{
            box-sizing: border-box;
            font-family: "Segoe UI", sans-serif;
        }}

        .main-wrapper {{
            max-width: 1320px;
            margin: 18px auto 30px auto;
            background: #f4f7fb;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 18px 34px rgba(0,0,0,0.18);
        }}

        .topbar {{
            background: linear-gradient(90deg, #1c248b 0%, #2738b2 100%);
            color: white;
            padding: 24px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .brand-section {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}

        .brand-icon {{
            font-size: 34px;
        }}

        .brand-title {{
            font-size: 21px;
            font-weight: 800;
            line-height: 1.05;
        }}

        .nav-center {{
            display: flex;
            gap: 34px;
            align-items: center;
        }}

        .nav-item {{
            font-size: 17px;
            font-weight: 600;
            position: relative;
            opacity: 0.96;
        }}

        .nav-item.active::after {{
            content: "";
            position: absolute;
            left: 0;
            bottom: -9px;
            width: 100%;
            height: 2px;
            background: #e87222;
            border-radius: 10px;
        }}

        .nav-right {{
            display: flex;
            align-items: center;
            gap: 16px;
            font-size: 16px;
            font-weight: 600;
        }}

        .user-badge {{
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: #f6d8c2;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px solid rgba(255,255,255,0.65);
        }}

        .content-area {{
            display: flex;
            gap: 24px;
            padding: 24px;
            align-items: flex-start;
            background: linear-gradient(180deg, #edf2fa 0%, #f8fbff 100%);
        }}

        .left-menu {{
            width: 240px;
            background: white;
            border-radius: 14px;
            overflow: hidden;
            border: 1px solid #e6edf6;
            box-shadow: 0 6px 18px rgba(0,0,0,0.08);
            flex-shrink: 0;
        }}

        .menu-header {{
            background: #232a91;
            color: white;
            font-weight: 800;
            padding: 18px 18px;
            font-size: 18px;
        }}

        .menu-item {{
            padding: 16px 18px;
            font-size: 17px;
            color: #21355e;
            border-bottom: 1px solid #edf1f7;
            background: white;
        }}

        .menu-item:last-child {{
            border-bottom: none;
        }}

        .main-panel {{
            flex: 1;
        }}

        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            margin-bottom: 22px;
        }}

        .kpi-card {{
            color: white;
            border-radius: 14px;
            padding: 18px 20px;
            display: flex;
            align-items: center;
            gap: 14px;
            min-height: 92px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.14);
        }}

        .blue-card {{
            background: linear-gradient(90deg, #2d4de2 0%, #3d59d3 100%);
        }}

        .blue-card-2 {{
            background: linear-gradient(90deg, #2e43d4 0%, #4052d7 100%);
        }}

        .orange-card {{
            background: linear-gradient(90deg, #e87222 0%, #f0b349 100%);
        }}

        .navy-card {{
            background: linear-gradient(90deg, #141414 0%, #232a74 100%);
        }}

        .kpi-icon {{
            width: 46px;
            height: 46px;
            border-radius: 12px;
            background: rgba(255,255,255,0.14);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 23px;
        }}

        .kpi-title {{
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 4px;
        }}

        .kpi-value {{
            font-size: 24px;
            font-weight: 800;
        }}

        .white-box {{
            background: white;
            border-radius: 14px;
            padding: 22px;
            box-shadow: 0 5px 16px rgba(0,0,0,0.07);
            border: 1px solid #e9eef6;
        }}

        .section-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 18px;
        }}

        .section-title {{
            font-size: 22px;
            font-weight: 800;
            color: #17326a;
        }}

        .small-btn {{
            border: 1px solid #d6deea;
            background: white;
            color: #30466f;
            padding: 9px 18px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 15px;
        }}

        .table-wrap {{
            border: 1px solid #edf2f8;
            border-radius: 10px;
            overflow: hidden;
        }}

        .table-header,
        .table-row {{
            display: grid;
            grid-template-columns: 2.3fr 1.2fr 1fr 1fr;
            align-items: center;
        }}

        .table-header {{
            background: #eff4fa;
            color: #30415f;
            font-weight: 700;
            font-size: 16px;
        }}

        .table-header div,
        .table-row div {{
            padding: 15px 18px;
        }}

        .table-row {{
            border-top: 1px solid #edf1f7;
            color: #27395f;
            background: white;
            font-size: 16px;
        }}

        .status-pill {{
            display: inline-block;
            padding: 6px 12px;
            border-radius: 8px;
            color: white;
            font-size: 14px;
            font-weight: 700;
        }}

        .pill-blue {{ background: #2f53d8; }}
        .pill-blue2 {{ background: #3950b9; }}
        .pill-orange {{ background: #e8a035; }}
        .pill-orange2 {{ background: #d88c27; }}
        .pill-navy {{ background: #111111; }}
        .pill-gray {{ background: #7b88a5; }}

        .bottom-grid {{
            display: grid;
            grid-template-columns: 1.35fr 1fr;
            gap: 22px;
            margin-top: 22px;
        }}

        .box-title {{
            font-size: 20px;
            font-weight: 800;
            color: #17326a;
            margin-bottom: 12px;
        }}

        .chart-layout {{
            display: grid;
            grid-template-columns: 1.35fr 1fr;
            gap: 10px;
            align-items: center;
        }}

        .chart-area {{
            height: 250px;
            display: flex;
            align-items: flex-end;
            gap: 12px;
            padding: 10px 8px 0 8px;
            border-top: 1px solid #edf1f7;
            margin-top: 8px;
        }}

        .bar {{
            width: 38px;
            border-radius: 8px 8px 0 0;
        }}

        .bar-blue {{ background: #2d4de2; }}
        .bar-blue2 {{ background: #4155c9; }}
        .bar-blue3 {{ background: #8ca0ea; }}
        .bar-orange {{ background: #e87222; }}
        .bar-orange2 {{ background: #f0b349; }}
        .bar-navy {{ background: #111111; }}

        .chart-legend {{
            display: flex;
            gap: 22px;
            flex-wrap: wrap;
            margin-top: 16px;
            font-weight: 600;
            color: #223660;
        }}

        .legend-item {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .legend-color {{
            width: 14px;
            height: 14px;
            border-radius: 3px;
        }}

        .pie-wrap {{
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .pie-chart {{
            width: 170px;
            height: 170px;
            border-radius: 50%;
            background: conic-gradient(#2d4de2 0deg 220deg, #e87222 220deg 320deg, #111111 320deg 360deg);
            position: relative;
        }}

        .pie-chart::after {{
            content: "";
            position: absolute;
            inset: 42px;
            background: white;
            border-radius: 50%;
        }}

        .pie-center {{
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 2;
            font-size: 28px;
            font-weight: 800;
            color: #17326a;
        }}

        .activity-list {{
            list-style: none;
            padding-left: 0;
            margin: 0;
            border-top: 1px solid #edf1f7;
        }}

        .activity-list li {{
            padding: 16px 0;
            border-bottom: 1px solid #edf1f7;
            font-size: 17px;
            color: #27395f;
            line-height: 1.4;
        }}

        .activity-list li:last-child {{
            border-bottom: none;
        }}

        .dot {{
            color: #2d4de2;
            font-weight: 900;
            margin-right: 10px;
        }}

        @media (max-width: 1100px) {{
            .content-area {{
                flex-direction: column;
            }}

            .left-menu {{
                width: 100%;
            }}

            .kpi-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}

            .bottom-grid {{
                grid-template-columns: 1fr;
            }}

            .nav-center {{
                display: none;
            }}
        }}

        @media (max-width: 700px) {{
            .kpi-grid {{
                grid-template-columns: 1fr;
            }}

            .table-header,
            .table-row {{
                grid-template-columns: 1fr;
            }}

            .topbar {{
                flex-direction: column;
                align-items: flex-start;
                gap: 16px;
            }}

            .chart-layout {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>

    <div class="topbar">
        <div class="brand-section">
            <div class="brand-icon">📄</div>
            <div class="brand-title">Panel de<br>Oportunidades</div>
        </div>

        <div class="nav-center">
            <div class="nav-item active">Inicio</div>
            <div class="nav-item">Procesos</div>
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
            <div class="menu-item">📅 Mis Procesos</div>
            <div class="menu-item">🗃️ Historial</div>
            <div class="menu-item">✉️ Documentos</div>
            <div class="menu-item">⚙️ Configuración</div>
        </div>

        <div class="main-panel">

            <div class="kpi-grid">
                <div class="kpi-card blue-card">
                    <div class="kpi-icon">☑️</div>
                    <div>
                        <div class="kpi-title">Procesos Totales</div>
                        <div class="kpi-value">{procesos_totales}</div>
                    </div>
                </div>

                <div class="kpi-card blue-card-2">
                    <div class="kpi-icon">⚖️</div>
                    <div>
                        <div class="kpi-title">En Curso</div>
                        <div class="kpi-value">{en_curso}</div>
                    </div>
                </div>

                <div class="kpi-card orange-card">
                    <div class="kpi-icon">📁</div>
                    <div>
                        <div class="kpi-title">Ganadas</div>
                        <div class="kpi-value">{ganadas}</div>
                    </div>
                </div>

                <div class="kpi-card navy-card">
                    <div class="kpi-icon">➖</div>
                    <div>
                        <div class="kpi-title">Perdidas</div>
                        <div class="kpi-value">{perdidas}</div>
                    </div>
                </div>
            </div>

            <div class="white-box">
                <div class="section-header">
                    <div class="section-title">Resumen de Oportunidades</div>
                    <div class="small-btn">Vista actual</div>
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

            <div class="bottom-grid">

                <div class="white-box">
                    <div class="box-title">📊 Estadísticas</div>

                    <div class="chart-layout">
                        <div>
                            <div class="chart-area">
                                {bars_html}
                            </div>

                            <div class="chart-legend">
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

                        <div class="pie-wrap">
                            <div class="pie-chart">
                                <div class="pie-center">{procesos_totales}</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="white-box">
                    <div class="box-title">Última Actividad</div>
                    <ul class="activity-list">
                        {actividad_html}
                    </ul>
                </div>

            </div>

        </div>
    </div>
</div>
"""

st.markdown(dashboard_html, unsafe_allow_html=True)

# =========================================
# TABLA DETALLADA ABAJO
# =========================================
with st.expander("Ver tabla detallada"):
    columnas_mostrar = [
        "tipo", "licitacion", "convocante", "estado",
        "estatus", "resultado", "fallo", "elaboro"
    ]
    columnas_existentes = [c for c in columnas_mostrar if c in df_filtrado.columns]
    st.dataframe(df_filtrado[columnas_existentes], use_container_width=True)

with st.expander("Ver actividades detalladas"):
    if not df_act.empty:
        st.dataframe(df_act, use_container_width=True)
    else:
        st.info("No hay actividades registradas.")
