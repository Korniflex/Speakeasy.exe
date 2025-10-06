# Speakeasy – Translation and Text-to-Speech Application

## English Version

### Overview

Speakeasy is a Python-based desktop application designed to make working with text more efficient. It enables users to read, translate, listen to, and store text from different file formats, including documents and images. The application integrates translation and text-to-speech services and offers a simple graphical user interface.

This project was developed as part of a collaborative portfolio work to demonstrate skills in text processing, API integration, GUI development, and data handling.

### Purpose and Features

The main goal of this project is to provide an accessible and practical solution for handling multilingual text content. Users can load text from various sources, translate it into multiple languages, convert it into spoken audio, and store translations for later use. The application was designed with a focus on clarity, simplicity, and real-world usability.

Key features include:

- Reading text from `.txt`, `.csv`, `.pdf`, `.docx`, `.xlsx`, and image files (`.jpg`, `.png`)
- Translating text into different languages using the DeepL API
- Converting translated text into speech using gTTS and playing it directly
- Saving translations locally and retrieving them later
- Operating through a user-friendly GUI built with Tkinter

### Technology Stack

The application is implemented in Python (≥3.10) and uses the following key libraries and services:

- Tkinter for the graphical user interface
- DeepL API for translation services
- gTTS (Google Text-to-Speech) for audio generation
- PyPDF2, python-docx, pandas, and Pillow for file handling
- pytesseract for OCR (text extraction from images)
- pygame for audio playback

### Project Structure

```
├── SpeakEasy_1.0.py
├── translations.json
├── uebersetzungen/
├── requirements.txt
└── README.md
```

### Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/speakeasy.git
cd speakeasy
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Add your DeepL API key to the script:

```python
deepl_api_key = "YOUR_API_KEY"
```

4. Install Tesseract OCR for image-to-text functionality. Follow the instructions at:
https://github.com/tesseract-ocr/tesseract

### Usage

Run the application with:

```
python SpeakEasy_1.0.py
```

Once launched, you can import text files, translate content, generate audio output, and manage stored translations directly from the GUI.

### Future Development

Future iterations of this project could include features such as CSV/database export for saved translations, text summarization, speech recognition, and full packaging as a cross-platform desktop application.

---

## Deutsche Version

### Überblick

Speakeasy ist eine auf Python basierende Desktop-Anwendung, die das Arbeiten mit Texten einfacher und effizienter macht. Sie ermöglicht es, Texte aus verschiedenen Dateiformaten zu lesen, zu übersetzen, anzuhören und zu speichern. Die Anwendung integriert Übersetzungs- und Sprachausgabedienste und bietet eine einfache grafische Benutzeroberfläche.

Dieses Projekt wurde im Rahmen einer gemeinschaftlichen Portfolioarbeit entwickelt, um Kompetenzen in der Textverarbeitung, API-Integration, GUI-Entwicklung und Datenverarbeitung zu demonstrieren.

### Ziel und Funktionen

Das Hauptziel des Projekts ist es, eine praktische Lösung für den Umgang mit mehrsprachigen Textinhalten bereitzustellen. Nutzer können Texte aus verschiedenen Quellen laden, in mehrere Sprachen übersetzen, in gesprochene Sprache umwandeln und für die spätere Verwendung speichern. Bei der Entwicklung wurde besonderer Wert auf Benutzerfreundlichkeit und Praxistauglichkeit gelegt.

Wichtige Funktionen:

- Einlesen von Texten aus `.txt`, `.csv`, `.pdf`, `.docx`, `.xlsx` und Bilddateien (`.jpg`, `.png`)
- Übersetzung von Texten mit der DeepL API
- Umwandlung übersetzter Texte in Sprache mit gTTS und direkte Wiedergabe
- Lokales Speichern von Übersetzungen mit späterem Zugriff
- Intuitive Benutzeroberfläche mit Tkinter

### Technologie-Stack

Die Anwendung wurde in Python (≥3.10) entwickelt und verwendet folgende zentrale Bibliotheken und Dienste:

- Tkinter für die grafische Benutzeroberfläche
- DeepL API für Übersetzungsdienste
- gTTS (Google Text-to-Speech) für Sprachausgabe
- PyPDF2, python-docx, pandas und Pillow für die Dateiverarbeitung
- pytesseract für OCR (Texterkennung aus Bildern)
- pygame für Audiowiedergabe

### Projektstruktur

```
├── SpeakEasy_1.0.py
├── translations.json
├── uebersetzungen/
├── requirements.txt
└── README.md
```

### Installation

1. Repository klonen:

```
git clone https://github.com/yourusername/speakeasy.git
cd speakeasy
```

2. Abhängigkeiten installieren:

```
pip install -r requirements.txt
```

3. DeepL API-Schlüssel im Skript eintragen:

```python
deepl_api_key = "DEIN_API_KEY"
```

4. Tesseract OCR für die Texterkennung aus Bildern installieren. Anleitung hier:
https://github.com/tesseract-ocr/tesseract

### Verwendung

Die Anwendung kann mit folgendem Befehl gestartet werden:

```
python SpeakEasy_1.0.py
```

Nach dem Start können Texte importiert, übersetzt, in Sprache umgewandelt und gespeicherte Übersetzungen direkt über die Benutzeroberfläche verwaltet werden.

### Weiterentwicklung

Zukünftige Versionen könnten Funktionen wie den Export von Übersetzungen in CSV/Datenbanken, Textzusammenfassungen, Spracherkennung oder die Bereitstellung als plattformübergreifende Desktop-Anwendung enthalten.
