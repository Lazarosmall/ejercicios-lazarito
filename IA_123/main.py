from speech import escuchar, hablar
from music_player import reproducir_musica
from info_search import buscar_informacion
from jokes_stories import contar_chiste, contar_cuento

def main():
    hablar("Hola puto, soy tu asistente. ¿En qué puedo ayudarte hoy pinche perra?")
    while True:
        comando = escuchar()
        if "musica" in comando:
            hablar("Entendido, reproduciendo música.")
            reproducir_musica()
        elif "buscar" in comando:
            hablar("¿Qué quieres buscar?")
            consulta = escuchar()
            resultado = buscar_informacion(consulta)
            hablar(resultado)
        elif "chiste" in comando:
            chiste = contar_chiste()
            hablar(chiste)
        elif "cuento" in comando:
            cuento = contar_cuento()
            hablar(cuento)
        elif "salir" in comando:
            hablar("¡Adiós! Espero haberte hecho reír.")
            break
        else:
            hablar("Lo siento, no entendí eso. ¿Puedes repetirlo?")

if __name__ == "__main__":
    main()
