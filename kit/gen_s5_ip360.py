"""Semana 5 (29 de octubre al 4 de noviembre de 2026): @ip360.co. Copia del kit (page, win, foot, st); solo cambia el contenido."""
import os, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_ip360 import page, win, foot

P = {}
def qs(titulo, q1, q2, q3, pg, intro=""):
    i = f'<div class="mono" style="font-size:30px;color:var(--gris2);margin-top:40px">{intro}</div>' if intro else ""
    return page(f"""<div class="pad">{i}<h1 style="font-size:84px;margin-top:{20 if intro else 40}px">{titulo}</h1>
<div style="margin-top:50px">
<div class="q"><b>01</b>{q1}</div>
<div class="q"><b>02</b>{q2}</div>
<div class="q" style="border-bottom:2px solid #333"><b>03</b>{q3}</div></div>
{foot("Responde con el número →")}</div>""", pg=pg)
def cierre(inner, pg):
    return page(f"""<div class="pad" style="justify-content:center">{inner}
<div style="position:absolute;left:88px;right:88px;bottom:96px">{foot()}</div></div>""", pg=pg)

# I9 · Pensión (ajuste de tema) · viernes 30
P["I9_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("pension.exe", '<p class="mono" style="font-size:40px;line-height:1.6"><span class="oro">C:\\&gt;</span> consultar pension_estimada<br><br>Último acceso: nunca.<br><br><span style="color:var(--gris2)">[Consultar]  [Más tarde]</span></p>')}</div>
<h1 style="font-size:100px;margin-top:80px">La pensión <span class="oro">no se improvisa.</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I9_2"] = qs("Tres preguntas para hacerte a tiempo:", "¿Sabes cuánto recibirías al mes si te pensionaras con lo que llevas hoy?",
               "¿Le has preguntado a tu fondo o a Colpensiones cómo va tu pensión?", "¿Cuánto hay entre ese número y lo que gastas hoy?", "2/3")
P["I9_3"] = cierre('<h1 style="font-size:88px">La diferencia entre lo que recibirías y lo que gastas</h1><h1 class="oro" style="font-size:88px;margin-top:40px">es la parte que te toca planear.</h1>', "3/3")

# I6 · Optimización fiscal
P["I6_1"] = page(f"""<div class="pad"><h1 style="font-size:130px;margin-top:150px">Pagar impuestos no se negocia.</h1>
<h1 class="oro" style="font-size:130px;margin-top:30px">Planearlos, sí.</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I6_2"] = qs("Empieza con tres preguntas:", "¿Sabes qué deducciones y rentas exentas te aplica la ley?",
               "¿Las revisas durante el año o solo cuando toca declarar?", "¿Alguien te lo ha explicado simple?", "2/3")
P["I6_3"] = cierre(win("optimizar.txt", '<p style="font-size:66px;line-height:1.2;font-weight:700">Optimizar no es evadir.</p><p class="oro" style="font-size:66px;line-height:1.2;font-weight:700;margin-top:24px">Es planear dentro de la ley.</p>'), "3/3")

# I10 · Revisar el plan · miércoles 4
P["I10_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("plan.exe", '<p class="mono" style="font-size:40px;line-height:1.6"><span class="oro">C:\\&gt;</span> plan --version<br><br>Última revisión: hace años.<br>Cambios en tu vida: varios.</p>')}</div>
<h1 style="font-size:100px;margin-top:80px">Un plan no se hace <span class="oro">una sola vez.</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I10_2"] = qs("Revisa si tu plan sabe lo que cambió:", "¿Cuándo revisaste tu plan por última vez?",
               "¿Qué cambió desde entonces: ingresos, deudas, personas que dependen de ti?", "¿Tu plan tiene en cuenta esos cambios?", "2/3")
P["I10_3"] = cierre('<h1 style="font-size:100px">Un plan que<br>no se revisa</h1><h1 class="oro" style="font-size:100px;margin-top:40px">es una foto vieja.</h1>', "3/3")

# Historias 1080x1920
def st(inner):
    return page(f'<div class="pad" style="padding:260px 96px 280px;justify-content:center">{inner}</div><div style="position:absolute;left:96px;right:96px;bottom:260px">{foot()}</div>', 1080, 1920)
P["S18"] = st(win("claim.txt", '<p style="font-size:80px;line-height:1.15;font-weight:700">Lo que nos dijeron de las finanzas…</p><p class="oro" style="font-size:80px;line-height:1.15;font-weight:700;margin-top:30px">pero no entendimos.</p>'))
P["S19"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Vivir mucho</div><h1 style="font-size:116px;margin-top:30px">¿Sabes cuánto recibirías de pensión?</h1><p style="margin-top:60px;font-size:46px">La pensión no se improvisa. Se consulta, se compara y se <span class="oro">planea.</span></p>')
P["S20"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Nos dijeron:</div><h1 style="font-size:116px;margin-top:20px">«Invierte en tu futuro.»</h1><p style="margin-top:60px;font-size:50px">Nadie nos dijo en cuál futuro, cuánto, ni para qué riesgo.</p><h1 class="oro" style="font-size:72px;margin-top:70px">Por eso, esto lo planeo con IP360.</h1>')
P["S21"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Nos dijeron:</div><h1 style="font-size:104px;margin-top:20px">«Planear es para gente con plata.»</h1><h1 class="oro" style="font-size:84px;margin-top:70px">Planear empieza con preguntas, no con plata.</h1>')
P["S13"] = st(win("impuestos.exe", '<p class="mono" style="font-size:44px;line-height:1.6"><span class="oro">C:\\&gt;</span> revisar_impuestos<br>--durante_el_año<span class="cursor"></span></p>') + '<h1 style="font-size:110px;margin-top:80px">Optimizar no es <span class="oro">evadir.</span></h1>')
P["S22"] = st(win("plan.exe", '<p class="mono" style="font-size:44px;line-height:1.6"><span class="oro">C:\\&gt;</span> plan --revisar<br><br>Última revisión:<br>no encontrada.<span class="cursor"></span></p>') + '<h1 style="font-size:100px;margin-top:80px">¿Tu plan sabe que <span class="oro">tu vida cambió?</span></h1>')
P["S23"] = st(win("contrato.pdf", '<p class="mono" style="font-size:40px;line-height:1.6">Términos y condiciones<br><span style="color:var(--gris2)">letra pequeña · letra pequeña<br>letra pequeña · letra pequeña</span></p>') + '<h1 style="font-size:110px;margin-top:80px">Si no lo entiendes, <span class="oro">no lo firmes.</span></h1>')

if __name__ == "__main__":
    only = sys.argv[1:] or list(P)
    OUT = os.environ["OUT"]; os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for k in only:
            w, h = (1080, 1920) if k.startswith("S") else (1080, 1350)
            pg = b.new_page(viewport={"width": w, "height": h})
            path = f"{OUT}/_{k}.html"; open(path, "w").write(P[k])
            pg.goto(f"file://{path}"); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{OUT}/{k}.png"); pg.close()
        b.close()
    print("ok", len(only))
