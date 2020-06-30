#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import re




def contar_lineas(archivo):

   cantidad_lineas = len(archivo)

   return cantidad_lineas


def ej1():
    # Ejercicios con archivos txt
    
    with open("notas.txt") as notas:
        x = list(csv.DictReader(notas))

    cantidad_lineas = contar_lineas(x)
    print(cantidad_lineas)

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea alinea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura.

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    fi = open("notas.txt", "r")
    fo = open("nuevo.txt", "w")

    for line in fi:
        
        fo.write(line)
        cantidad_lineas += 1

    print(cantidad_lineas)

    fi.close()
    fo.close()

    # Recuerde cerrar los archivos al final ;)


def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
    dptos_2amb = 0
    dptos_3amb = 0
    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))

    for i in range(len(data)):
        row = data[i]
        
        try:
            ambientes = int(row.get("ambientes"))
            if ambientes == 2:
                dptos_2amb += 1
            else:
                if ambientes == 3:
                    dptos_3amb += 1
        except:
            continue

    print(dptos_2amb)
    print(dptos_3amb)


def ej4():
    # Ejercicios con diccionarios
    inventario = {}
    condicion = True

    while condicion:
        f_v = str(input("Ingrese nombre fruta/verdura o fin para salir:\n"))
        if f_v == "fin":
            break
        else:
            cantidad = int(input("Ingrese cantidad en stock:\n"))
                
        inventario[f_v] = cantidad

    while condicion:
        f_v_s = str(input("Ingrese nombre fruta/verdura a saber stock o fin para salir:\n"))
        if f_v_s == "fin":
            break
        else:
                print(inventario.get(f_v_s)) 
        


    
    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario el par:
    <fruta>:<cantidad>
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    Al finalizar el bucle anterior, debe generar otro bucle
    en donde se pida ingresar la fruta o verdura que desea
    conocer su estado de stock.
    Deberá imprimir en pantalla la cantidad de esa fruta en
    inventario, y en caso de no exista ese elemento en nuestro
    inventario se debe imprimir en pantalla "Elemento no encuentrado"
    NOTA: Proponemos utilizarel método "get" que devuelve "None" si el
    elemeto no existe en el diccionario.

    Se debe terminar ese segundo bucle cuando se ingrese la palabra FIN
    '''

    # 1) Bucle 1
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"

    # 2) Bucle 2
    # Ingresar por consola la fruta que desea conocer en stock
    # Finalizar cuando la fruta ingresada sea igual a "FIN"


def ej5():
    # Ejercicios con archivos CSV
    inventario = {}

    invent = open('inventario.csv', 'w', newline='')

    header = ["fruta/verdura", "cantidad"]

    writer = csv.DictWriter(invent, fieldnames=header)

    

    condicion = True
    
    while condicion:
        
        f_v = str(input("Ingrese nombre fruta verdura o fin para salir:\n"))    
        
        
        if f_v == "fin":
            invent.close()
            break
        else:
            cant = int(input("Ingrese cantidad en stock:\n"))
            writer.writeheader()
            
            writer.writerow({"fruta/verdura": f_v, "cantidad": cant})

    
        
        
            
         







    '''
    Basado en el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario que utilizaremos para escribir en el archivo CSV

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    #ej2()
    ej3()
    #ej4()
    ej5()
