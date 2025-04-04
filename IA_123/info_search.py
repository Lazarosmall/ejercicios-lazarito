import wikipediaapi

def buscar_informacion(consulta):
    try:
        wikipediaapi.set_lang("es")
        resumen = wikipediaapi.summary(consulta, sentences=2)
        print(f"Resultado: {resumen}")
        return resumen
    except wikipediaapi.exceptions.PageError:
        return "No encontré información sobre eso."
    except Exception as e:
        return "Ocurrió un error durante la búsqueda."
