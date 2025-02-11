# Easy Overlay Settings

## Overview
Easy Overlay Settings is a simple Python application with a Tkinter-based GUI that allows users to enable or disable the experimental overlay feature by modifying a configuration file.

## Features
- Toggle the "Enable Experimental Overlay" setting using a user-friendly interface.
- Automatically detects the configuration file and updates its contents.
- Provides user feedback with warning and success messages.
- Supports PyInstaller packaging for standalone execution.

## How It Works
1. **Loading Settings:**
   - The script checks for the configuration file located at `DigitalZone/steam_settings/configs.overlay.ini`.
   - If the file does not exist, a warning message appears.
   - The script reads the `enable_experimental_overlay` value to determine the current state.

2. **Toggling Settings:**
   - Clicking the toggle button switches between `ON` and `OFF` states.
   - The button label updates dynamically to reflect the selected state.

3. **Saving Settings:**
   - Clicking "Save Settings" writes the updated value (`1` for ON, `0` for OFF) to the configuration file.
   - A success message appears if the operation is successful.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contributing
Feel free to submit pull requests or report issues to improve this tool!
