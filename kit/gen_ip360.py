import os, sys
from playwright.sync_api import sync_playwright

D = os.path.dirname(os.path.abspath(__file__))
F = f"file://{D}/fonts"
A = f"file://{D}/assets"

CSS = f"""
@font-face{{font-family:SG;src:url('{F}/SpaceGrotesk.ttf')}}
@font-face{{font-family:JM;src:url('{F}/JetBrainsMono.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--negro:#000;--blanco:#fff;--oro:#D4AF37;--gris:#1a1a1a;--gris2:#8c8c8c}}
body{{width:var(--w);height:var(--h);overflow:hidden;background:var(--negro);color:var(--blanco);font-family:SG;position:relative}}
.pad{{position:absolute;inset:0;padding:96px 88px;display:flex;flex-direction:column}}
.mono{{font-family:JM}}
h1{{font-weight:700;letter-spacing:-2px;line-height:1}}
.oro{{color:var(--oro)}}
.win{{border:3px solid var(--blanco);background:var(--negro)}}
.bar{{display:flex;align-items:center;justify-content:space-between;background:var(--blanco);color:var(--negro);font-family:JM;font-weight:700;font-size:26px;padding:10px 18px}}
.btns{{display:flex;gap:8px}}.btns i{{display:block;width:26px;height:26px;border:3px solid var(--negro)}}
.body{{padding:44px 44px}}
.prompt:before{{content:'C:\\\\> ';color:var(--oro)}}
.cursor{{display:inline-block;width:22px;height:46px;background:var(--oro);vertical-align:middle;margin-left:8px}}
.foot{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-family:JM;font-size:24px;color:var(--gris2)}}
.foot img{{height:84px}}
.page{{position:absolute;right:88px;top:104px;font-family:JM;font-size:24px;color:var(--gris2)}}
p{{font-size:38px;line-height:1.35}}
.q{{border-top:2px solid #333;padding:40px 0;font-size:52px;line-height:1.25;font-weight:500}}
.q b{{font-family:JM;color:var(--oro);font-weight:700;margin-right:18px}}
"""

LOGO = f'<img src="{A}/logo_ip_blanco.png">'
def page(body, w=1080, h=1350, pg=""):
    p = f'<div class="page">{pg}</div>' if pg else ""
    return f"<html><head><style>:root{{--w:{w}px;--h:{h}px}}{CSS}</style></head><body>{p}{body}</body></html>"
def foot(txt="@ip360.co"):
    return f'<div class="foot"><span>{txt}</span>{LOGO}</div>'
def win(title, inner, extra=""):
    return f'<div class="win" {extra}><div class="bar"><span>{title}</span><span class="btns"><i></i><i></i><i></i></span></div><div class="body">{inner}</div></div>'

P = {}
# I1 presentación (4)
P["I1_1"] = page(f"""<div class="pad"><div class="mono" style="font-size:28px;color:var(--gris2)">IP360 · planeación financiera</div>
<h1 style="font-size:118px;margin-top:150px">Lo que nos dijeron de las finanzas…</h1>
<h1 class="oro" style="font-size:118px;margin-top:30px">pero no entendimos.</h1>
{foot("Desliza →")}</div>""", pg="1/4")
P["I1_2"] = page(f"""<div class="pad" style="justify-content:center">
{win("consejo_financiero.txt", '<p class="mono" style="font-size:44px;line-height:1.5">Nos dijeron:<br><span style="font-size:96px;font-family:SG;font-weight:700">«Ahorra.»</span></p><p style="margin-top:40px;font-size:44px">Nadie nos dijo <span class="oro">para qué.</span></p>')}
</div>""", pg="2/4")
P["I1_3"] = page(f"""<div class="pad"><h1 style="font-size:96px;margin-top:40px">Ahorrar no es planear.</h1>
<p style="margin-top:40px;color:var(--gris2)">Planear es responder tres preguntas:</p>
<div style="margin-top:30px">
<div class="q"><b>01</b>Vivir poco. ¿Quién queda protegido?</div>
<div class="q"><b>02</b>Vivir mucho. ¿De qué vas a vivir?</div>
<div class="q" style="border-bottom:2px solid #333"><b>03</b>Vivir mal. ¿Qué pasa con tus ingresos si enfermas o tienes un accidente?</div></div>
{foot()}</div>""", pg="3/4")
P["I1_4"] = page(f"""<div class="pad"><div style="margin-top:120px">{win("ip360.exe", '<p class="mono prompt" style="font-size:40px">lo_complicado --a simple<span class="cursor"></span></p>')}</div>
<h1 style="font-size:84px;margin-top:80px">De lo complicado a lo simple, para que se pueda <span class="oro">planear.</span></h1>
{foot()}</div>""", pg="4/4")

# I2 pensión (3)
P["I2_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("pension.exe", '<p class="mono" style="font-size:40px;line-height:1.6"><span class="oro">C:\\&gt;</span> abrir plan_pension<br><br>ERROR 404:<br>plan no encontrado.<br><br><span style="color:var(--gris2)">[Reintentar]  [Ignorar 20 años]</span></p>')}</div>
<h1 style="font-size:104px;margin-top:80px">La pensión no se <span class="oro">improvisa.</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I2_2"] = page(f"""<div class="pad"><h1 style="font-size:84px;margin-top:40px">Tres preguntas antes de seguir:</h1>
<div style="margin-top:50px">
<div class="q"><b>01</b>¿En qué régimen pensional estás?</div>
<div class="q"><b>02</b>¿Cuántas semanas llevas cotizadas?</div>
<div class="q" style="border-bottom:2px solid #333"><b>03</b>¿Sobre qué ingreso estás cotizando?</div></div>
{foot()}</div>""", pg="2/3")
P["I2_3"] = page(f"""<div class="pad" style="justify-content:center">
<h1 style="font-size:100px">Si no sabes alguna,</h1>
<h1 style="font-size:100px;margin-top:20px">no estás planeando.</h1>
<h1 class="oro" style="font-size:100px;margin-top:20px">Estás esperando.</h1>
<div style="position:absolute;left:88px;right:88px;bottom:96px">{foot()}</div></div>""", pg="3/3")

# I3 firmar (3)
P["I3_1"] = page(f"""<div class="pad"><h1 style="font-size:150px;margin-top:150px">Si no lo entiendes,</h1>
<h1 class="oro" style="font-size:150px;margin-top:20px">no lo firmes.</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I3_2"] = page(f"""<div class="pad"><div class="mono" style="font-size:30px;color:var(--gris2);margin-top:40px">Antes de firmar un seguro o una inversión</div>
<h1 style="font-size:84px;margin-top:20px">pregunta:</h1>
<div style="margin-top:50px">
<div class="q"><b>01</b>¿Qué cubre y qué no cubre?</div>
<div class="q"><b>02</b>¿Cuánto cuesta en total, no solo al mes?</div>
<div class="q" style="border-bottom:2px solid #333"><b>03</b>¿Qué pasa si quiero salir antes?</div></div>
{foot()}</div>""", pg="2/3")
P["I3_3"] = page(f"""<div class="pad" style="justify-content:center">
{win("duda.txt", '<p style="font-size:62px;line-height:1.2;font-weight:700">Si quien te lo vende no te lo puede explicar simple,</p><p class="oro" style="font-size:62px;line-height:1.2;font-weight:700;margin-top:24px">la duda no es tuya.</p>')}
<div style="position:absolute;left:88px;right:88px;bottom:96px">{foot()}</div></div>""", pg="3/3")

# Historias 1080x1920
def st(inner):
    return page(f'<div class="pad" style="padding:260px 96px 280px;justify-content:center">{inner}</div><div style="position:absolute;left:96px;right:96px;bottom:260px">{foot()}</div>', 1080, 1920)
P["S1"] = st('<h1 style="font-size:120px">Lo que nos dijeron de las finanzas…</h1><h1 class="oro" style="font-size:120px;margin-top:30px">pero no entendimos.</h1>')
P["S2"] = st(win("verdad_incomoda.txt", '<h1 style="font-size:130px">Ahorrar</h1><h1 style="font-size:130px">no es</h1><h1 class="oro" style="font-size:130px">planear.</h1>'))
P["S3"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Los 3 riesgos</div><h1 style="font-size:120px;margin-top:30px">Vivir poco.</h1><h1 style="font-size:120px;margin-top:16px">Vivir mucho.</h1><h1 style="font-size:120px;margin-top:16px">Vivir mal.</h1><p style="margin-top:60px;font-size:44px">Un ahorro sin destino no sabe cuál está cubriendo.</p>')
P["S4"] = st(win("pension.exe", '<p class="mono" style="font-size:44px;line-height:1.6">ERROR 404:<br>plan no encontrado.</p>') + '<h1 style="font-size:110px;margin-top:80px">La pensión no se <span class="oro">improvisa.</span></h1>')
P["S5"] = st('<h1 style="font-size:96px">No se trata de dejar de pagar impuestos.</h1><h1 class="oro" style="font-size:96px;margin-top:50px">Se trata de optimizarlos mientras planeas.</h1>')
P["S6"] = st('<h1 style="font-size:140px">Si no lo entiendes,</h1><h1 class="oro" style="font-size:140px;margin-top:20px">no lo firmes.</h1>')
P["S7"] = st(win("filtro.exe", '<p class="mono" style="font-size:42px;line-height:1.6"><span class="oro">C:\\&gt;</span> ¿Podría decirlo un banco?<br><br>&gt; Sí.<br>&gt; Descartado.</p>') + '<h1 style="font-size:84px;margin-top:80px">Aquí solo decimos lo que un banco <span class="oro">no te diría.</span></h1>')

if __name__ == "__main__":
    only = sys.argv[1:] or list(P)
    OUT = os.environ.get("OUT", f"{D}/out_ip"); os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for k in only:
            w, h = (1080, 1920) if k.startswith("S") else (1080, 1350)
            pg = b.new_page(viewport={"width": w, "height": h})
            path = f"{OUT}/_{k}.html"; open(path, "w").write(P[k])
            pg.goto(f"file://{path}"); pg.wait_for_timeout(300)
            pg.screenshot(path=f"{OUT}/{k}.png"); pg.close()
        b.close()
    print("ok", len(only))
