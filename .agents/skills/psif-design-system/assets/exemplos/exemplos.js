// Comportamento dos exemplos: gaveta no celular (§7.9), barra recolhível no web
// (§7.12), mostrar senha (§20.7) e confirmação de descarte (§10.3).
(function () {
  var lateral = document.getElementById('navegacao');
  if (!lateral) return;

  var abrir = document.querySelector('[aria-controls="navegacao"][aria-label="Abrir menu"]');
  var recolher = document.querySelector('.psif-cabecalho [aria-controls="navegacao"]');
  var veu = null;
  var web = window.matchMedia('(min-width: 768px)');
  var focaveis = 'a[href], button:not([disabled])';

  function fecharGaveta() {
    if (!veu) return;
    lateral.classList.remove('psif-lateral--aberta');
    lateral.removeAttribute('role');
    lateral.removeAttribute('aria-modal');
    veu.remove();
    veu = null;
    document.removeEventListener('keydown', teclado);
    abrir.setAttribute('aria-expanded', 'false');
    if (!web.matches) abrir.focus();
  }

  function teclado(evento) {
    if (evento.key === 'Escape') {
      fecharGaveta();
      return;
    }
    if (evento.key !== 'Tab') return;
    var itens = lateral.querySelectorAll(focaveis);
    var primeiro = itens[0];
    var ultimo = itens[itens.length - 1];
    if (evento.shiftKey && document.activeElement === primeiro) {
      evento.preventDefault();
      ultimo.focus();
    } else if (!evento.shiftKey && document.activeElement === ultimo) {
      evento.preventDefault();
      primeiro.focus();
    }
  }

  if (abrir) {
    abrir.addEventListener('click', function () {
      veu = document.createElement('div');
      veu.className = 'psif-veu';
      veu.addEventListener('click', fecharGaveta);
      document.body.appendChild(veu);
      lateral.classList.add('psif-lateral--aberta');
      lateral.setAttribute('role', 'dialog');
      lateral.setAttribute('aria-modal', 'true');
      abrir.setAttribute('aria-expanded', 'true');
      document.addEventListener('keydown', teclado);
      var ativo = lateral.querySelector('[aria-current="page"]') || lateral.querySelector(focaveis);
      if (ativo) ativo.focus();
    });
    lateral.addEventListener('click', function (evento) {
      if (veu && evento.target.closest('a')) fecharGaveta();
    });
  }

  // Gaveta aberta e janela passando de 768px (--bp-md): a barra volta a ser
  // fixa, e o véu ficaria bloqueando a página.
  web.addEventListener('change', function (evento) {
    if (evento.matches) fecharGaveta();
  });

  if (recolher) {
    recolher.addEventListener('click', function () {
      var recolhida = lateral.classList.toggle('psif-lateral--recolhida');
      recolher.setAttribute('aria-expanded', String(!recolhida));
      recolher.setAttribute('aria-label', recolhida ? 'Expandir menu' : 'Recolher menu');
    });
  }
})();

(function () {
  document.querySelectorAll('[data-mostrar-senha]').forEach(function (botao) {
    var campo = document.getElementById(botao.getAttribute('data-mostrar-senha'));
    botao.addEventListener('click', function () {
      var mostrando = campo.type === 'password';
      campo.type = mostrando ? 'text' : 'password';
      botao.setAttribute('aria-pressed', String(mostrando));
    });
  });
})();

(function () {
  var voltar = document.querySelector('[data-descarte]');
  if (!voltar) return;
  var folha = document.getElementById(voltar.getAttribute('data-descarte'));
  var form = document.getElementById(voltar.getAttribute('data-formulario'));
  var veu = null;

  function preenchido() {
    return Array.prototype.some.call(form.elements, function (campo) {
      return (campo.tagName === 'INPUT' || campo.tagName === 'TEXTAREA') && campo.value.trim() !== '';
    });
  }

  function fechar() {
    folha.hidden = true;
    if (veu) veu.remove();
    veu = null;
    document.removeEventListener('keydown', esc);
    voltar.focus();
  }

  function esc(evento) {
    if (evento.key === 'Escape') fechar();
  }

  voltar.addEventListener('click', function () {
    if (!preenchido()) return;
    veu = document.createElement('div');
    veu.className = 'psif-veu';
    veu.addEventListener('click', fechar);
    document.body.appendChild(veu);
    folha.hidden = false;
    document.addEventListener('keydown', esc);
    folha.querySelector('[data-continuar]').focus();
  });
  folha.querySelector('[data-continuar]').addEventListener('click', fechar);
  folha.querySelector('[data-descartar]').addEventListener('click', function () {
    form.reset();
    fechar();
  });
})();
