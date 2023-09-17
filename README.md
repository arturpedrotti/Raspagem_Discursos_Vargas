# Raspagem de Discursos de Getúlio Vargas

## 📜 Descrição

Este programa foi desenvolvido para fazer a raspagem de discursos do ex-presidente brasileiro Getúlio Vargas. O código é parte do projeto hospedado em [este repositório GitHub](https://github.com/arturpedrotti/Raspagem_Discursos_Vargas). O programa utiliza Selenium para navegar pelos sites e BeautifulSoup para extrair os links dos discursos em PDF. Posteriormente, esses PDFs são baixados e armazenados em uma pasta definida.

### 👨‍💻 Autores

- Artur Pedrotti Grochau
- Bruno Alexandre Rodrigues do Nascimento Gonçalves
- Matheus Guimarães Ferreira Rocha
- Pedro Henrique Oliveira da Cunha

## 🛠 Pré-requisitos

- Python 3.x
- pip
- Google Chrome instalado (o WebDriver é para o Chrome)

## 🚀 Instalação e Configuração

### Linux/Mac

1. **Clone o Repositório**
    ```bash
    git clone https://github.com/arturpedrotti/Raspagem_Discursos_Vargas.git
    ```

2. **Entre no Diretório do Projeto**
    ```bash
    cd Raspagem_Discursos_Vargas
    ```

3. **Ambiente Virtual (Opcional)**
    ```bash
    python3 -m venv venv
    ```

4. **Ative o Ambiente Virtual**
    ```bash
    source venv/bin/activate
    ```

5. **Instale as Dependências**
    ```bash
    pip install -r requirements.txt
    ```

### Windows

1. **Clone o Repositório**
    ```powershell
    git clone https://github.com/arturpedrotti/Raspagem_Discursos_Vargas.git
    ```

2. **Entre no Diretório do Projeto**
    ```powershell
    cd Raspagem_Discursos_Vargas
    ```

3. **Ambiente Virtual (Opcional)**
    ```powershell
    python -m venv venv
    ```

4. **Ative o Ambiente Virtual**
    ```powershell
    .\venv\Scripts\Activate
    ```

5. **Instale as Dependências**
    ```powershell
    pip install -r requirements.txt
    ```

## 🚦 Como Usar

1. **Execute o Script Python**
    ```bash
    python3 seleniumScrapingfin.py  # Linux/Mac
    python seleniumScrapingfin.py   # Windows
    ```

## 📦 Descompactando os PDFs Baixados

### Linux/Mac

- Utilize o comando `unzip -d 'nomedir' caminho/para/o/arquivo.zip` para descompactar o arquivo ZIP em um diretório especificado.

### Windows

- Use softwares como WinRAR ou 7-Zip, ou utilize o comando `Expand-Archive` no PowerShell.

## ⚠️ Advertências

- Este script pode não funcionar corretamente em conexões de internet lentas. O tempo de download dos PDFs pode variar.
- Certifique-se de que a pasta de download esteja vazia ou de que nenhum arquivo nela conflite com os nomes dos arquivos baixados pelo programa.

## 🤝 Contribuição

Para contribuir com este projeto, por favor, faça um fork do repositório e crie uma Pull Request.

## 📝 Licença

MIT

