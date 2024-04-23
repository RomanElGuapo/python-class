# -*- coding: utf-8 -*-

'''
NAME: Conteo de Bases de ADN

VERSION: 2.2

AUTHOR: Ángel Román Zamora López

DESCRIPTION: Este programa cuenta las bases de ADN (A, C, G, T) presentes en un archivo de secuencia de ADN.

CATEGORY: Biología / Bioinformática

USAGE:

    % python programName

ARGUMENTS:

    - Ninguno

METHOD:

    El programa utiliza un enfoque de lectura de archivo línea por línea y cuenta las ocurrencias de cada base de ADN (A, C, G, T) en la secuencia.

SEE ALSO:

    - Documentación oficial de Python: https://docs.python.org/3/

'''

# ===========================================================================
# =                            imports
# ===========================================================================

import argparse

# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# No se requieren opciones de línea de comandos adicionales.

# ===========================================================================
# =                            functions
# ===========================================================================

# No se requieren funciones adicionales.

# ===========================================================================
# =                            main
# ===========================================================================

# Se define un analizador de argumentos para manejar las opciones de línea de comandos.
parser = argparse.ArgumentParser(description="Lee archivo de entrada y salida")

# Se agrega un argumento posicional para el archivo de entrada.
parser.add_argument("input_file", type=str, help="El archivo de texto que quieres procesar.")

# Se agrega un argumento opcional para especificar el nucleótido cuyo conteo se desea obtener.
parser.add_argument('-n', choices=['A', 'C', 'T','G'],
                    help='Elige tu nucleotido')

# Se analizan los argumentos de la línea de comandos.
args = parser.parse_args()

# Se guarda la ruta del archivo de ADN en una variable.
cadena_ADN = args.input_file

# Se inicializan contadores para cada base de ADN.
A = C = G = T = 0

# Se abre el archivo de ADN para su procesamiento.
try:
    with open(cadena_ADN) as raw_text:
        secuencia = raw_text.readlines()
        if len(secuencia) == 0:
            print('Empty file')
except:
    print('Sorry, couldnt find the file')
        
# Se itera sobre cada línea del archivo.
for linea in secuencia:
    # Se itera sobre cada letra en la línea.
    for letra in linea:
        # Se incrementa el contador correspondiente a la base de ADN encontrada.
        if letra.upper() == 'A':
            A += 1
        elif letra.upper() == 'C': 
            C += 1
        elif letra.upper() == 'T':
            T += 1 
        elif letra.upper() == 'G':
            G += 1
        else:
            try:
                raise ValueError()
            except:
                print('Caracter invalido',letra)
                exit()
# Se imprime el conteo de la base de ADN especificada por el usuario, si se proporcionó.
if args.n == 'A':
    print('Cantidad de A:', A)
if args.n == 'C':
    print('Cantidad de C:', C)
if args.n == 'T':
    print('Cantidad de T:', T)
if args.n == 'G':
    print('Cantidad de G:', G)

# Si no se especifica ninguna base de ADN, se imprime el conteo de todas las bases.
if not args.n:
    print('Cantidad de A:', A, 'C:', C, 'T:', T, 'G:', G)
