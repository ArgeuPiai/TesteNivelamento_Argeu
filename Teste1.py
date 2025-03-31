import requests
from bs4 import BeautifulSoup
import zipfile
import os

link_teste1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
resposta = requests.get(link_teste1)
print(resposta)
print(resposta.raise_for_status())

soup = BeautifulSoup(response.text, '')