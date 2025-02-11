# Language Changer

## Overview
Language Changer is a Python application with a Tkinter-based GUI that allows users to change the game language by modifying a configuration file.

## Features
- Select a language from a predefined list.
- Reads and updates the configuration file automatically.
- Provides user feedback with warnings and success messages.
- Includes a Discord support button.

## How It Works
1. **Loading Configuration:**
   - Normally, there is no need for `language_changer.ini`.
   - If `language_changer.ini` exists, it allows specifying a custom folder location.
   - The application checks for `configs.user.ini` and `supported_languages.txt` in the specified directory.

2. **Loading Supported Languages:**
   - Reads `supported_languages.txt` if available.
   - Defaults to a predefined list of languages if the file is missing.

3. **Updating Language:**
   - The user selects a language from the dropdown menu.
   - Clicking "Apply Language" updates the `language` field in `configs.user.ini`.
   - If the file is missing, a warning is displayed.

4. **Support on Discord:**
   - Clicking "Support on Discord" opens the GameDrive.Org Discord page.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contributing
Feel free to submit pull requests or report issues to improve this tool!
