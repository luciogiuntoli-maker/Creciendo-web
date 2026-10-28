// WhatsApp de Creciendo: cada enlace con data-wa abre el chat con ese mensaje ya escrito
const TEL = '5493400657816';
document.querySelectorAll('[data-wa]').forEach(a => {
  a.href = `https://wa.me/${TEL}?text=${encodeURIComponent(a.dataset.wa)}`;
  a.target = '_blank';
  a.rel = 'noopener';
});

// Menú en celulares
const boton = document.querySelector('.abrir-menu');
const menu = document.querySelector('.menu');
if (boton) {
  boton.addEventListener('click', () => {
    const abierto = menu.classList.toggle('abierto');
    boton.setAttribute('aria-expanded', abierto);
  });
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    menu.classList.remove('abierto');
    boton.setAttribute('aria-expanded', false);
  }));
}

// Pestañas (página de tratamientos corporales); el hash de la URL abre la pestaña correspondiente
const pestanas = [...document.querySelectorAll('[role="tab"]')];
const mostrar = id => {
  pestanas.forEach(p => {
    const activa = p.getAttribute('aria-controls') === id;
    p.setAttribute('aria-selected', activa);
    p.tabIndex = activa ? 0 : -1;
    document.getElementById(p.getAttribute('aria-controls')).hidden = !activa;
  });
};
pestanas.forEach((p, i) => {
  p.addEventListener('click', () => { mostrar(p.getAttribute('aria-controls')); history.replaceState(null, '', '#' + p.getAttribute('aria-controls')); });
  p.addEventListener('keydown', e => {
    const paso = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
    if (!paso) return;
    const sig = pestanas[(i + paso + pestanas.length) % pestanas.length];
    sig.focus(); sig.click();
  });
});
if (pestanas.length) {
  const inicial = pestanas.find(p => '#' + p.getAttribute('aria-controls') === location.hash);
  mostrar((inicial || pestanas[0]).getAttribute('aria-controls'));
}

// Aparición suave al hacer scroll
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
}), { threshold: .12 });
document.querySelectorAll('.aparecer').forEach(el => io.observe(el));
