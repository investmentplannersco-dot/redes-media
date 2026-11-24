"""Elementos visuales para @contrainingfarma (desde la semana 9).
Íconos de línea, sellos y gráficos simples con la paleta del kit (Sea Green, Apricot, Champagne, Peach, Olive).
Sin degradados ni fotos. Se usan dentro de ct() y st() de gen_contraining_personal."""
from gen_contraining_personal import A

_P = {  # trazos en una cuadrícula de 24 x 24
    "equipo": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.6 2.7-6 6-6s6 2.4 6 6"/><circle cx="17" cy="9" r="2.6"/><path d="M15.5 14.3c3 .1 5.5 2.2 5.5 5.7"/>',
    "lupa": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/>',
    "diana": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5.5"/><circle cx="12" cy="12" r="2" fill="currentColor"/>',
    "grafica": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 6-7"/><path d="M16 7h4v4"/>',
    "enlace": '<path d="M10 14a4.5 4.5 0 0 0 6.4 0l3-3a4.5 4.5 0 0 0-6.4-6.4l-1.2 1.2"/><path d="M14 10a4.5 4.5 0 0 0-6.4 0l-3 3a4.5 4.5 0 0 0 6.4 6.4l1.2-1.2"/>',
    "calendario": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "reloj": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
    "pantalla": '<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8 21h8M12 17v4"/><circle cx="12" cy="10.5" r="2.4" fill="currentColor"/>',
    "docente": '<rect x="9" y="3" width="12" height="9" rx="1"/><circle cx="6" cy="9" r="2.6"/><path d="M1.5 21c0-3.4 2-5.8 4.5-5.8S10.5 17.6 10.5 21"/><path d="M8.5 15 13 12"/>',
    "maletin": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 1 15 5v2M3 13h18"/>',
    "etiqueta": '<path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z"/><circle cx="7.5" cy="7.5" r="1.6" fill="currentColor"/>',
    "chat": '<path d="M4 18.5V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H8z"/><path d="M8 9h8M8 12.5h5"/>',
}

def icono(nombre, size=72, color="var(--sea)", grosor=1.8):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{grosor}" stroke-linecap="round" stroke-linejoin="round" style="color:{color};flex:none">{_P[nombre]}</svg>')

def sello(nombre, size=150, fondo="var(--peach)", color="var(--sea)"):
    """Ícono dentro de un cuadrado redondeado."""
    return (f'<div style="width:{size}px;height:{size}px;border-radius:{size*.26:.0f}px;background:{fondo};display:flex;'
            f'align-items:center;justify-content:center;flex:none">{icono(nombre, int(size*.56), color)}</div>')

def tarjeta(nombre, titulo, texto, fondo="#FFF8EA"):
    return f"""<div style="display:flex;gap:34px;align-items:center;background:{fondo};border-radius:30px;padding:30px 34px;margin-top:24px">
{sello(nombre, 120)}<div><div style="font-family:LS;font-weight:700;font-size:44px;color:var(--sea);line-height:1.05">{titulo}</div>
<div style="font-size:32px;line-height:1.3;margin-top:6px">{texto}</div></div></div>"""

def marca_agua(size=760, right=-220, bottom=-200, opacidad=.10):
    """Isotipo grande recortado en una esquina (opacidad plana, sin degradado)."""
    return (f'<img src="{A}/iso_ct.png" style="position:absolute;width:{size}px;right:{right}px;bottom:{bottom}px;'
            f'opacity:{opacidad};pointer-events:none;z-index:-1">')

def circulo(size, top, left, color="var(--apr)", opacidad=1):
    return (f'<div style="position:absolute;width:{size}px;height:{size}px;border-radius:50%;background:{color};'
            f'top:{top}px;left:{left}px;opacity:{opacidad};z-index:-1"></div>')

def franja(alto=24, color="var(--sea)", abajo=False):
    lado = "bottom:0" if abajo else "top:0"
    return f'<div style="position:absolute;left:0;right:0;{lado};height:{alto}px;background:{color};z-index:-1"></div>'

def calendario(dias, marcado, hoy, mes_de=None, ancho=888):
    """Tira de días. `marcado` = último día del precio (casilla verde); `hoy` = casilla con borde.
    `mes_de` = {día: 'NOV'|'DIC'} para rotular el cambio de mes."""
    w = (ancho - 14 * (len(dias) - 1)) / len(dias)
    cel = []
    for d in dias:
        if d == marcado:
            est = "background:var(--sea);color:#fff"
        elif d == hoy:
            est = "background:#fff;color:var(--sea);outline:6px solid var(--apr);outline-offset:-6px"
        else:
            est = "background:#FFF8EA;color:var(--ink)"
        mes = (mes_de or {}).get(d, "")
        cel.append(f'<div style="width:{w:.0f}px;height:150px;border-radius:22px;{est};display:flex;flex-direction:column;'
                   f'align-items:center;justify-content:center"><div style="font-family:LS;font-weight:600;font-size:22px;letter-spacing:2px;opacity:.75">{mes}</div>'
                   f'<div style="font-family:LS;font-weight:700;font-size:64px;line-height:1">{d}</div></div>')
    return f'<div style="display:flex;gap:14px;margin-top:40px">{"".join(cel)}</div>'

def precios(antes="$2.753.000", despues="$3.110.000", rot_antes="Hasta el 30 de noviembre", rot_despues="Desde el 1 de diciembre"):
    """Dos barras proporcionales al precio (2.753.000 / 3.110.000 = 88,5 %)."""
    pct = 2753000 / 3110000 * 100
    return f"""<div style="margin-top:44px">
<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-size:34px">{rot_antes}</span><span class="n" style="font-size:72px">{antes}</span></div>
<div style="height:34px;border-radius:17px;background:#E9DCC0;margin-top:10px"><div style="height:34px;width:{pct:.1f}%;border-radius:17px;background:var(--sea)"></div></div>
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:30px"><span style="font-size:34px">{rot_despues}</span><span style="font-family:LS;font-weight:700;font-size:56px;color:var(--ash)">{despues}</span></div>
<div style="height:34px;border-radius:17px;background:var(--ash);margin-top:10px"></div></div>"""
