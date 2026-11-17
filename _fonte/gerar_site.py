#!/usr/bin/env python3
"""Gera o site estático da Eko Clínica a partir de _fonte/conteudo.py.

Uso, na raiz do repositório:
    python3 _fonte/gerar_site.py
"""
import html
import json
import os
import sys
from urllib.parse import quote, urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "_fonte"))
from conteudo import CLINICA as C, TRATAMENTOS, REDIRECIONAMENTOS, MSG_HOME  # noqa: E402

E = html.escape


def _versao(arquivo):
    import hashlib
    with open(os.path.join(RAIZ, "assets", arquivo), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


# Versão nos links de CSS/JS para o navegador não usar arquivo antigo do cache.
V_CSS = _versao("site.css")
V_JS = _versao("site.js")
ENDERECO = f'{C["rua"]}, {C["bairro"]}, {C["cidade"]} - {C["uf"]}, CEP {C["cep"]}'
MAPA = "https://www.google.com/maps/search/?api=1&query=" + quote(
    f'{C["rua"]}, {C["bairro"]}, {C["cidade"]} - {C["uf"]}, {C["cep"]}')

ICONE_PIN = ('<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" '
             'd="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>')
ICONE_RELOGIO = ('<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" '
                 'd="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.4 3.2 1.9-.8 1.3L11 13V7h2z"/></svg>')


def icone_wa(prefixo, tam=20):
    # Ícone oficial do WhatsApp (Brand Resource Center), versão branca.
    return (f'<img class="ico-wa" src="{prefixo}assets/whatsapp-glyph-white.svg" alt="" '
            f'width="{tam}" height="{tam}">')


def link_wa(mensagem):
    return f'https://wa.me/{C["whatsapp"]}?text=' + quote(mensagem)


def botao_wa(texto, classe="btn btn-wa", prefixo=""):
    return (f'<a class="{classe}" href="{link_wa(MSG_HOME)}" target="_blank" rel="noopener" data-wa '
            f'data-servico="pagina principal">{icone_wa(prefixo, 22)}<span>{E(texto)}</span></a>')


def botao_flutuante(prefixo=""):
    return (f'<a class="wa-flutuante" href="{link_wa(MSG_HOME)}" target="_blank" rel="noopener" data-wa '
            f'data-servico="pagina principal" aria-label="Falar com a Eko Clínica pelo WhatsApp">'
            f'{icone_wa(prefixo, 34)}</a>')


def cabeca(titulo, descricao, caminho, prefixo, jsonld=None, classe_body=""):
    canonical = C["url_base"] + caminho
    ld = ""
    if jsonld:
        ld = '<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False) + "</script>\n"
    body = f' class="{classe_body}"' if classe_body else ""
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{C["gtm"]}');</script>
<!-- End Google Tag Manager -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(titulo)}</title>
<meta name="description" content="{E(descricao)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0149ad">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(titulo)}">
<meta property="og:description" content="{E(descricao)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{C["url_base"]}assets/logo-eko-clinica.png">
<meta property="og:locale" content="pt_BR">
<link rel="icon" href="{prefixo}assets/favicon-64.png" sizes="64x64">
<link rel="apple-touch-icon" href="{prefixo}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{prefixo}assets/site.css?v={V_CSS}">
{ld}<script src="{prefixo}assets/site.js?v={V_JS}" defer></script>
</head>
<body{body}>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={C["gtm"]}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""


def topo(prefixo):
    return f"""<header class="topo">
  <div class="topo-in">
    <a class="marca" href="{prefixo or './'}" aria-label="Eko Clínica, página inicial">
      <img src="{prefixo}assets/logo-eko-clinica.png" alt="" width="44" height="44">
      <span><strong>Eko Clínica</strong><small>Odontologia em Mangabeira</small></span>
    </a>
    <nav class="menu" aria-label="Menu">
      <a href="{prefixo}#tratamentos">Tratamentos</a>
      <a href="{prefixo}#onde-estamos">Onde estamos</a>
    </nav>
  </div>
</header>
"""


def rodape(prefixo):
    return f"""<footer class="rodape">
  <div class="in">
    <p><strong>Eko Clínica</strong> · {E(ENDERECO)}</p>
    <p>Responsável técnica: {E(C["rt_nome"])}, {E(C["rt_cargo"].lower())}, {E(C["rt_cro"])}</p>
    <p>WhatsApp {E(C["telefone_exibicao"])} · {E(C["horario_curto"])}</p>
    <p><a href="{prefixo}privacidade/">Política de privacidade</a></p>
  </div>
</footer>
{botao_flutuante(prefixo)}
</body>
</html>
"""


def jsonld_clinica():
    return {
        "@context": "https://schema.org",
        "@type": "Dentist",
        "name": "Eko Clínica",
        "url": C["url_base"],
        "image": C["url_base"] + "assets/logo-eko-clinica.png",
        "telephone": "+" + C["whatsapp"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": C["rua"],
            "addressLocality": C["cidade"],
            "addressRegion": C["uf"],
            "postalCode": C["cep"],
            "addressCountry": "BR",
        },
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
             "opens": "08:00", "closes": "18:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday",
             "opens": "09:00", "closes": "12:00"},
        ],
    }


def escrever(caminho_rel, conteudo):
    destino = os.path.join(RAIZ, caminho_rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(conteudo)


def pagina_inicial():
    cards = "\n".join(
        f"""      <a class="card-trat" href="{t['slug']}/">
        <h3>{E(t['nome'])}</h3>
        <p>{E(t['sub'])}</p>
        <span class="mais">Agendar avaliação →</span>
      </a>""" for t in TRATAMENTOS)
    corpo = f"""{topo("")}<main>
<section class="hero">
  <div class="in">
    <p class="selo">Mangabeira · João Pessoa</p>
    <h1>Dentista em Mangabeira, João Pessoa</h1>
    <p class="lead">Sedação consciente, implantes, tratamento de canal, extração de siso e facetas em resina. Fale com a equipe pelo WhatsApp e agende sua avaliação.</p>
    <p class="acoes">{botao_wa("Agendar avaliação pelo WhatsApp")}</p>
    <ul class="fatos">
      <li>{ICONE_PIN}<span>{E(C["rua"])}, {E(C["bairro"])}</span></li>
      <li>{ICONE_RELOGIO}<span>{E(C["horario_curto"])}</span></li>
    </ul>
  </div>
</section>
<section class="secao" id="tratamentos" aria-labelledby="trat-titulo">
  <div class="in">
    <h2 id="trat-titulo">Tratamentos</h2>
    <div class="grade-cards">
{cards}
    </div>
  </div>
</section>
<section class="secao destaque" aria-labelledby="medo-titulo">
  <div class="in grade-2">
    <div>
      <h2 id="medo-titulo">Tem medo de dentista?</h2>
      <p>Com a sedação consciente, você fica relaxado e acordado durante o tratamento. Ela pode ser usada em procedimentos como extração de siso, canal e implantes, conforme avaliação.</p>
    </div>
    <p class="acoes"><a class="btn btn-claro" href="sedacao-consciente/">Agendar com sedação consciente</a></p>
  </div>
</section>
<section class="secao" aria-labelledby="como-titulo">
  <div class="in">
    <h2 id="como-titulo">Como agendar</h2>
    <ol class="etapas">
      <li><strong>Chame no WhatsApp</strong><span>Conte qual tratamento procura. A equipe responde no horário de atendimento.</span></li>
      <li><strong>Marque sua avaliação</strong><span>A equipe encontra o melhor horário para você.</span></li>
      <li><strong>Converse com a dentista</strong><span>Na avaliação, a dentista explica as opções e o plano de tratamento para o seu caso.</span></li>
    </ol>
  </div>
</section>
<section class="secao local" id="onde-estamos" aria-labelledby="onde-titulo">
  <div class="in grade-2">
    <div>
      <h2 id="onde-titulo">Onde estamos</h2>
      <p class="info">{ICONE_PIN}<span>{E(C["rua"])}<br>{E(C["bairro"])}, {E(C["cidade"])} - {E(C["uf"])}<br>CEP {E(C["cep"])}</span></p>
      <p class="info">{ICONE_RELOGIO}<span>Segunda a sexta, 8h às 18h<br>Sábado, 9h às 12h<br>Atendimento com horário agendado</span></p>
      <p class="acoes">{botao_wa("Agendar pelo WhatsApp")}
        <a class="btn btn-claro" href="{MAPA}" target="_blank" rel="noopener">Ver no mapa</a></p>
    </div>
    <div class="cartao-rt">
      <p class="rotulo">Responsável técnica</p>
      <p class="rt-nome">{E(C["rt_nome"])}</p>
      <p>{E(C["rt_cargo"])} · {E(C["rt_cro"])}</p>
    </div>
  </div>
</section>
</main>
"""
    pagina = cabeca(
        "Dentista em Mangabeira, João Pessoa | Eko Clínica",
        "Dentista em Mangabeira, João Pessoa: sedação consciente, implantes, tratamento de canal, extração de siso e facetas em resina. Agende sua avaliação pelo WhatsApp.",
        "", "", jsonld_clinica()) + corpo + rodape("")
    escrever("index.html", pagina)


def pagina_servico(t):
    """Página enxuta de serviço: um cartão com nome, procedimento e botão para o WhatsApp."""
    p = "../"
    opcoes = "\n".join(
        f'          <option value="{E(x["servico_msg"])}"{" selected" if x["slug"] == t["slug"] else ""}>{E(x["nome"])}</option>'
        for x in TRATAMENTOS)
    corpo = f"""<main class="lp">
  <section class="lp-card" aria-labelledby="lp-titulo">
    <a class="lp-logo" href="{p}" aria-label="Eko Clínica, página inicial">
      <img src="{p}assets/logo-eko-clinica.png" alt="Eko Clínica, Centro de Saúde" width="88" height="88">
    </a>
    <h1 id="lp-titulo">{E(t["h1"])}</h1>
    <p class="lp-sub">{E(t["sub"])}</p>
    <form id="form-agendar" novalidate>
      <label for="nome">Seu nome</label>
      <input id="nome" name="nome" type="text" autocomplete="given-name" maxlength="60" placeholder="Como podemos chamar você?" required>
      <label for="procedimento">Procedimento</label>
      <select id="procedimento" name="procedimento">
{opcoes}
          <option value="uma avaliação">Outro / avaliação geral</option>
      </select>
      <button type="submit" class="btn btn-wa btn-largo">{icone_wa(p, 24)}<span>Agendar pelo WhatsApp</span></button>
      <p id="form-aviso" class="lp-aviso" role="status" aria-live="polite"></p>
    </form>
    <a id="wa-envio" class="oculto" href="https://wa.me/{C["whatsapp"]}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true">WhatsApp</a>
    <p class="lp-nota">O WhatsApp abre com a sua mensagem pronta para enviar.<br>{E(C["horario_curto"])}</p>
    <p class="lp-rodape">{E(C["rua"])}, {E(C["bairro"])}, {E(C["cidade"])} - {E(C["uf"])}<br>
      Responsável técnica: {E(C["rt_nome"])}, {E(C["rt_cro"])} · <a href="{p}privacidade/">Privacidade</a></p>
  </section>
</main>
</body>
</html>
"""
    pagina = cabeca(f'{t["h1"]}, João Pessoa | Eko Clínica', t["description"], t["slug"] + "/", p,
                    jsonld_clinica(), "pagina-lp") + corpo
    escrever(f'{t["slug"]}/index.html', pagina)


def pagina_privacidade():
    p = "../"
    corpo = f"""{topo(p)}<main>
<section class="secao">
  <div class="in estreito texto">
    <h1>Política de privacidade</h1>
    <p>Última atualização: 17 de novembro de 2026.</p>
    <p>Esta política explica como o site da Eko Clínica ({E(ENDERECO)}) trata informações de quem o visita, conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).</p>
    <h2>O que coletamos neste site</h2>
    <p>Nas páginas de agendamento, o nome e o procedimento que você informa servem apenas para montar a mensagem do WhatsApp. Eles não são gravados pelo site. O contato acontece pelo WhatsApp, quando você decide enviar a mensagem. Não informe dados de saúde no site.</p>
    <p>Quando você chega ao site por um anúncio do Google, o endereço da página traz um identificador do clique, criado pelo Google. O site gera um código de atendimento (por exemplo, EK7F3K), guarda esse código no seu navegador e o inclui na mensagem do WhatsApp. O código e o identificador do clique são registrados em uma planilha de acesso restrito da clínica e da agência que gerencia os anúncios, sem nome, telefone ou outros dados pessoais.</p>
    <h2>Para que usamos</h2>
    <p>Para saber quais anúncios trazem pacientes e informar ao Google Ads quais cliques resultaram em agendamento ou tratamento. Isso permite investir melhor e mostrar menos anúncios irrelevantes.</p>
    <h2>Cookies e ferramentas de terceiros</h2>
    <p>O site usa o Google Tag Manager e as ferramentas de medição do Google Ads, que podem gravar cookies no seu navegador. Você pode apagar ou bloquear cookies nas configurações do navegador.</p>
    <h2>Mensagens pelo WhatsApp</h2>
    <p>As conversas pelo WhatsApp são usadas para atendimento e agendamento. Informações clínicas são tratadas na consulta, com sigilo profissional.</p>
    <h2>Seus direitos</h2>
    <p>Você pode pedir acesso, correção ou exclusão dos seus dados pelo WhatsApp {E(C["telefone_exibicao"])}.</p>
    <h2>Responsável</h2>
    <p>Eko Clínica, {E(ENDERECO)}. Responsável técnica: {E(C["rt_nome"])}, {E(C["rt_cro"])}.</p>
  </div>
</section>
</main>
"""
    pagina = cabeca("Política de privacidade | Eko Clínica",
                    "Como o site da Eko Clínica trata as informações de quem o visita.",
                    "privacidade/", p) + corpo + rodape(p)
    escrever("privacidade/index.html", pagina)


def redirecionamentos():
    for antigo, novo in REDIRECIONAMENTOS.items():
        nivel = "../" * (antigo.count("/") + 1)
        destino = nivel + novo
        escrever(f"{antigo}/index.html", f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="robots" content="noindex">
<link rel="canonical" href="{C["url_base"]}{novo}">
<script>location.replace("{destino}" + location.search + location.hash);</script>
<meta http-equiv="refresh" content="0; url={destino}">
<title>Eko Clínica</title></head>
<body><p><a href="{destino}">Eko Clínica</a></p></body></html>
""")


def pagina_404():
    base = urlparse(C["url_base"]).path or "/"
    escrever("404.html", f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>Página não encontrada | Eko Clínica</title>
<link rel="stylesheet" href="{base}assets/site.css"></head>
<body><main class="secao"><div class="in estreito texto">
<h1>Página não encontrada</h1>
<p>Esse endereço não existe mais. <a href="{base}">Ir para a página inicial da Eko Clínica</a>.</p>
</div></main></body></html>
""")


def sitemap():
    urls = [C["url_base"]] + [C["url_base"] + t["slug"] + "/" for t in TRATAMENTOS] + [C["url_base"] + "privacidade/"]
    corpo = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    escrever("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{corpo}\n</urlset>\n')
    escrever("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {C['url_base']}sitemap.xml\n")


if __name__ == "__main__":
    pagina_inicial()
    for t in TRATAMENTOS:
        pagina_servico(t)
    pagina_privacidade()
    redirecionamentos()
    pagina_404()
    sitemap()
    print("Site gerado.")
