from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from zipfile import ZipFile
import time
import os

# Configure WebDriver options
options = Options()
options.add_argument("--headless")  # optional: run headless for automation
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URLs and constants
BASE_URL = "http://www.biblioteca.presidencia.gov.br/presidencia/ex-presidentes/getulio-vargas/discursos/"
YEARS = ['1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1943', '1944', '1951', '1952', '1953']
DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
MAX_FILES = 35

# Collect PDF URLs
discourse_links = []
for year in YEARS:
    driver.get(f"{BASE_URL}{year}")
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    discourse_links += [a['href'] for a in soup.select("a.summary.url")]

discourse_links = discourse_links[:MAX_FILES]

# Download and rename PDFs
for i, link in enumerate(discourse_links):
    driver.get(link)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    pdf_link = soup.select_one("a[href*='.pdf']")
    if not pdf_link:
        print(f"No PDF found at {link}")
        continue

    driver.get(pdf_link['href'])
    time.sleep(5)

    try:
        files = [os.path.join(DOWNLOAD_DIR, f) for f in os.listdir(DOWNLOAD_DIR)]
        latest_file = max(files, key=os.path.getctime)

        if latest_file.endswith('.crdownload'):
            print("Download in progress... waiting.")
            time.sleep(10)
            continue

        if latest_file.endswith('.pdf'):
            target_name = os.path.join(DOWNLOAD_DIR, f"Vargas_{i+1}.pdf")
            os.rename(latest_file, target_name)

    except Exception as e:
        print(f"Error processing file {link}: {e}")
        continue

# Create ZIP with all Vargas PDFs
with ZipFile("discourses.zip", "w") as zipf:
    for f in os.listdir(DOWNLOAD_DIR):
        if f.startswith("Vargas") and f.endswith(".pdf"):
            zipf.write(os.path.join(DOWNLOAD_DIR, f), arcname=f)

driver.quit()
