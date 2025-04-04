import speech_recognition as sr
import pyttsx3

# Función para hablar
def hablar(texto):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    # Buscar una voz en español
    for voz in engine.getProperty("voices"):
        if "spanish" in voz.name.lower():
            engine.setProperty("voice", voz.id)
            break

    engine.say(texto)
    engine.runAndWait()

# Función para escuchar mejorando claridad
def escuchar():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando al ruido ambiental...")
        recognizer.adjust_for_ambient_noise(source, duration=1.5)  # ✅ Mejora comprensión

        print("Escuchando...")
        try:
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=7)  # más tiempo para hablar
            comando = recognizer.recognize_google(audio, language="es-ES")  # Puedes cambiar a "es-MX" si hablas mexicano
            print(f"Dijiste: {comando}")
            return comando.lower()

        except sr.UnknownValueError:
            hablar("No entendí lo que dijiste.")
            return ""
        except sr.RequestError:
            hablar("No puedo conectarme al servicio de reconocimiento de voz.")
            return ""
