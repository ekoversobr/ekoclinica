# Eko Clínica — site independente (versão inicial)

Este é um site estático em HTML, CSS e JavaScript. O objetivo é dar à equipe um ponto de partida que possa ser editado sem WordPress, Elementor ou plugins.

## Arquivos
- `index.html` — conteúdo e estrutura
- `styles.css` — aparência e responsividade
- `script.js` — menu móvel e formulário que prepara mensagem para WhatsApp

## Importante antes de publicar
1. Confirme que o número `5583996809052` é o WhatsApp correto da Eko Clínica.
2. Revise os textos, atendimentos disponíveis, endereço, horários, responsáveis técnicos e política de privacidade.
3. O formulário **não salva dados num banco**: ele abre o WhatsApp com uma mensagem pré-preenchida. A pessoa ainda precisa revisar e enviar.
4. O botão flutuante abre diretamente o WhatsApp.
5. Este pacote não inclui rastreamento do Google Ads/Google Tag Manager. A mensuração deve ser adicionada e testada depois, quando o domínio e a estratégia de publicação estiverem definidos.
6. Não publique informações clínicas sensíveis no formulário.
7. A publicação em `ekoclinica.com.br` exige acesso ao DNS/domínio e à plataforma de hospedagem, ou ajuda de quem controla esses acessos. Este pacote não altera o site atual.

## Como testar localmente
Abra `index.html` num navegador moderno. Para testar o formulário, use um dispositivo com WhatsApp Web/app disponível.

## Liberdade e portabilidade
O site usa arquivos abertos e pode ser hospedado em qualquer serviço que aceite arquivos estáticos. O conteúdo não depende de WordPress ou Elementor. A fonte tipográfica Inter é carregada do Google Fonts; se quiser evitar essa dependência externa, remova a linha `@import` de `styles.css` e o site usará fontes locais do sistema.
