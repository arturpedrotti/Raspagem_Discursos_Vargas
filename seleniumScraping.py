from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os
from zipfile import ZipFile

# Inicializar o WebDriver com as opções necessárias
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Lista para armazenar os links dos PDFs
pdf_links = []

# Lista de anos que queremos pesquisar
anos = ['1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1943', '1944', '1951', '1952', '1953']

# URL inicial da página de discursos
initial_url = "http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/getulio-vargas/discursos/"

# Loop para acessar cada ano e coletar os PDFs
for ano in anos:
    # URL completa para o ano específico
    ano_url = initial_url + ano
    driver.get(ano_url)
    time.sleep(2)
    
    # Encontrar o número de PDFs neste ano
    soup = BeautifulSoup(driver.page_source, 'lxml')
    num_pdfs = len(soup.select("a.summary.url"))

    # Montar a URL do PDF e adicioná-la à lista
    for i in range(1, num_pdfs+1):
        pdf_url = f"{ano_url}/{str(i).zfill(2)}.pdf/view"
        pdf_links.append(pdf_url)

# Fazer o download de cada PDF na lista
for pdf_link in pdf_links:
    driver.get(pdf_link)
    time.sleep(2)

# Pasta de Downloads para zipar os arquivos posteriormente
download_folder = os.path.expanduser("~") + "/Downloads/"

# Criar um zip com todos os PDFs baixados
with ZipFile('discursos.zip', 'w') as myzip:
    for root, _, files in os.walk(download_folder):
        for file in files:
            if file.endswith(".pdf"):
                myzip.write(os.path.join(root, file), file)

# Fechar o WebDriver
driver.quit()

