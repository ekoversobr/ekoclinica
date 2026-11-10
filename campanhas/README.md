# Landing pages de campanhas — Eko Clínica

Landing principal de captação:
- `index.html` — formulário com nome e assunto, encaminhando para o WhatsApp.

Páginas específicas por serviço:
- `sedacao-consciente/`
- `implantes-dentarios/`
- `aparelhos-dentarios/`
- `facetas-em-resina/`
- `limpeza-e-clareamento/`

## Arquivos compartilhados
- `assets/landing.css` — apresentação responsiva.
- `assets/landing.js` — validação do formulário e abertura do WhatsApp.
- A logo utilizada na landing principal vem de `../logo-eko-clinica.png`.

## Mensuração
Esta landing foi deliberadamente mantida sem Google tag, Google Tag Manager, GA4, pixels ou eventos `dataLayer`. A mensuração deverá ser instalada separadamente, depois da definição da arquitetura correta para a Eko Clínica e de um plano de testes que evite tags duplicadas.

O formulário abre o WhatsApp com uma mensagem pré-preenchida. Isso mede apenas a intenção de iniciar uma conversa; não confirma que a mensagem foi enviada, que houve resposta, agendamento, comparecimento ou venda.

## Privacidade
O nome e o assunto são usados somente para compor a mensagem no WhatsApp. O site não grava esses campos em banco de dados nem os envia para ferramentas de analytics. Não informe diagnóstico, exames ou outros dados clínicos neste formulário.

## Antes de anunciar
1. Confirmar com a clínica o número de WhatsApp configurado em `assets/landing.js`.
2. Testar o formulário em celular e desktop.
3. Confirmar serviços, textos e regras de publicidade profissional.
4. Instalar e validar a mensuração em uma etapa separada, sem duplicar tags.
