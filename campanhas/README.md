# Landing pages de campanhas — Eko Clínica

Páginas dos cinco serviços prioritários. Cada pasta contém apenas o seu `index.html`; os arquivos compartilhados estão em `assets/`.

- `sedacao-consciente/`
- `implantes-dentarios/`
- `aparelhos-dentarios/`
- `facetas-em-resina/`
- `limpeza-e-clareamento/`

## Configuração compartilhada
- `assets/landing.css`: apresentação responsiva.
- `assets/landing.js`: validação simples, encaminhamento ao WhatsApp e eventos de intenção.

O número de WhatsApp está definido no JavaScript e deve ser confirmado antes da publicação. O GTM não foi incluído nas páginas porque há divergência entre IDs antigos; confirmar o container da Eko Clínica antes de adicionar tracking.

## Eventos
- `form_start`: primeira interação no campo de nome.
- `whatsapp_handoff`: formulário validado, imediatamente antes do encaminhamento ao WhatsApp.

Esses eventos não comprovam envio da mensagem, conversa, lead qualificado, agendamento ou venda. Não enviar nome, telefone ou dados clínicos para o dataLayer, GA4 ou Google Ads.


## Formulário único com assunto

A página `campanhas/` apresenta dois campos: nome e assunto. As opções são Agendamento, Sedação, Implantes, Aparelhos, Limpeza, Clareamento, Pediatria e Outras informações.

A mensagem pré-preenchida no WhatsApp segue o formato: “Olá! Vim do anúncio do Google. Me chamo [nome] e estou em busca de informações sobre [assunto].”

O número configurado é o mesmo que consta no site institucional: 5583996809052. Confirmar com a clínica antes de anunciar. O formulário envia somente o identificador técnico do assunto ao dataLayer; nome e assunto em texto não são enviados ao GA4/Google Ads.
