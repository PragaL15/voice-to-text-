import speech_recognition as sr
import io

def convert_audio(audio_data):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    try:
        # Convert byte data to AudioData instance
        audio = sr.AudioData(audio_data, sample_rate=16000, sample_width=2)  # Adjust sample rate and width as needed

        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        raise Exception(f"Could not request results from the service: {e}")
    except Exception as e:
        raise Exception(f"Error processing audio: {e}")
