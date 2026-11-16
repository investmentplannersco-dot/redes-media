"""Semana 8 (19 al 25 de noviembre de 2026): @ip360.co. Copia del kit (page, win, foot, st); solo cambia el contenido."""
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

# I17 · Independientes: prestaciones que nadie te paga · viernes 20
P["I17_1"] = page(f"""<div class="pad"><div class="mono" style="font-size:30px;color:var(--gris2);margin-top:130px">Nos dijimos:</div><h1 style="font-size:108px;margin-top:20px">«Soy independiente: no tengo prima ni cesantías.»</h1>
<h1 class="oro" style="font-size:100px;margin-top:50px">¿Y quién te las paga?</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I17_2"] = qs("Si nadie te las paga, responde:", "¿Separas algo de cada pago para los meses que vienen?",
                "¿Sabes qué pasa con tus ingresos si te enfermas un mes?", "¿Tienes un plan para los meses en que no entra plata?", "2/3")
P["I17_3"] = cierre(win("independiente.txt", '<p style="font-size:64px;line-height:1.2;font-weight:700">Sin empleador,</p><p class="oro" style="font-size:64px;line-height:1.2;font-weight:700;margin-top:24px">el plan también es tuyo.</p>'), "3/3")

# I18 · Optimización fiscal: el año gravable se cierra en diciembre · lunes 23 (tema ajustado)
P["I18_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("renta_2026.exe", '<p class="mono" style="font-size:40px;line-height:1.6"><span class="oro">C:\\&gt;</span> renta --año 2026<br><br>Se declara: en 2027.<br>Se decide: en 2026.</p>')}</div>
<h1 style="font-size:100px;margin-top:80px">La renta de 2026 se declara en 2027. <span class="oro">Se planea antes del 31 de diciembre.</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I18_2"] = qs("Antes de que cierre el año, responde:", "¿Sabes si vas a tener que declarar renta por 2026?",
                "¿Guardas los soportes de lo que la ley te deja descontar?", "¿Lo revisas en diciembre o cuando ya toca declarar?", "2/3")
P["I18_3"] = cierre('<h1 style="font-size:96px">La declaración es en 2027.</h1><h1 class="oro" style="font-size:96px;margin-top:40px">Las decisiones son en 2026.</h1>', "3/3")

# I19 · Método: escenarios · miércoles 25
P["I19_1"] = page(f"""<div class="pad"><div class="mono" style="font-size:30px;color:var(--gris2);margin-top:130px">Nos dijimos:</div><h1 style="font-size:118px;margin-top:20px">«Eso no me va a pasar.»</h1>
<h1 class="oro" style="font-size:96px;margin-top:50px">Nadie nos dijo qué hacer si pasa.</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I19_2"] = qs("Responde:", "¿Qué pasa con tus gastos si tus ingresos bajan tres meses?",
                "¿Quién depende de lo que ganas?", "¿Tu plan tiene un escenario para lo que no esperas?", "2/3")
P["I19_3"] = cierre(win("plan.txt", '<p style="font-size:70px;line-height:1.2;font-weight:700">Un plan sin escenarios</p><p class="oro" style="font-size:70px;line-height:1.2;font-weight:700;margin-top:24px">es un deseo.</p>'), "3/3")

# Historias 1080x1920
def st(inner):
    return page(f'<div class="pad" style="padding:260px 96px 280px;justify-content:center">{inner}</div><div style="position:absolute;left:96px;right:96px;bottom:260px">{foot()}</div>', 1080, 1920)
P["S38"] = st('<h1 style="font-size:110px">¿Sabes cuánto te cuesta un mes?</h1><h1 class="oro" style="font-size:96px;margin-top:60px">No cuánto ganas. Cuánto gastas.</h1>')
P["S39"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Independientes</div><h1 style="font-size:108px;margin-top:30px">Nadie te paga la prima.</h1><h1 class="oro" style="font-size:100px;margin-top:60px">¿Quién la planea?</h1>')
P["S40"] = st(win("contrato.pdf", '<p style="font-size:78px;line-height:1.15;font-weight:700">Si no lo entiendes,</p><p class="oro" style="font-size:78px;line-height:1.15;font-weight:700;margin-top:30px">no lo firmes.</p>'))
P["S41"] = st('<h1 style="font-size:112px">Enero se paga con lo que dejes en diciembre.</h1><h1 class="oro" style="font-size:100px;margin-top:60px">¿Ya sabes cuánto?</h1>')
P["S42"] = st(win("renta_2026.exe", '<p class="mono" style="font-size:44px;line-height:1.6"><span class="oro">C:\\&gt;</span> renta --año 2026<br><br>Se declara: en 2027.<br>Se decide: en 2026.<span class="cursor"></span></p>') + '<h1 style="font-size:96px;margin-top:80px">El año gravable <span class="oro">cierra el 31 de diciembre.</span></h1>')
P["S43"] = st('<h1 style="font-size:130px">La pensión</h1><h1 class="oro" style="font-size:130px;margin-top:20px">no se improvisa.</h1><p style="margin-top:70px;font-size:50px">Por eso, esto lo planeo con IP360.</p>')
P["S44"] = st(win("plan.txt", '<p style="font-size:74px;line-height:1.15;font-weight:700">Un plan sin escenarios</p><p class="oro" style="font-size:74px;line-height:1.15;font-weight:700;margin-top:30px">es un deseo.</p>'))

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
