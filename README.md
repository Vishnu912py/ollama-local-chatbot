# Local AI Chat

A minimal local chat web app built with Flask that sends conversation history to an Ollama model and displays responses in a browser UI.

## Project Structure

- `app.py` - Flask application that serves the web page and handles chat requests.
- `templates/index.html` - Simple chat UI with live messaging.

## Features

- Local Flask server running on `http://127.0.0.1:5000`
- Sends conversation history to Ollama using `ollama.chat`
- Basic browser chat interface with user and assistant messages
- Error handling for Ollama connectivity issues

## Requirements

- Python 3.10+ (recommended)
- Flask
- `ollama` Python package
- Ollama server installed and running locally

## Setup

1. Install Python dependencies:

```bash
pip install flask ollama
```

2. Ensure Ollama is installed and running:

- Install Ollama from https://ollama.com/
- Start Ollama locally before running the app

3. Run the Flask app:

```bash
python app.py
```

4. Open your browser at:

```
http://127.0.0.1:5000
```

## Usage

- Type a message in the input box and press `Send` or `Enter`
- The client sends the message to `/chat`
- The server forwards the conversation history to the Ollama model
- The assistant reply appears in the chat window

## Notes

- The app currently uses the `qwen2.5:1.5b` model in `app.py`. Update the model name there if you want to use a different Ollama model.
- Conversation history is stored in memory while the Flask app runs. Restarting the app clears the history.

## Troubleshooting

- If the server returns an Ollama connection error, verify Ollama is running and accessible.
- If the port is already in use, change `port=5000` in `app.py`.

## License

This project is provided as-is for local experimentation.