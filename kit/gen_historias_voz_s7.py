"""Historias con voz en off (ElevenLabs, voz Lina) semana 7 (12 al 18 de noviembre de 2026): H40 y H42.
Usa la misma plantilla de historias de Contraining (st) del kit."""
import os, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_contraining_personal import st

END = '<div style="height:120px"></div>'
CHIP = '<div style="margin-top:70px"><span class="chip">WhatsApp 301 727 6517</span></div>'

pieces = {}

# Lun 16 · laboratorios: planes de marketing (voz)
pieces["H40"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:110px;margin-top:30px">¿Tu laboratorio tiene un plan de marketing?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:64px;margin-top:50px">Planes de marketing y entrenamiento a la medida.</h2>
<p style="margin-top:40px;font-size:42px">Más de 27 años formando visitadores médicos en Colombia.</p>
{CHIP}</div>{END}""")

# Mié 18 · diplomado: cambio de precio (voz, con el número)
pieces["H42"] = st(f"""<div style="margin-top:auto"><div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:104px;margin-top:30px">¿Cuándo cambia el precio?</h1>
<h2 style="font-size:76px;margin-top:20px">El 1 de diciembre.</h2>
<div class="bar" style="margin-top:50px"></div>
<div style="margin-top:50px;font-size:40px">Hasta el 30 de noviembre</div>
<div class="n" style="font-size:150px;line-height:1">$2.753.000</div>
<div style="margin-top:30px;font-size:40px">Desde el 1 de diciembre: <b>$3.110.000</b></div>
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
