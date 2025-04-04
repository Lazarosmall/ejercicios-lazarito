import wikipedia

def buscar_informacion(consulta):
    try:
        wikipedia.set_lang("es")
        resumen = wikipedia.summary(consulta, sentences=2)
        print(f"Resultado: {resumen}")
        return resumen
    except wikipedia.exceptions.PageError:
        return "No encontré información sobre eso."
    except Exception as e:
        return "Ocurrió un error durante la búsqueda."
