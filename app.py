import streamlit as st
import pandas as pd

# =========================
# CONFIG
# =========================
st.set_page_config(layout="wide")

# =========================
# CARGAR EXCEL
# =========================
df = pd.read_excel("data/APLICACION LICITACIONES.xlsx")

# Limpiar nombres de columnas (MUY IMPORTANTE)
df.columns = df.columns.str.strip()

# =========================
# MAPEO DE COLUMNAS
# =========================
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

# =========================
# KPIs
# =========================
total = len(df)

en_curso = df[df["estatus"].astype(str).str.contains("EN PROCESO|CURSO", case=False, na=False)].shape[0]

ganadas = df[df["resultado"].astype(str).str.contains("GANADA", case=False, na=False)].shape[0]

perdidas = df[df["resultado"].astype(str).str.contains("PERDIDA", case=False, na=False)].shape[0]

# =========================
# FILTROS
# =========================
col1, col2, col3, col4 = st.columns(4)

with col1:
    tipo_filtro = st.selectbox("Tipo", ["Todos"] + list(df["tipo"].dropna().unique()))

with col2:
    convocante_filtro = st.selectbox("Convocante", ["Todos"] + list(df["convocante"].dropna().unique()))

with col3:
    estado_filtro = st.selectbox("Estado", ["Todos"] + list(df["estado"].dropna().unique()))

with col4:
    elaboro_filtro = st.selectbox("Elaboró", ["Todos"] + list(df["elaboro"].dropna().unique()))

# Aplicar filtros
df_filtrado = df.copy()

if tipo_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo"] == tipo_filtro]

if convocante_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["convocante"] == convocante_filtro]

if estado_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["estado"] == estado_filtro]

if elaboro_filtro != "Todos":
    df_filtrado = df_filtrado[df_filtrado["elaboro"] == elaboro_filtro]

# =========================
# UI
# =========================
st.title("📊 Panel de Oportunidades")

# KPIs
k1, k2, k3, k4 = st.columns(4)

k1.metric("Procesos Totales", total)
k2.metric("En curso", en_curso)
k3.metric("Ganadas", ganadas)
k4.metric("Perdidas", perdidas)

# =========================
# TABLA PRINCIPAL
# =========================
st.subheader("📄 Oportunidades")

columnas_mostrar = [
    "tipo",
    "licitacion",
    "convocante",
    "estado",
    "estatus",
    "resultado",
    "fallo",
    "elaboro"
]

st.dataframe(df_filtrado[columnas_mostrar], use_container_width=True)

# =========================
# PROXIMAS ACTIVIDADES
# =========================
st.subheader("📅 Próximas actividades")

fechas_cols = [
    "ENVIO DE PREGUNTAS",
    "JUNTA ACLARACIONES",
    "PROPUESTA ECONOMICA",
    "FALLO"
]

df_actividades = df.copy()

actividades = []

for _, row in df_actividades.iterrows():
    for col in fechas_cols:
        if col in df.columns and pd.notnull(row[col]):
            actividades.append({
                "licitacion": row["licitacion"],
                "evento": col,
                "fecha": row[col]
            })

df_act = pd.DataFrame(actividades)

if not df_act.empty:
    df_act = df_act.sort_values("fecha")
    st.dataframe(df_act, use_container_width=True)
else:
    st.info("No hay actividades registradas")
