def leer_dfa(nombre_archivo):
    """
    Leer un DFA desde un archivo TXT con el formato:
    1. Número de estados.
    2. Alfabeto separado por espacios.
    3. Estados finales separados por espacios.
    4. Transiciones: Cada línea tiene tres números (estado, transición con 'a', transición con 'b').
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()

        num_casos = int(contenido[0].strip())
        casos = []
        indice = 1

        for _ in range(num_casos):
            # Leer número de estados
            n_estados = int(contenido[indice].strip())
            indice += 1

            # Leer alfabeto
            alfabeto = contenido[indice].strip().split()
            indice += 1

            # Leer estados finales
            estados_finales = set(map(int, contenido[indice].strip().split()))
            indice += 1

            # Leer la función de transición
            transiciones = {}
            for _ in range(n_estados):
                fila = list(map(int, contenido[indice].strip().split()))
                estado_actual = fila[0]
                transiciones[estado_actual] = {alfabeto[i]: fila[i + 1] for i in range(len(alfabeto))}
                indice += 1

            # Guardar el caso del DFA
            casos.append((n_estados, alfabeto, estados_finales, transiciones))

        return casos

    except FileNotFoundError:
        print("Error: No se encontró el archivo")
        return []
    except ValueError as e:
        print(f"Error en el formato del archivo: {e}")
        return []


def encontrar_pares_equivalentes_con_particiones(n_estados, estados_finales, transiciones):
    """
    Encuentra pares de estados equivalentes usando particiones.
    """
    # Paso 1: Dividir estados en dos particiones iniciales: finales y no-finales
    particiones = [
        {estado for estado in range(n_estados) if estado in estados_finales},  # Estados finales
        {estado for estado in range(n_estados) if estado not in estados_finales}  # Estados no finales
    ]
    particiones = [p for p in particiones if p]  # Eliminar particiones vacías

    # Paso 2: Refinar las particiones iterativamente
    refinando = True
    while refinando:
        refinando = False
        nuevas_particiones = []

        for grupo in particiones:
            # Dividir el grupo según las transiciones hacia las particiones actuales
            divisiones = {}
            for estado in grupo:
                # Crear una clave basada en las transiciones del estado hacia las particiones
                clave = tuple(
                    next((i for i, part in enumerate(particiones) if transiciones[estado][simbolo] in part), None)
                    for simbolo in transiciones[estado]
                )
                divisiones.setdefault(clave, set()).add(estado)

            # Agregar las nuevas divisiones resultantes del grupo
            nuevas_particiones.extend(divisiones.values())

        # Si hubo cambios en las particiones, seguimos refinando
        if len(nuevas_particiones) > len(particiones):
            refinando = True
        particiones = nuevas_particiones

    # Paso 3: Extraer pares equivalentes de las particiones finales
    equivalentes = []
    for grupo in particiones:
        estados = sorted(grupo)  # Ordenamos para generar pares ordenados
        for i in range(len(estados)):
            for j in range(i + 1, len(estados)):
                equivalentes.append((estados[i], estados[j]))

    return equivalentes


def main():
    """
    Leer archivo y procesar los estados equivalentes para cada DFA encontrado.
    """
    nombre_archivo = "Ejemplo1.txt"  # Ajusta el nombre del archivo según sea necesario
    casos = leer_dfa(nombre_archivo)

    if not casos:
        return

    for i, (n_estados, alfabeto, estados_finales, transiciones) in enumerate(casos):
        equivalentes = encontrar_pares_equivalentes_con_particiones(n_estados, estados_finales, transiciones)

        # Imprimir el encabezado del DFA
        print(f"DFA {i + 1}")

        # Imprimir los pares equivalentes
        if equivalentes:
            print(" ".join(f"({par[0]}, {par[1]})" for par in equivalentes))
        else:
            print()  # Línea vacía si no hay estados equivalentes


main()











