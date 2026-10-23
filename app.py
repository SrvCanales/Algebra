import streamlit as st
from core import interfaz as ui
from problemas import cargar

st.set_page_config(page_title="Álgebra Lineal · Práctica", layout="wide",
                   initial_sidebar_state="collapsed")
ui.iniciar_estado()
problemas = cargar()
P = problemas[st.session_state.actual - 1]

ui.encabezado(P)          # PARTE SUPERIOR
st.divider()

# Si el panel derecho está abierto, ocupa la mayor parte de la pantalla.
proporciones = [1.3, 2.2, 5.0] if st.session_state.panel else [1.3, 6.0, 1.6]
col_izq, col_centro, col_der = st.columns(proporciones)

with col_izq:
    ui.lista(problemas)   # COSTADO IZQUIERDO
with col_centro:
    ui.visualizacion(P)   # 3D + parámetro
with col_der:
    ui.panel_error(P)     # COSTADO DERECHO
