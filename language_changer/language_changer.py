import os
import sys
import configparser
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

DEFAULT_CONFIG_PATH = "steam_settings"
CONFIG_FILE = "language_changer.ini"

class LanguageChangerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Language Changer")
        self.geometry("600x250")
        self.resizable(False, False)

        if getattr(sys, 'frozen', False):
            base_path = Path(sys._MEIPASS)
        else:
            base_path = Path(__file__).parent

        icon_path = base_path / "icon.ico"
        if icon_path.exists():
            self.iconbitmap(str(icon_path))

        self.language_map = {}
        self.load_config()
        self.load_supported_languages()
        self.create_ui()

    def load_config(self):
        """Loads configuration paths from the config file."""
        config = configparser.ConfigParser()
        config_path = DEFAULT_CONFIG_PATH  

        if os.path.exists(CONFIG_FILE):
            try:
                config.read(CONFIG_FILE)
                raw_path = config.get("Settings", "config_path", fallback=DEFAULT_CONFIG_PATH)
                config_path = os.path.normpath(raw_path)  
            except Exception as e:
                print(f"Warning: Failed to read config file {CONFIG_FILE}: {e}")

        base_path = Path(config_path).resolve()
        self.ini_file_path = base_path / "configs.user.ini"
        self.languages_file_path = base_path / "supported_languages.txt"

    def load_supported_languages(self):
        """Loads supported languages from the file or defaults to all available ones."""
        available_languages = set()

        if self.languages_file_path.exists():
            try:
                with open(self.languages_file_path, "r", encoding="utf-8") as file:
                    available_languages = {line.strip() for line in file}
            except Exception as e:
                print(f"Warning: Failed to read {self.languages_file_path}: {e}")

        all_languages = {
            "Arabic": "arabic", "Bulgarian": "bulgarian", "Chinese (Simplified)": "schinese",
            "Chinese (Traditional)": "tchinese", "Czech": "czech", "Danish": "danish",
            "Dutch": "dutch", "English": "english", "Finnish": "finnish", "French": "french",
            "German": "german", "Greek": "greek", "Hungarian": "hungarian", "Indonesian": "indonesian",
            "Italian": "italian", "Japanese": "japanese", "Korean": "koreana", "Norwegian": "norwegian",
            "Polish": "polish", "Portuguese": "portuguese", "Portuguese-Brazil": "brazilian",
            "Romanian": "romanian", "Russian": "russian", "Spanish-Spain": "spanish",
            "Spanish-Latin America": "latam", "Swedish": "swedish", "Thai": "thai",
            "Turkish": "turkish", "Ukrainian": "ukrainian", "Vietnamese": "vietnamese"
        }
        self.language_map = {name: code for name, code in all_languages.items() if not available_languages or code in available_languages}

    def update_language(self):
        """Updates the language setting in the configuration file."""
        selected_name = self.language_combobox.get()
        if not selected_name:
            messagebox.showwarning("Warning", "Please select a language.")
            return

        selected_code = self.language_map.get(selected_name)

        if not self.ini_file_path.exists():
            messagebox.showwarning("Warning", f"Config file not found: {self.ini_file_path}\nSkipping language update.")
            return
        
        try:
            lines = []
            language_updated = False
            with open(self.ini_file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            with open(self.ini_file_path, "w", encoding="utf-8") as file:
                for line in lines:
                    if line.startswith("language="):
                        file.write(f"language={selected_code}\n")
                        language_updated = True
                    else:
                        file.write(line)
                if not language_updated:
                    file.write(f"language={selected_code}\n")

            messagebox.showinfo("Success", f"Language changed to '{selected_name}'!\nRestart your game to apply changes.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update language: {e}")

    def open_discord(self):
        """Opens the Discord support link."""
        webbrowser.open("https://gamedrive.org/discord")

    def create_ui(self):
        """Creates a compact UI."""
        container = tk.Frame(self)
        container.pack(fill="none", expand=False, pady=5)

        self.label = ttk.Label(container, text="Select Game Language", font=("Arial", 14, "bold"))
        self.label.grid(row=0, column=0, pady=(5, 2))

        self.language_combobox = ttk.Combobox(container, values=list(self.language_map.keys()), width=40, state="readonly")
        self.language_combobox.grid(row=1, column=0, pady=2)

        current_lang = self.get_current_language()
        if current_lang in self.language_map:
            self.language_combobox.set(current_lang)

        self.apply_button = ttk.Button(container, text="Apply Language", command=self.update_language)
        self.apply_button.grid(row=2, column=0, pady=8, ipadx=10, ipady=5)

        self.discord_button = ttk.Button(container, text="Support on Discord", command=self.open_discord)
        self.discord_button.grid(row=3, column=0, pady=5, ipadx=10, ipady=5)

        self.footer = ttk.Label(container, text="Powered by GameDrive.Org", font=("Arial", 10, "italic"))
        self.footer.grid(row=4, column=0, pady=(5, 0))

    def get_current_language(self):
        """Reads the current language setting from the config file."""
        if not self.ini_file_path.exists():
            return "English"

        try:
            with open(self.ini_file_path, "r", encoding="utf-8") as file:
                for line in file:
                    if line.startswith("language="):
                        lang_code = line.strip().split("=")[1]
                        for name, code in self.language_map.items():
                            if code == lang_code:
                                return name
            return "English"
        except Exception as e:
            print(f"Error reading language setting: {e}")
            return "English"

if __name__ == "__main__":
    app = LanguageChangerApp()
    app.mainloop()
