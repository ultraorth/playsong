# Playsong 🎵

Playsong is a simple command-line application to search and play songs from YouTube directly from your terminal.

---

## Features

- **Search and Play Songs**: Instantly play any song on YouTube.
- **Lightweight**: Minimal setup and easy to use.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## Installation

1. **Download**: Get the latest release from the [Releases page](https://github.com/ultraorth/playsong/releases).
2. **Add to PATH**:

   - **Linux/macOS**:
     ```bash
     sudo mv playsong /usr/local/bin/
     chmod +x /usr/local/bin/playsong
     ```
   - **Windows**: Place `playsong.exe` in a folder included in your system `PATH` (e.g., `C:\Windows\System32`).

3. **Set Up API Key**: Create a `config.json` file in the same directory as the executable:
   ```json
   {
     "YOUTUBE_API_KEY": "your_api_key_here"
   }
   ```
