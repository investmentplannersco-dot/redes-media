"""Semana 7 (12 al 18 de noviembre de 2026): LinkedIn de Joaquín y @contrainingfarma.
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


pieces["L15"] = info("¿Su equipo usa el material en la visita?", "Reuniones con médicos en las que el equipo de campo compartió material",
    '<div style="display:flex;gap:30px;margin-top:30px">' + columna(39, "2023", "var(--piedra)") + columna(46, "2024", "var(--piedra)") + columna(48, "1T 2025", "var(--sea)") + '</div>'
    + """<p style="margin-top:26px;font-size:32px;font-weight:600;line-height:1.3">Cuando sí se usa, las nuevas iniciaciones de tratamiento más que se duplican.</p>
<p style="margin-top:18px;font-family:FR;font-size:46px;font-weight:600;line-height:1.15">El material se aprueba. Usarlo se entrena.</p>""",
    "Fuente: Veeva Pulse Report, Top Insights 1Q25 (datos 4T 2022 a 1T 2025). Datos de la industria a nivel global, no de Colombia.",
    "Joaquín Piña · Contraining", "var(--sea)", f"{A}/iso_ct.png", tsize=82)

def par(anio, lid, emp):
    def b(v, c):
        return f"""<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:380px">
<div style="font-family:FR;font-size:52px;font-weight:600">{v} %</div>
<div style="width:110px;height:{v*9:.0f}px;flex:none;background:{c};margin-top:8px"></div></div>"""
    return f"""<div style="flex:1;display:flex;flex-direction:column;align-items:center">
<div style="display:flex;gap:14px;align-items:flex-end">{b(lid, "var(--carbon)")}{b(emp, "var(--piedra)")}</div>
<div style="font-size:32px;font-weight:600;margin-top:12px">{anio}</div></div>"""
LEY = """<div style="display:flex;gap:40px;margin-top:24px;font-size:28px;font-weight:600">
<span><span style="display:inline-block;width:26px;height:26px;background:var(--carbon);vertical-align:-4px;margin-right:10px"></span>Gerentes</span>
<span><span style="display:inline-block;width:26px;height:26px;background:var(--piedra);vertical-align:-4px;margin-right:10px"></span>Todos los empleados</span></div>"""
pieces["L16"] = info("¿Quién acompaña al que acompaña?", "Empleados comprometidos con su trabajo, en el mundo",
    LEY + '<div style="display:flex;gap:20px;margin-top:10px">' + par("2023", 30, 23) + par("2024", 27, 21) + par("2025", 22, 20) + '</div>'
    + """<p style="margin-top:22px;font-family:FR;font-size:44px;font-weight:600;line-height:1.15">Los gerentes cayeron más rápido que sus equipos.</p>""",
    "Fuente: Gallup, State of the Global Workplace, informes 2025 y 2026. Datos mundiales, no de Colombia.",
    "Joaquín Piña · Coach ontológico ICF", "var(--carbon)", tsize=92)

pieces["L17"] = info("¿Lo que piden las empresas se puede entrenar?", "Empleadores con dificultad para encontrar el talento que necesitan, 2026",
    barra(61, "Colombia", "var(--sea)") + barra(72, "Global (41 países)", "var(--piedra)")
    + """<p style="margin-top:36px;font-size:30px;font-weight:700">Habilidades humanas que destacan:</p>
<p style="margin-top:10px;font-size:30px;line-height:1.45">Comunicación y trabajo en equipo · Profesionalismo · Adaptabilidad y ganas de aprender · Pensamiento crítico</p>
<p style="margin-top:26px;font-family:FR;font-size:46px;font-weight:600;line-height:1.15">Ninguna viene en un título. Se practican.</p>""",
    "Fuente: ManpowerGroup, Escasez de Talento 2026 (39.063 empleadores en 41 países), citado por INCP y Portafolio.",
    "Joaquín Piña · Contraining", "var(--sea)", f"{A}/iso_ct.png", tsize=82)

# ---------- @contrainingfarma publicaciones ----------
# P10 · Laboratorios: reclutamiento (carrusel de 3) · jueves 12, 18:00
pieces["P10_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:150px" class="kicker">Para laboratorios</div>
<h1 style="font-size:116px;margin-top:30px">¿Tu laboratorio necesita visitadores médicos?</h1>
<div class="bar" style="margin-top:56px"></div>
<h2 style="font-size:58px;margin-top:40px">Encontrar a la persona es una parte. La otra es que llegue preparada.</h2>
{FOOT}</div>""", page="1/3")
pieces["P10_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:90px;margin-top:70px">Tres frentes para tu laboratorio</h1>
<ul class="big" style="margin-top:40px">
<li><b>Reclutamiento</b> de visitadores médicos.</li>
<li><b>Enlace</b> entre profesionales comerciales de alto nivel y compañías farmacéuticas.</li>
<li><b>Entrenamiento</b> a la medida.</li>
</ul>{FOOT}</div>""", page="2/3")
pieces["P10_3"] = ct(f"""<div class="pad">{ISO}
<div class="n" style="font-size:240px;line-height:.9;margin-top:90px">+3.000</div>
<h2 style="font-size:60px;margin-top:20px">egresados y más de 27 años formando visitadores médicos en Colombia</h2>
<div class="bar" style="margin-top:56px"></div>
<p style="margin-top:40px;font-size:40px">Cuéntanos qué perfil buscas.</p>
<div style="margin-top:auto"><span class="chip">WhatsApp 301 727 6517 · contraining.co</span></div>
</div>""", page="3/3")

# P11 · Diplomado: trayectoria (carrusel de 3) · martes 17, 18:00
pieces["P11_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:170px" class="kicker">Diplomado en Visita Médica</div>
<div class="n" style="font-size:300px;line-height:.9;margin-top:30px">158</div>
<h1 style="font-size:96px;margin-top:20px">promociones antes que la tuya.</h1>
{FOOT}</div>""", page="1/3")
pieces["P11_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:96px;margin-top:70px">Una trayectoria que se puede medir</h1>
<ul class="big" style="margin-top:40px">
<li><b>Más de 27 años</b> formando visitadores médicos en Colombia.</li>
<li><b>Más de 3.000</b> egresados.</li>
<li><b>120 horas</b> en 3 meses: teoría farmacéutica, entrenamiento comercial y acompañamiento para la inserción laboral.</li>
</ul>{FOOT}</div>""", page="2/3")
pieces["P11_3"] = ct(f"""<div class="pad">{ISO}
<div class="kicker" style="margin-top:70px">Inicio</div>
<h1 style="font-size:104px;margin-top:20px">18 de febrero de 2027</h1>
<div style="margin-top:50px;font-size:36px">Hasta el 30 de noviembre de 2026</div>
<div class="n" style="font-size:112px;line-height:1;margin-top:8px">$2.753.000</div>
<div style="margin-top:24px;font-size:36px">Desde el 1 de diciembre de 2026: <b>$3.110.000</b></div>
<div style="margin-top:36px;background:var(--peach);padding:28px 36px;border-radius:24px;font-size:34px;line-height:1.35">
<b style="font-family:LS">12 % de descuento</b> para referidos de egresados y por pronto pago.</div>
<div style="margin-top:auto"><span class="chip">Escríbenos: WhatsApp 301 727 6517</span></div>
</div>""", page="3/3")


# ---------- @contrainingfarma historias (H40 y H42 llevan voz: ver gen_historias_voz_s7.py) ----------
pieces["H36"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<h1 style="font-size:110px;margin-top:30px">¿Buscas visitadores médicos?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:64px;margin-top:50px">Reclutamos visitadores médicos para laboratorios.</h2>
<p style="margin-top:40px;font-size:42px">Y los formamos desde hace más de 27 años.</p>
{CHIP}</div>{END}""")
pieces["H37"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<h1 style="font-size:110px;margin-top:30px">¿Quién te enseña a visitar?</h1>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:66px;margin-top:50px">Docentes con experiencia en la industria farmacéutica.</h2>
<p style="margin-top:40px;font-size:42px">Inicio: 18 de febrero de 2027.</p>
{CHIP}</div>{END}""")
pieces["H38"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Para laboratorios</div>
<div class="n" style="font-size:280px;line-height:.9;margin-top:30px">+30</div>
<div style="font-family:LS;font-weight:600;font-size:60px">fuerzas de ventas administradas</div>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:70px;margin-top:50px">Outsourcing de fuerzas de ventas para laboratorios.</h2>
{CHIP}</div>{END}""")
pieces["H39"] = st(f"""<div style="margin-top:auto">
<div class="kicker">¿Eres egresado de Contraining?</div>
<h1 style="font-size:104px;margin-top:30px">¿Conoces a alguien que quiera entrar a la visita médica?</h1>
<div class="bar" style="margin-top:60px"></div>
<div class="n" style="font-size:170px;line-height:1;margin-top:40px">12 %</div>
<h2 style="font-size:56px;margin-top:10px">de descuento para referidos de egresados y por pronto pago.</h2>
{CHIP}</div>{END}""")
pieces["H41"] = st(f"""<div style="margin-top:auto">
<div class="kicker">Diplomado en Visita Médica</div>
<div class="n" style="font-size:300px;line-height:.9;margin-top:30px">158</div>
<div style="font-family:LS;font-weight:600;font-size:60px">promociones antes que la tuya</div>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:66px;margin-top:50px">Próxima promoción: 18 de febrero de 2027.</h2>
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
