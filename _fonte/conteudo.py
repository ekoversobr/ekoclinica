# Conteúdo do site da Eko Clínica.
# Edite aqui e rode `python3 _fonte/gerar_site.py` na raiz do repositório.

CLINICA = {
    "nome": "Eko Clínica",
    "whatsapp": "5583996809052",
    "telefone_exibicao": "(83) 99680-9052",
    "rua": "Rua Pedro Alves Sabino, 13",
    "bairro": "Mangabeira",
    "cidade": "João Pessoa",
    "uf": "PB",
    "cep": "58059-126",
    "rt_nome": "Dra. Caroline Chaves",
    "rt_cargo": "Cirurgiã-dentista",
    "rt_cro": "CRO-PB 6742",
    "horario_curto": "Seg a sex, 8h às 18h · Sáb, 9h às 12h",
    "url_base": "https://ekoversobr.github.io/ekoclinica/",
    "gtm": "GTM-N7R9G9RZ",
}

TRATAMENTOS = [
    {"slug": "sedacao-consciente", "nome": "Sedação consciente", "servico_msg": "sedação consciente",
     "h1": "Sedação consciente em Mangabeira",
     "sub": "Para quem tem medo de dentista: você fica relaxado e acordado durante o tratamento.",
     "description": "Sedação consciente em Mangabeira, João Pessoa. Agende sua avaliação na Eko Clínica pelo WhatsApp."},
    {"slug": "implantes-dentarios", "nome": "Implantes dentários", "servico_msg": "implante dentário",
     "h1": "Implante dentário em Mangabeira",
     "sub": "Reponha dentes perdidos com uma solução fixa. O plano e o orçamento saem na avaliação.",
     "description": "Implante dentário em Mangabeira, João Pessoa. Agende sua avaliação na Eko Clínica pelo WhatsApp."},
    {"slug": "tratamento-de-canal", "nome": "Tratamento de canal", "servico_msg": "tratamento de canal",
     "h1": "Tratamento de canal em Mangabeira",
     "sub": "Trate o dente por dentro e mantenha o seu dente natural.",
     "description": "Tratamento de canal em Mangabeira, João Pessoa. Agende sua avaliação na Eko Clínica pelo WhatsApp."},
    {"slug": "extracao-de-siso", "nome": "Extração de siso", "servico_msg": "extração de siso",
     "h1": "Extração de siso em Mangabeira",
     "sub": "Siso doendo ou sem espaço para nascer? Com opção de sedação consciente.",
     "description": "Extração de siso em Mangabeira, João Pessoa, com opção de sedação consciente. Agende pelo WhatsApp."},
    {"slug": "facetas-em-resina", "nome": "Facetas em resina", "servico_msg": "facetas em resina",
     "h1": "Facetas em resina em Mangabeira",
     "sub": "Ajuste cor, formato e pequenos espaços dos dentes da frente.",
     "description": "Facetas em resina em Mangabeira, João Pessoa. Agende sua avaliação na Eko Clínica pelo WhatsApp."},
]

# Mensagem dos botões da página principal (o site acrescenta o código de atendimento no fim).
MSG_HOME = ("Olá, tudo bem? Cliquei no anúncio da Eko Clínica no Google, fui ao site e cliquei "
            "no botão do WhatsApp e gostaria de mais informações.")

# Endereços antigos que passam a redirecionar para as páginas novas.
REDIRECIONAMENTOS = {
    "campanhas": "",
    "campanhas/nova": "",
    "campanhas/sedacao-consciente": "sedacao-consciente/",
    "campanhas/implantes-dentarios": "implantes-dentarios/",
    "campanhas/facetas-em-resina": "facetas-em-resina/",
    "campanhas/aparelhos-dentarios": "",
    "campanhas/limpeza-e-clareamento": "",
}
