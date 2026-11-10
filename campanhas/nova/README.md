# Nova landing de captação — Eko Clínica

Esta versão foi criada separadamente em `campanhas/nova/` para permitir testes sem substituir a landing anterior.

## Arquivos
- `index.html`: estrutura e formulário.
- `style.css`: identidade visual responsiva.
- `script.js`: validação, prévia dinâmica e encaminhamento para WhatsApp.

## Campos
- Nome.
- Telefone com DDD.
- Atendimento desejado.
- Prévia automática da mensagem.

## Mensuração
Esta versão não contém Google tag, GTM, GA4, pixels ou eventos de analytics. A configuração de mensuração será feita em uma etapa posterior, com um container novo e exclusivo da Eko Clínica, depois de validar a página e o fluxo de WhatsApp.

## Privacidade
Os dados são usados no navegador apenas para montar a mensagem. Não são gravados em banco de dados nem enviados a analytics. O visitante revisa e decide enviar a mensagem pelo WhatsApp. O clique não comprova que a mensagem foi enviada ou que houve agendamento.

Não coletar diagnóstico, exames ou informações clínicas sensíveis neste formulário.

## Configuração
Antes de anunciar, confirmar o número de WhatsApp definido em `script.js`, testar em celular e desktop e revisar os serviços listados com a clínica.
