"""Historias con voz en off (ElevenLabs, voz Lina) semana 9 (26 de noviembre al 2 de diciembre de 2026): H51 y H54.
Usa la misma plantilla de historias de Contraining (st) del kit."""
import os, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_contraining_personal import st

END = '<div style="height:120px"></div>'
CHIP = '<div style="margin-top:70px"><span class="chip">WhatsApp 301 727 6517</span></div>'

pieces = {}

from visual_ct import icono, sello, marca_agua, franja, calendario, precios
def kick(nombre, texto):
    return f'<div style="display:flex;gap:20px;align-items:center">{sello(nombre, 84)}<div class="kicker">{texto}</div></div>'
def deco():
    return marca_agua(900, -320, -260, .08) + franja(20) + franja(20, abajo=True)

# Vie 27 · laboratorios: outsourcing de fuerzas de ventas (voz)
def paso(nombre, rotulo):
    return f"""<div style="flex:1;background:#FFF8EA;border-radius:26px;padding:28px 16px;display:flex;flex-direction:column;align-items:center;gap:16px">
{sello(nombre, 110)}<span style="font-family:LS;font-weight:700;font-size:32px;text-align:center;line-height:1.1">{rotulo}</span></div>"""
pieces["H51"] = st(f"""{deco()}<div style="margin-top:auto">
{kick("maletin", "Para laboratorios")}
<h1 style="font-size:104px;margin-top:40px">¿Tu laboratorio necesita una fuerza de ventas?</h1>
<h2 style="font-size:54px;margin-top:40px">Outsourcing de fuerzas de ventas:</h2>
<div style="display:flex;gap:18px;margin-top:30px">{paso("lupa", "Reclutamiento")}{paso("diana", "Entrenamiento a la medida")}{paso("grafica", "Seguimiento")}</div>
<p style="margin-top:40px;font-size:42px">Más de 30 fuerzas de ventas administradas.</p>
{CHIP}</div>{END}""")

# Lun 30 · diplomado: último día del precio actual (voz, con el número)
pieces["H54"] = st(f"""{deco()}<div style="margin-top:auto">
{kick("reloj", "Diplomado en Visita Médica")}
<h1 style="font-size:118px;margin-top:40px">Hoy es el<br>último día</h1>
<h2 style="font-size:56px;margin-top:16px">con el precio actual.</h2>
{calendario([26, 27, 28, 29, 30, 1], 30, 30, {26: "NOV", 1: "DIC"})}
{precios(rot_antes="Hasta hoy, 30 de noviembre", rot_despues="Desde mañana")}
{CHIP}</div>{END}""")

if __name__ == "__main__":
    only = sys.argv[1:] or list(pieces)
    OUT = os.environ["OUT"]; os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for k in only:
            pg = b.new_page(viewport={"width": 1080, "height": 1920})
            path = f"{OUT}/_{k}.html"
            open(path, "w").write(pieces[k])
            pg.goto(f"file://{path}"); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{OUT}/{k}.png")
            pg.close()
        b.close()
    print("ok", len(only))
