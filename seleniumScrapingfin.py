from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os
from zipfile import ZipFile

# Inicializar o WebDriver com o webdriver_manager e opções
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navegar até o site inicial
driver.get("http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/getulio-vargas/discursos/")
time.sleep(2)

# Inicializar lista para guardar os links dos discursos
discourse_links = []

# Visitar cada link de ano e extrair os links dos discursos desse ano
years = ['1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1943', '1944', '1951', '1952', '1953']
for year in years:
    driver.get(f"http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/getulio-vargas/discursos/{year}")
    time.sleep(2)
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    discourse_links += [a['href'] for a in soup.select("a.summary.url")]

# Limitar para 35 links de discursos
discourse_links = discourse_links[:35]

# Pasta onde os PDFs serão baixados
download_folder = os.path.expanduser("~") + "/Downloads/"

# Loop para baixar os PDFs
for i, discourse_link in enumerate(discourse_links):
    driver.get(discourse_link)
    time.sleep(2)
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    pdf_link = soup.select_one("a[href*='.pdf']")['href']
    driver.get(pdf_link)
    
    time.sleep(5)
    
    try:
        latest_file = max([os.path.join(download_folder, filename) for filename in os.listdir(download_folder)], key=os.path.getctime)
        
        if latest_file.endswith('.pdf'):
            os.rename(latest_file, os.path.join(download_folder, f"Vargas_{i+1}.pdf"))
        elif latest_file.endswith('.crdownload'):
            print("Download ainda em progresso. Aguardando mais 10 segundos.")
            time.sleep(10)
    except Exception as e:
        print(f"Um erro ocorreu: {e}. Movendo para o próximo arquivo.")
        continue

# Criar um arquivo ZIP contendo apenas os PDFs baixados que têm "Vargas" em seus nomes
with ZipFile('discourses.zip', 'w') as myzip:
    for filename in os.listdir(download_folder):
        if filename.startswith("Vargas") and filename.endswith(".pdf"):
            myzip.write(os.path.join(download_folder, filename), filename)

# Fechar o driver
driver.quit()

