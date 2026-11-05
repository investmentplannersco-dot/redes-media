"""Semana 6 (5 al 11 de noviembre de 2026): LinkedIn de Joaquín y @contrainingfarma.
Copia del kit: usa las plantillas ct(), st() y pr() de gen_contraining_personal; solo cambia el contenido."""
import os, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_contraining_personal import ct, st, pr, FOOT, ISO, LOGO_H, A, FOTO

END = '<div style="height:120px"></div>'
CHIP = '<div style="margin-top:70px"><span class="chip">WhatsApp 301 727 6517</span></div>'
pieces = {}

# ---------- LinkedIn (retrato en todas) ----------
def li(title, sub, accent, who, logo="", tsize=110):
    lg = f'<img src="{logo}" style="height:80px;position:absolute;left:88px;bottom:200px">' if logo else ""
    return pr(f"""
<img src="{FOTO}" style="position:absolute;right:-60px;bottom:0;height:860px">
<div class="pad"><div class="name">Joaquín Piña Labastida</div>
<h1 style="font-size:{tsize}px;margin-top:80px;max-width:900px">{title}</h1>
<div style="width:90px;height:6px;background:{accent};margin-top:56px"></div>
<p style="margin-top:36px;max-width:470px">{sub}</p>
{lg}
<div class="foot"><div class="who">{who}</div></div></div>""")

pieces["L12"] = li("Una sola opción no es una decisión.", "Es una instrucción.",
                   "var(--oro)", "Joaquín Piña<span>IP360</span>", f"{A}/logo_ip.png", 104)
pieces["L13"] = li("«No lo sé.»", "Tres palabras que un líder comercial debería practicar.",
                   "var(--carbon)", "Joaquín Piña<span>Coach ontológico ICF</span>", tsize=132)
pieces["L14"] = li("La primera visita no debería ser la primera práctica.", "La visita médica no se improvisa. Se entrena.",
                   "var(--sea)", "Joaquín Piña<span>Contraining</span>", f"{A}/iso_ct.png", 92)

# ---------- @contrainingfarma publicaciones ----------
# P8 · Laboratorios: coordinación de formación (carrusel de 3) · jueves 5, 18:00
pieces["P8_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:150px" class="kicker">Para laboratorios</div>
<h1 style="font-size:112px;margin-top:30px">¿Quién coordina la formación de tu fuerza de ventas?</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:58px;margin-top:40px">Entrenar también es coordinar.</h2>
{FOOT}</div>""", page="1/3")
pieces["P8_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:90px;margin-top:70px">Tres frentes para tu laboratorio</h1>
<ul class="big" style="margin-top:40px">
<li><b>Coordinación</b> de programas de formación.</li>
<li><b>Entrenamiento</b> a la medida.</li>
<li><b>Seguimiento</b> de la fuerza de ventas.</li>
</ul>{FOOT}</div>""", page="2/3")
pieces["P8_3"] = ct(f"""<div class="pad">{ISO}
<div class="n" style="font-size:280px;line-height:.9;margin-top:90px">+27</div>
<h2 style="font-size:64px;margin-top:20px">años formando visitadores médicos en Colombia</h2>
<div class="bar" style="margin-top:56px"></div>
<p style="margin-top:40px;font-size:40px">Cuéntanos cómo forma hoy tu laboratorio a su equipo.</p>
<div style="margin-top:auto"><span class="chip">WhatsApp 301 727 6517 · contraining.co</span></div>
</div>""", page="3/3")

# P9 · Diplomado: dignificar la visita (carrusel de 3) · martes 10, 18:00
pieces["P9_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:170px" class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:132px;margin-top:30px">Visitar no es repartir muestras.</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:62px;margin-top:40px">Es conversar con criterio.</h2>
{FOOT}</div>""", page="1/3")
pieces["P9_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:96px;margin-top:70px">Eso se estudia</h1>
<ul class="big" style="margin-top:40px">
<li><b>Teoría farmacéutica</b>, la base para hablar con el médico.</li>
<li><b>Entrenamiento comercial</b>, con docentes con experiencia en la industria farmacéutica.</li>
<li><b>Acompañamiento</b> para la inserción laboral.</li>
</ul>{FOOT}</div>""", page="2/3")
pieces["P9_3"] = ct(f"""<div class="pad">{ISO}
<div class="kicker" style="margin-top:70px">Inicio</div>
<h1 style="font-size:104px;margin-top:20px">18 de febrero de 2027</h1>
<div style="margin-top:50px;font-size:36px">Hasta el 30 de noviembre de 2026</div>
<div class="n" style="font-size:112px;line-height:1;margin-top:8px">$2.753.000</div>
<div style="margin-top:24px;font-size:36px">Desde el 1 de diciembre de 2026: <b>$3.110.000</b></div>
<div style="margin-top:36px;background:var(--peach);padding:28px 36px;border-radius:24px;font-size:34px;line-height:1.35">
<b style="font-family:LS">12 % de descuento</b> para referidos de egresados y por pronto pago.</div>
<div style="margin-top:auto"><span class="chip">Escríbenos: WhatsApp 301 727 6517</span></div>
</div>""", page="3/3")

# ---------- @contrainingfarma historias (H30, H33 y H35 llevan voz) ----------
pieces["H29"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:112px;margin-top:30px">Un programa de formación también se coordina.</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:64px;margin-top:50px">Coordinamos programas de formación y entrenamos a la medida.</h2>
{CHIP}</div>{END}""")
pieces["H30"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<div class="n" style="font-size:176px;line-height:1;margin-top:24px;white-space:nowrap">120 horas</div>
<div style="font-family:LS;font-weight:600;font-size:60px">en 3 meses</div>
<div class="bar" style="margin-top:60px"></div>
<ul style="margin-top:30px">
<li><b>Teoría farmacéutica</b></li>
<li><b>Entrenamiento comercial</b></li>
<li><b>Acompañamiento</b> para la inserción laboral</li>
</ul>
{CHIP}</div>{END}""")
pieces["H31"] = st(f"""<div style="margin-top:auto">
<div class="n" style="font-size:280px;line-height:.9;margin-top:30px">+27</div>
<div style="font-family:LS;font-weight:600;font-size:60px">años formando visitadores médicos en Colombia</div>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:76px;margin-top:50px">La visita médica no se improvisa.</h2>
{CHIP}</div>{END}""")
pieces["H32"] = st(f"""<div style="margin-top:auto"><div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:120px;margin-top:30px">Quedan 22 días</h1>
<div style="margin-top:60px;font-size:40px">Hasta el 30 de noviembre</div>
<div class="n" style="font-size:150px;line-height:1">$2.753.000</div>
<div style="margin-top:40px;font-size:40px">Desde el 1 de diciembre</div>
<div style="font-family:LS;font-weight:700;font-size:96px;color:var(--ash)">$3.110.000</div>
{CHIP}</div>{END}""")
pieces["H33"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:100px;margin-top:30px">¿Tu fuerza de ventas recibe un entrenamiento hecho para ella?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:62px;margin-top:50px">Entrenamiento a la medida de cada laboratorio.</h2>
<p style="margin-top:40px;font-size:42px">Coordinación de programas de formación y seguimiento.</p>
{CHIP}</div>{END}""")
pieces["H34"] = st(f"""<div style="margin-top:auto">
<h1 style="font-size:124px">Visitar no es repartir muestras.</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:76px;margin-top:50px">Es conversar con criterio.</h2>
<p style="margin-top:40px;font-size:42px">Diplomado en Visita Médica. Inicio: 18 de febrero de 2027.</p>
{CHIP}</div>{END}""")
pieces["H35"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:112px;margin-top:30px">¿En 2027 quieres estar en la visita médica?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:66px;margin-top:50px">Próxima promoción: 18 de febrero de 2027.</h2>
<p style="margin-top:40px;font-size:42px">120 horas en 3 meses. En vivo, de 7:00 a 9:00 p. m.</p>
{CHIP}</div>{END}""")

if __name__ == "__main__":
    only = sys.argv[1:] or list(pieces)
    OUT = os.environ["OUT"]; os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for k in only:
            w, h = (1080, 1920) if k.startswith("H") else (1080, 1350)
            pg = b.new_page(viewport={"width": w, "height": h})
            path = f"{OUT}/_{k}.html"; open(path, "w").write(pieces[k])
            pg.goto(f"file://{path}"); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{OUT}/{k}.png"); pg.close()
        b.close()
    print("ok", len(only))
