(function(){
  "use strict";
  var form=document.getElementById("contact-form");
  var nameField=document.getElementById("name");
  var feedback=document.getElementById("feedback");
  var serviceSlug=document.body.getAttribute("data-service")||"";
  var whatsapp="5583996809052";
  var serviceName=document.title.split("|")[0].trim();
  var started=false;
  window.dataLayer=window.dataLayer||[];
  if(nameField){
    nameField.addEventListener("input",function(){
      if(started)return;
      started=true;
      window.dataLayer.push({event:"form_start",form_name:"service_landing",service_slug:serviceSlug});
    });
  }
  if(!form)return;
  form.addEventListener("submit",function(event){
    event.preventDefault();
    var name=nameField.value.trim();
    if(name.length<2){feedback.textContent="Informe seu nome para continuar.";nameField.focus();return;}
    window.dataLayer.push({event:"whatsapp_handoff",form_name:"service_landing",service_slug:serviceSlug});
    var msg="Olá! Meu nome é "+name+". Gostaria de informações sobre "+serviceName.toLowerCase()+" e disponibilidade de atendimento.";
    window.location.href="https://wa.me/"+whatsapp+"?text="+encodeURIComponent(msg);
  });
})();