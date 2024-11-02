from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import wave
import io
import speech_recognition as sr
import logging

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # Set max file size to 5MB
CORS(app, resources={r"/convert": {"origins": "http://localhost:5173"}})

# Setup logger for better debugging
logging.basicConfig(level=logging.INFO)
logger = app.logger
logger.setLevel(logging.INFO)

recognizer = sr.Recognizer()

@app.before_request
def log_request_info():
    logger.info(f"Received {request.method} request on {request.path}")

@app.route('/convert', methods=['POST'])
def convert_audio():
    if 'audio_data' not in request.files:
        logger.error("No audio file uploaded")
        return jsonify({'error': 'No audio file uploaded'}), 400

    audio_file = request.files['audio_data']

    try:
        # Verify the audio file is in WAV format
        with wave.open(audio_file, 'rb') as wav_file:
            wav_file.getnchannels()  # Check we can read the file
        audio_file.seek(0)  # Reset file pointer for further reading
    except wave.Error:
        logger.error("Uploaded file is not in WAV format")
        return jsonify({'error': 'Uploaded file is not in WAV format'}), 400

    # Process audio for speech recognition
    audio_data = sr.AudioFile(audio_file)
    try:
        with audio_data as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Improved ambient noise adjustment
            audio = recognizer.record(source)

        # Attempt to recognize the speech
        text = recognizer.recognize_google(audio)
        logger.info("Speech recognized successfully")
        return jsonify({'text': text}), 200

    except sr.UnknownValueError:
        logger.error("Speech Recognition could not understand audio")
        return jsonify({'error': 'Could not understand audio. Please speak clearly.'}), 400
    except sr.RequestError as e:
        logger.error(f"Request to Google Speech Recognition failed: {e}")
        return jsonify({'error': 'Could not process audio. Please try again later.'}), 503
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred. Please try again.'}), 500

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

@app.errorhandler(413)
def file_too_large(error):
    return jsonify({'error': 'File is too large. Maximum size is 5MB.'}), 413

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
