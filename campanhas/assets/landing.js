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

    window.location.assign(whatsappUrl);
  });
})();
