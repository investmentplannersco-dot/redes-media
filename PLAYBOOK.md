# Playbook semanal de redes — Joaquín Piña · Contraining · IP360

Este repositorio guarda las imágenes que se programan en Metricool y el kit para producirlas.
Lo usa la tarea programada de cada lunes. Idioma de trabajo: español.

## Reglas que no se negocian

- Exactitud estricta: no inventar datos, cifras, testimonios ni anécdotas de Joaquín. Si algo no se puede verificar, escribir "No puedo confirmar esto" y no publicarlo.
- Toda cifra en un texto debe venir de los datos confirmados (abajo) o de una fuente verificable citada.
- Sin emojis. Sin degradados en los diseños (el logo de Contraining se respeta tal cual).
- Nada se programa en Metricool sin la aprobación explícita de Joaquín en la conversación.
- No usar, nombrar ni describir propuestas a clientes (por ejemplo, la metodología de la propuesta a Altadis). Los servicios se describen en términos generales.

## Cuentas en Metricool (zona horaria America/Bogota)

| Marca Metricool | blogId | Cuenta | Frecuencia y horario |
| --- | --- | --- | --- |
| Visita Medica - Contraining Farma | 7261921 | LinkedIn personal de Joaquín | 3 por semana: martes, miércoles y jueves 11:00 |
| Visita Medica - Contraining Farma | 7261921 | Instagram @contrainingfarma | Publicación martes y jueves 18:00; historia diaria 12:00 |
| IP360 | 7314879 | Instagram @ip360.co | Carrusel lunes, miércoles y viernes 19:00; historia diaria 12:00 |

Los horarios se ajustan según el análisis del lunes (un solo cambio por marca por semana).

## Ventana de cada lunes

Cada lunes se prepara contenido desde el primer día sin contenido programado de cada cuenta hasta el miércoles de la semana siguiente. Consultar primero `getScheduledPosts` de cada marca para no duplicar.

## Datos confirmados por Joaquín

**Contraining**
- Más de 27 años formando visitadores médicos en Colombia (brandbook). 158 promociones. Más de 3.000 egresados. Más de 30 fuerzas de ventas administradas.
- Diplomado en Visita Médica: inicio 18 de febrero de 2027; 120 horas en 3 meses; clases virtuales en vivo, lunes a viernes de 7:00 a 9:00 p. m.; docentes con experiencia en la industria farmacéutica; teoría farmacéutica, entrenamiento comercial y acompañamiento para la inserción laboral.
- Precio: $2.753.000 hasta el 30 de noviembre de 2026; $3.110.000 desde el 1 de diciembre de 2026. 12 % de descuento para referidos de egresados y por pronto pago (usar exactamente esa frase).
- Servicios para laboratorios: outsourcing de fuerzas de ventas, seguimiento de la fuerza de ventas, reclutamiento de visitadores médicos, entrenamiento a la medida, coordinación de programas de formación, planes de marketing, enlace entre profesionales comerciales de alto nivel y compañías farmacéuticas.
- Contacto: WhatsApp 301 727 6517 · contraining.co
- En 2027 lanza un diplomado para gerentes de distrito y de producto (sin fecha ni detalles confirmados: no publicar detalles).

**Joaquín (marca personal)**
- Coach ontológico certificado ICF. Unos 8 años en formación para la industria farmacéutica. Fundador y gerente general de IP360; Gerente Comercial / Coach de Entrenamiento en Contraining.

**IP360**
- Claim: «Lo que nos dijeron de las finanzas… pero no entendimos.» Cierre: «Por eso, esto lo planeo con IP360.» Promesa: «De lo complicado a lo simple en las finanzas, para que se puedan planear.»
- Pilares: vivir poco (seguros), vivir mucho (retiro y pensión), vivir mal (salud y accidentes), optimización fiscal.
- Frases clave: «Ahorrar no es planear», «La pensión no se improvisa», «Si no lo entiendes, no lo firmes».
- Lenguaje permitido: planear, estructurar, comparar, escenarios, método, largo plazo. Prohibido: garantizado, oportunidad única, libertad financiera genérica, vibra.
- Filtro: «¿Podría decirlo un banco?» Si sí, se descarta.
- Objetivo actual: solo posicionar. Sin productos, tasas, rentabilidades ni promesas. Ley 1328 de 2009, art. 7 lit. c: publicidad transparente, clara, veraz y oportuna.

## Voz por cuenta

| Cuenta | Voz | Trato | Notas |
| --- | --- | --- | --- |
| LinkedIn (personal) | Primera persona, Joaquín como coach y líder comercial | usted | Hilo: «método o improvisación» aplicado a la carrera (Contraining) y al patrimonio (IP360). Preguntas socráticas. Alternar temas: neutro, Contraining, IP360. |
| @contrainingfarma | Institucional, profesional, sin promesas vacías | tú | Dignificar la visita médica. Alternar diplomado (B2C) y servicios a laboratorios (B2B). CTA: WhatsApp 301 727 6517. |
| @ip360.co | Confrontador y claro, ironía hacia los bancos, retro-tech 90s-00s | tú | Mayéutica: preguntas que llevan a la conclusión. CTA suave (guardar, responder). |

## Diseño (kit/)

- `kit/gen_contraining_personal.py`: plantillas de Contraining (Champagne #F7EBD4, Sea Green #3A8844, Apricot #FECB83, League Spartan + Nunito) y de la marca personal (hueso #F4F1EC, carbón #2B2B2B, piedra #8A8580, Fraunces + Manrope; acento Sea Green si habla de Contraining, dorado #D4AF37 si habla de IP360).
- `kit/gen_ip360.py`: plantillas de IP360 (negro, blanco, dorado #D4AF37, Space Grotesk + JetBrains Mono, ventanas tipo Windows 95 y líneas de comando).
- Tamaños: publicaciones 1080×1350; historias 1080×1920 con zona segura de 260 px arriba y 280 px abajo.
- Uso: copiar el script, reemplazar el diccionario de piezas con el contenido nuevo y ejecutar `OUT=<carpeta> python3 <script> [claves]`. Chromium está en /opt/pw-browsers. Revisar visualmente cada pieza antes de mostrarla.
- Logo de Contraining solo sobre fondos claros.

## Historias con voz en off (ElevenLabs) — solo @contrainingfarma

Dentro de las historias diarias de Contraining que se preparan cada lunes, entre 2 y 3 por semana llevan voz en off. No son contenido adicional: reemplazan a historias estáticas de esa misma semana, así nunca compiten con lo demás. No se usan en IP360 ni en LinkedIn.

- **Voz:** Lina (colombiana), `voice_id` `yfUfwZTRubVrsUZWqzwp`, `model_id` `eleven_v4`, `generations_count` 1, con `creative_generate_speech`. Una llamada por guion; nunca repetir una llamada para reintentar (cada una cobra créditos).
- **Guion:** 35 a 50 palabras (13 a 16 segundos), con pregunta o gancho inicial y cierre invitando a escribir por WhatsApp. El número se escribe "tres cero uno, siete dos siete, sesenta y cinco diecisiete" y aparece en máximo una historia con voz por semana. Solo datos confirmados de este playbook.
- **Diseño:** plantilla `st()` del kit, igual que `kit/gen_historias_voz_s2.py` (copiar ese script, cambiar solo el contenido). El texto de la imagen resume lo que dice la voz.
- **Anotar** de cada audio, con `creative_get_flow_run_status`: `duration_secs`, créditos y `flow_id`. En la aprobación, mostrar el costo total con la suma desglosada.
- **Audios:** el espacio de trabajo no puede descargarlos de ElevenLabs. Al pedir la aprobación, pedirle a Joaquín que adjunte en la conversación los audios descargados desde el reproductor.
- **Emparejar** cada archivo adjunto con su historia comparando su duración (`ffprobe`) con `duration_secs`: el archivo mide unos 0,02 a 0,06 s más. Si dos duraciones quedan a menos de 0,15 s, confirmar con Joaquín.
- **Video:** `ffmpeg -loop 1 -framerate 30 -i Hn.png -i audio.mp3 -af "apad=pad_dur=1" -c:v libx264 -tune stillimage -pix_fmt yuv420p -c:a aac -b:a 160k -ar 44100 -shortest -movflags +faststart Hn.mp4`. Subir PNG y MP4 a la carpeta de la semana.
- **Programar** como historia con el MP4: `instagramData` = `{"type":"STORY","isAiGenerated":true}` (la voz es sintética). Si Joaquín no adjunta los audios, esas historias se programan como imagen sola, sin voz.
- **Destacados:** Metricool no los agrega por esta vía; recordarle a Joaquín que los agrega a mano en Instagram (Destacar o desde Archivo).

## Publicar imágenes y programar

1. Exportar a JPG (calidad 92) en `AAAA-MM-<marca>-semanaN/` dentro de este repositorio; commit y push a `main`.
2. Verificar que `https://raw.githubusercontent.com/investmentplannersco-dot/redes-media/main/<carpeta>/<archivo>.jpg` responda 200.
3. Programar con `createScheduledPost` usando esas URLs (Metricool copia la imagen a su servidor). Historias: `instagramData.type = "STORY"`, sin texto. Carruseles: varias URLs en `media`, `type = "POST"`. LinkedIn: `linkedinData.type = "post"`. Siempre `autoPublish: true` y `mediaAltText` por imagen.
4. Confirmar con `getScheduledPosts` que todo quedó en estado PENDING.
