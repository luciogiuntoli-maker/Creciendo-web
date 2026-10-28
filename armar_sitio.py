"""Genera index.html y tratamientos-corporales.html con la misma cabecera, pie e íconos.
Los textos de servicios son los que envió Creciendo; editar acá y volver a correr: python armar_sitio.py"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = 'https://images.unsplash.com/photo-{}?w={}&q=72'

SIMBOLOS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <symbol id="flor" viewBox="0 0 100 100">
      <g transform="translate(50 52)">
        <ellipse rx="9" ry="24" fill="#8e5cc7" transform="rotate(-70) translate(0 -22)"/>
        <ellipse rx="9" ry="24" fill="#e2559b" transform="rotate(-35) translate(0 -22)"/>
        <ellipse rx="9" ry="24" fill="#f39c33" transform="rotate(0) translate(0 -22)"/>
        <ellipse rx="9" ry="24" fill="#f6c838" transform="rotate(35) translate(0 -22)"/>
        <ellipse rx="9" ry="24" fill="#7dbb57" transform="rotate(70) translate(0 -22)"/>
        <ellipse rx="9" ry="24" fill="#3fa9d6" transform="rotate(105) translate(0 -22)" opacity=".9"/>
        <circle r="7" fill="#fff"/>
      </g>
    </symbol>
    <symbol id="wa" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21h.01c5.46 0 9.91-4.45 9.91-9.91A9.85 9.85 0 0 0 12.04 2Zm5.8 14.03c-.24.68-1.41 1.3-1.95 1.38-.5.07-1.13.1-1.82-.12-.42-.13-.96-.31-1.65-.61-2.9-1.25-4.8-4.18-4.94-4.37-.14-.19-1.18-1.57-1.18-3 0-1.42.75-2.12 1.01-2.41.27-.29.58-.36.78-.36h.56c.18 0 .42-.07.66.5.24.58.82 2.01.89 2.15.07.15.12.32.02.51-.1.19-.14.31-.29.48-.14.17-.3.38-.43.51-.14.14-.29.3-.12.59.17.29.75 1.24 1.6 2 1.1.98 2.03 1.28 2.32 1.43.29.14.46.12.63-.07.17-.19.72-.84.92-1.13.19-.29.38-.24.65-.14.26.1 1.68.79 1.97.94.29.14.48.22.55.34.07.12.07.7-.17 1.38Z"/></symbol>
    <symbol id="i-escudo" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6l8-3Z"/><path d="m8.5 12 2.5 2.5 4.5-5"/></symbol>
    <symbol id="i-profesional" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="7.5" r="3.5"/><path d="M5 20c.8-3.6 3.6-6 7-6s6.2 2.4 7 6"/><path d="M12 14v3m-1.5-1.5h3"/></symbol>
    <symbol id="i-evaluacion" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6M9 18h3"/></symbol>
    <symbol id="i-corazon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z"/><path d="M8.5 11h2l1-2 1.5 4 1-2h1.5"/></symbol>
    <symbol id="i-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></symbol>
    <symbol id="i-reloj" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></symbol>
    <symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><rect x="3.5" y="5.5" width="17" height="13" rx="2"/><path d="m4 7 8 6 8-6"/></symbol>
  </defs>
</svg>'''


def cabecera(titulo, descripcion, en_index):
    pre = '' if en_index else 'index.html'
    actual = '' if en_index else ' aria-current="page"'
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=DM+Sans:wght@400;500;700&family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<!-- Flor del logo (provisoria hasta recibir el logo original) e íconos -->
{SIMBOLOS}

<header>
  <div class="contenedor nav">
    <a href="{pre or '#inicio'}" class="marca" aria-label="Creciendo, inicio">
      <svg><use href="#flor"/></svg>
      <span class="marca-texto"><b>Creciendo</b><small>Tu espacio de bienestar</small></span>
    </a>
    <nav class="menu" id="menu">
      <a href="{pre}#movimiento">Movimiento</a>
      <a href="{pre}#estetica"{actual}>Estética</a>
      <a href="{pre}#nosotros">Nosotros</a>
      <a href="{pre}#opiniones">Opiniones</a>
      <a href="{pre}#contacto">Contacto</a>
    </nav>
    <a class="btn btn-primario" data-wa="Hola, quisiera solicitar un turno en Creciendo." href="{pre}#contacto"><svg fill="currentColor"><use href="#wa"/></svg><span>Solicitar turno</span></a>
    <button class="abrir-menu" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
    </button>
  </div>
</header>
'''


PIE = '''
<footer>© Creciendo, tu espacio de bienestar · Av. San Martín 1917, Villa Constitución, Santa Fe · Desde 2001</footer>

<a class="flotante" data-wa="Hola, quisiera realizar una consulta." href="#" aria-label="Escribir por WhatsApp"><svg><use href="#wa"/></svg></a>

<script src="app.js"></script>
</body>
</html>
'''


def tarjeta(titulo, bajada, resumen, mas, img, alt, msg, cta, insignia='', extra=''):
    parrafos = ''.join(f'<p>{p}</p>' for p in mas)
    badge = f'<span class="insignia">{insignia}</span>' if insignia else ''
    return f'''
      <article class="tarjeta aparecer">
        {badge}<img src="{IMG.format(img, 800)}" alt="{alt}" loading="lazy">
        <div class="cuerpo">
          <h3>{titulo}</h3>
          <p class="bajada">{bajada}</p>
          <p>{resumen}</p>{extra}
          <details><summary>Conocer más</summary>{parrafos}</details>
          <div class="pie-tarjeta"><a class="enlace" data-wa="{msg}" href="#contacto">{cta}</a></div>
        </div>
      </article>'''


MOVIMIENTO = [
    ('Yoga Integral', 'Movimiento consciente, respiración y relajación.',
     'Una práctica que integra movimiento consciente, posturas, respiración y relajación para favorecer la movilidad, la flexibilidad, el equilibrio y el bienestar integral.',
     ['En Creciendo, acompañamos a cada persona respetando sus posibilidades, necesidades y tiempos, promoviendo una conexión más consciente con su cuerpo.'],
     '1599901860904-17e6ed7083a0', 'Clase de Yoga Integral', 'Hola, quisiera consultar los días y horarios de Yoga Integral.'),
    ('Pilates Postural', 'Fuerza, movilidad, equilibrio y conciencia corporal.',
     'En Creciendo trabajamos con resortes en la pared, que ofrecen un entorno más estable y permiten adaptar los ejercicios a diferentes necesidades y capacidades físicas.',
     ['Desde personas que requieren mayor seguridad y estabilidad hasta quienes buscan mejorar su condición física mediante ejercicios más dinámicos, combinando resortes con otros elementos.'],
     '1518611012118-696072aa579a', 'Práctica de Pilates Postural', 'Hola, quisiera consultar los días y horarios de Pilates Postural.'),
    ('Reacondicionamiento Físico', 'Actividad física adaptada para una vida más activa.',
     'Una propuesta orientada a mejorar la fuerza muscular, la movilidad, el equilibrio y la autonomía en las actividades cotidianas.',
     ['En Creciendo acompañamos a cada persona con ejercicios progresivos, respetando sus capacidades, necesidades y ritmo individual, para favorecer una vida más activa e independiente.'],
     '1571019613454-1cb2f99b2d8b', 'Ejercicios de Reacondicionamiento Físico', 'Hola, quisiera consultar los días y horarios de Reacondicionamiento Físico.'),
]

ESTETICA = [
    ('Cosmiatría Funcional', 'El cuidado de tu piel en cada etapa de la vida, con fundamento científico.',
     'Desde los primeros cuidados preventivos en la preadolescencia hasta las necesidades específicas de la piel adulta y madura, promoviendo un envejecimiento saludable.',
     ['En Creciendo abordamos cada piel de manera personalizada, integrando conocimientos científicos sobre su estructura, funciones y necesidades, junto con técnicas cosmiátricas y tecnología estética.',
      'Cada procedimiento se selecciona respetando las características individuales de la piel, priorizando su equilibrio, la integridad de la barrera cutánea y su bienestar.'],
     '1570172619644-dfd03ed5d881', 'Tratamiento de cosmiatría facial', 'Hola, quisiera consultar por los tratamientos de Cosmiatría Funcional.', 'Consultar tratamientos', ''),
    ('Depilación Definitiva', 'Tecnología, seguridad y atención personalizada.',
     'Realizamos depilación definitiva con tecnología láser Soprano ICE, utilizando equipos certificados y autorizados por ANMAT.',
     ['Cada tratamiento se adapta a las características de la piel, el tipo de vello y las necesidades individuales, buscando una reducción progresiva y duradera del crecimiento del vello.',
      'Trabajamos con profesionales de la salud a cargo de los procedimientos, priorizando la seguridad, el cuidado de la piel y el seguimiento personalizado durante todo el proceso.'],
     '1560750588-73207b1ef5b8', 'Espacio de tratamiento', 'Hola, quisiera consultar turnos de Depilación Definitiva.', 'Consultar turnos', 'Láser Soprano ICE'),
    ('Longevidad Cutánea', 'Un enfoque funcional para acompañar el envejecimiento saludable de la piel.',
     'El objetivo no es detener el paso del tiempo, sino favorecer una piel saludable, equilibrada y de buena calidad en cada etapa de la vida.',
     ['A través de conocimientos científicos, técnicas cosmiátricas y tecnología estética, trabajamos para mejorar la hidratación, la textura, la firmeza y la apariencia general de la piel, respetando sus características y procesos naturales.',
      'Cada procedimiento se adapta a las necesidades individuales, priorizando la función cutánea y el bienestar a largo plazo.'],
     '1616394584738-fc6e612e71b9', 'Cuidado de la piel', 'Hola, quisiera consultar por los tratamientos de Longevidad Cutánea.', 'Consultar tratamientos', ''),
    ('Tratamientos Faciales Personalizados', 'Tecnología estética y conocimientos científicos al servicio de tu piel.',
     'Combinamos diferentes técnicas cosmiátricas y tecnologías estéticas para abordar las necesidades particulares de cada piel.',
     ['Ofrecemos procedimientos como higiene facial profunda, hidratación, peelings cosméticos, microneedling (Dermapen), láser de picosegundos, radiofrecuencia y otras tecnologías orientadas a mejorar la textura, la luminosidad, la firmeza y la calidad general de la piel.',
      'Cada tratamiento se selecciona de manera personalizada, respetando las características y necesidades cutáneas, priorizando el equilibrio, la funcionalidad y el bienestar de la piel.'],
     '1552693673-1bf958298935', 'Tratamiento facial personalizado', 'Hola, quisiera consultar por los Tratamientos Faciales Personalizados.', 'Consultar tratamientos', ''),
]
ETIQUETAS_FACIALES = ['Higiene facial profunda', 'Hidratación', 'Peelings cosméticos', 'Dermapen', 'Láser de picosegundos', 'Radiofrecuencia']

OPINIONES = [  # textuales de Google Maps
    ('Carmela M.', 'Es un espacio especial para sentirte mimada. Donde cuidan tu bienestar interior y tu belleza exterior.', '#8e5cc7'),
    ('Paola B.', 'Siempre placentero. Siempre la mejor atención y profesionalidad. Creciendo es bienestar y calidez.', '#e2559b'),
    ('Ziomara G.', 'Hice 3 sesiones de depilación definitiva y fue un éxito. Muy profesionales.', '#f39c33'),
    ('Lucía V.', 'Mi experiencia en este lugar me cambió en cuerpo y alma. Hace más de 2 años que estoy en Creciendo y no pienso irme.', '#7dbb57'),
    ('María Cristina F.', 'Creciendo es el lugar donde encontré comodidad, compañerismo y muy buena atención.', '#3fa9d6'),
    ('Ramiro D.', 'Excelente atención y resultados del tratamiento. Muy conforme.', '#6b3fa0'),
]

SUBTRATAMIENTOS = [  # borradores para que Creciendo los revise
    ('reductor', 'Tratamiento reductor', 'Un abordaje personalizado de la adiposidad localizada y de la apariencia de la piel con celulitis.',
     ['A partir de una evaluación inicial, diseñamos un plan que puede combinar tecnologías como ultrasonidos de diferentes frecuencias y potencias, radiofrecuencia, vacuumterapia y presoterapia, según las características y los objetivos de cada persona.',
      'Trabajamos de manera progresiva y con seguimiento en cada sesión, priorizando el cuidado de los tejidos y resultados realistas, que se potencian con hábitos saludables y actividad física.'],
     '1544161515-4ab6ce6db874'),
    ('flacidez-cutanea', 'Flacidez cutánea', 'Tratamientos orientados a mejorar la firmeza, la elasticidad y la calidad de la piel.',
     ['La flacidez cutánea se relaciona con cambios en el colágeno y la elastina a lo largo del tiempo, con variaciones de peso y con otros factores. Seleccionamos tecnologías como la radiofrecuencia y técnicas complementarias para estimular la piel y mejorar su textura y su tono.',
      'Cada plan se adapta a la zona a tratar y a las características de la piel, con controles periódicos para acompañar su evolución.'],
     '1515377905703-c4788e51af15'),
    ('flacidez-muscular', 'Flacidez muscular', 'Estimulación y fortalecimiento muscular para mejorar la tonicidad corporal.',
     ['Utilizamos estimulación muscular mediante pulso magnético y corrientes de electroestimulación, que generan contracciones musculares para trabajar la tonicidad en zonas como abdomen, glúteos y piernas.',
      'Este tratamiento puede complementarse con nuestras propuestas de movimiento, como Pilates Postural o Reacondicionamiento Físico, para potenciar los resultados.'],
     '1540555700478-4be289fbecef'),
]


def index():
    mov = ''.join(tarjeta(t, b, r, m, i, a, w, 'Consultar días y horarios') for t, b, r, m, i, a, w in MOVIMIENTO)
    est = ''
    for t, b, r, m, i, a, w, cta, ins in ESTETICA:
        extra = ''
        if t.startswith('Tratamientos Faciales'):
            extra = '\n          <div class="etiquetas">' + ''.join(f'<span>{e}</span>' for e in ETIQUETAS_FACIALES) + '</div>'
        est += tarjeta(t, b, r, m, i, a, w, cta, ins, extra)
    sub = ''.join(f'<a href="tratamientos-corporales.html#{k}">{n}</a>' for k, n, *_ in SUBTRATAMIENTOS)
    ops = ''.join(f'''
      <figure class="opinion"><div class="estrellas">★★★★★</div><p>“{t}”</p>
      <figcaption class="autor"><span class="avatar" style="background:{c}">{n[0]}</span>{n}</figcaption></figure>''' for n, t, c in OPINIONES)
    return cabecera('Creciendo · Tu espacio de bienestar en Villa Constitución',
                    'Yoga Integral, Pilates Postural, Reacondicionamiento Físico, cosmiatría, depilación definitiva Soprano ICE y tratamientos corporales en Villa Constitución, desde 2001.', True) + f'''
<main>
<section class="portada" id="inicio">
  <div class="contenedor portada-grid">
    <div>
      <span class="antetitulo">Villa Constitución · Desde 2001</span>
      <h1>Una mirada integral de <em>tu bienestar</em></h1>
      <p class="lead">El movimiento, la estética y el cuidado personal se complementan para acompañarte en cada etapa de tu vida.</p>
      <p class="sub">En Creciendo, te ofrecemos diferentes propuestas para cuidar tu salud, tu cuerpo y tu bienestar, respetando tus necesidades.</p>
      <div class="acciones">
        <a class="btn btn-wa" data-wa="Hola, quisiera solicitar un turno en Creciendo." href="#contacto"><svg fill="currentColor"><use href="#wa"/></svg>Solicitar turno por WhatsApp</a>
        <a class="btn btn-borde" href="#movimiento">Conocer las propuestas</a>
      </div>
      <div class="datos">
        <div class="dato"><b>+25 años</b><span>cuidando personas</span></div>
        <div class="dato"><b>4,9 <span class="estrellas">★</span></b><span>58 opiniones en Google</span></div>
        <div class="dato"><b>8</b><span>propuestas de movimiento y estética</span></div>
      </div>
    </div>
    <div class="visual" aria-hidden="true">
      <div class="sol"></div>
      <img class="foto-principal" src="{IMG.format('1506126613408-eca07ce68773', 900)}" alt="">
      <img class="foto-chica" src="{IMG.format('1570172619644-dfd03ed5d881', 500)}" alt="">
      <div class="etiqueta e1"><i></i>Yoga Integral y Pilates Postural</div>
      <div class="etiqueta e2"><i></i>Cosmiatría y estética</div>
    </div>
  </div>
</section>

<section class="confianza" aria-label="Por qué elegirnos">
  <div class="contenedor">
    <div class="confianza-grid aparecer">
      <div class="sello"><span class="ico"><svg><use href="#i-escudo"/></svg></span><div><b>Equipos autorizados por ANMAT</b><span>Láser Soprano ICE certificado</span></div></div>
      <div class="sello"><span class="ico"><svg><use href="#i-profesional"/></svg></span><div><b>Profesionales de la salud</b><span>A cargo de cada procedimiento</span></div></div>
      <div class="sello"><span class="ico"><svg><use href="#i-evaluacion"/></svg></span><div><b>Evaluación personalizada</b><span>Antes de cada tratamiento</span></div></div>
      <div class="sello"><span class="ico"><svg><use href="#i-corazon"/></svg></span><div><b>Área Protegida</b><span>Tranquilidad en cada práctica</span></div></div>
    </div>
  </div>
</section>

<section class="mov" id="movimiento">
  <div class="contenedor">
    <div class="cabecera aparecer">
      <span class="antetitulo">Movimiento</span>
      <h2>Prácticas que respetan tus tiempos</h2>
      <p>Grupos reducidos y profesionales que acompañan a cada persona, respetando sus posibilidades y sus tiempos.</p>
    </div>
    <div class="tarjetas">{mov}
    </div>
  </div>
</section>

<section class="est estetica" id="estetica">
  <div class="contenedor">
    <div class="cabecera aparecer">
      <span class="antetitulo">Estética</span>
      <h2>El cuidado de tu piel, con fundamento científico</h2>
      <p>Técnicas cosmiátricas y tecnología estética, seleccionadas de manera personalizada para cada piel.</p>
    </div>
    <div class="tarjetas dos">{est}
    </div>
    <div class="destacado aparecer" id="corporales">
      <img src="{IMG.format('1519823551278-64ac92734fb1', 1000)}" alt="Tratamiento corporal" loading="lazy">
      <div class="texto">
        <span class="antetitulo">Tratamientos corporales</span>
        <h3>Tratamientos Corporales Personalizados</h3>
        <p class="bajada">Tecnología estética y conocimientos científicos para el cuidado corporal.</p>
        <p>Trabajamos sobre la apariencia de la piel con celulitis, la adiposidad localizada, la flacidez cutánea, la tonicidad muscular y el bienestar circulatorio, a partir de una evaluación personalizada.</p>
        <div class="sub-lista">{sub}</div>
        <a class="btn btn-claro" href="tratamientos-corporales.html">Ver tratamientos corporales</a>
      </div>
    </div>
  </div>
</section>

<section id="nosotros">
  <div class="contenedor">
    <div class="cabecera aparecer">
      <span class="antetitulo">Por qué Creciendo</span>
      <h2>Atención personalizada, sin soluciones mágicas</h2>
    </div>
    <div class="porque-grid">
      <div class="porque aparecer"><h3>Escuchamos primero</h3><p>Nuestra esencia está en escuchar, comprender y respetar las necesidades de cada persona.</p></div>
      <div class="porque aparecer"><h3>Mirada interdisciplinaria</h3><p>Profesionales con formación continua que trabajan de manera conjunta, porque cada persona es única.</p></div>
      <div class="porque aparecer"><h3>Criterio profesional</h3><p>Procedimientos con fundamento científico, seleccionados según las características de cada persona.</p></div>
      <div class="porque aparecer"><h3>Espacio protegido</h3><p>Contamos con servicio de Área Protegida para que cada práctica se realice con tranquilidad.</p></div>
    </div>
    <div class="cita aparecer">“En tiempos que cambian, seguimos eligiendo cuidar personas.”<small>Creciendo, tu espacio de bienestar · desde 2001</small></div>
  </div>
</section>

<section class="opiniones" id="opiniones">
  <div class="contenedor">
    <div class="cabecera aparecer">
      <span class="antetitulo">Opiniones</span>
      <h2>Lo que dicen quienes nos eligen</h2>
    </div>
    <div class="resumen-google aparecer">
      <b>4,9</b>
      <div><div class="estrellas" style="font-size:1.3rem">★★★★★</div><span style="color:var(--gris)">58 opiniones en Google Maps</span></div>
    </div>
    <div class="carrusel">{ops}
    </div>
  </div>
</section>

<section>
  <div class="contenedor">
    <div class="llamado aparecer">
      <div>
        <h2>Tu bienestar comienza con una consulta</h2>
        <p>Te orientamos sobre la propuesta o el tratamiento más adecuado para tus necesidades.</p>
      </div>
      <a class="btn btn-claro" data-wa="Hola, quisiera recibir orientación sobre las propuestas de Creciendo." href="#contacto"><svg fill="currentColor"><use href="#wa"/></svg>Realizar una consulta</a>
    </div>
  </div>
</section>

<section id="regalos" style="padding-top:0">
  <div class="contenedor gift">
    <div class="giftcard aparecer" aria-hidden="true">
      <span class="marca-texto"><b>Creciendo</b><small>Tu espacio de bienestar</small></span>
      <div><small style="opacity:.85;letter-spacing:.15em;text-transform:uppercase;font-size:.75rem">Gift Card</small><br><big>Bienestar para regalar</big></div>
    </div>
    <div class="aparecer">
      <span class="antetitulo">Gift Cards</span>
      <h2>Un regalo que se siente</h2>
      <p style="color:var(--gris);margin-top:.8rem">Armamos Gift Cards personalizadas combinando nuestras propuestas, ideales para cumpleaños y fechas especiales.</p>
      <ul class="lista-check">
        <li>Tratamientos faciales y corporales</li>
        <li>Clases de Yoga Integral y Pilates Postural</li>
        <li>Depilación definitiva</li>
      </ul>
      <a class="btn btn-primario" data-wa="Hola, quisiera armar una Gift Card de Creciendo." href="#contacto"><svg fill="currentColor"><use href="#wa"/></svg>Armar una Gift Card</a>
    </div>
  </div>
</section>

<section class="contacto" id="contacto">
  <div class="contenedor contacto-grid">
    <div class="datos-contacto">
      <div><span class="antetitulo">Contacto</span><h2>Te esperamos</h2></div>
      <div class="fila"><div class="ico"><svg><use href="#i-pin"/></svg></div><div><b>Dirección</b><span>Av. San Martín 1917, Villa Constitución, Santa Fe</span></div></div>
      <div class="fila"><div class="ico"><svg><use href="#i-reloj"/></svg></div><div><b>Horario</b><span>Lunes a viernes de 7 a 21 h · Sábados de 8 a 12 h<br>Atención con turno previo</span></div></div>
      <div class="fila"><div class="ico"><svg fill="currentColor"><use href="#wa"/></svg></div><div><b>WhatsApp</b><a data-wa="Hola, quisiera realizar una consulta." href="#">+54 9 3400 65-7816</a></div></div>
      <div class="fila"><div class="ico"><svg><use href="#i-mail"/></svg></div><div><b>Correo electrónico</b><a href="mailto:creciendo1917@hotmail.com">creciendo1917@hotmail.com</a></div></div>
      <div class="redes">
        <a href="https://www.instagram.com/creciendotuespacio/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg></a>
        <a href="https://www.facebook.com/Creciendotuespaciodebienestar/" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8h3V4h-3c-2.8 0-4 1.7-4 4.2V10H7v4h3v8h4v-8h3l1-4h-4V8.6c0-.4.3-.6.6-.6Z"/></svg></a>
      </div>
    </div>
    <iframe class="mapa" title="Ubicación de Creciendo" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://www.google.com/maps?q=Creciendo+Tu+Espacio+de+Bienestar,+Av.+San+Mart%C3%ADn+1917,+Villa+Constituci%C3%B3n&output=embed"></iframe>
  </div>
</section>
</main>
''' + PIE


def corporales():
    pestanas = ''.join(f'''
      <button role="tab" id="t-{k}" aria-controls="{k}" aria-selected="{'true' if n == 0 else 'false'}"{'' if n == 0 else ' tabindex="-1"'}>{t}</button>'''
                       for n, (k, t, *_) in enumerate(SUBTRATAMIENTOS))
    paneles = ''
    for n, (k, t, b, ps, img) in enumerate(SUBTRATAMIENTOS):
        cuerpo = ''.join(f'<p>{p}</p>' for p in ps)
        paneles += f'''
    <div class="panel" id="{k}" role="tabpanel" aria-labelledby="t-{k}"{'' if n == 0 else ' hidden'}>
      <img src="{IMG.format(img, 900)}" alt="{t}" loading="lazy">
      <div>
        <h2>{t}</h2>
        <p class="bajada">{b}</p>
        {cuerpo}
        <div class="acciones"><a class="btn btn-wa" data-wa="Hola, quisiera consultar por {t.lower()}." href="index.html#contacto"><svg fill="currentColor"><use href="#wa"/></svg>Consultar tratamientos</a></div>
      </div>
    </div>'''
    tec = ['Radiofrecuencia', 'Vacuumterapia', 'Ultrasonidos de diferentes frecuencias y potencias', 'Estimulación muscular mediante pulso magnético',
           'Corrientes de electroestimulación', 'Presoterapia', 'Otras técnicas complementarias', 'Evaluación personalizada previa']
    return cabecera('Tratamientos corporales · Creciendo',
                    'Tratamientos corporales personalizados en Creciendo, Villa Constitución: tratamiento reductor, flacidez cutánea y flacidez muscular.', False) + f'''
<main>
<section class="encabezado-pagina">
  <div class="contenedor">
    <p class="miga"><a href="index.html#estetica">Estética</a> / Tratamientos corporales</p>
    <div class="grid">
      <div>
        <span class="antetitulo">Tratamientos corporales</span>
        <h1>Tratamientos Corporales Personalizados</h1>
        <p class="bajada">Tecnología estética y conocimientos científicos para el cuidado corporal.</p>
        <p>En Creciendo abordamos las diferentes necesidades estéticas corporales mediante procedimientos personalizados, combinando tecnologías y técnicas específicas según las características y objetivos de cada persona.</p>
        <p>Nuestro enfoque comienza con una evaluación personalizada, que nos permite identificar las necesidades y objetivos de cada persona para seleccionar los procedimientos y tecnologías más adecuados, priorizando la seguridad, el cuidado de los tejidos y resultados estéticos progresivos y realistas.</p>
        <div class="acciones"><a class="btn btn-wa" data-wa="Hola, quisiera solicitar una evaluación para tratamientos corporales." href="index.html#contacto"><svg fill="currentColor"><use href="#wa"/></svg>Solicitar evaluación</a></div>
      </div>
      <img src="{IMG.format('1519823551278-64ac92734fb1', 1000)}" alt="Tratamiento corporal">
    </div>
  </div>
</section>

<section>
  <div class="contenedor">
    <div class="cabecera">
      <span class="antetitulo">Tratamientos</span>
      <h2>Un plan para cada objetivo</h2>
    </div>
    <div class="pestanas" role="tablist" aria-label="Tipos de tratamiento corporal">{pestanas}
    </div>{paneles}
  </div>
</section>

<section class="tecnologias">
  <div class="contenedor">
    <div class="cabecera">
      <span class="antetitulo">Tecnología</span>
      <h2>Tecnologías con las que trabajamos</h2>
      <p>Cada combinación se define a partir de la evaluación personalizada.</p>
    </div>
    <ul class="lista-tec">{''.join(f'<li>{t}</li>' for t in tec)}</ul>
  </div>
</section>
</main>
''' + PIE


for nombre, html in (('index.html', index()), ('tratamientos-corporales.html', corporales())):
    with open(os.path.join(BASE, nombre), 'w', encoding='utf-8') as f:
        f.write(html)
    print('ok', nombre)
