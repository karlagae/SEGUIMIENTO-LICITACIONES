import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pathlib import Path
import html

st.set_page_config(
    page_title="Panel de Oportunidades",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================
# ESTILO GENERAL STREAMLIT
# =========================================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding-top: 0.6rem !important;
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
# FECHAS
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
# LIMPIEZA TEXTO
# =========================================
for col in ["tipo", "convocante", "estado", "estatus", "resultado", "elaboro", "licitacion"]:
    if col in df.columns:
        df[col] = df[col].fillna("").astype(str).str.strip()

# =========================================
# FILTROS
# =========================================
f1, f2, f3, f4 = st.columns(4)

with f1:
    tipo_filtro = st.selectbox(
        "Tipo",
        ["Todos"] + sorted([x for x in df["tipo"].unique().tolist() if x != ""])
    )

with f2:
    convocante_filtro = st.selectbox(
        "Convocante",
        ["Todos"] + sorted([x for x in df["convocante"].unique().tolist() if x != ""])
    )

with f3:
    estado_filtro = st.selectbox(
        "Estado",
        ["Todos"] + sorted([x for x in df["estado"].unique().tolist() if x != ""])
    )

with f4:
    elaboro_filtro = st.selectbox(
        "Elaboró",
        ["Todos"] + sorted([x for x in df["elaboro"].unique().tolist() if x != ""])
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
        return ""
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

if "fallo" in df_tabla.columns:
    df_tabla = df_tabla.sort_values(by="fallo", ascending=True, na_position="last")
elif "PUBLICACION" in df_tabla.columns:
    df_tabla = df_tabla.sort_values(by="PUBLICACION", ascending=False, na_position="last")

df_tabla = df_tabla.head(6)

filas_html = ""

for _, row in df_tabla.iterrows():
    titulo = limpiar(row.get("licitacion", "")) or "Sin identificador"
    estado_badge, badge_class = badge_estado(row)
    referencia = limpiar(row.get("tipo", "")) or "-"
    cierre = formatear_fecha(row.get("fallo", "")) if "fallo" in row else ""

    filas_html += f"""
    <div class="table-row">
        <div>{html.escape(titulo)}</div>
        <div><span class="status-pill {badge_class}">{html.escape(estado_badge)}</span></div>
        <div>{html.escape(referencia)}</div>
        <div>{html.escape(cierre if cierre else "-")}</div>
    </div>
    """

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

actividad_html = ""
if not df_act.empty:
    df_act = df_act.dropna(subset=["fecha"]).sort_values("fecha").head(5)
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
# DETALLE OPCIONAL
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
