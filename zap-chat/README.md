# ⚡ Zap Chat

A playful CLI chatbot powered by [Ollama](https://ollama.com) — runs entirely locally, no API key needed.

## Requirements

- [Python 3.x](https://python.org)
- [Ollama](https://ollama.com) installed and running

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/Mr4gem/Zap-CLI-Chatbot.git
cd Zap-CLI-Chatbot
```

**2. Install the Python dependency**
```bash
pip install ollama
```

**3. Pull a model**
```bash
ollama pull llama3.2
```

**4. Run it**
```bash
python chatbot_cli.py
```

## Make it a global command (optional)

**Windows (cmd)** — add `zap.bat` to a folder on your PATH, or from the project folder:
```cmd
copy zap.bat C:\Windows\System32\zap.bat
```

**PowerShell** — add this to your `$PROFILE`:
```powershell
function zap { python "C:\path\to\zap-chat\chatbot_cli.py" @args }
```

Then just type `zap` anywhere.

## Changing the model

Edit the `MODEL` line at the top of `chatbot_cli.py`:
```python
MODEL = "llama3.2"  # swap for any model you have pulled
```

Any model from [ollama.com/library](https://ollama.com/library) works.

## Commands

| Command | Action |
|---------|--------|
| `new` | Wipe conversation history and start fresh |
| `help` | Show available commands |
| `quit` | Exit the chatbot |
