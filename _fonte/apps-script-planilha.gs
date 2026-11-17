/**
 * Recebe do site o par código de atendimento + GCLID e grava na aba
 * "Cliques do site" da planilha
 * "Ekoverso | Eko Clínica – Controle de Leads e Vendas (Google Ads)".
 *
 * Como instalar (uma vez):
 * 1. Abra a planilha > Extensões > Apps Script.
 * 2. Apague o conteúdo do arquivo Code.gs e cole este código. Salve.
 * 3. Selecione a função "autorizar" e clique em Executar (autoriza o acesso).
 * 4. Implantar > Nova implantação > tipo "App da Web".
 *    Executar como: Eu. Quem pode acessar: Qualquer pessoa.
 * 5. Copie a URL que termina em /exec.
 * 6. Cole essa URL em ENDPOINT, no arquivo assets/site.js do site.
 *
 * O site envia só o código (ex.: EK7F3K), o GCLID e a página. Nenhum dado pessoal.
 */
const PLANILHA_ID = '1pNQRTggS2l1uw3QvTLhU5fSUw8KEKbcTstrzbV0KpFw';
const ABA = 'Cliques do site';

function doPost(e) {
  const lock = LockService.getScriptLock();
  try {
    const d = JSON.parse(e.postData.contents);
    const codigo = String(d.codigo || '');
    const gclid = String(d.gclid || '').slice(0, 300);
    const pagina = String(d.pagina || '').slice(0, 120);
    if (!/^EK[A-Z0-9]{4}$/.test(codigo) || !gclid) return resposta('ignorado');

    lock.waitLock(5000);
    const aba = SpreadsheetApp.openById(PLANILHA_ID).getSheetByName(ABA);
    const ultima = aba.getLastRow();
    if (ultima > 1) {
      const codigos = aba.getRange(2, 1, ultima - 1, 1).getValues().flat();
      if (codigos.indexOf(codigo) !== -1) return resposta('ok');
    }
    aba.appendRow([codigo, gclid, new Date(), pagina]);
    return resposta('ok');
  } catch (err) {
    return resposta('erro');
  } finally {
    try { lock.releaseLock(); } catch (e2) {}
  }
}

// Rode esta função uma vez pelo editor (botão Executar) para autorizar o acesso à planilha.
function autorizar() {
  const aba = SpreadsheetApp.openById(PLANILHA_ID).getSheetByName(ABA);
  Logger.log('Acesso OK: ' + aba.getName());
}

function resposta(texto) {
  return ContentService.createTextOutput(texto);
}
