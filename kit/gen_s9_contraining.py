"""Semana 9 (26 de noviembre al 2 de diciembre de 2026): LinkedIn de Joaquín y @contrainingfarma.
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




def barra2(pct, etiqueta, color):
    return barra(pct, etiqueta, color).replace('margin-top:30px','margin-top:16px').replace('height:30px','height:22px')
def num(n, etiqueta, color, size=150):
    return f"""<div style="margin-top:34px;display:flex;align-items:baseline;gap:26px"><span style="font-family:FR;font-size:{size}px;font-weight:600;line-height:.9;color:{color}">{n}</span>
<span style="font-size:32px;font-weight:600;line-height:1.25;max-width:470px">{etiqueta}</span></div>"""
def puntos(v, etiqueta, color):
    return f"""<div style="margin-top:26px"><div style="display:flex;justify-content:space-between;align-items:baseline">
<span style="font-size:29px;font-weight:600">{etiqueta}</span><span style="font-family:FR;font-size:44px;font-weight:600">{str(v).replace(".", ",")} / 100</span></div>
<div style="height:26px;background:#E4DED4;margin-top:8px"><div style="height:26px;width:{v}%;background:{color}"></div></div></div>"""

pieces["L21"] = info("¿Coach o consejero?", "El coaching en el mundo, 2025",
    num("122.974", "personas ejercen como coach, 15 % más que en 2023", "var(--carbon)", 120)
    + """<p style="margin-top:26px;font-size:30px;font-weight:700">Además del coaching, ofrecen:</p>"""
    + barra2(60, "Formación", "var(--piedra)") + barra2(57, "Consultoría", "var(--piedra)") + barra2(55, "Facilitación", "var(--piedra)") + barra2(49, "Mentoría", "var(--piedra)")
    + """<p style="margin-top:26px;font-family:FR;font-size:40px;font-weight:600;line-height:1.15">Aconsejar es dar la respuesta. Hacer coaching es hacer la pregunta.</p>""",
    "Fuente: ICF, 2025 Global Coaching Study (más de 10.000 participantes en 127 países; realizado por PwC). Datos mundiales, no de Colombia.",
    "Joaquín Piña · Coach ontológico ICF", "var(--carbon)", tsize=88)

pieces["L22"] = info("¿Cuántos oncólogos reciben a la visita?", "Acceso de los representantes de la industria a los especialistas",
    barra(68, "Oncología: acceso restringido", "var(--sea)") + barra(32, "Oncología: acceso pleno", "var(--piedra)") + barra(61, "Hematología: acceso restringido", "var(--sea)")
    + """<p style="margin-top:34px;font-size:30px;font-weight:700">Oncólogos visitados 12 o más veces al año:</p>
<p style="margin-top:8px;font-size:30px;line-height:1.4">Hace una década: <b>cerca del 20 %</b> · Ahora: <b>5 %</b></p>
<p style="margin-top:22px;font-family:FR;font-size:46px;font-weight:600;line-height:1.15">Con menos visitas, cada una pesa más.</p>""",
    "Fuente: ZS, análisis sobre acceso restringido en oncología (2024), con datos de ZS Access Monitor. No son datos de Colombia.",
    "Joaquín Piña · Contraining", "var(--sea)", f"{A}/iso_ct.png", tsize=80)

pieces["L23"] = info("¿Le sobra plata<br>al final del mes?", "Bienestar financiero en Colombia, 2026",
    num("37,7 %", "de los colombianos encuestados tiene dinero disponible al terminar el mes", "#B8962E")
    + """<p style="margin-top:34px;font-size:30px;font-weight:700">Puntaje del índice (de 0 a 100):</p>"""
    + puntos(58.2, "Ahorro frente al ingreso", "#D4AF37") + puntos(59.1, "Seguimiento del presupuesto", "#D4AF37")
    + """<p style="margin-top:30px;font-size:30px;font-weight:600;line-height:1.3">El 32 % de los hogares con menos de tres salarios mínimos no logra ahorrar de forma constante.</p>
<p style="margin-top:18px;font-family:FR;font-size:46px;font-weight:600;line-height:1.15">Ahorrar no es planear.</p>""",
    "Fuente: DataCrédito Experian, Índice de Bienestar Financiero 2026, citado por Portafolio (27 de octubre de 2026). Datos de Colombia.",
    "Joaquín Piña · IP360", "#D4AF37", tsize=80)

# ---------- @contrainingfarma publicaciones (ajuste: las dos del ciclo son de laboratorios) ----------
# P14 · Laboratorios: outsourcing de fuerzas de ventas · jueves 26, 18:00
pieces["P14_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:150px" class="kicker">Para laboratorios</div>
<h1 style="font-size:116px;margin-top:30px">¿Necesitas una fuerza de ventas en campo?</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:62px;margin-top:40px">Outsourcing de fuerzas de ventas.</h2>
{FOOT}</div>""", page="1/3")
pieces["P14_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:92px;margin-top:70px">Lo que hacemos por tu laboratorio</h1>
<ul class="big" style="margin-top:40px">
<li><b>Reclutamiento</b> de visitadores médicos.</li>
<li><b>Entrenamiento a la medida</b> de tu fuerza de ventas.</li>
<li><b>Seguimiento</b> de la fuerza de ventas.</li>
</ul>{FOOT}</div>""", page="2/3")
pieces["P14_3"] = ct(f"""<div class="pad">{ISO}
<div class="n" style="font-size:240px;line-height:.9;margin-top:90px">+30</div>
<h2 style="font-size:64px;margin-top:20px">fuerzas de ventas administradas</h2>
<div class="bar" style="margin-top:56px"></div>
<p style="margin-top:40px;font-size:40px">Cuéntanos qué necesita tu equipo.</p>
<div style="margin-top:auto"><span class="chip">WhatsApp 301 727 6517 · contraining.co</span></div>
</div>""", page="3/3")

# P15 · Laboratorios: enlace con profesionales comerciales de alto nivel · martes 1 de diciembre, 18:00
pieces["P15_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:150px" class="kicker">Para laboratorios</div>
<h1 style="font-size:112px;margin-top:30px">¿Buscas un perfil comercial de alto nivel?</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:58px;margin-top:40px">El cargo no espera. El perfil correcto tampoco.</h2>
{FOOT}</div>""", page="1/3")
pieces["P15_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:92px;margin-top:70px">Hacemos el enlace</h1>
<p style="font-size:50px;line-height:1.3;margin-top:40px">entre <b>profesionales comerciales de alto nivel</b> y <b>compañías farmacéuticas</b>.</p>
<div class="bar" style="margin-top:56px"></div>
<p style="font-size:42px;line-height:1.35;margin-top:40px">Y si lo que necesitas es un equipo: <b>reclutamiento de visitadores médicos</b>.</p>
{FOOT}</div>""", page="2/3")
pieces["P15_3"] = ct(f"""<div class="pad">{ISO}
<div class="n" style="font-size:200px;line-height:.9;margin-top:90px">+27 años</div>
<h2 style="font-size:58px;margin-top:20px">formando visitadores médicos en Colombia</h2>
<p style="margin-top:30px;font-size:42px">Más de 3.000 egresados · 158 promociones</p>
<div class="bar" style="margin-top:50px"></div>
<p style="margin-top:40px;font-size:40px">Cuéntanos qué perfil buscas.</p>
<div style="margin-top:auto"><span class="chip">WhatsApp 301 727 6517 · contraining.co</span></div>
</div>""", page="3/3")

# ---------- @contrainingfarma historias (H51 y H54 llevan voz: ver gen_historias_voz_s9.py) ----------
PRECIOS = """<div class="bar" style="margin-top:50px"></div>
<div style="margin-top:50px;font-size:40px">Hasta el 30 de noviembre</div>
<div class="n" style="font-size:140px;line-height:1">$2.753.000</div>
<div style="margin-top:30px;font-size:40px">Desde el 1 de diciembre: <b>$3.110.000</b></div>"""
pieces["H50"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<div style="font-family:LS;font-weight:600;font-size:60px;margin-top:30px">Quedan</div>
<div class="n" style="font-size:300px;line-height:.9">4 días</div>
<h2 style="font-size:60px;margin-top:20px">con el precio actual.</h2>
{PRECIOS}
{CHIP}</div>{END}""")
pieces["H52"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:116px;margin-top:30px">¿Quién enseña?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:66px;margin-top:50px">Docentes con experiencia en la industria farmacéutica.</h2>
<p style="margin-top:40px;font-size:42px">Clases virtuales en vivo. Inicio: 18 de febrero de 2027.</p>
{CHIP}</div>{END}""")
pieces["H53"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:120px;margin-top:30px">Mañana es el último día</h1>
<h2 style="font-size:60px;margin-top:20px">con el precio actual.</h2>
{PRECIOS}
{CHIP}</div>{END}""")
pieces["H55"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:104px;margin-top:30px">¿Buscas un perfil comercial de alto nivel?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:60px;margin-top:50px">Enlazamos profesionales comerciales de alto nivel con compañías farmacéuticas.</h2>
{CHIP}</div>{END}""")
pieces["H56"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:104px;margin-top:30px">Inicio: 18 de febrero de 2027</h1>
<div class="bar" style="margin-top:60px"></div>
<div style="margin-top:50px;font-size:40px">Desde el 1 de diciembre de 2026</div>
<div class="n" style="font-size:140px;line-height:1">$3.110.000</div>
<div style="margin-top:36px;background:var(--peach);padding:28px 36px;border-radius:24px;font-size:36px;line-height:1.35">
<b style="font-family:LS">12 % de descuento</b> para referidos de egresados y por pronto pago.</div>
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
