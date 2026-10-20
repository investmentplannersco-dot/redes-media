"""Semana 4 (20 al 28 de octubre de 2026): LinkedIn de Joaquín y @contrainingfarma.
Copia del kit: usa las plantillas ct(), st() y pr() de gen_contraining_personal; solo cambia el contenido."""
import os, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_contraining_personal import ct, st, pr, FOOT, ISO, LOGO_H, A, FOTO

END = '<div style="height:120px"></div>'
CHIP = '<div style="margin-top:70px"><span class="chip">WhatsApp 301 727 6517</span></div>'
pieces = {}

# ---------- LinkedIn (retrato en todas, ajuste de la semana anterior) ----------
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

pieces["L4"] = li("¿Afirmación<br>o juicio?", "«Este médico no recibe visitadores.» Suena a hecho. No lo es.",
                  "var(--carbon)", "Joaquín Piña<span>Coach ontológico ICF</span>", tsize=132)
pieces["L5"] = li("Saber del producto no basta.", "La visita médica no se improvisa. Se entrena.",
                  "var(--sea)", "Joaquín Piña<span>Contraining</span>", f"{A}/iso_ct.png", 104)
pieces["L6"] = li("¿Y si un día no puede trabajar?", "Vivir mal: el riesgo del que menos se habla.",
                  "var(--oro)", "Joaquín Piña<span>IP360</span>", f"{A}/logo_ip.png", 104)
pieces["L7"] = li("Escuchar<br>no es oír.", "Oír es percibir sonidos. Escuchar es interpretar.",
                  "var(--carbon)", "Joaquín Piña<span>Coach ontológico ICF</span>", tsize=132)
pieces["L8"] = li("¿Lo entrenado llega a la visita?", "Entrenar es la mitad. La otra mitad es el seguimiento.",
                  "var(--sea)", "Joaquín Piña<span>Contraining</span>", f"{A}/iso_ct.png", 100)

# ---------- @contrainingfarma publicaciones ----------
# P3 · Diplomado (carrusel de 4)
pieces["P3_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:150px" class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:130px;margin-top:30px">No termina en el certificado.</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:54px;margin-top:40px">Son tres partes de una misma formación.</h2>
{FOOT}</div>""", page="1/4")
def parte(n, titulo, texto, pg):
    return ct(f"""<div class="pad">{ISO}
<div style="margin-top:auto"><div class="n" style="font-size:300px;line-height:.85;color:var(--peach)">0{n}</div>
<div class="kicker" style="margin-top:30px">Parte {n} de 3</div>
<h1 style="font-size:124px;margin-top:24px">{titulo}</h1>
<div class="bar" style="margin-top:50px"></div>
<p style="margin-top:44px;font-size:48px;max-width:880px">{texto}</p></div><div style="height:90px"></div>
{FOOT}</div>""", page=pg)
pieces["P3_2"] = parte(1, "Teoría farmacéutica", "La base para hablar con el médico con criterio.", "2/4")
pieces["P3_3"] = parte(2, "Entrenamiento comercial", "Con docentes con experiencia en la industria farmacéutica.", "3/4")
pieces["P3_4"] = ct(f"""<div class="pad">{ISO}
<div class="n" style="font-size:300px;line-height:.85;color:var(--peach);margin-top:40px">03</div>
<div class="kicker" style="margin-top:30px">Parte 3 de 3</div>
<h1 style="font-size:96px;margin-top:24px">Acompañamiento para la inserción laboral</h1>
<div class="bar" style="margin-top:50px"></div>
<p style="margin-top:44px;font-size:38px"><b style="font-family:LS">Inicio: 18 de febrero de 2027.</b><br>120 horas en 3 meses. Clases virtuales en vivo, de lunes a viernes, de 7:00 a 9:00 p. m.</p>
<div style="margin-top:auto"><span class="chip">Escríbenos: WhatsApp 301 727 6517</span></div>
</div>""", page="4/4")

# P4 · Laboratorios: entrenar es la mitad (carrusel de 3)
pieces["P4_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:170px" class="kicker">Para laboratorios</div>
<h1 style="font-size:140px;margin-top:30px">Entrenar es la mitad.</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:62px;margin-top:40px">La otra mitad es el seguimiento.</h2>
{FOOT}</div>""", page="1/3")
pieces["P4_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:86px;margin-top:70px">¿Tu equipo hace en la visita lo que practicó en el aula?</h1>
<p style="margin-top:40px;font-size:40px">Si nadie lo mide, no se sabe. Por eso trabajamos las dos mitades:</p>
<ul class="big" style="margin-top:30px">
<li><b>Entrenamiento a la medida</b> de cada laboratorio.</li>
<li><b>Seguimiento</b> de la fuerza de ventas.</li>
</ul>{FOOT}</div>""", page="2/3")
pieces["P4_3"] = ct(f"""<div class="pad">{ISO}
<div class="n" style="font-size:280px;line-height:.9;margin-top:90px">+30</div>
<h2 style="font-size:64px;margin-top:20px">fuerzas de ventas administradas</h2>
<div class="bar" style="margin-top:56px"></div>
<p style="margin-top:40px;font-size:40px">Más de 27 años formando visitadores médicos en Colombia.</p>
<div style="margin-top:auto">
<h2 style="font-size:50px">¿Diriges una fuerza de ventas?</h2>
<div style="margin-top:30px"><span class="chip">WhatsApp 301 727 6517 · contraining.co</span></div></div>
</div>""", page="3/3")

# P5 · El precio cambia el 1 de diciembre (carrusel de 3)
pieces["P5_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:150px" class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:120px;margin-top:30px">El precio cambia el 1 de diciembre.</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:58px;margin-top:40px">Si te inscribes antes, la diferencia es de $357.000.</h2>
{FOOT}</div>""", page="1/3")
pieces["P5_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:96px;margin-top:70px">Inversión</h1>
<div style="margin-top:56px;font-size:36px">Hasta el 30 de noviembre de 2026</div>
<div class="n" style="font-size:132px;line-height:1;margin-top:8px">$2.753.000</div>
<div style="margin-top:44px;font-size:36px">Desde el 1 de diciembre de 2026</div>
<div style="font-family:LS;font-weight:700;font-size:80px;color:var(--ash);margin-top:8px">$3.110.000</div>
<div style="margin-top:50px;background:var(--peach);padding:30px 36px;border-radius:24px;font-size:34px;line-height:1.35">
<b style="font-family:LS">12 % de descuento</b> para referidos de egresados y por pronto pago.</div>
{FOOT}</div>""", page="2/3")
pieces["P5_3"] = ct(f"""<div class="pad">{ISO}
<div class="kicker" style="margin-top:70px">Inicio: 18 de febrero de 2027</div>
<ul class="big" style="margin-top:40px">
<li><b>120 horas</b> en 3 meses</li>
<li><b>Clases virtuales en vivo</b>, de lunes a viernes, de 7:00 a 9:00 p. m.</li>
<li><b>Teoría farmacéutica, entrenamiento comercial</b> y acompañamiento para la inserción laboral</li>
</ul>
<div style="margin-top:auto"><span class="chip">Escríbenos: WhatsApp 301 727 6517</span></div>
</div>""", page="3/3")

# ---------- @contrainingfarma historias (H12, H14, H18 llevan voz) ----------
pieces["H12"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<div class="n" style="font-size:280px;line-height:.9;margin-top:30px">12 %</div>
<div style="font-family:LS;font-weight:600;font-size:60px">de descuento</div>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:68px;margin-top:50px">Para referidos de egresados y por pronto pago.</h2>
{CHIP}</div>{END}""")
pieces["H13"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<div class="n" style="font-size:300px;line-height:.9;margin-top:30px">+30</div>
<div style="font-family:LS;font-weight:600;font-size:60px">fuerzas de ventas administradas</div>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:80px;margin-top:50px">¿La tuya es la siguiente?</h2>
{CHIP}</div>{END}""")
pieces["H15"] = st(f"""<div style="margin-top:auto">
<h1 style="font-size:110px">¿Sabes del producto o sabes conversar?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:76px;margin-top:50px">El diplomado entrena las dos.</h2>
<p style="margin-top:40px;font-size:42px">Teoría farmacéutica + entrenamiento comercial.</p>
</div>{END}""")
pieces["H14"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:110px;margin-top:30px">¿Quién te enseña la visita médica?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:66px;margin-top:50px">Docentes con experiencia en la industria farmacéutica.</h2>
<p style="margin-top:40px;font-size:40px">Clases en vivo, de lunes a viernes.<br>Inicio: 18 de febrero de 2027.</p>
{CHIP}</div>{END}""")
pieces["H16"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:120px;margin-top:30px">No termina en el certificado.</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:68px;margin-top:50px">Incluye acompañamiento para la inserción laboral.</h2>
{CHIP}</div>{END}""")
pieces["H18"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:106px;margin-top:30px">¿Vacantes abiertas en tu fuerza de ventas?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:76px;margin-top:50px">Reclutamos visitadores médicos.</h2>
<p style="margin-top:40px;font-size:40px">Más de 27 años formándolos en Colombia.<br>+30 fuerzas de ventas administradas.</p>
{CHIP}</div>{END}""")
pieces["H19"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Profesionales comerciales</div>
<h1 style="font-size:96px;margin-top:30px">Hacemos de enlace entre profesionales comerciales de alto nivel y compañías farmacéuticas.</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:64px;margin-top:50px">¿Buscas talento o buscas tu siguiente paso?</h2>
{CHIP}</div>{END}""")
pieces["H20"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:120px;margin-top:30px">Entrenamiento a la medida.</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:68px;margin-top:50px">Diseñado para la fuerza de ventas que lo recibe.</h2>
<p style="margin-top:40px;font-size:40px">Y coordinación de programas de formación.</p>
{CHIP}</div>{END}""")
pieces["H21"] = st(f"""<div style="margin-top:auto"><h1 style="font-size:110px">El precio cambia el 1 de diciembre</h1>
<div style="margin-top:70px;font-size:40px">Hasta el 30 de noviembre</div>
<div class="n" style="font-size:150px;line-height:1">$2.753.000</div>
<div style="margin-top:40px;font-size:40px">Desde el 1 de diciembre</div>
<div style="font-family:LS;font-weight:700;font-size:96px;color:var(--ash)">$3.110.000</div>
<h2 style="font-size:56px;margin-top:50px">Diferencia: $357.000</h2>
{CHIP}</div>{END}""")
pieces["H22"] = st(f"""<div style="margin-top:auto"><div class="kicker">Nueva promoción</div>
<h1 style="font-size:140px;margin-top:30px">18 de febrero de 2027</h1>
<ul style="margin-top:50px">
<li><b>120 horas</b> en 3 meses</li>
<li><b>En vivo</b>, lunes a viernes, 7:00&nbsp;a&nbsp;9:00&nbsp;p.&nbsp;m.</li>
<li><b>Docentes</b> con experiencia en la industria farmacéutica</li></ul>
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
