import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageEnhance, ImageFilter, ImageTk
import PyPDF2
import pytesseract
from docx import Document
import pandas as pd
from gtts import gTTS
import os
import deepl
import pygame                                                                   # Für die Audiowiedergabe in der Oberfläche
import threading                                                                # Für die parallele Ausführung von Aufgaben
import tempfile
import time
import json
import uuid

# Pfad zu Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# DeepL API-Schlüssel
deepl_api_key = "0da97219-4171-4f65-8f39-9aa943648814:fx"                       # Ersetzen Sie diesen durch Ihren gültigen Schlüssel
translator = deepl.Translator(deepl_api_key)

# Globale Variablen
file_path = None                                                                 # Wir erstellen "leere" Variabeln um kein NameError zu bekommen
text = None
translated_text = ""

def get_audio_filename():
    # Create a unique filename using UUID to avoid conflicts
    unique_id = str(uuid.uuid4())[:8]
    temp_dir = tempfile.gettempdir()
    return os.path.join(temp_dir, f"translated_{unique_id}.mp3")             # Temporäre Datei
is_audio_playing = False



# Sprachzuordnung
LANG_MAPPING = {                                                                   # Wegen viele Errors in der Auswahlt der uebersetzungssprache, definieren wir die Sprachzuordung au▬5erhalb der def der Uebersetzung
    "Englisch": "EN-US",
    "Deutsch": "DE",
    "Französisch": "FR",
    "Spanisch": "ES",
    "Italienisch": "IT",
    "Portugiesisch": "PT-BR",
    "Russisch": "RU"
}
# Ordner zum Speichern der Übersetzungen
TRANSLATIONS_FOLDER = "uebersetzungen"                                                              # Wir haben eine Funktion die ermoeglicht, die uebersetzte Texte zu speichern. Die werden hier gespeichert.
# Pfad zur Persistenzdatei
PERSISTENCE_FILE = "translations.json"

# Erstellen des Ordners, falls er nicht existiert
if not os.path.exists(TRANSLATIONS_FOLDER):                                                          # Fehlerbehebung, erstellung eines Folder falls da was dummes passiert.
    os.makedirs(TRANSLATIONS_FOLDER)

# Initialisierung von pygame für die Audiowiedergabe
pygame.mixer.init()

# Funktionen zum Lesen verschiedener Dateitypen
def read_txt(file_path):                                                               
    try:
        with open(file_path, 'r', encoding='utf-8') as file:                                        # 'r' steht fuer read, utf-8 sodass Sonderzeichen mitgenommen werden
            return file.read()                                                                      # Liest den Inhalt und gibt ihn als String zurück 
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Lesen der Textdatei: {e}")                     # Falls ein Fehler auftritt, wird er ausgegeben
        return None

def read_pdf(file_path):
    try:
        with open(file_path, "rb") as file:                                                          # Öffnet die PDF-Datei im Binärmodus (rb = read binary)
            reader = PyPDF2.PdfReader(file)                                                          # Erstellt einen PDF-Reader
            text = "".join(page.extract_text() for page in reader.pages if page.extract_text())      # "" = leerer string wo das extraierter text vom pdf zugefuegt wird. pages ist von PyPDF definiert
            return text                                                                              # gibt den text zurueck
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Lesen der PDF-Datei: {e}")                      # Falls ein Fehler auftritt, wird er ausgegeben
        return None

def read_image(file_path):
    try:
        img = Image.open(file_path)                                                                   # Öffnet das Bild mit der Bibliothek 'PIL'
        
        # Bildverbesserung
        img = img.convert('L')                                                                        # Umwandlung in Graustufen
        img = img.filter(ImageFilter.SHARPEN)                                                         # Erhöhung der Schärfe
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)                                                                     # Verbesserung des Kontrastes
        
        # Textextraktion mit OCR
        text = pytesseract.image_to_string(img)                                                        # Verarbeitet das Bild mit Tesseract-OCR zur Texterkennung
        return text                                                                                    # Gibt den erkannten Text zurück
    except Exception as e:                                                                             # Falls ein Fehler auftritt, wird er ausgegeben
        messagebox.showerror("Fehler", f"Fehler beim Lesen des Bildes: {e}")
        return None

def read_docx(file_path):
    try:
        doc = Document(file_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])                          
        return text
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Lesen der Word-Datei: {e}")
        return None

def read_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        text = df.to_string(index=False)
        return text
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Lesen der Excel-Datei: {e}")
        return None

def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()                                                    #Extrahiert die Dateiendung und wandelt sie in Kleinbuchstaben um

    readers = {                                                                                     # Dictionary, das jeder Dateiendung eine spezifische Lese-Funktion zuordnet
        '.txt': read_txt,
        '.csv': read_txt,
        '.pdf': read_pdf,
        '.jpg': read_image,
        '.jpeg': read_image,
        '.png': read_image,
        '.gif': read_image,
        '.docx': read_docx,
        '.xlsx': read_excel
    }
    
    if ext in readers:                                                                              # Prüft, ob die Dateiendung im Dictionary vorhanden ist
        return readers[ext](file_path)                                                              # Ruft die passende Funktion mit dem übergebenen Dateipfad auf und gibt das Ergebnis zurück
    else:
        messagebox.showerror("Fehler", "Nicht unterstütztes Dateiformat.")
        return None

# Funktion zum Speichern von Text in eine Datei
def save_text_file(text, output_file):
    try:
        with open(output_file, 'w', encoding="utf-8") as file:                                      # Öffnet die Datei im Schreibmodus 'w' mit UTF-8-Kodierung
            file.write(text)                                                                        # Schreibt den Text in die Datei
        print(f"Text erfolgreich gespeichert in {output_file}")                                     # Gibt eine Erfolgsmeldung aus
        return True  
    except Exception as e:  
        messagebox.showerror("Fehler", f"Fehler beim Speichern der Datei: {e}")                     # Zeigt eine Fehlermeldung in einer GUI-Box an (fuer den user)
        return False

# Funktion zum Speichern der Übersetzung im Übersetzungsordner
def save_translation(text, filename="translated_text.txt"):                                         # Wir definieren eine Funktion die wir mit einen Button benutzten werden, um den text speichern zu koennen.
    output_file = os.path.join(TRANSLATIONS_FOLDER, filename)
    if save_text_file(text, output_file):
        messagebox.showinfo("Speichern", f"Übersetzung gespeichert in {output_file}")
        return True
    return False

# Wort-für-Wort-Übersetzung
def translate_word_by_word(text_to_translate, target_lang):
    global translated_text
    
    if not text_to_translate:
        messagebox.showwarning("Achtung", "Kein Text zum Übersetzen vorhanden.")
        return ""
    
    words = text_to_translate.split()
    translated_text = ""
    
    for word in words:
        try:
            translated_word = translator.translate_text(word, target_lang=target_lang).text
            translated_text += translated_word + " "
            # Aktualisierung der Oberfläche
            root.update_idletasks()
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler bei der Übersetzung: {e}")
            break
    
    return translated_text

# Funktion zum Übersetzen eines kompletten Textes
def translate_text(text_to_translate, target_lang):
    try:
        # Debug-Anzeige
        print(f"Übersetzung in Sprachcode: {target_lang}")
        
        # Überprüfung der Gültigkeit des API-Schlüssels
        if not deepl_api_key or len(deepl_api_key) < 10:
            raise ValueError("Ungültiger DeepL API-Schlüssel")
            
        # API-Aufruf
        result = translator.translate_text(text_to_translate, target_lang=target_lang)
        
        # Debug-Anzeige
        print(f"Übersetzung erfolgreich: {result.detected_source_lang} -> {target_lang}")
        
        return result.text
    except deepl.exceptions.DeepLException as e:
        error_msg = f"DeepL API-Fehler: {e}"
        print(error_msg)
        messagebox.showerror("Fehler", error_msg)
        return ""
    except Exception as e:
        error_msg = f"Übersetzungsfehler: {e}"
        print(error_msg)
        messagebox.showerror("Fehler", error_msg)
        return ""

# Funktion zum Übersetzen und Anzeigen des Textes
def translate_and_display(input_text, target_lang, output_text_widget):
    global translated_text
    
    if not input_text:
        messagebox.showwarning("Achtung", "Kein Text zum Übersetzen vorhanden.")
        return
    
    # Passenden Sprachcode holen
    lang_code = LANG_MAPPING.get(target_lang, target_lang)
    
    # Übersetzung
    progress_window = tk.Toplevel(root)
    progress_window.title("Übersetzung läuft")
    progress_window.geometry("300x100")
    
    progress_label = ttk.Label(progress_window, text="Übersetzung läuft, bitte warten...")
    progress_label.pack(pady=20)
    
    def translate_task():
        global translated_text
        translated_text = translate_text(input_text, lang_code)
        progress_window.destroy()
        output_text_widget.delete("1.0", tk.END)
        output_text_widget.insert(tk.END, translated_text)
    
    # Übersetzung in einem separaten Thread starten
    threading.Thread(target=translate_task).start()

# Audio für die Übersetzung generieren
def generate_audio(text_to_speak, lang_code):
    global audio_file, is_audio_playing
    
    if not text_to_speak.strip():
        messagebox.showwarning("Achtung", "Kein Text zum Generieren von Audio verfügbar.")
        return False
    
    # Sprachcode in gTTS-kompatibles Format konvertieren
    tts_lang = get_language_code(lang_code)
    
    try:
        # Stop any playing audio
        if is_audio_playing:
            pygame.mixer.music.stop()
            is_audio_playing = False
        
        # Generate new audio filename each time
        audio_file = get_audio_filename()
            
        # Generate and save audio
        tts = gTTS(text_to_speak, lang=tts_lang)
        tts.save(audio_file)
        
        messagebox.showinfo("Erfolg", f"Audio generiert und gespeichert als {audio_file}")
        return True
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler bei der Audiogenerierung: {e}")
        # Print more details about the error to help with debugging
        print(f"Detailed error: {e}")
        print(f"Attempted to write to: {audio_file}")
        return False

# Funktion zum Abspielen des Audios
# Revised play_audio function
def play_audio():
    global is_audio_playing, audio_file
    
    # Check if we have a generated audio file
    if not audio_file or not os.path.exists(audio_file):
        messagebox.showwarning("Achtung", "Keine Audiodatei gefunden. Bitte generieren Sie zuerst Audio.")
        return
    
    try:
        if not is_audio_playing:
            # Load and play the audio file
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            is_audio_playing = True
            
            # Add event handler to detect when playback ends
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
            
            # Start a thread to monitor playback completion
            threading.Thread(target=monitor_playback, daemon=True).start()
        else:
            # Stop the audio if it's already playing
            pygame.mixer.music.stop()
            is_audio_playing = False
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler bei der Audiowiedergabe: {e}")
        print(f"Detailed playback error: {e}")
        is_audio_playing = False


# Funktion zum Erhalten des Sprachcodes für TTS
def get_language_code(language_name):
    language_codes = {
        "DE": "de",
        "EN-US": "en",
        "EN": "en",
        "FR": "fr",
        "ES": "es",
        "IT": "it",
        "PT-BR": "pt",
        "RU": "ru",
        "Deutsch": "de",
        "Englisch": "en",
        "Französisch": "fr",
        "Spanisch": "es",
        "Italienisch": "it",
        "Portugiesisch": "pt",
        "Russisch": "ru"
    }
    return language_codes.get(language_name, "en")
def monitor_playback():
    global is_audio_playing
    
    while is_audio_playing:
        # Check if music is still playing
        if not pygame.mixer.music.get_busy():
            is_audio_playing = False
            break
        time.sleep(0.1)

# Funktion für die Dateiauswahl
def open_file_dialog():
    global file_path, text
    file_types = [
        ("Alle unterstützten Dateien", "*.txt;*.csv;*.pdf;*.jpg;*.jpeg;*.png;*.gif;*.docx;*.xlsx"),
        ("Textdateien", "*.txt"),
        ("CSV-Dateien", "*.csv"),
        ("PDF-Dateien", "*.pdf"),
        ("Bilder", "*.jpg;*.jpeg;*.png;*.gif"),
        ("Word-Dokumente", "*.docx"),
        ("Excel-Tabellen", "*.xlsx")
    ]
    file_path = filedialog.askopenfilename(filetypes=file_types)
    if file_path:
        text = read_file(file_path)
        if text:
            display_original_text(text)
            # Logo ausblenden und Hauptoberfläche anzeigen
            if hasattr(root, 'logo_frame'):
                root.logo_frame.pack_forget()
            main_frame.pack(fill=tk.BOTH, expand=True)

# Funktion zum Anzeigen des Originaltextes
def display_original_text(text):
    original_text_widget.delete("1.0", tk.END)
    original_text_widget.insert("1.0", text)

# Übersetzungen speichern
def save_current_translation():
    text_to_save = translated_text_widget.get("1.0", tk.END).strip()
    if text_to_save:
        # Dateinamen vorschlagen
        suggested_name = f"uebersetzung_{len(gespeicherte_uebersetzungen)+1}.txt"
        filename = filedialog.asksaveasfilename(
            initialdir=TRANSLATIONS_FOLDER,
            initialfile=suggested_name,
            defaultextension=".txt",
            filetypes=[("Textdateien", "*.txt")]
        )
        if filename:
            if save_text_file(text_to_save, filename):
                original = original_text_widget.get("1.0", tk.END).strip()
                gespeicherte_uebersetzungen.append((original, text_to_save))
                update_saved_list()
    else:
        messagebox.showwarning("Achtung", "Kein Text zum Speichern vorhanden.")

# Liste der gespeicherten Übersetzungen aktualisieren
def update_saved_list():
    gespeicherte_liste.delete(0, tk.END)
    for i, (original, translated) in enumerate(gespeicherte_uebersetzungen):
        gespeicherte_liste.insert(tk.END, f"{i+1}. {translated[:50]}...")

# Funktion zum Laden einer gespeicherten Übersetzung
def on_listbox_select(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        original, translated = gespeicherte_uebersetzungen[index]
        original_text_widget.delete("1.0", tk.END)
        original_text_widget.insert("1.0", original)
        translated_text_widget.delete("1.0", tk.END)
        translated_text_widget.insert("1.0", translated)

# Speichern der Daten in einer JSON-Datei
def save_data_to_file():
    try:
        with open(PERSISTENCE_FILE, "w", encoding="utf-8") as file:
            json.dump(gespeicherte_uebersetzungen, file, ensure_ascii=False, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Fehler beim Speichern der Daten: {e}")

# Laden der Daten aus einer JSON-Datei
def load_data_from_file():
    global gespeicherte_uebersetzungen
    try:
        if os.path.exists(PERSISTENCE_FILE):
            with open(PERSISTENCE_FILE, "r", encoding="utf-8") as file:
                gespeicherte_uebersetzungen = json.load(file)
                aktualisiere_gespeicherte_liste()
    except Exception as e:
        messagebox.showerror("Error", f"Fehler beim Laden der Daten: {e}")

# Funktion zum Konfigurieren der Stile
def configure_styles():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', background='#2a2d34', foreground='white', font=('Arial', 10))
    style.configure('TCombobox', fieldbackground='#2a2d34', foreground='white', font=('Arial', 10))
    style.configure('TLabel', background='#2a2d34', foreground='white', font=('Arial', 10))
    style.configure('TFrame', background='#2a2d34')
    style.configure('TListbox', background='#2a2d34', foreground='white', font=('Arial', 10))

# Funktion zum Anzeigen des Logos
def display_logo():
    logo_path = os.path.join(os.path.dirname(__file__), "Speakeasy_logo_1080p.webp")
    if os.path.exists(logo_path):
        try:
            img = Image.open(logo_path)
            img = img.resize((600, 600), Image.LANCZOS)
            logo_img = ImageTk.PhotoImage(img)
            logo_label.config(image=logo_img)
            logo_label.image = logo_img
        except Exception as e:
            print(f"Fehler beim Laden des Logos: {e}")
    else:
        print(f"Logo nicht gefunden: {logo_path}")

# Hauptfunktion
def main():
    global root, main_frame, original_text_widget, translated_text_widget, gespeicherte_liste # wir packen alle unsere frames und widget in der main rein
    global gespeicherte_uebersetzungen, language_combobox, logo_label                         # damit koennen wir alle aufrufen
    
    # Initialisierung der Variablen
    gespeicherte_uebersetzungen = []
    
    # Erstellung des Hauptfensters
    root = ThemedTk(theme="arc")                                                               # ThemedTk für besseres Aussehen verwenden, mit den Theme 'arc'
    root.geometry("1000x800")
    root.title("Speakeasy Übersetzer")
    
    # Stile konfigurieren
    configure_styles()                                                                              # Wir rufen die Funktion die die BUttons konfiguriert     
    
    # Frame für das Logo (beim Start angezeigt)
    logo_frame = ttk.Frame(root)                                                                   # Wir stellen unser Widget-behaelter auf unser Hauptfenster
    logo_frame.pack(fill=tk.BOTH, expand=True)                                                     # wir setzten die Groeße des Frames ein
    root.logo_frame = logo_frame                                                                   # logo_frame kann jetzt außerhalb der def aufgerufen werden .
    
    logo_label = ttk.Label(logo_frame, text="Speakeasy Übersetzer", font=('Arial', 20))             # Wir setzen den titel des Fensters ein
    logo_label.pack(pady=20)
    
    # Logo anzeigen
    display_logo()
    
    welcome_label = ttk.Label(logo_frame, text="Willkommen bei Speakeasy Übersetzer."               # Neues Label im logo_Frame mit Willkommen-text
                        "\nBitte wählen Sie eine Datei aus, um zu beginnen.", 
                          font=('Arial', 12))
    welcome_label.pack(pady=10)
    
    browse_button = ttk.Button(logo_frame, text="Datei auswählen", command=open_file_dialog)        # Wir sezten user filebrowser Button im Frame
    browse_button.pack(pady=20)
    
    # Hauptframe (beim Start unsichtbar)
    main_frame = ttk.Frame(root)                                                                    #Wir setzen ein neues Main-frame ein auf unser root
    
    # Frame für Buttons oben
    button_frame = ttk.Frame(main_frame)                                                            # auf diesen Frame wollen ein Frame ( Frameception)
    button_frame.pack(side=tk.TOP, pady=5)                                                          # auf der wir verschiede Sachen einfuegen werden
    
    btn_open = ttk.Button(button_frame, text="Datei auswählen", command=open_file_dialog)           # ein neuer Filebrowser button (um neue/ andere Datei zu offnen)
    btn_open.pack(side=tk.LEFT, padx=5)
    
    # Dropdown für Sprachauswahl
    language_combobox = ttk.Combobox(button_frame, values=list(LANG_MAPPING.keys()))                    # Combobox fuer Sprache auswahl der auf einen Dictionnary zugreift
    language_combobox.pack(side=tk.LEFT, padx=5)
    language_combobox.set("Englisch")  # Standardsprache
    
    # Button zum Übersetzen
    btn_translate = ttk.Button(button_frame, text="Übersetzen",                             
                           command=lambda: threading.Thread(target=lambda: translate_and_display(       # Buttonbefehlt um den text zu uebersetzten
                               original_text_widget.get("1.0", tk.END),                                 # nimmt den Text im linken Fenster
                               language_combobox.get(),                                                 # nimmt die Sprache aus der Combobox. 
                               translated_text_widget)).start())                                        # schreibt den Befehlt ...
    btn_translate.pack(side=tk.LEFT, padx=5)                                                            # in der ausgewaehlte Stelle (rechtes Fenster)
                                                                                                        # threading.Thread ist ein Befehlt damit Tkinter nicht 'freezed' wahrend er arbeitet.
    # Button zum Generieren von Audio
    btn_generate_audio = ttk.Button(button_frame, text="Audio generieren",                              # Neuer Knopf 
                                command=lambda: threading.Thread(target=lambda: generate_audio(         # generate_audio Befehl
                                    translated_text_widget.get("1.0", tk.END),                          # nimmt den ganzen Text des rechten Fensters
                                    language_combobox.get())).start())                                  # nimmt wieder die ausgewaehlte Sprache
    btn_generate_audio.pack(side=tk.LEFT, padx=5)                                                       # text und sprache auswahlt -> generate_audio -> .mp3
    
    # Button zum Abspielen/Stoppen von Audio
    btn_audio = ttk.Button(button_frame, text="Audio abspielen/stoppen", command=play_audio)            # NEUER KNOPF der Befehl play_audio aufruft
    btn_audio.pack(side=tk.LEFT, padx=5)
    
    # Button zum Speichern
    btn_save = ttk.Button(button_frame, text="Speichern", command=save_current_translation)             # Speicherknopf
    btn_save.pack(side=tk.LEFT, padx=5)
    
    # Frame für Textfelder (links und rechts)
    text_frame = ttk.Frame(main_frame)                                                                  # TextFrame im Main-frame fur Textfeld links und rechts
    text_frame.pack(side=tk.LEFT, pady=10, fill=tk.BOTH, expand=True)                                   # mach dich breit Junge !
    
    # Linkes Textfeld für Originaltext
    original_text_label = ttk.Label(text_frame, text="Originaltext:", font=('Arial', 10))               # Erstellung eines Label der text_frame gehoert, wo der original.txt eingefegt wird durch text=
    original_text_label.pack(side=tk.LEFT, padx=10, pady=5, anchor=tk.N)                                # Positionning vom Textlabel
    original_text_widget = tk.Text(text_frame, height=15, width=40, bg="#2a2d34", fg="white", insertbackground="white", font=('Arial', 10)) # Farben vom Hintergrund, Text und Maus
    original_text_widget.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.BOTH, expand=True)                 # Positionning vom Widget
    
    # Rechtes Textfeld für die Übersetzung
    translated_text_label = tk.Label(text_frame, text="Übersetzter Text:", bg="#2a2d34", fg="white", font=('Arial', 10))        # Potato patata
    translated_text_label.pack(side=tk.RIGHT, padx=10, pady=5, anchor=tk.N)
    translated_text_widget = tk.Text(text_frame, height=15, width=40, bg="#2a2d34", fg="white", insertbackground="white", font=('Arial', 10))
    translated_text_widget.pack(side=tk.RIGHT, padx=10, pady=5, fill=tk.BOTH, expand=True)
    
    # Frame für die Liste der gespeicherten Übersetzungen
    list_frame = ttk.Frame(main_frame)                                                                  # Neuer Frame innerhalb des Main-Frame
    list_frame.pack(side=tk.RIGHT, pady=10, fill=tk.BOTH, expand=True)                                  # Plazierung rechts, groeße etc.
    
    # Beschriftung für die Liste
    list_label = ttk.Label(list_frame, text="Gespeicherte Übersetzungen:", font=('Arial', 10))          # Label wo die Liste angezeigt wird durch text= []
    list_label.pack(side=tk.TOP, padx=5, pady=5)
    
    gespeicherte_liste = tk.Listbox(list_frame, bg="#2a2d34", fg="white", font=('Arial', 10), selectmode=tk.SINGLE) #Listbox wo User auf Elemente zugreifen kann tk.SINGLE = nur ein aufs Mal
    gespeicherte_liste.pack(fill=tk.BOTH, expand=True)
    gespeicherte_liste.bind('<<ListboxSelect>>', on_listbox_select)                                     # Verknuepft die "Auswahl" des users in der Listbox mit einen Befehlt
    
    # Starten der Hauptschleife
    load_data_from_file()

    root.mainloop()

# Anwendung starten
if __name__ == "__main__":
    main()