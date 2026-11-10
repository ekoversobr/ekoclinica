# Eko Clínica — site independente

Site institucional e páginas de campanha em HTML, CSS e JavaScript, sem WordPress, Elementor ou dependências de CMS.

## Site institucional
- `index.html` — página principal.
- `styles.css` — estilos.
- `script.js` — interações e formulário WhatsApp.

## Landing pages de campanhas
A pasta `campanhas/` contém a landing principal e páginas específicas por serviço. Os arquivos compartilhados estão em `campanhas/assets/`.

- `campanhas/index.html` — formulário único com nome e assunto.
- `campanhas/sedacao-consciente/`
- `campanhas/implantes-dentarios/`
- `campanhas/aparelhos-dentarios/`
- `campanhas/facetas-em-resina/`
- `campanhas/limpeza-e-clareamento/`

A landing principal de campanhas está deliberadamente sem Google tag, Google Tag Manager, GA4, pixels e eventos `dataLayer`. A mensuração será implantada separadamente após a confirmação da arquitetura correta e dos testes de disparo e deduplicação.

## WhatsApp e dados
O formulário abre o WhatsApp com uma mensagem pré-preenchida. A pessoa precisa revisar e enviar a mensagem. O site não salva os dados em banco nem os envia a plataformas de analytics. O clique/encaminhamento não comprova conversa, agendamento, comparecimento ou venda.

Não solicitar ou incluir diagnóstico, exames ou informações clínicas sensíveis em formulários, URLs ou ferramentas de publicidade.

## Antes de anunciar
1. Confirmar com a clínica o número configurado no JavaScript.
2. Revisar textos, serviços, dados institucionais e política de privacidade.
3. Testar em celular e desktop.
4. Implantar mensuração em etapa separada, verificando cada evento e evitando tags duplicadas.
5. Validar textos e regras de publicidade profissional aplicáveis.

## Teste local
Abra `index.html` em um navegador moderno ou sirva os arquivos por um servidor estático local.
