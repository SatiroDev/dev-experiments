import pdfplumber

# caminho onde se encontra o pdf
caminho = "./read-of-pdf/test.pdf"

# abre o pdf
with pdfplumber.open(caminho) as pdf:
    texto = ""
    # percorre todas as páginas do pdf
    for pag in pdf.pages:
        texto += pag.extract_text() or ""

print(texto)

