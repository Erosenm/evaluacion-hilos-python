import threading
import time

def tarea_hilo(nombre, duracion):
    print(f"-> [Inicio] Hilo {nombre} comenzando su ejecucion.")
    for i in range(3):
        print(f"   Hilo {nombre} - Paso {i+1}")
        time.sleep(duracion) # Simula trabajo o espera
    print(f"<- [Fin] Hilo {nombre} ha terminado.")

if __name__ == "__main__":
    print("=== INICIO DEL PROGRAMA PRINCIPAL (MAIN) ===")

    # Creación de tres hilos
    hilo1 = threading.Thread(target=tarea_hilo, args=("A", 1))
    hilo2 = threading.Thread(target=tarea_hilo, args=("B", 1))
    hilo3 = threading.Thread(target=tarea_hilo, args=("C", 1))

    # Iniciar los hilos
    hilo1.start()
    hilo2.start()
    hilo3.start()

    # Esperar a que todos terminen
    hilo1.join()
    hilo2.join()
    hilo3.join()

    print("=== FIN ===")