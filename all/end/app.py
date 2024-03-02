from flask import Flask, render_template, request
from threading import Thread
import pyttsx3

app = Flask(__name__)
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak_route():
    text = request.form['userText']
    speak_thread = Thread(target=speak, args=(text,))
    speak_thread.start()
    return 'Text spoken successfully'

if __name__ == '__main__':
    app.run(debug=True)
