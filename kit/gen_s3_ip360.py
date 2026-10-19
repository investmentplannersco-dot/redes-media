"""Semana 3 (19 al 28 de octubre de 2026): @ip360.co. Copia del kit (page, win, foot, st); solo cambia el contenido."""
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

# I4 · Vivir poco
P["I4_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("vivir_poco.exe", '<p class="mono" style="font-size:40px;line-height:1.6"><span class="oro">C:\\&gt;</span> buscar quien_paga<br><br>Respuesta no encontrada.<br><br><span style="color:var(--gris2)">[Reintentar]  [Después]</span></p>')}</div>
<h1 style="font-size:100px;margin-top:80px">Si mañana no estás, <span class="oro">¿quién paga?</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I4_2"] = qs("La primera pregunta del riesgo de vivir poco:", "¿Quién depende hoy de tus ingresos?",
               "¿Por cuántos años necesitaría ese apoyo?", "¿Qué deudas o gastos quedarían pendientes?", "2/3")
P["I4_3"] = cierre('<h1 style="font-size:100px">Proteger no es tener miedo.</h1><h1 class="oro" style="font-size:100px;margin-top:30px">Es saber cuánto necesitarían.</h1>', "3/3")

# I5 · Vivir mal
P["I5_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("ingresos.exe", '<p class="mono" style="font-size:40px;line-height:1.6">ERROR:<br>titular no disponible<br>para trabajar.<br><br><span style="color:var(--gris2)">[Aceptar]  [¿Y ahora qué?]</span></p>')}</div>
<h1 style="font-size:100px;margin-top:80px">¿Y si un día <span class="oro">no puedes trabajar?</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I5_2"] = qs("Antes de que pase, responde:", "¿Cuántos meses podrías cubrir tus gastos sin tu ingreso?",
               "¿Sabes qué parte de tu ingreso cubre la EPS si te incapacitan?", "¿Qué pasa con tus gastos fijos mientras te recuperas?", "2/3")
P["I5_3"] = cierre('<h1 style="font-size:96px">Tu ingreso depende de algo que casi nunca planeamos:</h1><h1 class="oro" style="font-size:120px;margin-top:40px">poder trabajar.</h1>', "3/3")

# I6 · Optimización fiscal
P["I6_1"] = page(f"""<div class="pad"><h1 style="font-size:130px;margin-top:150px">Pagar impuestos no se negocia.</h1>
<h1 class="oro" style="font-size:130px;margin-top:30px">Planearlos, sí.</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I6_2"] = qs("Empieza con tres preguntas:", "¿Sabes qué deducciones y rentas exentas te aplica la ley?",
               "¿Las revisas durante el año o solo cuando toca declarar?", "¿Alguien te lo ha explicado simple?", "2/3")
P["I6_3"] = cierre(win("optimizar.txt", '<p style="font-size:66px;line-height:1.2;font-weight:700">Optimizar no es evadir.</p><p class="oro" style="font-size:66px;line-height:1.2;font-weight:700;margin-top:24px">Es planear dentro de la ley.</p>'), "3/3")

# I7 · Vivir mucho
P["I7_1"] = page(f"""<div class="pad"><div style="margin-top:110px">{win("retiro.exe", '<p class="mono" style="font-size:40px;line-height:1.6"><span class="oro">C:\\&gt;</span> calcular gasto_mensual<br>--despues_de_trabajar<br><br>Dato no disponible.</p>')}</div>
<h1 style="font-size:100px;margin-top:80px">Vivir mucho también <span class="oro">es un riesgo.</span></h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I7_2"] = qs("Tres preguntas para empezar:", "¿Cuánto gastas hoy en un mes normal?",
               "¿Cuánto de ese gasto seguirá cuando dejes de trabajar?", "¿De dónde va a salir ese dinero?", "2/3")
P["I7_3"] = cierre('<h1 style="font-size:96px">Vivir mucho no es el problema.</h1><h1 class="oro" style="font-size:96px;margin-top:40px">Llegar sin saber de qué vas a vivir, sí.</h1>', "3/3")

# I8 · Método
P["I8_1"] = page(f"""<div class="pad"><h1 style="font-size:150px;margin-top:150px">Planear no es</h1>
<h1 class="oro" style="font-size:150px;margin-top:20px">adivinar.</h1>
{foot("Desliza →")}</div>""", pg="1/3")
P["I8_2"] = page(f"""<div class="pad" style="justify-content:center">{win("metodo.exe", '<p class="mono" style="font-size:44px;line-height:1.7"><span class="oro">1.</span> Entender qué tienes<br>&nbsp;&nbsp;&nbsp;y qué riesgo cubre.<br><span class="oro">2.</span> Comparar escenarios.<br><span class="oro">3.</span> Decidir.</p>')}
<p style="margin-top:60px;font-size:44px">En ese orden. Saltarse el 1 o el 2 es adivinar con más pasos.</p>
<div style="position:absolute;left:88px;right:88px;bottom:96px">{foot()}</div></div>""", pg="2/3")
P["I8_3"] = cierre('<h1 style="font-size:92px">Si alguien decide por ti sin mostrarte escenarios,</h1><h1 class="oro" style="font-size:92px;margin-top:40px">no estás planeando. Estás obedeciendo.</h1>', "3/3")

# Historias 1080x1920
def st(inner):
    return page(f'<div class="pad" style="padding:260px 96px 280px;justify-content:center">{inner}</div><div style="position:absolute;left:96px;right:96px;bottom:260px">{foot()}</div>', 1080, 1920)
P["S8"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Vivir poco</div><h1 style="font-size:120px;margin-top:30px">¿Quién depende de tus ingresos?</h1><p style="margin-top:60px;font-size:46px">Si la respuesta es «alguien», ya tienes una razón para <span class="oro">planear.</span></p>')
P["S9"] = st(win("promesa.txt", '<p style="font-size:76px;line-height:1.15;font-weight:700">De lo complicado a lo simple en las finanzas,</p><p class="oro" style="font-size:76px;line-height:1.15;font-weight:700;margin-top:30px">para que se puedan planear.</p>'))
P["S10"] = st('<h1 style="font-size:116px">¿Cuántos meses aguantarías sin ingresos?</h1><p style="margin-top:60px;font-size:46px">Si no lo sabes, ese es el dato que le falta a tu <span class="oro">plan.</span></p>')
P["S14"] = st('<h1 style="font-size:104px">¿Puedes explicar tu plan financiero en tres frases?</h1><h1 class="oro" style="font-size:84px;margin-top:70px">Si no, todavía no es un plan. Es una idea.</h1>')
P["S13"] = st(win("impuestos.exe", '<p class="mono" style="font-size:44px;line-height:1.6"><span class="oro">C:\\&gt;</span> revisar_impuestos<br>--durante_el_año<span class="cursor"></span></p>') + '<h1 style="font-size:110px;margin-top:80px">Optimizar no es <span class="oro">evadir.</span></h1>')
P["S11"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Nos dijeron:</div><h1 style="font-size:130px;margin-top:20px">«Trabaja duro.»</h1><p style="margin-top:60px;font-size:50px">Nadie nos dijo qué pasa si un día no puedes trabajar.</p><h1 class="oro" style="font-size:72px;margin-top:70px">Por eso, esto lo planeo con IP360.</h1>')
P["S16"] = st('<h1 style="font-size:124px">Una sola opción no es una decisión.</h1><h1 class="oro" style="font-size:124px;margin-top:40px">Es una instrucción.</h1>')
P["S15"] = st('<div class="mono" style="font-size:34px;color:var(--gris2)">Vivir mucho</div><h1 style="font-size:116px;margin-top:30px">¿Sabes cuánto necesitas al mes para vivir?</h1><p style="margin-top:60px;font-size:46px">Sin ese número, la pensión es una <span class="oro">esperanza</span>, no un plan.</p>')
P["S17"] = st(win("checklist.exe", '<p class="mono" style="font-size:42px;line-height:1.8">[ ] Sé quién depende de mí.<br>[ ] Sé cuántos meses aguanto<br>&nbsp;&nbsp;&nbsp;&nbsp;sin ingresos.<br>[ ] Sé cuánto necesito<br>&nbsp;&nbsp;&nbsp;&nbsp;al mes para vivir.</p>') + '<h1 style="font-size:96px;margin-top:80px">¿Cuántas <span class="oro">marcaste?</span></h1>')
P["S12"] = st(win("metodo.exe", '<p class="mono" style="font-size:46px;line-height:1.7">planear =<br><span class="oro">1.</span> Entender<br><span class="oro">2.</span> Comparar escenarios<br><span class="oro">3.</span> Decidir</p>') + '<h1 style="font-size:110px;margin-top:80px">Planear no es <span class="oro">adivinar.</span></h1>')

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
