import yt_dlp
import vlc
import time

# Crear instancia de VLC sin video
vlc_instance = vlc.Instance("--no-video")

def buscar_y_reproducir(nombre_cancion):
    print(f"🔍 Buscando: {nombre_cancion}")
    
    opciones = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'extract_flat': True
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        try:
            resultados = ydl.extract_info(f"ytsearch:{nombre_cancion}", download=False)['entries']
            if not resultados:
                print("❌ No encontré la canción.")
                return

            url_video = resultados[0]['url']
            print(f"✅ Encontrado: {resultados[0]['title']}")
            reproducir_audio_youtube(f"https://www.youtube.com/watch?v={url_video}")
        
        except Exception as e:
            print(f"❌ Error al buscar: {str(e)}")

def reproducir_audio_youtube(url):
    try:
        opciones = {
            'format': 'bestaudio',
            'quiet': True
        }

        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=False)
            stream_url = info['url']

        media = vlc_instance.media_new(stream_url)
        player = vlc_instance.media_player_new()
        player.set_media(media)
        player.play()
        
        print("🎧 Reproduciendo audio...")
        time.sleep(info['duration'])  # Espera la duración total
    except Exception as e:
        print(f"❌ Error al reproducir: {str(e)}")
