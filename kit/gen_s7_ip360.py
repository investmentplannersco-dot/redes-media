"""Semana 7 (12 al 18 de noviembre de 2026): @ip360.co. Copia del kit (page, win, foot, st); solo cambia el contenido."""
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

# I14 · Vivir mal: la EPS · viernes 13
P["I14_1"] = page(f"""<div class="pad"><div class="mono" style="font-size:30px;color:var(--gris2);margin-top:130px">Nos dijimos:</div><h1 style="font-size:118px;margin-top:20px">«Para eso tengo EPS.»</h1>
<h1 class="oro" style="font-size:100px;margin-top:50px">¿Y lo que no cubre?</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I14_2"] = qs("Vivir mal también se planea:", "¿Sabes qué cubre tu EPS y qué no?",
                "¿Sabes qué pasa con tus ingresos si te incapacitan?", "¿Quién paga lo que no está cubierto?", "2/3")
P["I14_3"] = cierre(win("salud.txt", '<p style="font-size:70px;line-height:1.2;font-weight:700">Tener EPS</p><p class="oro" style="font-size:70px;line-height:1.2;font-weight:700;margin-top:24px">no es tener un plan.</p>'), "3/3")

# I15 · La prima de diciembre · lunes 16
P["I15_1"] = page(f"""<div class="pad"><div class="mono" style="font-size:30px;color:var(--gris2);margin-top:120px">Nos dijeron:</div><h1 style="font-size:112px;margin-top:20px">«La prima es plata extra.»</h1>
<h1 class="oro" style="font-size:84px;margin-top:50px">Nadie nos dijo que diciembre ya la tiene repartida.</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I15_2"] = qs("Antes de que llegue, responde:", "¿Ya sabes en qué se va a ir?",
                "¿Lo decides tú o lo deciden las ofertas de diciembre?", "¿Alguna parte va a algo que siga importando el próximo año?", "2/3")
P["I15_3"] = cierre('<h1 style="font-size:100px">Plata sin destino no es plata extra.</h1><h1 class="oro" style="font-size:100px;margin-top:40px">Es plata ya gastada.</h1>', "3/3")

# I16 · Las cesantías · miércoles 18 (18:00, hora ajustada)
P["I16_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("cesantias.exe", '<p class="mono" style="font-size:40px;line-height:1.6"><span class="oro">C:\\&gt;</span> cesantias --para_que<br><br>Resultado:<br>«por si acaso».</p>')}</div>
<h1 style="font-size:104px;margin-top:80px">«Las cesantías son un ahorro.» <span class="oro">¿Para qué?</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I16_2"] = qs("Responde:", "¿Sabes cuánto tienes hoy en cesantías?",
                "¿Sabes en qué fondo están?", "¿Tienen un para qué o esperan a la próxima urgencia?", "2/3")
P["I16_3"] = cierre('<h1 style="font-size:100px">Un ahorro sin para qué no es un plan.</h1><h1 class="oro" style="font-size:100px;margin-top:40px">Es un colchón.</h1>', "3/3")

# Historias 1080x1920
def st(inner):
    return page(f'<div class="pad" style="padding:260px 96px 280px;justify-content:center">{inner}</div><div style="position:absolute;left:96px;right:96px;bottom:260px">{foot()}</div>', 1080, 1920)
P["S31"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Nos dijeron:</div><h1 style="font-size:112px;margin-top:20px">«Tranquilo, la cuota es baja.»</h1><h1 class="oro" style="font-size:90px;margin-top:70px">Nadie nos dijo por cuántos meses.</h1>')
P["S32"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Vivir mal</div><h1 style="font-size:116px;margin-top:30px">«Para eso tengo EPS.»</h1><h1 class="oro" style="font-size:100px;margin-top:70px">¿Y lo que no cubre?</h1>')
P["S33"] = st(win("plan.txt", '<p style="font-size:74px;line-height:1.15;font-weight:700">Un plan no es un producto.</p><p class="oro" style="font-size:74px;line-height:1.15;font-weight:700;margin-top:30px">Es una decisión con escenarios.</p>'))
P["S34"] = st('<h1 style="font-size:116px">Diciembre llega todos los años.</h1><h1 class="oro" style="font-size:110px;margin-top:60px">¿Por qué nos sigue sorprendiendo?</h1>')
P["S35"] = st(win("prima.exe", '<p class="mono" style="font-size:44px;line-height:1.6"><span class="oro">C:\\&gt;</span> prima --destino<br><br>Resultado:<br>no definido.<span class="cursor"></span></p>') + '<h1 style="font-size:100px;margin-top:80px">La prima no es plata extra. <span class="oro">Es plata con destino.</span></h1>')
P["S36"] = st('<h1 style="font-size:112px">Que te lo expliquen bien</h1><h1 class="oro" style="font-size:112px;margin-top:40px">no es haberlo comparado.</h1><p style="margin-top:70px;font-size:50px">Por eso, esto lo planeo con IP360.</p>')
P["S37"] = st(win("cesantias.exe", '<p class="mono" style="font-size:44px;line-height:1.6"><span class="oro">C:\\&gt;</span> cesantias --para_que<br><br>Resultado:<br>«por si acaso».<span class="cursor"></span></p>') + '<h1 style="font-size:96px;margin-top:80px">Un ahorro sin para qué <span class="oro">es un colchón.</span></h1>')

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
