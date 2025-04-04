import vlc
import os

# Ruta al archivo libvlc.dll (ajústala según la ubicación en tu sistema)
vlc_instance = vlc.Instance("--no-video")
vlc.libvlc_get_version()  # Verifica si se encuentra correctamente el archivo DLL

def reproducir_musica(ruta_archivo):
    try:
        # Crear un reproductor y reproducir música
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new(ruta_archivo)
        player.set_media(media)
        player.play()
        print(f"Reproduciendo: {ruta_archivo}")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
