# Evaluación Continua 1: Hilos con Python

## Descripción de la Tarea
Este repositorio contiene la implementación en Python del uso de hilos concurrentes utilizando la librería estándar `threading`, junto con capturas de pantalla de las pruebas de ejecución y su respectiva interpretación de comportamiento.

---

## Contenido del Repositorio
* **hilos.py**: Código fuente en Python que implementa la ejecución concurrente de hilos con retardos y conteos.
* **1.jpeg / 2.jpeg / 3.jpeg / 4.jpeg**: Capturas de pantalla de la terminal mostrando la ejecución del programa con diferentes configuraciones de hilos y tiempos.

---

## Interpretación del Comportamiento
Durante la ejecución del programa, se observa que los mensajes impresos por cada hilo no aparecen en un orden estrictamente secuencial, sino que se **intercalan**. 

Esto ocurre debido a la **concurrencia** gestionada por el planificador (scheduler) del sistema operativo. Al utilizar hilos (`threading.Thread`), el procesador alterna rápidamente la ejecución entre el hilo principal y los hilos creados (Hilo A, Hilo B, etc.). Las funciones `time.sleep()` simulan tiempos de espera o tareas de procesamiento, lo que permite que el control pase de un hilo a otro de manera dinámica, demostrando cómo múltiples tareas pueden avanzar de forma simultánea dentro del mismo proceso.
