import os, sys
from playwright.sync_api import sync_playwright

D = os.path.dirname(os.path.abspath(__file__))
F = f"file://{D}/fonts"
A = f"file://{D}/assets"
FOTO = f"{A}/joaquin_recorte_transparente.png"

FONTS = f"""
@font-face{{font-family:LS;src:url('{F}/LeagueSpartan.ttf')}}
@font-face{{font-family:NU;src:url('{F}/Nunito.ttf')}}
@font-face{{font-family:FR;src:url('{F}/Fraunces.ttf')}}
@font-face{{font-family:MR;src:url('{F}/Manrope.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:var(--w);height:var(--h);overflow:hidden}}
"""

# ---------- Contraining ----------
CT = """
:root{--sea:#3A8844;--apr:#FECB83;--oli:#8BAD64;--peach:#FEDFA2;--ash:#AAB5B4;--cham:#F7EBD4;--ink:#24302A}
body{background:var(--cham);font-family:NU;color:var(--ink);position:relative}
.pad{position:absolute;inset:0;padding:96px 88px;display:flex;flex-direction:column}
.iso{width:120px}
h1{font-family:LS;font-weight:700;color:var(--sea);line-height:.95;letter-spacing:-1px}
h2{font-family:LS;font-weight:600;color:var(--ink);line-height:1.05}
p{font-size:34px;line-height:1.35}
.kicker{font-family:LS;font-weight:600;font-size:30px;letter-spacing:4px;text-transform:uppercase;color:var(--oli)}
.bar{width:120px;height:10px;background:var(--apr);border-radius:5px}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-family:LS;font-weight:600;font-size:28px;color:var(--sea)}
.foot img{height:46px}
ul{list-style:none}
li{font-size:38px;line-height:1.3;padding:26px 0 26px 44px;border-top:2px solid rgba(58,136,68,.25);position:relative}
li:before{content:'';position:absolute;left:0;top:44px;width:18px;height:18px;border-radius:50%;background:var(--sea)}
li b{font-family:LS;font-weight:700}
.n{font-family:LS;font-weight:700;color:var(--sea)}
.chip{display:inline-block;background:var(--sea);color:#fff;font-family:LS;font-weight:600;padding:18px 30px;border-radius:999px;font-size:34px}
.big li{font-size:46px;padding:34px 0 34px 50px}.big li:before{top:56px;width:20px;height:20px}
.page{position:absolute;right:88px;top:104px;font-family:LS;font-weight:600;font-size:26px;color:var(--ash)}
"""

def ct(body, w=1080, h=1350, page=""):
    pg = f'<div class="page">{page}</div>' if page else ""
    return f"<html><head><style>:root{{--w:{w}px;--h:{h}px}}{FONTS}{CT}</style></head><body>{pg}{body}</body></html>"

FOOT = f'<div class="foot"><span>WhatsApp 301 727 6517 · contraining.co</span></div>'
LOGO_H = f'<img src="{A}/logo_ct_h.png" style="height:64px;align-self:flex-start">'
ISO = f'<img class="iso" src="{A}/iso_ct.png">'

pieces = {}

# P1 carrusel diplomado
pieces["P1_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:150px" class="kicker">Nueva promoción</div>
<h2 style="font-size:64px;margin-top:22px">Diplomado en<br>Visita Médica</h2>
<h1 style="font-size:190px;margin-top:40px">18 de<br>febrero</h1>
<div style="font-family:LS;font-weight:700;font-size:64px;color:var(--ink);margin-top:10px">2027</div>
<div class="bar" style="margin-top:46px"></div>
<p style="margin-top:30px;max-width:780px">Más de 27 años formando visitadores médicos en Colombia.</p>
{FOOT}</div>""", page="1/3")

pieces["P1_2"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:96px;margin-top:70px">Qué incluye</h1>
<ul style="margin-top:50px">
<li><b>120 horas</b> en 3 meses</li>
<li><b>Clases virtuales en vivo</b>, de lunes a viernes, de 7:00 a 9:00 p. m.</li>
<li><b>Docentes con experiencia</b> en la industria farmacéutica</li>
<li><b>Teoría farmacéutica, entrenamiento comercial</b> y acompañamiento para la inserción laboral</li>
</ul>{FOOT}</div>""", page="2/3")

pieces["P1_3"] = ct(f"""<div class="pad">{ISO}
<h1 style="font-size:96px;margin-top:70px">Inversión</h1>
<div style="margin-top:60px;font-size:34px">Hasta el 30 de noviembre</div>
<div class="n" style="font-size:132px;line-height:1;margin-top:8px">$2.753.000</div>
<div style="margin-top:44px;font-size:34px">Desde el 1 de diciembre</div>
<div style="font-family:LS;font-weight:700;font-size:76px;color:var(--ash);margin-top:8px">$3.110.000</div>
<div style="margin-top:56px;background:var(--peach);padding:30px 36px;border-radius:24px;font-size:34px;line-height:1.35">
<b style="font-family:LS">12 % de descuento</b> para referidos de egresados y por pronto pago.</div>
<div style="margin-top:auto"><span class="chip">Escríbenos: WhatsApp 301 727 6517</span></div>
</div>""", page="3/3")

# P2 carrusel laboratorios
pieces["P2_1"] = ct(f"""<div class="pad">{LOGO_H}
<div style="margin-top:170px" class="kicker">Para laboratorios</div>
<h1 style="font-size:104px;margin-top:30px">No solo formamos visitadores médicos.</h1>
<h2 style="font-size:58px;margin-top:40px;color:var(--ink)">Trabajamos con los laboratorios que los contratan.</h2>
<div class="bar" style="margin-top:56px"></div>
{FOOT}</div>""", page="1/4")

pieces["P2_2"] = ct(f"""<div class="pad">{ISO}
<div class="kicker" style="margin-top:60px">01 / 03</div>
<h1 style="font-size:104px;margin-top:20px">Equipo comercial</h1>
<ul class="big" style="margin-top:50px">
<li><b>Outsourcing de fuerzas de ventas.</b> Hemos administrado más de 30.</li>
<li><b>Reclutamiento</b> de visitadores médicos.</li>
<li><b>Seguimiento</b> de la fuerza de ventas.</li>
</ul>{FOOT}</div>""", page="2/4")

pieces["P2_3"] = ct(f"""<div class="pad">{ISO}
<div class="kicker" style="margin-top:60px">02 / 03</div>
<h1 style="font-size:104px;margin-top:20px">Formación</h1>
<ul class="big" style="margin-top:50px">
<li><b>Entrenamiento a la medida</b> de cada laboratorio.</li>
<li><b>Coordinación de programas</b> de formación.</li>
</ul>{FOOT}</div>""", page="3/4")

pieces["P2_4"] = ct(f"""<div class="pad">{ISO}
<div class="kicker" style="margin-top:60px">03 / 03</div>
<h1 style="font-size:104px;margin-top:20px">Mercado</h1>
<ul class="big" style="margin-top:50px">
<li><b>Planes de marketing.</b></li>
<li><b>Enlace</b> entre profesionales comerciales de alto nivel y compañías farmacéuticas.</li>
</ul>
<div style="margin-top:auto">
<h2 style="font-size:52px">¿Diriges una fuerza de ventas o un área de formación?</h2>
<div style="margin-top:30px"><span class="chip">WhatsApp 301 727 6517</span></div></div>
</div>""", page="4/4")

# Historias 1080x1920 (zona segura: 250px arriba y abajo)
def st(inner):
    inner=inner.replace('<ul style=','<ul class="big" style=')
    return ct(f'<div class="pad" style="padding:260px 96px 280px">{ISO}{inner}</div>', 1080, 1920)

pieces["H1"] = st("""<div style="margin-top:auto"><h1 style="font-size:120px">Contraining</h1>
<div style="font-family:LS;font-weight:600;font-size:56px;margin-top:30px">= Contratación + Training</div>
<div class="bar" style="margin-top:60px"></div>
<h2 style="font-size:84px;margin-top:50px">Formar para emplear.</h2></div><div style="height:120px"></div>""")

pieces["H2"] = st("""<div style="margin-top:auto"><div class="kicker">Nueva promoción</div>
<h2 style="font-size:70px;margin-top:24px">Diplomado en Visita Médica</h2>
<h1 style="font-size:150px;margin-top:40px">Inicio:<br>18 de febrero de 2027</h1>
<div style="margin-top:70px"><span class="chip">WhatsApp 301 727 6517</span></div></div><div style="height:120px"></div>""")

pieces["H3"] = st("""<div style="margin-top:auto">
<div class="n" style="font-size:300px;line-height:.9">158</div>
<div style="font-family:LS;font-weight:600;font-size:60px">promociones</div>
<div class="bar" style="margin:60px 0"></div>
<div class="n" style="font-size:220px;line-height:.9">3.000+</div>
<div style="font-family:LS;font-weight:600;font-size:60px">egresados</div></div><div style="height:120px"></div>""")

pieces["H4"] = st("""<div style="margin-top:110px"><h1 style="font-size:96px">Para laboratorios</h1>
<ul style="margin-top:46px">
<li>Outsourcing de fuerzas de ventas</li><li>Seguimiento de la fuerza de ventas</li><li>Reclutamiento</li>
<li>Entrenamiento a la medida</li><li>Coordinación de programas de formación</li><li>Planes de marketing</li>
<li>Enlace con perfiles comerciales de alto nivel</li></ul></div>""")

pieces["H5"] = st("""<div style="margin-top:auto"><h1 style="font-size:130px">Clases en vivo</h1>
<div class="bar" style="margin:56px 0"></div>
<h2 style="font-size:70px">Virtuales</h2>
<h2 style="font-size:70px;margin-top:20px">Lunes a viernes</h2>
<h2 style="font-size:70px;margin-top:20px">7:00 a 9:00 p. m.</h2>
<p style="margin-top:50px">Diplomado en Visita Médica · 120 horas en 3 meses</p></div><div style="height:120px"></div>""")

pieces["H6"] = st("""<div style="margin-top:110px"><h1 style="font-size:110px">¿Para quién es?</h1>
<ul style="margin-top:50px">
<li>Recién graduados que buscan entrar al sector farmacéutico</li>
<li>Tecnólogos en ventas, salud o servicio al cliente</li>
<li>Vendedores con experiencia, sin conocimiento farmacéutico</li>
<li>Profesionales de la salud que quieren aprender a comunicarse con el médico</li></ul></div>""")

pieces["H7"] = st("""<div style="margin-top:auto"><h1 style="font-size:110px">El precio cambia en diciembre</h1>
<div style="margin-top:80px;font-size:40px">Hasta el 30 de noviembre</div>
<div class="n" style="font-size:150px;line-height:1">$2.753.000</div>
<div style="margin-top:50px;font-size:40px">Desde el 1 de diciembre</div>
<div style="font-family:LS;font-weight:700;font-size:96px;color:var(--ash)">$3.110.000</div>
<div style="margin-top:70px"><span class="chip">WhatsApp 301 727 6517</span></div></div><div style="height:120px"></div>""")

# ---------- Marca personal ----------
PR = """
:root{--hueso:#F4F1EC;--carbon:#2B2B2B;--piedra:#8A8580;--sea:#3A8844;--oro:#D4AF37}
body{background:var(--hueso);font-family:MR;color:var(--carbon);position:relative}
.pad{position:absolute;inset:0;padding:96px 88px;display:flex;flex-direction:column}
h1{font-family:FR;font-weight:600;line-height:1;letter-spacing:-1.5px;font-variation-settings:'opsz' 144,'SOFT' 0,'WONK' 0}
.name{font-family:MR;font-weight:700;font-size:26px;letter-spacing:5px;text-transform:uppercase;color:var(--piedra)}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end}
.foot .who{font-weight:700;font-size:28px}
.foot .who span{display:block;font-weight:500;font-size:24px;color:var(--piedra);margin-top:6px}
p{font-size:34px;line-height:1.4}
"""
def pr(body, w=1080, h=1350):
    return f"<html><head><style>:root{{--w:{w}px;--h:{h}px}}{FONTS}{PR}</style></head><body>{body}</body></html>"

pieces["L1"] = pr(f"""
<img src="{FOTO}" style="position:absolute;right:-40px;bottom:0;height:900px">
<div class="pad"><div class="name">Joaquín Piña Labastida</div>
<h1 style="font-size:118px;margin-top:80px">¿Método o<br>improvisación?</h1>
<div style="width:90px;height:6px;background:var(--carbon);margin-top:56px"></div>
<p style="margin-top:36px;max-width:440px">La misma pregunta, en la carrera y en el patrimonio.</p>
<div class="foot"><div class="who">Contraining · IP360<span>Coach ICF</span></div></div></div>""")

pieces["L2"] = pr(f"""<div class="pad"><div class="name">Joaquín Piña Labastida</div>
<div style="position:relative;margin-top:150px;align-self:flex-start">
<h1 style="font-size:150px;white-space:nowrap">7 · 38 · 55</h1>
<div style="position:absolute;left:-10px;right:-10px;top:52%;height:12px;background:var(--sea)"></div></div>
<p style="font-size:44px;line-height:1.3;margin-top:70px;max-width:860px;font-weight:600">La cifra más repetida en capacitaciones de ventas casi siempre se cita fuera de contexto.</p>
<p style="margin-top:36px;color:var(--piedra);max-width:820px">Mehrabian midió sentimientos y actitudes, no información científica.</p>
<div class="foot"><div class="who">Joaquín Piña<span>Contraining</span></div><img src="{A}/iso_ct.png" style="height:70px"></div></div>""")

pieces["L3"] = pr(f"""<div class="pad"><div class="name">Joaquín Piña Labastida</div>
<h1 style="font-size:124px;margin-top:80px">Ahorrar no es planear.</h1>
<div style="width:90px;height:6px;background:var(--oro);margin-top:50px"></div>
<div style="margin-top:50px">
<div style="border-top:2px solid #DDD7CE;padding:26px 0"><b style="font-family:FR;font-size:46px;font-weight:600">Vivir poco</b><p style="font-size:30px;color:var(--piedra);margin-top:6px">¿Qué pasa con quienes dependen de mí?</p></div>
<div style="border-top:2px solid #DDD7CE;padding:26px 0"><b style="font-family:FR;font-size:46px;font-weight:600">Vivir mucho</b><p style="font-size:30px;color:var(--piedra);margin-top:6px">¿De qué voy a vivir?</p></div>
<div style="border-top:2px solid #DDD7CE;border-bottom:2px solid #DDD7CE;padding:26px 0"><b style="font-family:FR;font-size:46px;font-weight:600">Vivir mal</b><p style="font-size:30px;color:var(--piedra);margin-top:6px">¿Qué pasa con mis ingresos si enfermo o tengo un accidente?</p></div></div>
<div class="foot"><div class="who">Joaquín Piña<span>IP360</span></div><img src="{A}/logo_ip.png" style="height:96px"></div></div>""")

if __name__ == "__main__":
    only = sys.argv[1:] or list(pieces)
    OUT = os.environ.get("OUT", f"{D}/out"); os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for k in only:
            html = pieces[k]
            w, h = (1080, 1920) if k.startswith("H") else (1080, 1350)
            pg = b.new_page(viewport={"width": w, "height": h})
            path = f"{OUT}/_{k}.html"
            open(path, "w").write(html)
            pg.goto(f"file://{path}"); pg.wait_for_timeout(300)
            pg.screenshot(path=f"{OUT}/{k}.png")
            pg.close()
        b.close()
    print("ok", len(only))
