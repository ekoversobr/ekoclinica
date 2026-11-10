# Eko Clínica — site independente

Site institucional e páginas de campanha em HTML, CSS e JavaScript, sem WordPress, Elementor ou dependências de CMS.

## Site institucional
- `index.html` — página principal.
- `styles.css` — estilos.
- `script.js` — interações e formulário WhatsApp.

## Landing pages de campanhas
- `campanhas/index.html` — landing simplificada anterior, mantida para referência.
- `campanhas/nova/` — nova landing de captação criada do zero, com nome, telefone, seleção do atendimento e prévia automática da mensagem para WhatsApp.
- `campanhas/sedacao-consciente/`
- `campanhas/implantes-dentarios/`
- `campanhas/aparelhos-dentarios/`
- `campanhas/facetas-em-resina/`
- `campanhas/limpeza-e-clareamento/`

## Nova landing
A versão nova fica em `campanhas/nova/` para ser testada sem substituir a URL antiga. Ela possui arquivos independentes de HTML, CSS e JavaScript e não inclui Google tag, GTM, GA4, pixels ou eventos `dataLayer`.

## WhatsApp, mensuração e privacidade
O formulário monta uma mensagem no navegador e abre o WhatsApp para o visitante revisar e enviar. Os campos não são armazenados em banco de dados nem enviados para analytics. O clique/encaminhamento não comprova mensagem enviada, conversa, agendamento, comparecimento ou venda.

A mensuração será implantada em etapa separada, usando um container exclusivo da Eko Clínica, após testar a landing e definir os eventos e as regras de deduplicação. Não instalar tags de clientes no template mestre.

Não solicitar ou incluir diagnóstico, exames ou informações clínicas sensíveis em formulários, URLs ou ferramentas de publicidade.

## Antes de anunciar
1. Confirmar com a clínica o número de WhatsApp configurado em `campanhas/nova/script.js`.
2. Revisar os serviços e os textos.
3. Testar o formulário em celular e desktop.
4. Implantar e validar GTM/Google Ads em etapa separada.
5. Validar textos e regras de publicidade profissional aplicáveis.

## Teste local
Abra o arquivo HTML por um servidor estático local ou publique pelo GitHub Pages.
