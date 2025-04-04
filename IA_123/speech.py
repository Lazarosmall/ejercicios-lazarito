import speech_recognition as sr
import pyttsx3

def hablar(texto):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("voice", "spanish")  # Cambiar la voz a español
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            comando = recognizer.recognize_google(audio, language="es-ES")
            print(f"Dijiste: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            hablar("No entendí lo que dijiste.")
            return ""
        except sr.RequestError:
            hablar("No puedo conectarme al servicio de reconocimiento de voz.")
            return ""
