## Integrantes:

- David Alejandro Gutiérrez Leal
- Ginna Alejandra Valencia Macuace
- Kadiha Muhamad Orta
- **Código de clase:** 7308
  
**Sistema Operativo:** Windows 10

**Lenguaje de programación utilizado:** Python 3.12

**Herramientas:** PyCharm 2024.2.4 / onlineGDB

## Instrucciones para la Ejecución:

Para ejecutar el código, se debe crear o descargar un archivo de texto que contenga ejemplos de DFA con el formato especificado indicado dentro del documento correspondiente a esta actividad. El archivo debe guardarse en la misma carpeta donde se encuentra el script de Python, o en su defecto, se debe proporcionar la ruta completa en la variable nombre_archivo dentro de la función main(). Una vez realizado este ajuste, se ejecuta el script en un entorno compatible con Python 3. Si el archivo no se encuentra o su formato es incorrecto, el programa mostrará un mensaje de error y finalizará su ejecución.

## Explicación del Algoritmo:

Esta implementación encuentra estados equivalentes en un Autómata Finito Determinista (DFA) utilizando refinamiento de particiones:

**Inicialización de particiones:** Los estados se dividen en dos grupos: estados finales y estados no finales.

### Refinamiento iterativo de particiones:

- A cada estado se le asigna una firma basada en sus transiciones y a qué partición conducen esas transiciones.
- Los estados con las mismas firmas de transición permanecen en la misma partición.
- Si un estado tiene transiciones a particiones diferentes en comparación con otro estado en la misma partición, se crea una nueva partición.

Este proceso se repite hasta que las particiones ya no cambien.

**Extracción de estados equivalentes:**

Al final del proceso de particionamiento, los estados que permanecen en la misma partición se consideran equivalentes.

El algoritmo genera estos pares de estados equivalentes como salida.
