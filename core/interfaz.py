"""Dibuja la pantalla. No necesitas tocar este archivo."""
import streamlit as st


def iniciar_estado():
    st.session_state.setdefault("actual", 1)
    st.session_state.setdefault("panel", False)


def _ir(n):
    st.session_state.actual = n


def _toggle_panel():
    st.session_state.panel = not st.session_state.panel


def _toggle_error(n):
    k = f"error_{n}"
    st.session_state[k] = not st.session_state.get(k, False)


def encabezado(P):
    st.markdown(f"### Problema {P.numero}. {P.titulo or '(pendiente)'}")
    if P.concepto:
        st.caption(f"Concepto: {P.concepto}")
    if P.pendiente:
        st.warning(f"Este problema aún no está escrito. Completa `problemas/p{P.numero:02d}.py`.")
    else:
        st.markdown(P.enunciado)


def lista(problemas):
    st.markdown("**Problemas**")
    for p in problemas:
        activo = p.numero == st.session_state.actual
        st.button(f"{p.numero}. {p.etiqueta or 'pendiente'}", key=f"btn_{p.numero}",
                  type="primary" if activo else "secondary",
                  on_click=_ir, args=(p.numero,), width="stretch")


def visualizacion(P):
    if P.pendiente:
        return
    pr = P.parametro
    t = st.slider(pr.etiqueta, float(pr.minimo), float(pr.maximo), float(pr.valor),
                  float(pr.paso), key=f"par_{P.numero}")
    fig, mensaje = P.figura(round(t, 6))
    st.plotly_chart(fig, key=f"fig_{P.numero}")
    if mensaje:
        st.markdown(mensaje)


def panel_error(P):
    abierto = st.session_state.panel
    st.button("Desarrollo Errado " + ("◂" if abierto else "▸"), key="toggle_panel",
              on_click=_toggle_panel, width="stretch")
    if not abierto or P.pendiente:
        return
    mostrar = st.session_state.get(f"error_{P.numero}", False)
    for i, paso in enumerate(P.pasos, 1):
        texto = f"**Paso {i}.** {paso}"
        if mostrar and i == P.paso_erroneo:
            st.error(texto)
        else:
            with st.container(border=True):
                st.markdown(texto)
    st.button("Ocultar Error" if mostrar else "Mostrar Error",
              key=f"btn_error_{P.numero}", on_click=_toggle_error,
              args=(P.numero,), type="primary")
    if mostrar:
        st.markdown("#### ¿Dónde está el error?")
        st.info(P.explicacion)
