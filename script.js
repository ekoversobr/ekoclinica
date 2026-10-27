const WHATSAPP_NUMBER = "5583996809052";

const menuToggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".nav");
if (menuToggle && nav) {
  menuToggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
  });
  nav.querySelectorAll("a").forEach(link => link.addEventListener("click", () => {
    nav.classList.remove("open");
    menuToggle.setAttribute("aria-expanded", "false");
  }));
}

const form = document.getElementById("appointment-form");
if (form) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const name = document.getElementById("name").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const email = document.getElementById("email").value.trim();
    const service = document.getElementById("service").value;
    const feedback = document.getElementById("form-feedback");

    if (!name || !phone || !service) {
      feedback.textContent = "Preencha seu nome, telefone e o tipo de solicitação.";
      return;
    }

    const lines = [
      "Olá! Gostaria de falar com a Eko Clínica.",
      "",
      `Nome: ${name}`,
      `Meu telefone: ${phone}`,
      email ? `E-mail: ${email}` : null,
      `Solicitação: ${service}`,
      "",
      "Gostaria de informações sobre disponibilidade de atendimento."
    ].filter(Boolean);

    const url = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(lines.join("\n"))}`;
    feedback.textContent = "Abrindo o WhatsApp para você revisar e enviar a mensagem…";
    window.open(url, "_blank", "noopener,noreferrer");
  });
}
