import speech_recognition as sr
import pyttsx3
import yt_dlp
import vlc
import time
#esto es lago que agrego porque quiero

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad de habla
engine.setProperty('voice', 'spanish')  # Voz en español

# Inicializar el reproductor de VLC
vlc_instance = vlc.Instance('--no-video')
player = vlc_instance.media_player_new()

def hablar(texto):
    """Función para que el asistente hable."""
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    """Función para reconocer comandos de voz."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustar al ruido ambiental
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            comando = recognizer.recognize_google(audio, language='es-ES')
            print(f"Dijiste: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            hablar("No entendí lo que dijiste. ¿Podrías repetirlo?")
            return ""
        except sr.RequestError:
            hablar("No puedo conectarme al servicio de reconocimiento de voz.")
            return ""

def buscar_y_reproducir(nombre_cancion):
    """Función para buscar y reproducir una canción desde YouTube."""
    hablar(f"Buscando {nombre_cancion} en YouTube...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'extract_flat': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            resultados = ydl.extract_info(f"ytsearch:{nombre_cancion}", download=False)['entries']
            if not resultados:
                hablar("No encontré la canción.")
                return
            url_audio = resultados[0]['url']
            media = vlc_instance.media_new(url_audio)
            player.set_media(media)
            player.play()
            hablar(f"Reproduciendo {resultados[0]['title']}")
            time.sleep(1)  # Esperar un momento antes de continuar
        except Exception as e:
            hablar(f"Hubo un error al buscar o reproducir la canción: {e}")

def main():
    """Función principal que ejecuta el asistente de voz."""
    hablar("Hola, soy tu asistente de voz. ¿Qué canción te gustaría escuchar?")
    while True:
        comando = escuchar()
        if comando:
            buscar_y_reproducir(comando)
        else:
            break

if __name__ == "__main__":
    main()
