# 🗣️ Speakeasy – Translation, Text-to-Speech & Document Reader

This repository contains **Speakeasy**, a Python-based desktop application that allows users to **translate text, generate audio output, and save translations** — all through a user-friendly graphical interface. The application can read text from multiple file types (including PDFs, Word documents, Excel files, and even images via OCR), translate them using the **DeepL API**, convert the translated text into speech with **gTTS**, and manage saved translations in a local database.

---

## 📚 Table of Contents

- [English Version](#english-version)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Future Improvements](#future-improvements)
- [Deutsche Version](#deutsche-version)

---

## 🇬🇧 English Version

### Project Overview

**Speakeasy** is a desktop application built with Python and Tkinter that brings together translation, speech synthesis, and document reading. The goal of this project is to make text processing more accessible by allowing users to load text from various sources, translate it into multiple languages, listen to the result, and save it for future reference.

### ✨ Features

- 📄 **File Import:** Read text from `.txt`, `.csv`, `.pdf`, `.docx`, `.xlsx`, and image files (`.jpg`, `.png`) using **PyPDF2**, **pytesseract**, and **PIL**  
- 🌐 **Translation:** Translate text into multiple languages using the **DeepL API**  
- 🔊 **Text-to-Speech:** Generate spoken audio with **gTTS** and play it directly in the app using **pygame**  
- 💾 **Save & Manage:** Store translated texts locally as `.txt` files and retrieve them anytime  
- 🖥️ **User-Friendly GUI:** Built with **Tkinter** and **ttkthemes** for a clean and intuitive interface  

### 🧰 Tech Stack

- **Languages & Frameworks:** Python, Tkinter  
- **APIs & Libraries:**  
  - Translation: [DeepL API](https://www.deepl.com/pro)  
  - Text-to-Speech: [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)  
  - Optical Character Recognition: [pytesseract](https://pypi.org/project/pytesseract/)  
  - Document Processing: PyPDF2, python-docx, pandas  
  - Audio Playback: pygame  
  - Image Processing: PIL (Pillow)  

### 📁 Project Structure

```
├── SpeakEasy_1.0.py            # Main application script  
├── translations.json           # Stored translation data  
├── uebersetzungen/             # Folder containing saved translations  
├── requirements.txt            # Dependencies  
├── README.md                   # Documentation  
└── assets/                     # Logo and additional resources  
```

### ⚙️ Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/speakeasy.git
   cd speakeasy
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Add your **DeepL API key** in the script:  
   ```python
   deepl_api_key = "YOUR_API_KEY"
   ```

4. Make sure [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) is installed and its path is correctly configured in the script.

### ▶️ Usage

Run the application:  
```bash
python SpeakEasy_1.0.py
```

From the GUI you can:  
- Select and load a file  
- Translate text into your chosen language  
- Generate and play audio output  
- Save translations locally

### 🔮 Future Improvements

- Export translations to CSV or database  
- Add text summarization features  
- Integrate voice input and speech recognition  
- Package as a standalone cross-platform desktop application

---

## 🇩🇪 Deutsche Version

### Projektübersicht

**Speakeasy** ist eine Python-Desktopanwendung, die Übersetzung, Sprachausgabe und Texterkennung in einer benutzerfreundlichen Oberfläche vereint. Ziel des Projekts ist es, die Verarbeitung von Texten zu vereinfachen, indem Nutzer Inhalte aus verschiedenen Dateiformaten einlesen, übersetzen, anhören und speichern können.

### ✨ Funktionen

- 📄 **Dateiimport:** Texte aus `.txt`, `.csv`, `.pdf`, `.docx`, `.xlsx` und Bilddateien (`.jpg`, `.png`) einlesen mit **PyPDF2**, **pytesseract** und **PIL**  
- 🌐 **Übersetzung:** Texte mit der **DeepL API** in verschiedene Sprachen übersetzen  
- 🔊 **Sprachausgabe:** Audio mit **gTTS** generieren und direkt in der Anwendung abspielen  
- 💾 **Speichern & Verwalten:** Übersetzungen lokal als `.txt` speichern und jederzeit abrufen  
- 🖥️ **Benutzeroberfläche:** Klare und intuitive GUI mit **Tkinter** und **ttkthemes**  

### 🧰 Tech Stack

- **Programmiersprache & Framework:** Python, Tkinter  
- **APIs & Bibliotheken:**  
  - Übersetzung: [DeepL API](https://www.deepl.com/pro)  
  - Sprachausgabe: [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)  
  - Texterkennung: [pytesseract](https://pypi.org/project/pytesseract/)  
  - Dokumentenverarbeitung: PyPDF2, python-docx, pandas  
  - Audiowiedergabe: pygame  
  - Bildverarbeitung: PIL (Pillow)  

### 📁 Projektstruktur

```
├── SpeakEasy_1.0.py            # Hauptskript der Anwendung  
├── translations.json           # Gespeicherte Übersetzungsdaten  
├── uebersetzungen/             # Ordner mit gespeicherten Übersetzungen  
├── requirements.txt            # Abhängigkeiten  
├── README.md                   # Dokumentation  
└── assets/                     # Logo und weitere Ressourcen  
```

### ⚙️ Installation

1. Repository klonen:  
   ```bash
   git clone https://github.com/yourusername/speakeasy.git
   cd speakeasy
   ```

2. Abhängigkeiten installieren:  
   ```bash
   pip install -r requirements.txt
   ```

3. Deinen **DeepL API-Schlüssel** im Skript eintragen:  
   ```python
   deepl_api_key = "DEIN_API_SCHLÜSSEL"
   ```

4. Stelle sicher, dass [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installiert ist und der Pfad im Skript korrekt gesetzt ist.

### ▶️ Verwendung

Starte die Anwendung:  
```bash
python SpeakEasy_1.0.py
```

In der GUI kannst du:  
- Eine Datei auswählen und laden  
- Texte in die gewünschte Sprache übersetzen  
- Sprachausgabe erzeugen und abspielen  
- Übersetzungen lokal speichern

### 🔮 Ausblick

- Export von Übersetzungen in CSV oder Datenbanken  
- Implementierung einer Textzusammenfassung  
- Integration von Spracheingabe und Spracherkennung  
- Bereitstellung einer plattformübergreifenden Desktop-Version

---
