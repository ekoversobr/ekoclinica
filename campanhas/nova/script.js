(function () {
  "use strict";

  var WHATSAPP_NUMBER = "5583996809052";
  var form = document.getElementById("lead-form");
  var nameInput = document.getElementById("name");
  var phoneInput = document.getElementById("phone");
  var serviceInput = document.getElementById("service");
  var preview = document.getElementById("message-preview");
  var feedback = document.getElementById("form-feedback");

  if (!form || !nameInput || !phoneInput || !serviceInput || !preview) return;

  function digits(value) {
    return value.replace(/\D/g, "");
  }

  function currentMessage() {
    var name = nameInput.value.trim();
    var phone = phoneInput.value.trim();
    var service = serviceInput.value;
    var lines = ["Olá! Gostaria de falar com a equipe da Eko Clínica."];
    if (name) lines.push("Meu nome é " + name + ".");
    if (phone) lines.push("Meu telefone para contato é " + phone + ".");
    if (service) lines.push("Tenho interesse em: " + service + ".");
    lines.push("Aguardo o contato. Obrigado(a)!");
    return lines.join("\n");
  }

  function updatePreview() {
    preview.textContent = currentMessage();
  }

  function setError(id, message) {
    document.getElementById(id + "-error").textContent = message;
  }

  [nameInput, phoneInput, serviceInput].forEach(function (field) {
    field.addEventListener("input", updatePreview);
    field.addEventListener("change", updatePreview);
  });

  phoneInput.addEventListener("input", function () {
    var value = phoneInput.value.replace(/[^0-9()+\s-]/g, "");
    if (phoneInput.value !== value) phoneInput.value = value;
  });

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    feedback.textContent = "";
    setError("name", "");
    setError("phone", "");
    setError("service", "");

    var name = nameInput.value.trim();
    var phoneDigits = digits(phoneInput.value);
    var service = serviceInput.value;
    var valid = true;

    if (name.length < 2) {
      setError("name", "Informe seu nome para continuar.");
      valid = false;
    }
    if (phoneDigits.length < 10 || phoneDigits.length > 13) {
      setError("phone", "Informe um telefone válido com DDD.");
      valid = false;
    }
    if (!service) {
      setError("service", "Selecione o atendimento desejado.");
      valid = false;
    }

    if (!valid) {
      feedback.textContent = "Revise os campos destacados.";
      return;
    }

    var url = "https://wa.me/" + WHATSAPP_NUMBER + "?text=" +
      encodeURIComponent(currentMessage());
    window.location.href = url;
  });

  updatePreview();
})();
