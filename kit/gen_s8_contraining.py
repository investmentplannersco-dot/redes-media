"""Semana 8 (19 al 25 de noviembre de 2026): LinkedIn de Joaquín y @contrainingfarma.
Copia del kit: usa las plantillas ct(), st() y pr() de gen_contraining_personal; solo cambia el contenido."""
import os, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_contraining_personal import ct, st, pr, FOOT, ISO, LOGO_H, A

END = '<div style="height:120px"></div>'
CHIP = '<div style="margin-top:70px"><span class="chip">WhatsApp 301 727 6517</span></div>'
pieces = {}

# ---------- LinkedIn (infografías con datos, sin retrato) ----------
def info(title, sub, cuerpo, fuente, who, accent, logo="", tsize=84):
    lg = f'<img src="{logo}" style="height:72px">' if logo else ""
    return pr(f"""<div class="pad"><div class="name">Joaquín Piña Labastida</div>
<h1 style="font-size:{tsize}px;margin-top:56px">{title}</h1>
<p style="margin-top:22px;font-size:34px;color:var(--piedra)">{sub}</p>
<div style="width:90px;height:6px;background:{accent};margin-top:30px"></div>
{cuerpo}
<div class="foot" style="padding-top:20px"><div class="who">{who}<span style="font-size:21px;max-width:760px">{fuente}</span></div>{lg}</div></div>""")

def barra(pct, etiqueta, color):
    txt = (f"{pct:.1f}".replace(".", ",") + " %").replace(",0 %", " %")
    return f"""<div style="margin-top:30px"><div style="display:flex;justify-content:space-between;align-items:baseline">
<span style="font-size:30px;font-weight:600">{etiqueta}</span><span style="font-family:FR;font-size:48px;font-weight:600">{txt}</span></div>
<div style="height:30px;background:#E4DED4;margin-top:8px"><div style="height:30px;width:{pct}%;background:{color}"></div></div></div>"""

def fila(signo, color, caso, efecto):
    return f"""<div style="display:flex;align-items:center;gap:34px;border-top:2px solid #DDD7CE;padding:30px 0">
<div style="width:92px;height:92px;flex:none;background:{color};color:#fff;font-family:FR;font-size:64px;display:flex;align-items:center;justify-content:center">{signo}</div>
<div><div style="font-size:34px;font-weight:700;line-height:1.2">{caso}</div><div style="font-size:30px;color:var(--piedra);margin-top:6px">{efecto}</div></div></div>"""

def columna(pct, anio, color):
    return f"""<div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;height:400px">
<div style="font-family:FR;font-size:84px;font-weight:600">{pct} %</div>
<div style="width:230px;height:{pct*4.4:.0f}px;flex:none;background:{color};margin-top:12px"></div>
<div style="font-size:32px;font-weight:600;margin-top:14px">{anio}</div></div>"""



pieces["L18"] = info("¿Su programa de desarrollo se usa?", "Organizaciones según la madurez de su desarrollo de carrera, 2025",
    barra(36, "Programas consolidados («campeonas»)", "var(--carbon)") + barra(31, "Programas con adopción limitada", "var(--piedra)") + barra(33, "Sin iniciativas o apenas empezando", "var(--piedra)")
    + """<p style="margin-top:40px;font-size:32px;font-weight:600;line-height:1.3">31 % + 33 % = 64 % todavía no llega al nivel de las «campeonas».</p>
<p style="margin-top:18px;font-family:FR;font-size:46px;font-weight:600;line-height:1.15">Un programa se escribe. El desarrollo se conversa.</p>""",
    "Fuente: LinkedIn, Workplace Learning Report 2025 (937 profesionales de aprendizaje y RR. HH. en varias regiones). No son datos de Colombia.",
    "Joaquín Piña · Coach ontológico ICF", "var(--carbon)", tsize=88)

pieces["L19"] = info("¿Cómo prefieren los médicos recibir a la industria?", "Peso de cada canal en las preferencias de los profesionales de la salud, 2025",
    barra(40, "Visita individual presencial", "var(--sea)") + barra(16, "Congresos presenciales", "var(--piedra)") + barra(15, "Correo electrónico", "var(--piedra)")
    + """<p style="margin-top:34px;font-size:30px;font-weight:700">La visita presencial, por generación:</p>
<p style="margin-top:8px;font-size:30px;line-height:1.4">Nacidos antes de 1980: <b>43 %</b> · Nacidos después de 1980: <b>37 %</b></p>
<p style="margin-top:22px;font-family:FR;font-size:46px;font-weight:600;line-height:1.15">La visita sigue al frente. Llegar preparado se entrena.</p>""",
    "Fuente: IQVIA, ChannelDynamics Channel Preference Survey 2025 (más de 33.000 profesionales de la salud, 38 países). Cifras de EE. UU. y cinco países europeos. No son datos de Colombia.",
    "Joaquín Piña · Contraining", "var(--sea)", f"{A}/iso_ct.png", tsize=78)

def anios(v, etiqueta, color):
    return f"""<div style="margin-top:30px"><div style="display:flex;justify-content:space-between;align-items:baseline">
<span style="font-size:30px;font-weight:600">{etiqueta}</span><span style="font-family:FR;font-size:48px;font-weight:600">{str(v).replace(".", ",")} años</span></div>
<div style="height:30px;background:#E4DED4;margin-top:8px"><div style="height:30px;width:{v/8*100:.1f}%;background:{color}"></div></div></div>"""
pieces["L20"] = info("¿Cuánto ha cotizado de verdad?", "Años cotizados para pensión a los 30, si empezó a trabajar a los 22",
    anios(8, "Lo que debería llevar", "var(--carbon)") + anios(2.2, "Hombre, en promedio", "#D4AF37") + anios(1.8, "Mujer, en promedio", "#D4AF37")
    + """<p style="margin-top:36px;font-size:32px;font-weight:600;line-height:1.3">La mitad de las personas ha cotizado menos del 25 % del tiempo que necesita para pensionarse.</p>
<p style="margin-top:18px;font-family:FR;font-size:46px;font-weight:600;line-height:1.15">La pensión no se improvisa.</p>""",
    "Fuente: Asofondos, «La informalidad a lo largo del ciclo de vida» (2025), citado por El Colombiano (25 de noviembre de 2025). Datos de Colombia.",
    "Joaquín Piña · IP360", "#D4AF37", tsize=92)

# ---------- @contrainingfarma publicaciones (ajuste: diplomado el jueves, laboratorios el martes) ----------
# P12 · Diplomado: 5 respuestas antes de inscribirte (carrusel de 3) · jueves 19, 18:00
pieces["P12_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:160px" class="kicker">Diplomado en Visita Médica</div>
<div class="n" style="font-size:300px;line-height:.9;margin-top:30px">5</div>
<h1 style="font-size:104px;margin-top:20px">respuestas antes de inscribirte</h1>
{FOOT}</div>""", page="1/3")
def qa(q, a):
    return f"""<div style="border-top:2px solid rgba(58,136,68,.25);padding:34px 0"><div style="font-family:LS;font-weight:700;font-size:54px;color:var(--sea)">{q}</div><div style="font-size:44px;margin-top:10px;line-height:1.3">{a}</div></div>"""
pieces["P12_2"] = ct(f"""<div class="pad">{ISO}
<div style="margin-top:50px">
{qa("¿Cuándo empieza?", "El 18 de febrero de 2027.")}
{qa("¿Cuánto dura?", "120 horas en 3 meses.")}
{qa("¿En qué horario?", "Lunes a viernes, de 7:00 a 9:00 p. m., en clases virtuales en vivo.")}
{qa("¿Quién enseña?", "Docentes con experiencia en la industria farmacéutica.")}
</div>{FOOT}</div>""", page="2/3")
pieces["P12_3"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:96px;margin-top:70px">¿Cuánto cuesta?</h1>
<div style="margin-top:44px;font-size:36px">Hasta el 30 de noviembre de 2026</div>
<div class="n" style="font-size:112px;line-height:1;margin-top:8px">$2.753.000</div>
<div style="margin-top:24px;font-size:36px">Desde el 1 de diciembre de 2026: <b>$3.110.000</b></div>
<div style="margin-top:36px;background:var(--peach);padding:28px 36px;border-radius:24px;font-size:34px;line-height:1.35">
<b style="font-family:LS">12 % de descuento</b> para referidos de egresados y por pronto pago.</div>
<div style="margin-top:auto"><span class="chip">Escríbenos: WhatsApp 301 727 6517</span></div>
</div>""", page="3/3")

# P13 · Laboratorios: del plan a la visita (carrusel de 3) · martes 24, 18:00
pieces["P13_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:150px" class="kicker">Para laboratorios</div>
<h1 style="font-size:116px;margin-top:30px">¿Tu plan de marketing llega hasta la visita?</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:58px;margin-top:40px">Lo que se planea en la oficina se juega en el consultorio.</h2>
{FOOT}</div>""", page="1/3")
pieces["P13_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:96px;margin-top:70px">Del plan a la visita</h1>
<ul class="big" style="margin-top:40px">
<li><b>Planes de marketing</b> para tu laboratorio.</li>
<li><b>Entrenamiento a la medida</b> de tu fuerza de ventas.</li>
<li><b>Seguimiento</b> de la fuerza de ventas en campo.</li>
</ul>{FOOT}</div>""", page="2/3")
pieces["P13_3"] = ct(f"""<div class="pad">{ISO}
<div class="n" style="font-size:240px;line-height:.9;margin-top:90px">+30</div>
<h2 style="font-size:60px;margin-top:20px">fuerzas de ventas administradas y más de 27 años formando visitadores médicos en Colombia</h2>
<div class="bar" style="margin-top:56px"></div>
<p style="margin-top:40px;font-size:40px">Cuéntanos qué necesita tu equipo.</p>
<div style="margin-top:auto"><span class="chip">WhatsApp 301 727 6517 · contraining.co</span></div>
</div>""", page="3/3")

# ---------- @contrainingfarma historias (H44 y H47 llevan voz: ver gen_historias_voz_s8.py) ----------
pieces["H43"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:110px;margin-top:30px">¿Virtual significa grabado?</h1>
<h2 style="font-size:90px;margin-top:20px">No.</h2>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:62px;margin-top:50px">Clases virtuales en vivo, de lunes a viernes, de 7:00 a 9:00 p. m.</h2>
<p style="margin-top:40px;font-size:42px">Inicio: 18 de febrero de 2027.</p>
{CHIP}</div>{END}""")
pieces["H45"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:104px;margin-top:30px">¿Qué pasa en la visita después del entrenamiento?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:66px;margin-top:50px">Seguimiento de la fuerza de ventas para laboratorios.</h2>
{CHIP}</div>{END}""")
pieces["H46"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<div class="n" style="font-size:280px;line-height:.9;margin-top:30px">120</div>
<div style="font-family:LS;font-weight:600;font-size:60px">horas en 3 meses</div>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:58px;margin-top:50px">Teoría farmacéutica, entrenamiento comercial y acompañamiento para la inserción laboral.</h2>
{CHIP}</div>{END}""")
pieces["H48"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:104px;margin-top:30px">¿Tu plan de marketing llega hasta la visita?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:62px;margin-top:50px">Planes de marketing, entrenamiento a la medida y seguimiento de la fuerza de ventas.</h2>
{CHIP}</div>{END}""")
pieces["H49"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<div style="font-family:LS;font-weight:600;font-size:60px;margin-top:30px">Quedan</div>
<div class="n" style="font-size:300px;line-height:.9">5 días</div>
<h2 style="font-size:60px;margin-top:20px">con el precio actual.</h2>
<div class="bar" style="margin-top:50px"></div>
<div style="margin-top:50px;font-size:40px">Hasta el 30 de noviembre</div>
<div class="n" style="font-size:140px;line-height:1">$2.753.000</div>
<div style="margin-top:30px;font-size:40px">Desde el 1 de diciembre: <b>$3.110.000</b></div>
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
