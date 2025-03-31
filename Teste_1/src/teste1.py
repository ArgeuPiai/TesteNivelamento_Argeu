import requests
from bs4 import BeautifulSoup
import os

# 1. receber o site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 2. achar anexos I e II (tavez fazer uma função pra isso)
pdf_links = []
for link in soup.find_all('a'):
    href = link.get('href', '').lower()
    text = link.text.lower()

    # Verifica se é PDF e qual anexo
    if href.endswith('.pdf'):
        if 'anexo i.' in text:
            # Pega o nome original do arquivo da URL
            nome_arquivo = os.path.basename(href)
            pdf_links.append(('Anexo_I', link['href']))
        elif 'anexo ii.' in text:
            nome_arquivo = os.path.basename(href)
            pdf_links.append(('Anexo_II', link['href']))


# 3. salvar PDFs e compactar
for nome_arquivo, url_pdf in pdf_links:
    print(f"Baixando {nome_arquivo}...")

print("\n✅ baixados e compactados!")