import os
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

CONFIG_PATH = "DigitalZone/steam_settings/configs.overlay.ini"

class OverlaySettingsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Easy Overlay Settings")
        self.geometry("400x150")
        self.resizable(False, False)

        # Determine base path for PyInstaller compatibility
        if getattr(sys, 'frozen', False):
            base_path = Path(sys._MEIPASS)  # PyInstaller temp folder
        else:
            base_path = Path(__file__).parent

        # Set application icon
        icon_path = base_path / "icon.ico"
        if icon_path.exists():
            self.iconbitmap(str(icon_path))

        self.current_status = False
        self.create_ui()
        self.load_setting()

    def create_ui(self):
        """Creates the UI elements."""
        self.label = ttk.Label(self, text="Enable Experimental Overlay:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.toggle_frame = ttk.Frame(self)
        self.toggle_frame.pack(pady=5)

        self.toggle_button = ttk.Button(self.toggle_frame, text="OFF", width=10, command=self.toggle_setting)
        self.toggle_button.pack()

        self.save_button = ttk.Button(self, text="Save Settings", command=self.save_setting)
        self.save_button.pack(pady=10)

    def load_setting(self):
        """Loads the current setting from the INI file."""
        if not Path(CONFIG_PATH).exists():
            messagebox.showwarning("Warning", f"Config file not found: {CONFIG_PATH}\nCreating a new one.")
            return

        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as file:
                for line in file:
                    if line.startswith("enable_experimental_overlay="):
                        value = line.strip().split("=")[1]
                        self.current_status = value == "1"
                        self.update_toggle()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read config file: {e}")

    def toggle_setting(self):
        """Toggles the overlay setting."""
        self.current_status = not self.current_status
        self.update_toggle()

    def update_toggle(self):
        """Updates the toggle button appearance."""
        if self.current_status:
            self.toggle_button.config(text="ON", style="TButton")
        else:
            self.toggle_button.config(text="OFF", style="TButton")

    def save_setting(self):
        """Saves the updated setting to the INI file."""
        new_value = "1" if self.current_status else "0"
        try:
            lines = []
            with open(CONFIG_PATH, "r", encoding="utf-8") as file:
                lines = file.readlines()

            with open(CONFIG_PATH, "w", encoding="utf-8") as file:
                for line in lines:
                    if line.startswith("enable_experimental_overlay="):
                        file.write(f"enable_experimental_overlay={new_value}\n")
                    else:
                        file.write(line)

            messagebox.showinfo("Success", "Overlay setting updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update setting: {e}")

if __name__ == "__main__":
    app = OverlaySettingsApp()
    app.mainloop()
