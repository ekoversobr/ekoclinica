(function () {
  "use strict";

  var form = document.getElementById("contact-form");
  var nameField = document.getElementById("name");
  var subjectField = document.getElementById("subject");
  var feedback = document.getElementById("feedback");
  var whatsappNumber = "5583996809052";

  if (!form || !nameField || !subjectField) return;

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    var name = nameField.value.trim();
    var subject = subjectField.value;

    if (name.length < 2) {
      feedback.textContent = "Informe seu nome para continuar.";
      nameField.focus();
      return;
    }

    if (!subject) {
      feedback.textContent = "Selecione o assunto desejado.";
      subjectField.focus();
      return;
    }

    var message = "Olá! Me chamo " + name +
      " e gostaria de informações sobre " + subject +
      ". Vim pelo site da Eko Clínica.";

    var whatsappUrl = "https://wa.me/" + whatsappNumber +
      "?text=" + encodeURIComponent(message);

    // Registra apenas a intenção de abrir o WhatsApp.
    // Não envia nome, assunto ou qualquer dado clínico ao Google.
    window.dataLayer = window.dataLayer || [];

    var redirectStarted = false;
    function continueToWhatsApp() {
      if (redirectStarted) return;
      redirectStarted = true;
      window.location.assign(whatsappUrl);
    }

    window.dataLayer.push({
      event: "click_whatsapp",
      eventCallback: continueToWhatsApp,
      eventTimeout: 1000
    });

    // Fallback para o caso de o GTM não responder ao callback.
    window.setTimeout(continueToWhatsApp, 1200);
  });
})();
