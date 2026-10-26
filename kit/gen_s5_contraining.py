"""Semana 5 (29 de octubre al 4 de noviembre de 2026): LinkedIn de Joaquín y @contrainingfarma.
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

pieces["L9"] = li("Si no lo entiende,<br>no lo firme.", "Firmar algo que no se entiende no es confiar.",
                  "var(--oro)", "Joaquín Piña<span>IP360</span>", f"{A}/logo_ip.png", 104)
pieces["L10"] = li("¿Pidió algo<br>o lo insinuó?", "Una petición clara dice qué, quién y para cuándo.",
                  "var(--carbon)", "Joaquín Piña<span>Coach ontológico ICF</span>", tsize=120)
pieces["L11"] = li("Reclutar y formar no son dos procesos.", "Una vacante en la fuerza de ventas es un territorio sin visitar.",
                  "var(--sea)", "Joaquín Piña<span>Contraining</span>", f"{A}/iso_ct.png", 100)

# ---------- @contrainingfarma publicaciones ----------
# P6 · Laboratorios: outsourcing (carrusel de 3) · jueves 29, 20:00
pieces["P6_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:170px" class="kicker">Para laboratorios</div>
<h1 style="font-size:120px;margin-top:30px">¿Necesitas una fuerza de ventas en campo?</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:58px;margin-top:40px">No tienes que armarla desde cero.</h2>
{FOOT}</div>""", page="1/3")
pieces["P6_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:90px;margin-top:70px">Lo que hacemos por tu laboratorio</h1>
<ul class="big" style="margin-top:40px">
<li><b>Outsourcing</b> de fuerzas de ventas.</li>
<li><b>Reclutamiento</b> de visitadores médicos.</li>
<li><b>Seguimiento</b> de la fuerza de ventas.</li>
</ul>{FOOT}</div>""", page="2/3")
pieces["P6_3"] = ct(f"""<div class="pad">{ISO}
<div class="n" style="font-size:280px;line-height:.9;margin-top:90px">+30</div>
<h2 style="font-size:64px;margin-top:20px">fuerzas de ventas administradas</h2>
<div class="bar" style="margin-top:56px"></div>
<p style="margin-top:40px;font-size:40px">Cuéntanos qué necesita tu laboratorio.</p>
<div style="margin-top:auto"><span class="chip">WhatsApp 301 727 6517 · contraining.co</span></div>
</div>""", page="3/3")

# P7 · Diplomado: horario (carrusel de 3) · martes 3, 18:00
pieces["P7_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:170px" class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:150px;margin-top:30px">¿Trabajas de día?</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:62px;margin-top:40px">Las clases son de 7:00&nbsp;a&nbsp;9:00&nbsp;p.&nbsp;m.</h2>
{FOOT}</div>""", page="1/3")
pieces["P7_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:96px;margin-top:70px">Así son las clases</h1>
<ul class="big" style="margin-top:40px">
<li><b>Virtuales y en vivo</b>, de lunes a viernes.</li>
<li><b>De 7:00&nbsp;a&nbsp;9:00&nbsp;p.&nbsp;m.</b></li>
<li><b>120 horas</b> en 3 meses.</li>
<li><b>Docentes</b> con experiencia en la industria farmacéutica.</li>
</ul>{FOOT}</div>""", page="2/3")
pieces["P7_3"] = ct(f"""<div class="pad">{ISO}
<div class="kicker" style="margin-top:70px">Inicio</div>
<h1 style="font-size:120px;margin-top:20px">18 de febrero de 2027</h1>
<div style="margin-top:60px;font-size:36px">Inversión hasta el 30 de noviembre de 2026</div>
<div class="n" style="font-size:120px;line-height:1;margin-top:8px">$2.753.000</div>
<div style="margin-top:44px;background:var(--peach);padding:30px 36px;border-radius:24px;font-size:34px;line-height:1.35">
<b style="font-family:LS">12 % de descuento</b> para referidos de egresados y por pronto pago.</div>
<div style="margin-top:auto"><span class="chip">Escríbenos: WhatsApp 301 727 6517</span></div>
</div>""", page="3/3")

# ---------- @contrainingfarma historias (H23, H26 y H28 llevan voz) ----------
pieces["H19"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Profesionales comerciales</div>
<h1 style="font-size:96px;margin-top:30px">Hacemos de enlace entre profesionales comerciales de alto nivel y compañías farmacéuticas.</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:64px;margin-top:50px">¿Buscas talento o buscas tu siguiente paso?</h2>
{CHIP}</div>{END}""")
pieces["H23"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:120px;margin-top:30px">¿Trabajas de día?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:72px;margin-top:50px">Clases en vivo de 7:00&nbsp;a&nbsp;9:00&nbsp;p.&nbsp;m.</h2>
<p style="margin-top:40px;font-size:42px">Lunes a viernes. 120 horas en 3 meses.</p>
{CHIP}</div>{END}""")
pieces["H24"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:110px;margin-top:30px">Planes de marketing.</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:66px;margin-top:50px">Además de formar visitadores y administrar fuerzas de ventas.</h2>
{CHIP}</div>{END}""")
pieces["H25"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<div class="n" style="font-size:250px;line-height:.9;margin-top:30px">3.000+</div>
<div style="font-family:LS;font-weight:600;font-size:60px">egresados · 158 promociones</div>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:70px;margin-top:50px">La próxima empieza el 18 de febrero de 2027.</h2>
{CHIP}</div>{END}""")
pieces["H26"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:104px;margin-top:30px">¿Necesitas una fuerza de ventas en campo?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:62px;margin-top:50px">Outsourcing, reclutamiento y seguimiento.</h2>
<p style="margin-top:40px;font-size:42px">+30 fuerzas de ventas administradas.</p>
{CHIP}</div>{END}""")
pieces["H27"] = st(f"""<div style="margin-top:auto">
<h1 style="font-size:112px">La visita médica es una profesión.</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:76px;margin-top:50px">Y como toda profesión, se estudia.</h2>
<p style="margin-top:40px;font-size:42px">Diplomado en Visita Médica. Inicio: 18 de febrero de 2027.</p>
{CHIP}</div>{END}""")
pieces["H28"] = st(f"""<div style="margin-top:auto"><div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:104px;margin-top:30px">¿Cuánto cuesta?</h1>
<div style="margin-top:60px;font-size:40px">Hasta el 30 de noviembre</div>
<div class="n" style="font-size:150px;line-height:1">$2.753.000</div>
<div style="margin-top:40px;font-size:40px">Desde el 1 de diciembre</div>
<div style="font-family:LS;font-weight:700;font-size:96px;color:var(--ash)">$3.110.000</div>
<h2 style="font-size:50px;margin-top:50px">12 % de descuento para referidos de egresados y por pronto pago.</h2>
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
