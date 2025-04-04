import pyjokes

def contar_chiste():
    chiste = pyjokes.get_joke(language="es")
    print(f"Chiste: {chiste}")
    return chiste

def contar_cuento():
    cuento = (
        "Había una vez un programador que pensó que su código era perfecto. "
        "Hasta que su asistente virtual empezó a burlarse de él."
    )
    print(f"Cuento: {cuento}")
    return cuento
