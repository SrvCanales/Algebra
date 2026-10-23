"""Utilidades para dibujar en 3D. Úsalas desde figura(t) en cada problema."""
import numpy as np
import plotly.graph_objects as go

COLORES = {
    "azul": "#4F9DFF",
    "verde": "#2ED3A5",
    "violeta": "#B58CFF",
    "rojo": "#FF6B6B",
    "ambar": "#FFC857",
    "gris": "#5B6B8C",
}


def escena_base(rango=3.0, altura=560):
    """Figura vacía con ejes cúbicos de -rango a rango."""
    fig = go.Figure()
    ejes = dict(range=[-rango, rango], showbackground=False,
                gridcolor="#2A3140", zerolinecolor="#4A5468", color="#8A93A6")
    fig.update_layout(
        height=altura,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        scene=dict(
            xaxis=dict(title="x", **ejes),
            yaxis=dict(title="y", **ejes),
            zaxis=dict(title="z", **ejes),
            aspectmode="cube",
            camera=dict(eye=dict(x=1.5, y=-1.6, z=0.9)),
        ),
        legend=dict(font=dict(color="#C9D1E0"), bgcolor="rgba(0,0,0,0)"),
    )
    return fig


def agregar_vector(fig, v, nombre, color, origen=(0, 0, 0)):
    """Flecha desde `origen` hasta origen + v."""
    o = np.array(origen, float)
    v = np.array(v, float)
    p = o + v
    fig.add_trace(go.Scatter3d(
        x=[o[0], p[0]], y=[o[1], p[1]], z=[o[2], p[2]], mode="lines",
        line=dict(color=color, width=6), name=nombre, legendgroup=nombre))
    n = np.linalg.norm(v)
    if n > 1e-9:
        d = v / n
        fig.add_trace(go.Cone(
            x=[p[0]], y=[p[1]], z=[p[2]], u=[d[0]], v=[d[1]], w=[d[2]],
            anchor="tip", sizemode="absolute", sizeref=0.3, showscale=False,
            colorscale=[[0, color], [1, color]], hoverinfo="skip",
            legendgroup=nombre, showlegend=False))
    fig.add_trace(go.Scatter3d(
        x=[p[0]], y=[p[1]], z=[p[2]], mode="text", text=[nombre],
        textposition="top center", textfont=dict(color=color, size=14),
        hoverinfo="skip", showlegend=False, legendgroup=nombre))


def agregar_plano(fig, normal, d=0.0, color="#5B6B8C", opacidad=0.25,
                  nombre="plano", rango=3.0):
    """Plano  normal · (x,y,z) = d.   Ej.: z = x + y  ->  normal=(1,1,-1), d=0."""
    n0 = np.array(normal, float)
    p0 = n0 * d / np.dot(n0, n0)
    n = n0 / np.linalg.norm(n0)
    a = np.array([1.0, 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1.0, 0])
    u = np.cross(n, a); u /= np.linalg.norm(u)
    w = np.cross(n, u)
    r = rango * 1.3
    S, R = np.meshgrid(np.linspace(-r, r, 20), np.linspace(-r, r, 20))
    P = [p0[i] + u[i] * S + w[i] * R for i in range(3)]
    fig.add_trace(go.Surface(
        x=P[0], y=P[1], z=P[2], opacity=opacidad, showscale=False,
        colorscale=[[0, color], [1, color]], name=nombre, showlegend=True,
        hoverinfo="skip"))


def agregar_punto(fig, p, nombre="", color="#FFC857", tamano=6):
    fig.add_trace(go.Scatter3d(
        x=[p[0]], y=[p[1]], z=[p[2]], mode="markers",
        marker=dict(size=tamano, color=color), name=nombre or "punto",
        showlegend=bool(nombre)))


def agregar_segmento(fig, a, b, color="#8A93A6", dash="dash", nombre=""):
    fig.add_trace(go.Scatter3d(
        x=[a[0], b[0]], y=[a[1], b[1]], z=[a[2], b[2]], mode="lines",
        line=dict(color=color, width=3, dash=dash),
        name=nombre or "segmento", showlegend=bool(nombre)))
