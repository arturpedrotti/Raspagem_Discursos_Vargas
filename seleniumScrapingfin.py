from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os
from zipfile import ZipFile

# Inicializando o WebDriver. Estou usando o Chrome.
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Criando uma lista vazia para armazenar os links dos discursos.
discourse_links = []

# Estes são os anos que eu quero buscar no site.
anos = ['1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1943', '1944', '1951', '1952', '1953']
for ano in anos:
    # Acessando a página do ano específico.
    driver.get(f"http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/getulio-vargas/discursos/{ano}")
    time.sleep(2)

    # Usando BeautifulSoup para extrair os dados da página.
    sopa = BeautifulSoup(driver.page_source, 'lxml')

    # Adicionando os links dos discursos desse ano à nossa lista.
    discourse_links += [a['href'] for a in sopa.select("a.summary.url")]

# Pasta onde os PDFs serão baixados.
pasta_downloads = os.path.expanduser("~") + "/Downloads/"

# Contador para acompanhar o número de PDFs baixados.
contador_pdfs = 0
maximo_tentativas = 3

# Loop para baixar os PDFs.
for i, link_discurso in enumerate(discourse_links):
    tentativas = 0

    # Continuamos tentando até ter pelo menos 35 PDFs.
    while contador_pdfs < 35 and tentativas < maximo_tentativas:
        driver.get(link_discurso)
        time.sleep(2)
        sopa = BeautifulSoup(driver.page_source, 'lxml')
        link_pdf = sopa.select_one("a[href*='.pdf']")['href']
        driver.get(link_pdf)

        # Definindo um tempo limite para o download.
        tempo_limite = 30
        tempo_inicial = time.time()

        while True:
            tempo_decorrido = time.time() - tempo_inicial

            if tempo_decorrido > tempo_limite:
                print(f"Tempo limite atingido para o discurso {i+1}. Tentando novamente...")
                tentativas += 1
                break

            try:
                # Procurando por arquivos que tenham terminado o download (ou seja, não são '.crdownload')
                ultimo_arquivo = max(
                    [os.path.join(pasta_downloads, nome_arquivo) for nome_arquivo in os.listdir(pasta_downloads) if not nome_arquivo.startswith('.') and not nome_arquivo.endswith('.crdownload')],
                    key=os.path.getctime, default=None)
                if ultimo_arquivo and ultimo_arquivo.endswith(".pdf"):
                    novo_nome = os.path.join(pasta_downloads, f"Vargas_{contador_pdfs+1}.pdf")
                    os.rename(ultimo_arquivo, novo_nome)
                    contador_pdfs += 1
                    break  # Sai do loop interno.
            except Exception as e:
                print(f"Ocorreu um erro: {e}. Pulando o discurso {i+1}.")
                break  # Sai do loop interno.

            time.sleep(2)

# Compactando todos os PDFs em um arquivo zip.
with ZipFile('discursos.zip', 'w') as meu_zip:
    for nome_arquivo in os.listdir(pasta_downloads):
        if nome_arquivo.startswith("Vargas") and nome_arquivo.endswith(".pdf"):
            meu_zip.write(os.path.join(pasta_downloads, nome_arquivo), nome_arquivo)

# Fechando o navegador.
driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os
from zipfile import ZipFile

# Inicializando o WebDriver. Estou usando o Chrome.
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Criando uma lista vazia para armazenar os links dos discursos.
discourse_links = []

# Estes são os anos que eu quero buscar no site.
anos = ['1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1943', '1944', '1951', '1952', '1953']
for ano in anos:
    # Acessando a página do ano específico.
    driver.get(f"http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/getulio-vargas/discursos/{ano}")
    time.sleep(2)

    # Usando BeautifulSoup para extrair os dados da página.
    sopa = BeautifulSoup(driver.page_source, 'lxml')

    # Adicionando os links dos discursos desse ano à nossa lista.
    discourse_links += [a['href'] for a in sopa.select("a.summary.url")]

# Pasta onde os PDFs serão baixados.
pasta_downloads = os.path.expanduser("~") + "/Downloads/"

# Contador para acompanhar o número de PDFs baixados.
contador_pdfs = 0
maximo_tentativas = 3

# Loop para baixar os PDFs.
for i, link_discurso in enumerate(discourse_links):
    tentativas = 0

    # Continuamos tentando até ter pelo menos 35 PDFs.
    while contador_pdfs < 35 and tentativas < maximo_tentativas:
        driver.get(link_discurso)
        time.sleep(2)
        sopa = BeautifulSoup(driver.page_source, 'lxml')
        link_pdf = sopa.select_one("a[href*='.pdf']")['href']
        driver.get(link_pdf)

        # Definindo um tempo limite para o download.
        tempo_limite = 30
        tempo_inicial = time.time()

        while True:
            tempo_decorrido = time.time() - tempo_inicial

            if tempo_decorrido > tempo_limite:
                print(f"Tempo limite atingido para o discurso {i+1}. Tentando novamente...")
                tentativas += 1
                break

            try:
                # Procurando por arquivos que tenham terminado o download (ou seja, não são '.crdownload')
                ultimo_arquivo = max(
                    [os.path.join(pasta_downloads, nome_arquivo) for nome_arquivo in os.listdir(pasta_downloads) if not nome_arquivo.startswith('.') and not nome_arquivo.endswith('.crdownload')],
                    key=os.path.getctime, default=None)
                if ultimo_arquivo and ultimo_arquivo.endswith(".pdf"):
                    novo_nome = os.path.join(pasta_downloads, f"Vargas_{contador_pdfs+1}.pdf")
                    os.rename(ultimo_arquivo, novo_nome)
                    contador_pdfs += 1
                    break  # Sai do loop interno.
            except Exception as e:
                print(f"Ocorreu um erro: {e}. Pulando o discurso {i+1}.")
                break  # Sai do loop interno.

            time.sleep(2)

# Compactando todos os PDFs em um arquivo zip.
with ZipFile('discursos.zip', 'w') as meu_zip:
    for nome_arquivo in os.listdir(pasta_downloads):
        if nome_arquivo.startswith("Vargas") and nome_arquivo.endswith(".pdf"):
            meu_zip.write(os.path.join(pasta_downloads, nome_arquivo), nome_arquivo)

# Fechando o navegador.
driver.quit()

