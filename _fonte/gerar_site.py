#!/usr/bin/env python3
"""Gera o site estático da Eko Clínica a partir de _fonte/conteudo.py.

Uso, na raiz do repositório:
    python3 _fonte/gerar_site.py
"""
import html
import json
import os
import sys
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "_fonte"))
from conteudo import CLINICA as C, TRATAMENTOS, REDIRECIONAMENTOS  # noqa: E402

E = html.escape
POR_SLUG = {t["slug"]: t for t in TRATAMENTOS}
ENDERECO = f'{C["rua"]}, {C["bairro"]}, {C["cidade"]} - {C["uf"]}, CEP {C["cep"]}'
MAPA = "https://www.google.com/maps/search/?api=1&query=" + quote(
    f'{C["rua"]}, {C["bairro"]}, {C["cidade"]} - {C["uf"]}, {C["cep"]}')

ICONE_CHAT = ('<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" '
              'd="M12 3C6.5 3 2 6.9 2 11.7c0 2.4 1.1 4.6 3 6.2L4.2 21l3.7-1.6c1.3.4 2.7.6 4.1.6 5.5 0 10-3.9 '
              '10-8.7S17.5 3 12 3zm-4 9.9a1.2 1.2 0 1 1 0-2.4 1.2 1.2 0 0 1 0 2.4zm4 0a1.2 1.2 0 1 1 0-2.4 1.2 1.2 0 0 1 '
              '0 2.4zm4 0a1.2 1.2 0 1 1 0-2.4 1.2 1.2 0 0 1 0 2.4z"/></svg>')
ICONE_PIN = ('<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" '
             'd="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>')
ICONE_RELOGIO = ('<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" '
                 'd="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.4 3.2 1.9-.8 1.3L11 13V7h2z"/></svg>')


def msg_whatsapp(servico):
    if servico:
        return f"Olá! Vim pelo site da Eko Clínica e gostaria de informações sobre {servico}."
    return "Olá! Vim pelo site da Eko Clínica e gostaria de agendar uma avaliação."


def botao_wa(texto, servico, classe="btn btn-wa"):
    href = f'https://wa.me/{C["whatsapp"]}?text=' + quote(msg_whatsapp(servico))
    return (f'<a class="{classe}" href="{href}" target="_blank" rel="noopener" data-wa '
            f'data-servico="{E(servico or "avaliação")}">{ICONE_CHAT}<span>{E(texto)}</span></a>')


def cabeca(titulo, descricao, caminho, prefixo, jsonld=None, noindex=False):
    canonical = C["url_base"] + caminho
    ld = ""
    if jsonld:
        ld = '<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False) + "</script>\n"
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
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
{robots}<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0149ad">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(titulo)}">
<meta property="og:description" content="{E(descricao)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{C["url_base"]}assets/logo-eko-clinica.png">
<meta property="og:locale" content="pt_BR">
<link rel="icon" href="{prefixo}assets/favicon-64.png" sizes="64x64">
<link rel="apple-touch-icon" href="{prefixo}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{prefixo}assets/site.css">
{ld}<script src="{prefixo}assets/site.js" defer></script>
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={C["gtm"]}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""


def topo(prefixo, servico):
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
    {botao_wa("WhatsApp", servico, "btn btn-wa btn-sm")}
  </div>
</header>
"""


def bloco_local(servico):
    return f"""<section class="secao local" id="onde-estamos" aria-labelledby="onde-titulo">
  <div class="in grade-2">
    <div>
      <h2 id="onde-titulo">Onde estamos</h2>
      <p class="info">{ICONE_PIN}<span>{E(C["rua"])}<br>{E(C["bairro"])}, {E(C["cidade"])} - {E(C["uf"])}<br>CEP {E(C["cep"])}</span></p>
      <p class="info">{ICONE_RELOGIO}<span>Segunda a sexta, 8h às 18h<br>Sábado, 9h às 12h<br>Atendimento com horário agendado</span></p>
      <p class="acoes">{botao_wa("Agendar pelo WhatsApp", servico)}
        <a class="btn btn-claro" href="{MAPA}" target="_blank" rel="noopener">Ver no mapa</a></p>
    </div>
    <div class="cartao-rt">
      <p class="rotulo">Responsável técnica</p>
      <p class="rt-nome">{E(C["rt_nome"])}</p>
      <p>{E(C["rt_cargo"])} · {E(C["rt_cro"])}</p>
    </div>
  </div>
</section>
"""


def rodape(prefixo, servico):
    return f"""<footer class="rodape">
  <div class="in">
    <p><strong>Eko Clínica</strong> · {E(ENDERECO)}</p>
    <p>Responsável técnica: {E(C["rt_nome"])}, {E(C["rt_cargo"].lower())}, {E(C["rt_cro"])}</p>
    <p>WhatsApp {E(C["telefone_exibicao"])} · {E(C["horario_curto"])}</p>
    <p><a href="{prefixo}privacidade/">Política de privacidade</a></p>
  </div>
</footer>
<div class="barra-fixa">{botao_wa("Agendar avaliação pelo WhatsApp", servico, "btn btn-wa btn-largo")}</div>
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
        <p>{E(t['card'])}</p>
        <span class="mais">Saiba mais →</span>
      </a>""" for t in TRATAMENTOS)
    corpo = f"""{topo("", None)}<main>
<section class="hero">
  <div class="in">
    <p class="selo">Mangabeira · João Pessoa</p>
    <h1>Dentista em Mangabeira, João Pessoa</h1>
    <p class="lead">Sedação consciente, implantes, tratamento de canal, extração de siso e facetas em resina. Fale com a equipe pelo WhatsApp e agende sua avaliação.</p>
    <p class="acoes">{botao_wa("Agendar avaliação pelo WhatsApp", None)}</p>
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
    <p class="acoes"><a class="btn btn-claro" href="sedacao-consciente/">Conhecer a sedação consciente</a></p>
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
{bloco_local(None)}</main>
"""
    pagina = cabeca(
        "Dentista em Mangabeira, João Pessoa | Eko Clínica",
        "Dentista em Mangabeira, João Pessoa: sedação consciente, implantes, tratamento de canal, extração de siso e facetas em resina. Agende sua avaliação pelo WhatsApp.",
        "", "", jsonld_clinica()) + corpo + rodape("", None)
    escrever("index.html", pagina)


def pagina_tratamento(t):
    p = "../"
    itens = "\n".join(f"      <li>{E(i)}</li>" for i in t["para_quem"])
    nota = f'\n    <p class="nota">{E(t["para_quem_nota"])}</p>' if t.get("para_quem_nota") else ""
    etapas = "\n".join(f"      <li><strong>{E(a)}</strong><span>{E(b)}</span></li>" for a, b in t["etapas"])
    faq = "\n".join(f"""    <details>
      <summary>{E(q)}</summary>
      <p>{E(r)}</p>
    </details>""" for q, r in t["faq"])
    rel = "\n".join(
        f"""      <a class="card-trat" href="{p}{s}/"><h3>{E(POR_SLUG[s]['nome'])}</h3><p>{E(POR_SLUG[s]['card'])}</p><span class="mais">Saiba mais →</span></a>"""
        for s in t["relacionados"])
    ld_faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in t["faq"]],
    }
    corpo = f"""{topo(p, t["servico_msg"])}<main>
<section class="hero hero-trat">
  <div class="in">
    <p class="selo"><a href="{p}">Eko Clínica</a> · {E(t["nome"])}</p>
    <h1>{E(t["h1"])}</h1>
    <p class="lead">{E(t["intro"])}</p>
    <p class="acoes">{botao_wa("Agendar avaliação pelo WhatsApp", t["servico_msg"])}</p>
    <ul class="fatos">
      <li>{ICONE_PIN}<span>{E(C["rua"])}, {E(C["bairro"])}</span></li>
      <li>{ICONE_RELOGIO}<span>{E(C["horario_curto"])}</span></li>
    </ul>
  </div>
</section>
<section class="secao" aria-labelledby="pq-titulo">
  <div class="in">
    <h2 id="pq-titulo">{E(t["para_quem_titulo"])}</h2>
    <ul class="lista">
{itens}
    </ul>{nota}
  </div>
</section>
<section class="secao destaque" aria-labelledby="etapas-titulo">
  <div class="in">
    <h2 id="etapas-titulo">Como funciona</h2>
    <ol class="etapas">
{etapas}
    </ol>
  </div>
</section>
<section class="secao" aria-labelledby="faq-titulo">
  <div class="in estreito">
    <h2 id="faq-titulo">Perguntas frequentes</h2>
{faq}
    <p class="acoes">{botao_wa("Tirar dúvidas pelo WhatsApp", t["servico_msg"])}</p>
  </div>
</section>
<section class="secao" aria-labelledby="rel-titulo">
  <div class="in">
    <h2 id="rel-titulo">Veja também</h2>
    <div class="grade-cards grade-2c">
{rel}
    </div>
  </div>
</section>
{bloco_local(t["servico_msg"])}</main>
"""
    pagina = cabeca(t["title"], t["description"], t["slug"] + "/", p, [jsonld_clinica(), ld_faq]) \
        + corpo + rodape(p, t["servico_msg"])
    escrever(f'{t["slug"]}/index.html', pagina)


def pagina_privacidade():
    p = "../"
    corpo = f"""{topo(p, None)}<main>
<section class="secao">
  <div class="in estreito texto">
    <h1>Política de privacidade</h1>
    <p>Última atualização: 17 de novembro de 2026.</p>
    <p>Esta política explica como o site da Eko Clínica ({E(ENDERECO)}) trata informações de quem o visita, conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).</p>
    <h2>O que coletamos neste site</h2>
    <p>O site não tem formulários e não pede nome, telefone, e-mail ou informações de saúde. O contato acontece pelo WhatsApp, quando você decide enviar a mensagem.</p>
    <p>Quando você chega ao site por um anúncio do Google, o endereço da página traz um identificador do clique, criado pelo Google. O site gera um código de atendimento (por exemplo, EK7F3K), guarda esse código no seu navegador e o inclui na mensagem do WhatsApp. O código e o identificador do clique são registrados em uma planilha de acesso restrito da clínica e da agência que gerencia os anúncios, sem nenhum dado pessoal.</p>
    <h2>Para que usamos</h2>
    <p>Para saber quais anúncios trazem pacientes e informar ao Google Ads, de forma agregada, quais cliques resultaram em agendamento ou tratamento. Isso permite investir melhor e mostrar menos anúncios irrelevantes.</p>
    <h2>Cookies e ferramentas de terceiros</h2>
    <p>O site usa o Google Tag Manager e as ferramentas de medição do Google Ads, que podem gravar cookies no seu navegador. Você pode apagar ou bloquear cookies nas configurações do navegador.</p>
    <h2>Mensagens pelo WhatsApp</h2>
    <p>As conversas pelo WhatsApp são usadas apenas para atendimento e agendamento. Não envie exames ou detalhes de saúde pelo site. Informações clínicas são tratadas na consulta, com sigilo profissional.</p>
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
                    "privacidade/", p) + corpo + rodape(p, None)
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
    from urllib.parse import urlparse
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
        pagina_tratamento(t)
    pagina_privacidade()
    redirecionamentos()
    pagina_404()
    sitemap()
    print("Site gerado.")
