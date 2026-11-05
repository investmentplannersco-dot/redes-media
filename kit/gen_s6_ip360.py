"""Semana 6 (5 al 11 de noviembre de 2026): @ip360.co. Copia del kit (page, win, foot, st); solo cambia el contenido."""
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

# I11 · Retención en la fuente (ajuste de tema) · viernes 6
P["I11_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("retencion.exe", '<p class="mono" style="font-size:40px;line-height:1.6"><span class="oro">C:\\&gt;</span> consultar retencion_anual<br><br>Resultado:<br>«ya me lo descuentan».</p>')}</div>
<h1 style="font-size:100px;margin-top:80px">Que te lo descuenten <span class="oro">no es planearlo.</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I11_2"] = qs("Si te hacen retención, responde:", "¿Sabes cuánto te retuvieron el año pasado?",
                "¿Sabes cómo se cruza ese valor con tu declaración de renta?", "¿Lo revisas durante el año o cuando ya toca declarar?", "2/3")
P["I11_3"] = cierre(win("retencion.txt", '<p style="font-size:66px;line-height:1.2;font-weight:700">La retención no es tu impuesto.</p><p class="oro" style="font-size:66px;line-height:1.2;font-weight:700;margin-top:24px">Es un abono. La cuenta completa te toca a ti.</p>'), "3/3")

# I12 · Vivir poco: el seguro del trabajo · lunes 9
P["I12_1"] = page(f"""<div class="pad"><div class="mono" style="font-size:30px;color:var(--gris2);margin-top:130px">Nos dijimos:</div><h1 style="font-size:118px;margin-top:20px">«Tengo seguro por la empresa.»</h1>
<h1 class="oro" style="font-size:96px;margin-top:50px">¿Y si mañana no estás en la empresa?</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I12_2"] = qs("Tres preguntas sobre ese seguro:", "¿Sabes qué cubre y por cuánto?",
                "¿Qué pasa con ese seguro si cambias de trabajo?", "¿Alcanza para quienes dependen de ti?", "2/3")
P["I12_3"] = cierre('<h1 style="font-size:100px">Un seguro que no conoces</h1><h1 class="oro" style="font-size:100px;margin-top:40px">no es un plan. Es una suposición.</h1>', "3/3")

# I13 · Crédito preaprobado · miércoles 11
P["I13_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("felicidades.exe", '<p class="mono" style="font-size:40px;line-height:1.6">¡Felicidades!<br>Tienes un crédito preaprobado.<br><br><span style="color:var(--gris2)">[Aceptar]  [Aceptar]</span></p>')}</div>
<h1 style="font-size:112px;margin-top:80px">Preaprobado <span class="oro">no es planeado.</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I13_2"] = qs("Antes de aceptar, responde:", "¿Para qué lo necesitas?",
                "¿Cuánto pagas en total, no solo en la cuota?", "¿Qué dejas de hacer con esa cuota?", "2/3")
P["I13_3"] = cierre('<h1 style="font-size:100px">El banco ya hizo sus cuentas.</h1><h1 class="oro" style="font-size:100px;margin-top:40px">¿Tú hiciste las tuyas?</h1>', "3/3")

# Historias 1080x1920
def st(inner):
    return page(f'<div class="pad" style="padding:260px 96px 280px;justify-content:center">{inner}</div><div style="position:absolute;left:96px;right:96px;bottom:260px">{foot()}</div>', 1080, 1920)
P["S24"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Nos dijeron:</div><h1 style="font-size:116px;margin-top:20px">«El carro es una inversión.»</h1><p style="margin-top:60px;font-size:50px">Nadie nos dijo cuánto cuesta tenerlo.</p><h1 class="oro" style="font-size:72px;margin-top:70px">Por eso, esto lo planeo con IP360.</h1>')
P["S25"] = st(win("retencion.exe", '<p class="mono" style="font-size:44px;line-height:1.6"><span class="oro">C:\\&gt;</span> retencion --año_pasado<br><br>Resultado:<br>no lo sé.<span class="cursor"></span></p>') + '<h1 style="font-size:100px;margin-top:80px">¿Sabes cuánto <span class="oro">te retuvieron?</span></h1>')
P["S26"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Vivir poco</div><h1 style="font-size:116px;margin-top:30px">¿Cuándo leíste tu póliza por última vez?</h1><p style="margin-top:60px;font-size:46px">Si no sabes qué cubre, no sabes qué <span class="oro">tienes.</span></p>')
P["S27"] = st(win("ahorro.txt", '<p style="font-size:80px;line-height:1.15;font-weight:700">Ahorrar</p><p class="oro" style="font-size:80px;line-height:1.15;font-weight:700;margin-top:30px">no es planear.</p>'))
P["S28"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Nos dijimos:</div><h1 style="font-size:116px;margin-top:20px">«Tengo seguro por la empresa.»</h1><h1 class="oro" style="font-size:96px;margin-top:70px">¿Y si cambias de empresa?</h1>')
P["S29"] = st('<h1 style="font-size:112px">Si mañana no estás, ¿alguien sabe dónde están tus papeles?</h1><p style="margin-top:60px;font-size:50px">Planear también es <span class="oro">eso.</span></p>')
P["S30"] = st(win("felicidades.exe", '<p class="mono" style="font-size:44px;line-height:1.6">¡Felicidades!<br>Crédito preaprobado.<br><br><span style="color:var(--gris2)">[Aceptar]  [Aceptar]</span></p>') + '<h1 style="font-size:110px;margin-top:80px">Preaprobado <span class="oro">no es planeado.</span></h1>')

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
