<div align="justify">

## Installation

### Windows

1. Download the Tesseract installer from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki).
2. Run the `.exe` file and follow the installation steps. Remember the installation path.
3. Add the Tesseract path to the system environment variables:
   - Go to Control Panel > System and Security > System > Advanced system settings > Environment Variables.
   - Find "Path" under System variables, click "Edit," and add the path to the folder where `tesseract.exe` is installed.

### Linux (Ubuntu)

1. Open a terminal and run the following commands:
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr
   ```
2. To install additional language support (e.g., Vietnamese):
    ```bash
    sudo apt install tesseract-ocr-vie
    ```

### macOS

1. Install Homebrew if you don't have it:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install Tesseract OCR:

```bash
brew install tesseract
```

3. To install additional language packages

```bash
brew install tesseract-lang
```

## Usage

Once Tesseract is installed, you can use the __pytesseract__ library in Python to interact with the Tesseract OCR engine. To verify the installation:

```bash
tesseract --version
```

</div>