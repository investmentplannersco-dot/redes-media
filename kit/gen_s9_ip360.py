"""Semana 9 (26 de noviembre al 2 de diciembre de 2026): @ip360.co. Copia del kit (page, win, foot, st); solo cambia el contenido."""
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

# I20 · Optimización fiscal: el contador · viernes 27 (tema ajustado)
P["I20_1"] = page(f"""<div class="pad"><div class="mono" style="font-size:30px;color:var(--gris2);margin-top:130px">Nos dijimos:</div><h1 style="font-size:118px;margin-top:20px">«Eso lo ve el contador.»</h1>
<h1 class="oro" style="font-size:100px;margin-top:50px">¿Y quién lo planea?</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I20_2"] = qs("Responde:", "¿Hablas con tu contador antes de que cierre el año o después?",
                "¿Le llevas preguntas o le llevas una caja de papeles?", "¿Sabes qué decisiones de este año cambian lo que vas a declarar?", "2/3")
CONTADOR = '<p style="font-size:64px;line-height:1.2;font-weight:700">El contador declara lo que pasó.</p><p class="oro" style="font-size:64px;line-height:1.2;font-weight:700;margin-top:24px">Planear es decidir lo que va a pasar.</p>'
P["I20_3"] = cierre(win("contador.txt", CONTADOR), "3/3")

# I21 · Vivir mucho: la pensión · lunes 30
P["I21_1"] = page(f"""<div class="pad"><div class="mono" style="font-size:30px;color:var(--gris2);margin-top:130px">Nos dijimos:</div><h1 style="font-size:112px;margin-top:20px">«Ya veré con cuánto me pensiono.»</h1>
<h1 class="oro" style="font-size:100px;margin-top:50px">¿Y si lo ves antes?</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I21_2"] = qs("Responde:", "¿Sabes dónde estás cotizando para tu pensión?",
                "¿Sabes cuántas semanas llevas cotizadas?", "¿Has visto alguna vez una proyección de tu pensión?", "2/3")
PENSION = '<p class="mono" style="font-size:42px;line-height:1.6"><span class="oro">C:\\&gt;</span> pension --proyeccion<br><br>Resultado: no encontrado.<span class="cursor"></span></p>'
P["I21_3"] = cierre(win("pension.exe", PENSION) + '<h1 style="font-size:96px;margin-top:70px">La pensión <span class="oro">no se improvisa.</span></h1>', "3/3")

# I22 · Optimización fiscal: los soportes · miércoles 2 de diciembre (tema ajustado)
P["I22_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("soportes_2026", '<p class="mono" style="font-size:40px;line-height:1.6"><span class="oro">C:\\&gt;</span> dir soportes_2026<br><br>0 archivos encontrados.</p>')}</div>
<h1 style="font-size:104px;margin-top:80px">¿Dónde están los soportes <span class="oro">de tu 2026?</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I22_2"] = qs("Responde:", "¿Pides la factura a tu nombre cuando pagas algo que podrías soportar?",
                "¿Sabes cuáles de tus gastos te sirven y cuáles no?", "¿Los tienes en un solo lugar o regados en el correo?", "2/3")
P["I22_3"] = cierre('<h1 style="font-size:92px">Los soportes se guardan durante el año.</h1><h1 class="oro" style="font-size:92px;margin-top:40px">No cuando toca declarar.</h1>', "3/3")

# Historias 1080x1920
def st(inner):
    return page(f'<div class="pad" style="padding:260px 96px 280px;justify-content:center">{inner}</div><div style="position:absolute;left:96px;right:96px;bottom:260px">{foot()}</div>', 1080, 1920)
P["S45"] = st('<h1 style="font-size:150px">Ahorrar</h1><h1 class="oro" style="font-size:150px;margin-top:20px">no es planear.</h1>')
P["S46"] = st(win("contador.txt", CONTADOR))
P["S47"] = st('<h1 style="font-size:104px">Vivir poco.<br>Vivir mucho.<br>Vivir mal.</h1><h1 class="oro" style="font-size:100px;margin-top:70px">¿Para cuál tienes plan?</h1>')
P["S48"] = st('<h1 style="font-size:104px">Lo que nos dijeron de las finanzas…</h1><h1 class="oro" style="font-size:104px;margin-top:40px">pero no entendimos.</h1><p style="margin-top:70px;font-size:54px">¿Qué te dijeron a ti?</p>')
P["S49"] = st(win("pension.exe", PENSION) + '<h1 style="font-size:96px;margin-top:80px">¿Alguna vez <span class="oro">has visto la tuya?</span></h1>')
P["S50"] = st('<h1 style="font-size:120px">Empezó diciembre.</h1><h1 class="oro" style="font-size:100px;margin-top:60px">El año gravable 2026 cierra el 31.</h1>')
P["S51"] = st('<h1 style="font-size:108px">Los soportes se guardan durante el año.</h1><h1 class="oro" style="font-size:108px;margin-top:50px">No cuando toca declarar.</h1>')

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
