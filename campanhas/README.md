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

## Mensuração — estado atual

A landing principal `campanhas/index.html` agora contém a instalação do Google Tag Manager:
- Container: `GTM-KKX8Z44S`
- Conta GTM: `Eko Clínica — Landing Ads`
- Container: `Eko Clínica | Tracking`
- Conta Google Ads de destino: `AW-17620094050`

**Importante:** o container GTM foi criado do zero e seu snippet foi instalado na landing principal. Ainda não foram configuradas/publicadas a Google tag, as tags de conversão, os acionadores ou eventos. A instalação precisa ser validada no Tag Assistant antes de avançar.

Não instalar uma segunda cópia do GTM nem inserir a tag diretamente no HTML. A configuração de mensuração será administrada pelo container GTM.

O formulário abre o WhatsApp com uma mensagem pré-preenchida. Um evento de clique mede apenas a intenção de iniciar uma conversa; não confirma que a mensagem foi enviada, que houve resposta, agendamento, comparecimento ou venda.

## Privacidade
O nome e o assunto são usados somente para compor a mensagem no WhatsApp. O site não grava esses campos em banco de dados. Não informe diagnóstico, exames ou outros dados clínicos neste formulário. Não enviar dados de saúde identificáveis para ferramentas de anúncios ou analytics.

## Antes de anunciar
1. Confirmar com a clínica o número de WhatsApp configurado em `assets/landing.js`.
2. Testar o formulário em celular e desktop.
3. Validar a instalação do container `GTM-KKX8Z44S` no Tag Assistant.
4. Configurar tags, acionadores e conversões dentro do GTM; testar antes de publicar.
5. Confirmar serviços, textos e regras de publicidade profissional.
