'''
NAME: Conteo de Bases de ADN

VERSION: 1.0

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





# ===========================================================================
# =                            Command Line Options
# ===========================================================================






# ===========================================================================
# =                            functions
# ===========================================================================





# ===========================================================================
# =                            main
# ===========================================================================
cadena_ADN = input('Inserte el nombre de su archivo a continuación: ')

A=C=G=T = 0

with open(cadena_ADN) as secuencia:
  for linea in secuencia:
    for letra in linea:
      if letra.upper() == 'A':
        A += 1
      if letra.upper() == 'C': 
        C += 1
      if letra.upper() == 'T':
        T += 1 
      if letra.upper() == 'G':
        G += 1

print(f'Cantidad de A:{A}, C:{C}, T:{T}, G:{G}')
