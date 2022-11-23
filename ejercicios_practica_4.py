# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv

# Objetivo:
# Leer y trabajar con un archivo CSV complejo y el
# manejo de excepciones

def desafio():
    print('Ejercicios con archivos CSV complejos')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.
    
    csvdoc = open (archivo, 'r')
    lista_deptos = list(csv.DictReader(csvdoc))
    ambientes_2 = 0
    ambientes_3 = 0

    for i in lista_deptos:
        row = lista_deptos [i]
        try:
            cantidad_ambientes = int(row("ambientes"))

            if i == 2:
                ambientes_2 += 1
            elif i == 3:
                ambientes_3 += 1
        except:
            continue
    
    print(f"Hay {ambientes_2} departamentos de 2 ambientes y {ambientes_3} departamentos de 3 ambientes")

    csvdoc.close()


    # Según el valor ingresado en "ambientes" está función deberá
    # retornar (return):
    # 1) si ambientes == "2_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 2 ambientes
    # 2) si ambientes == "3_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 3 ambientes

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # Puede evitar que el programa explote utilizando "try except".

    # Comenzar aquí, recuerde el identado dentro de esta funcion


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio()
