'''
NAME: 
       

VERSION:
        

AUTHOR: ANGEL ROMAN ZAMORA LOPEZ
        

DESCRIPTION: 
        

CATEGORY
        

USAGE

    % python programName
    

ARGUMENTS


METHOD


SEE ALSO


        
'''


# ===========================================================================
# =                            imports
# ===========================================================================





# ===========================================================================
# =                            Command Line Options
# ===========================================================================






# ===========================================================================
# =                            functions
# ===========================================================================





# ===========================================================================
# =                            main
# ===========================================================================
def contar_bases(archivo):
    # Inicializamos los contadores
    contador_A = 0
    contador_T = 0
    contador_C = 0
    contador_G = 0

    # Abrimos el archivo en modo lectura
    with open(archivo, 'r') as f:
        # Leemos la secuencia de ADN línea por línea
        for linea in f:
            # Iteramos sobre cada carácter en la línea
            for base in linea.strip():
                # Incrementamos el contador correspondiente según la base
                if base == 'A':
                    contador_A += 1
                elif base == 'T':
                    contador_T += 1
                elif base == 'C':
                    contador_C += 1
                elif base == 'G':
                    contador_G += 1

    # Devolvemos un diccionario con los contadores
    return {
        'A': contador_A,
        'T': contador_T,
        'C': contador_C,
        'G': contador_G
    }

# Ruta al archivo que contiene la secuencia de ADN
archivo_adn = 'secuencia_adn.txt'

# Llamamos a la función para contar las bases
resultados = contar_bases(archivo_adn)

# Imprimimos los resultados
print("Cantidad de bases:")
for base, contador in resultados.items():
    print(f"{base}: {contador}")

# step 1.


# step 2.


# step 3.