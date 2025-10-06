# 🗣️ Speakeasy – Translation and Text-to-Speech Desktop App

## Overview

Speakeasy is a Python-based desktop application that combines text translation, speech synthesis, and document reading in one intuitive tool. It allows you to load text from various sources (including PDFs, Word documents, Excel sheets, and even images via OCR), translate it using the DeepL API, convert it into speech with gTTS, and store translations for future reference — all from a simple graphical interface.

The project was developed to practice end-to-end application design: from data extraction and processing to API integration and user interaction. It demonstrates how Python can be used to build real-world tools beyond scripts and notebooks.

---

## ✨ Key Features

- **File reading:** Import text from `.txt`, `.csv`, `.pdf`, `.docx`, `.xlsx` or image files (`.jpg`, `.png`)  
- **Translation:** Translate text into multiple languages using the [DeepL API](https://www.deepl.com/pro)  
- **Speech synthesis:** Convert translations into spoken audio with [gTTS](https://pypi.org/project/gTTS/) and play them directly in the app  
- **Storage:** Save translations locally and retrieve them later  
- **User interface:** Simple, responsive desktop GUI built with Tkinter and ttkthemes  

---

## 🧰 Tech Stack

- **Language:** Python (≥3.10)  
- **Core Libraries:** Tkinter, pandas, PyPDF2, python-docx, Pillow  
- **APIs:** DeepL (translation), gTTS (text-to-speech)  
- **Additional Tools:** pytesseract (OCR), pygame (audio playback)

---

## 📁 Project Structure

```
├── SpeakEasy_1.0.py            # Main application script  
├── translations.json           # Stored translation data  
├── uebersetzungen/             # Folder containing saved translations  
├── requirements.txt            # Dependencies  
└── README.md                   # Documentation  
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/speakeasy.git
cd speakeasy
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure your DeepL API key
Open `SpeakEasy_1.0.py` and insert your API key:
```python
deepl_api_key = "YOUR_API_KEY"
```

### 4. Install Tesseract OCR
For OCR functionality (text extraction from images), [download and install Tesseract](https://github.com/tesseract-ocr/tesseract).  
Make sure the executable path is correctly set in your environment or directly in the script.

---

## ▶️ Usage

Run the app:
```bash
python SpeakEasy_1.0.py
```

You can then:
- Select a file and extract its content  
- Translate text into your chosen language  
- Generate audio output and play it directly  
- Save translations for later use  

---

## 🔮 Future Improvements

- Add CSV/database export for saved translations  
- Include text summarization and sentiment analysis features  
- Integrate voice input and speech recognition  
- Package as a cross-platform desktop application  

---

# 🇩🇪 Speakeasy – Übersetzung und Sprachausgabe für den Desktop

## Überblick

Speakeasy ist eine Python-Desktopanwendung, die Übersetzung, Sprachausgabe und Texterkennung in einer intuitiven Oberfläche kombiniert. Texte können aus verschiedenen Formaten (PDF, Word, Excel oder Bilder per OCR) geladen, mit der DeepL API übersetzt, per gTTS in Sprache umgewandelt und lokal gespeichert werden.

Dieses Projekt zeigt, wie man mit Python vollständige Anwendungen entwickelt – von der Datenextraktion und API-Anbindung bis zur Benutzeroberfläche.

---

## ✨ Hauptfunktionen

- **Texterkennung:** Texte aus `.txt`, `.csv`, `.pdf`, `.docx`, `.xlsx` oder Bilddateien (`.jpg`, `.png`) einlesen  
- **Übersetzung:** Texte mit der [DeepL API](https://www.deepl.com/pro) übersetzen  
- **Sprachausgabe:** Übersetzungen mit [gTTS](https://pypi.org/project/gTTS/) in Sprache umwandeln und direkt abspielen  
- **Speicherung:** Übersetzungen lokal speichern und wieder abrufen  
- **Benutzeroberfläche:** Klare und einfache GUI mit Tkinter und ttkthemes  

---

## 🧰 Technologien

- **Sprache:** Python (≥3.10)  
- **Bibliotheken:** Tkinter, pandas, PyPDF2, python-docx, Pillow  
- **APIs:** DeepL (Übersetzung), gTTS (Sprachausgabe)  
- **Zusätzliche Tools:** pytesseract (OCR), pygame (Audiowiedergabe)

---

## 📁 Projektstruktur

```
├── SpeakEasy_1.0.py  
├── translations.json  
├── uebersetzungen/  
├── requirements.txt  
└── README.md  
```

---

## ⚙️ Installation

### 1. Repository klonen
```bash
git clone https://github.com/yourusername/speakeasy.git
cd speakeasy
```

### 2. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 3. DeepL API-Schlüssel konfigurieren
Öffne `SpeakEasy_1.0.py` und füge deinen API-Schlüssel ein:
```python
deepl_api_key = "DEIN_API_KEY"
```

### 4. Tesseract OCR installieren
Für die Texterkennung aus Bildern muss [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installiert sein.  
Stelle sicher, dass der Pfad korrekt in deiner Umgebung oder im Skript gesetzt ist.

---

## ▶️ Verwendung

Anwendung starten:
```bash
python SpeakEasy_1.0.py
```

Funktionen:
- Datei auswählen und Text extrahieren  
- Übersetzen und Sprachausgabe erzeugen  
- Übersetzungen lokal speichern und verwalten  

---

## 🔮 Ausblick

- Exportfunktion in CSV oder Datenbanken  
- Textzusammenfassung und Sentimentanalyse  
- Spracheingabe und Spracherkennung  
- Bereitstellung als plattformübergreifende Desktop-Anwendung  
