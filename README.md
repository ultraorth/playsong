# Playsong 🎵

Playsong is a simple and lightweight CLI application that lets you play songs on YouTube directly from your terminal. Whether you're a music lover or just want to quickly play a song, Playsong has you covered!

---

## ✨ Features

- **Play Songs**: Search and play any song on YouTube.
- **Check for Updates**: Easily check if a new version is available.
- **Self-Upgrade**: Upgrade to the latest version with a single command.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## 🚀 Installation

### 1. Download the Executable

- Download the latest release for your platform from the [Releases page](https://github.com/ultraorth/playsong/releases).

### 2. Add to PATH

- **Linux/macOS**:

  1. Move the executable to `/usr/local/bin`:
     ```bash
     sudo mv playsong /usr/local/bin/playsong
     ```
  2. Make it executable:
     ```bash
     chmod +x /usr/local/bin/playsong
     ```
  3. (Optional) Create a symlink for the `play` command:
     ```bash
     sudo ln -s /usr/local/bin/playsong /usr/local/bin/play
     ```

- **Windows**:
  1. Move the executable (`playsong.exe`) to a directory in your `PATH`, such as `C:\Windows\System32`.
  2. (Optional) Create a copy named `play.exe` for the `play` command.

### 3. Add a YouTube API Key

1. Create a `config.json` file in the same directory as the executable.
2. Add your YouTube API key:
   ```json
   {
     "YOUTUBE_API_KEY": "your_api_key_here"
   }
   ```
