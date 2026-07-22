# app.py
from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

# This holds the memory of our conversation
conversation_history = [
    {"role": "system", "content": "You are a helpful, concise AI assistant."}
]

@app.route('/')
def home():
    # Serves the HTML page when you open the browser
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # 1. Get the user's message from the web browser
    user_input = request.json.get('message')
    
    # 2. Add it to our conversation memory
    conversation_history.append({"role": "user", "content": user_input})
    
    try:
        # 3. Send the whole history to Ollama
        response = ollama.chat(model='qwen2.5:1.5b', messages=conversation_history)
        ai_reply = response['message']['content']
        
        # 4. Save the AI's reply to memory
        conversation_history.append({"role": "assistant", "content": ai_reply})
        
        # 5. Send the reply back to the browser
        return jsonify({"reply": ai_reply})
        
    except Exception as e:
        return jsonify({"reply": f"Error connecting to Ollama: {str(e)}"}), 500

if __name__ == '__main__':
    # Starts the server on port 5000
    app.run(debug=True, port=5000)