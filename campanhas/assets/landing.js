(function(){
  "use strict";
  var form=document.getElementById("contact-form");
  var nameField=document.getElementById("name");
  var subjectField=document.getElementById("subject");
  var feedback=document.getElementById("feedback");
  var whatsapp="5583996809052";
  var started=false;
  window.dataLayer=window.dataLayer||[];

  function trackStart(){
    if(started)return;
    started=true;
    window.dataLayer.push({event:"form_start",form_name:"google_ads_landing"});
  }
  if(nameField)nameField.addEventListener("input",trackStart,{once:true});
  if(subjectField)subjectField.addEventListener("change",trackStart,{once:true});

  if(!form)return;
  form.addEventListener("submit",function(event){
    event.preventDefault();
    var name=nameField.value.trim();
    var subject=subjectField.value;
    var subjectSlug=subjectField.options[subjectField.selectedIndex].dataset.slug||"";
    if(name.length<2){
      feedback.textContent="Informe seu nome para continuar.";
      nameField.focus();
      return;
    }
    if(!subject){
      feedback.textContent="Selecione o assunto desejado.";
      subjectField.focus();
      return;
    }

    window.dataLayer.push({
      event:"whatsapp_handoff",
      form_name:"google_ads_landing",
      subject_slug:subjectSlug
    });

    var message="Olá, tudo bem? Me chamo "+name+" e vim do anúncio do Google e gostaria de informações.";
    window.location.href="https://wa.me/"+whatsapp+"?text="+encodeURIComponent(message);
  });
})();