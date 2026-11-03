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
