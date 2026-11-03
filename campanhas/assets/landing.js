(function(){
  "use strict";
  var form=document.getElementById("contact-form");
  var nameField=document.getElementById("name");
  var serviceField=document.getElementById("service");
  var feedback=document.getElementById("feedback");
  var whatsapp="5583996809052";
  var started=false;
  window.dataLayer=window.dataLayer||[];

  function trackStart(){
    if(started)return;
    started=true;
    window.dataLayer.push({event:"form_start",form_name:"campaign_landing"});
  }
  if(nameField)nameField.addEventListener("input",trackStart,{once:true});
  if(serviceField)serviceField.addEventListener("change",trackStart,{once:true});

  if(!form)return;
  form.addEventListener("submit",function(event){
    event.preventDefault();
    var name=nameField.value.trim();
    var service=serviceField.value;
    var serviceSlug=serviceField.options[serviceField.selectedIndex].dataset.slug||"";
    if(name.length<2){
      feedback.textContent="Informe seu nome para continuar.";
      nameField.focus();
      return;
    }
    if(!service){
      feedback.textContent="Selecione o serviço desejado.";
      serviceField.focus();
      return;
    }
    window.dataLayer.push({
      event:"whatsapp_handoff",
      form_name:"campaign_landing",
      service_slug:serviceSlug
    });
    var msg="Olá! Me chamo "+name+" e estou em busca de informações sobre "+service+".";
    window.location.href="https://wa.me/"+whatsapp+"?text="+encodeURIComponent(msg);
  });
})();