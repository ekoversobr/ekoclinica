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

    // Abre uma aba em branco durante o clique do usuário para evitar
    // bloqueio de pop-up. A aba atual permanece aberta para o Tag Assistant.
    var whatsappWindow = window.open("about:blank", "_blank");

    window.dataLayer = window.dataLayer || [];

    var completed = false;
    function continueToWhatsApp() {
      if (completed) return;
      completed = true;

      if (whatsappWindow && !whatsappWindow.closed) {
        whatsappWindow.location.href = whatsappUrl;
        feedback.textContent = "O WhatsApp foi aberto em uma nova aba.";
        return;
      }

      // Se o navegador bloquear a nova aba, mantém a landing aberta
      // e oferece um link manual, sem interromper a depuração.
      feedback.textContent = "O navegador bloqueou a nova aba. ";
      var link = document.createElement("a");
      link.href = whatsappUrl;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.textContent = "Clique aqui para abrir o WhatsApp.";
      feedback.appendChild(link);
    }

    // Mede somente a intenção de abrir o WhatsApp; não envia nome,
    // assunto ou dados clínicos ao Google.
    window.dataLayer.push({
      event: "click_whatsapp",
      eventCallback: continueToWhatsApp,
      eventTimeout: 1500
    });

    // Fallback caso o GTM não execute o callback.
    window.setTimeout(continueToWhatsApp, 1700);
  });
})();
