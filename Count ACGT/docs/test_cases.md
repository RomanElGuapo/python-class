# Casos de prueba o escenario

Este documento describe los casos de prueba para el script de Python desarrollado para contar las bases de ADN presentes en un archivo de secuencia de ADN. El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script está diseñado para leer un archivo de secuencia de ADN y contar las ocurrencias de cada base de ADN (A, C, G, T) en la secuencia.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.

### Caso de prueba 1: Comprobación de conteo de bases de ADN
Descripción: Verificar que el script puede contar correctamente las bases de ADN en un archivo de secuencia.
Datos de entrada: Archivo de secuencia de ADN con las siguientes bases: AAAACCCGGT
Resultado esperado: Cantidad de A: 4, Cantidad de C: 3, Cantidad de G: 2, Cantidad de T: 1
Estado: Éxito

### Caso de prueba 2: Comprobación de error caracter inválido

Descripción: Verificar que el script puede manejar adecuadamente un archivo de secuencia de ADN con caracteres inválidos
Datos de entrada: Archivo de secuencia de ADN con las siguientes bases: AAAACCCGGTN
Resultado esperado: Error de caracter inválido
Estado: Fracaso

### Caso de prueba 3: Comprobación de error archivo vacío
Descripción: Verificar que el script puede manejar adecuadamente un archivo de secuencia de ADN vacío
Datos de entrada: Archivo de secuencia de ADN con las siguientes bases:
Resultado esperado: Error de "Empty file"
Estado: Fracaso

