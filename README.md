## Overview

This repository contains two Python-based GUI applications designed to modify game configuration settings easily: **Language Changer** and **Easy Overlay Settings**. Both applications use Tkinter for a simple and user-friendly interface.

---

## Language Changer

### Features
- Select a language from a predefined list.
- Reads and updates the game configuration file automatically.
- Provides user feedback with warnings and success messages.
- Includes a Discord support button for assistance.

### How It Works
1. **Loading Configuration:**
   - The tool works without requiring `language_changer.ini`.
   - If `language_changer.ini` exists, it allows specifying a custom folder location.
   - The application checks for `configs.user.ini` and `supported_languages.txt` in the specified directory.

2. **Loading Supported Languages:**
   - Reads `supported_languages.txt` if available.
   - Defaults to a predefined list of languages if the file is missing.

3. **Updating Language:**
   - Users select a language from the dropdown menu.
   - Clicking "Apply Language" updates the `language` field in `configs.user.ini`.
   - If the file is missing, a warning is displayed.

4. **Support on Discord:**
   - Clicking "Support on Discord" opens the GameDrive.Org Discord page.

---

## Easy Overlay Settings

### Features
- Toggle the "Enable Experimental Overlay" setting via a simple interface.
- Detects and updates the configuration file automatically.
- Provides user feedback with warning and success messages.
- Supports PyInstaller for packaging into a standalone executable.

### How It Works
1. **Loading Settings:**
   - The application searches for `DigitalZone/steam_settings/configs.overlay.ini`.
   - If the file does not exist, a warning message appears.
   - The script reads the `enable_experimental_overlay` value to determine its current state.

2. **Toggling Settings:**
   - Users click the toggle button to switch between `ON` and `OFF`.
   - The button dynamically updates to reflect the current selection.

3. **Saving Settings:**
   - Clicking "Save Settings" updates the configuration file (`1` for ON, `0` for OFF).
   - A success message confirms the change.
