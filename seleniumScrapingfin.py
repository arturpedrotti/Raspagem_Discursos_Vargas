from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os
from zipfile import ZipFile

# Inicializando o WebDriver. Estou usando o Chrome aqui.
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Lista vazia para guardar os links dos discursos.
discourse_links = []

# Esses são os anos que eu quero verificar no site. Vou visitar cada um deles.
years = ['1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1943', '1944', '1951', '1952', '1953']
for year in years:
    # Acessando a página do ano específico.
    driver.get(f"http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/getulio-vargas/discursos/{year}")
    
    # Esperando a página carregar.
    time.sleep(2)
    
    # Usando o BeautifulSoup para fazer o parsing da página.
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    # Adicionando os links dos discursos deste ano na nossa lista.
    discourse_links += [a['href'] for a in soup.select("a.summary.url")]

# Eu só quero 35 discursos, então vou pegar só os 35 primeiros links.
discourse_links = discourse_links[:35]

# Pasta onde os PDFs vão ser baixados.
download_folder = os.path.expanduser("~") + "/Downloads/"

# Vamos agora baixar cada um dos PDFs.
for i, discourse_link in enumerate(discourse_links):
    driver.get(discourse_link)
    
    # Mais uma vez, dando tempo para a página carregar.
    time.sleep(2)
    
    # Parsing da página.
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    # Pegando o link do PDF.
    pdf_link = soup.select_one("a[href*='.pdf']")['href']
    driver.get(pdf_link)
    
    # Esperando um pouco mais aqui porque estamos baixando o PDF.
    time.sleep(5)
    
    # Renomeando o PDF mais recente para incluir "Vargas" e o número.
    latest_file = max([os.path.join(download_folder, filename) for filename in os.listdir(download_folder)], key=os.path.getctime)
    os.rename(latest_file, os.path.join(download_folder, f"Vargas_{i+1}.pdf"))

# Agora vamos compactar todos os PDFs que têm "Vargas" no nome em um arquivo zip.
with ZipFile('discourses.zip', 'w') as myzip:
    for filename in os.listdir(download_folder):
        if filename.startswith("Vargas") and filename.endswith(".pdf"):
            myzip.write(os.path.join(download_folder, filename), filename)

# Finalmente, fechando o navegador.
driver.quit()

