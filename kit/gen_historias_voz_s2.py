"""Historias con voz en off (ElevenLabs, voz Lina) para jue 15 a dom 18 de octubre de 2026.
Usa la misma plantilla de historias de Contraining (st) del kit."""
import os, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_contraining_personal import st

END = '<div style="height:120px"></div>'
CHIP = '<div style="margin-top:70px"><span class="chip">WhatsApp 301 727 6517</span></div>'

pieces = {}

# Jue 15 · "visitador que vende"
pieces["H8"] = st(f"""<div style="margin-top:auto">
<h1 style="font-size:104px">¿Qué separa a quien vende de quien solo visita?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:76px;margin-top:50px">No es suerte.<br>Es formación.</h2>
<p style="margin-top:40px">Formamos visitadores médicos desde 1998.</p>
{CHIP}</div>{END}""")

# Vie 16 · trayectoria
pieces["H9"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<div class="n" style="font-size:260px;line-height:.9;margin-top:30px">158</div>
<div style="font-family:LS;font-weight:600;font-size:56px">promociones · 3.000+ egresados</div>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:80px;margin-top:50px">¿Quieres ser parte de la siguiente?</h2>
{CHIP}</div>{END}""")

# Sáb 17 · reflexión
pieces["H10"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Pregúntate esto</div>
<h1 style="font-size:96px;margin-top:30px">¿Tu próximo paso depende de alguien más o de lo que aprendes hoy?</h1>
<div class="bar" style="margin-top:60px"></div>
<p style="margin-top:40px;font-size:40px">La visita médica es una carrera que se construye con formación.</p>
<h2 style="font-size:60px;margin-top:40px;color:var(--sea)">Contraining, desde 1998.</h2>
</div>{END}""")

# Dom 18 · diplomado 2027
pieces["H11"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Próximamente · 2027</div>
<h1 style="font-size:104px;margin-top:30px">Los visitadores de hoy son los gerentes de mañana.</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:64px;margin-top:50px">Nuevo diplomado para gerentes de distrito y de producto.</h2>
<p style="margin-top:36px">¿Quieres enterarte primero?</p>
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
