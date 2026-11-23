"""Historias con voz en off (ElevenLabs, voz Lina) semana 9 (26 de noviembre al 2 de diciembre de 2026): H51 y H54.
Usa la misma plantilla de historias de Contraining (st) del kit."""
import os, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_contraining_personal import st

END = '<div style="height:120px"></div>'
CHIP = '<div style="margin-top:70px"><span class="chip">WhatsApp 301 727 6517</span></div>'

pieces = {}

# Vie 27 · laboratorios: outsourcing de fuerzas de ventas (voz)
pieces["H51"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:104px;margin-top:30px">¿Tu laboratorio necesita una fuerza de ventas?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:60px;margin-top:50px">Outsourcing de fuerzas de ventas: reclutamiento, entrenamiento a la medida y seguimiento.</h2>
<p style="margin-top:40px;font-size:42px">Más de 30 fuerzas de ventas administradas.</p>
{CHIP}</div>{END}""")

# Lun 30 · diplomado: último día del precio actual (voz, con el número)
pieces["H54"] = st(f"""<div style="margin-top:auto"><div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:130px;margin-top:30px">Hoy es el último día</h1>
<h2 style="font-size:60px;margin-top:20px">con el precio actual.</h2>
<div class="bar" style="margin-top:50px"></div>
<div style="margin-top:50px;font-size:40px">Hasta hoy, 30 de noviembre</div>
<div class="n" style="font-size:140px;line-height:1">$2.753.000</div>
<div style="margin-top:30px;font-size:40px">Desde mañana: <b>$3.110.000</b></div>
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
