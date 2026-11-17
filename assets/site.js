/*
 * Eko Clínica: código de atendimento nos links do WhatsApp.
 *
 * 1. Quando o visitante chega por um anúncio do Google, o endereço traz o
 *    parâmetro gclid. O site gera um código curto (ex.: EK7F3K) e guarda os
 *    dois no navegador por 90 dias.
 * 2. Se ENDPOINT estiver preenchido, o par código + gclid é enviado uma vez
 *    para a planilha (aba "Cliques do site"). Nenhum dado pessoal é enviado.
 * 3. Todos os links com data-wa recebem o código no fim da mensagem.
 * 4. No clique, envia o evento "whatsapp_click" para o dataLayer (GTM).
 */
(function () {
  "use strict";

  var ENDPOINT = "https://script.google.com/macros/s/AKfycbygHslpQ1rQhn10pftrihMVbH2iKofrFEj6J-VmvWWO7pD9pBPrCqcsYnEcOMJM1qzNEA/exec"; // App da Web do Apps Script da planilha
  var CHAVE = "eko_atendimento";
  var VALIDADE_MS = 90 * 24 * 60 * 60 * 1000;

  function gerarCodigo() {
    var letras = "ABCDEFGHJKMNPQRSTUVWXYZ23456789";
    var c = "EK";
    for (var i = 0; i < 4; i++) c += letras.charAt(Math.floor(Math.random() * letras.length));
    return c;
  }

  function ler() {
    try {
      var d = JSON.parse(localStorage.getItem(CHAVE) || "{}");
      if (d.criado && Date.now() - d.criado > VALIDADE_MS) return {};
      return d;
    } catch (e) { return {}; }
  }

  function gravar(d) {
    try { localStorage.setItem(CHAVE, JSON.stringify(d)); } catch (e) { /* navegação privada */ }
  }

  var params = new URLSearchParams(location.search);
  var gclid = params.get("gclid");
  var dados = ler();

  if (gclid && gclid !== dados.gclid) {
    dados = { codigo: gerarCodigo(), gclid: gclid, criado: Date.now(), enviado: false };
  } else if (!dados.codigo) {
    dados = { codigo: gerarCodigo(), gclid: "", criado: Date.now(), enviado: false };
  }
  gravar(dados);

  if (ENDPOINT && dados.gclid && !dados.enviado) {
    try {
      fetch(ENDPOINT, {
        method: "POST",
        mode: "no-cors",
        keepalive: true,
        headers: { "Content-Type": "text/plain;charset=utf-8" },
        body: JSON.stringify({ codigo: dados.codigo, gclid: dados.gclid, pagina: location.pathname })
      });
      dados.enviado = true;
      gravar(dados);
    } catch (e) { /* segue sem registrar */ }
  }

  function avisarGTM(servico) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: "whatsapp_click",
      servico: servico || "",
      origem_anuncio: dados.gclid ? "google_ads" : "outra"
    });
  }

  // Páginas de serviço: formulário curto que abre o WhatsApp com a mensagem pronta.
  // O envio passa por um link wa.me real (#wa-envio) para o acionador de clique
  // em links do GTM continuar contando a conversão "Contato".
  var form = document.getElementById("form-agendar");
  var envio = document.getElementById("wa-envio");
  if (form && envio) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var nome = form.nome.value.trim().replace(/\s+/g, " ");
      var proc = form.procedimento.value;
      var aviso = document.getElementById("form-aviso");
      if (nome.length < 2) {
        aviso.textContent = "Informe seu nome para continuar.";
        form.nome.focus();
        return;
      }
      var pedido = proc === "uma avaliação" ? "agendar uma avaliação" : "agendar uma avaliação de " + proc;
      var msg = "Olá, tudo bem? Me chamo " + nome + ". Cliquei no anúncio da Eko Clínica no Google e gostaria de " +
        pedido + ". (cód. " + dados.codigo + ")";
      envio.href = "https://wa.me/" + envio.href.split("wa.me/")[1].split("?")[0] + "?text=" + encodeURIComponent(msg);
      avisarGTM(proc);
      aviso.textContent = "Abrindo o WhatsApp…";
      envio.click();
    });
  }

  var links = document.querySelectorAll("a[data-wa]");
  for (var i = 0; i < links.length; i++) {
    var a = links[i];
    try {
      var url = new URL(a.href);
      var texto = url.searchParams.get("text") || "";
      // encodeURIComponent (e não searchParams.set) para os espaços virarem %20, não "+".
      a.href = url.origin + url.pathname + "?text=" +
        encodeURIComponent(texto + " (cód. " + dados.codigo + ")");
    } catch (e) { /* mantém o link original */ }

    a.addEventListener("click", function (ev) {
      avisarGTM(ev.currentTarget.getAttribute("data-servico"));
    });
  }
})();
