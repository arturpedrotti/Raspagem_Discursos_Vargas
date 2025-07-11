# 📜 Getúlio Vargas Speech Scraper

This project automates the scraping and downloading of speeches by former Brazilian president Getúlio Vargas from government websites. It uses **Selenium** for web navigation and **BeautifulSoup** for PDF link extraction, downloading the files to a local directory.

---

## 🚀 Features

- Full automation of browser navigation using Selenium
- PDF link extraction with BeautifulSoup
- Batch download of all available speeches
- Compatible with Linux/macOS and Windows
- Optional virtual environment setup
- Guidance for unzipping collected files

---

## 🛠 Requirements

- Python 3.x
- pip
- Google Chrome
- ChromeDriver compatible with your Chrome version

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

To run the script:
```bash
python seleniumScrapingfin.py
```

Ensure the `downloads` folder is clear before running to avoid conflicts.

---

## 💡 Example Use Case

Researchers or historians can use this tool to automate the collection of speeches for textual analysis, natural language processing, or archival purposes.

---

## 📦 Extracting ZIP Files

**Linux/macOS:**
```bash
unzip -d output_dir path/to/file.zip
```

**Windows:**

Use:
- File Explorer
- PowerShell: `Expand-Archive -Path path\to\file.zip -DestinationPath output_dir`
- WinRAR or 7-Zip

---

## 👤 Author

Developed primarily by **Artur Pedrotti Grochau**, with academic collaboration:

- Bruno Alexandre Rodrigues do Nascimento Gonçalves  
- Matheus Guimarães Ferreira Rocha  
- Pedro Henrique Oliveira da Cunha  

This was part of a university data collection project.

---

## 📝 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🤝 Contributions

Pull requests are welcome. Please fork the repository and submit your proposal.
