#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import re


def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0

    with open('texto.txt') as fi:
        for line in fi:
            cantidad_letras += len(line)
        print(cantidad_letras)
        

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''


def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    
    fo = open("archivo_nvo", "w")
    
    while True:
        linea = input("Ingrese linea:\n")
        if linea == "":
            break
        else:
            cantidad_letras += len(linea)
            fo.write(linea + "\n")
            fo.flush()        
    fo.close

    print(cantidad_letras)


    

    
    
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa 
    termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''


def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = 4
    pesos = 0
    valores = []

    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))

    for i in range(len(data)):
        row = data[i]
        try:
            ambientes = int(row.get("ambientes"))
            if ambientes == cantidad_ambientes:
                moneda = str(row.get("moneda"))
                precio = float(row.get("precio"))
            
                if moneda == "ARS":
                    pesos += 1
                    valores.append(precio)

        except:
            continue

    promedio = sum(valores) / len(valores)

    max_valor = max(valores)
    min_valor = min(valores)
    print("alquileres en pesos:", pesos)
    print("maximo precio:", max_valor)
    print("minimo precio:", min_valor)
    print("promedio: {:.2f}".format(promedio))

   




        

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''


def ej4():
    print("Ahora sí! buena suerte :)")

    with open('iwsresults.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    mp_swim = []
    mp_bike = []
    mp_run = []

    m4_swim = []
    m4_bike = []
    m4_run = []

    m2_swim = []
    m2_bike = []
    m2_run = []

    m1_swim = []
    m1_bike = []
    m1_run = []

    for i in range(len(data)):
        row = data[i]
        
        division = str(row.get("Division"))
        if division == "MPRO":

            try:
                swim = str(row.get("Swim"))
                bike = str(row.get("Bike"))
                run = str(row.get("Run"))
                a,b,c = swim.split(":")
                d,e,f = bike.split(":")
                g,h,i = run.split(":")
                swim2 = int(a)*3600 + int(b)*60 + int(c)
                bike2 = int(d)*3600 + int(e)*60 + int(f)
                run2 = int(g)*3600 + int(h)*60 + int(i)
            
                mp_swim.append(swim2)
                mp_bike.append(bike2)
                mp_run.append(run2)
            except:
                continue
            
        elif division == "M45-49":
            try:
                swim = str(row.get("Swim"))
                bike = str(row.get("Bike"))
                run = str(row.get("Run"))
                a,b,c = swim.split(":")
                d,e,f = bike.split(":")
                g,h,i = run.split(":")
                swim2 = int(a)*3600 + int(b)*60 + int(c)
                bike2 = int(d)*3600 + int(e)*60 + int(f)
                run2 = int(g)*3600 + int(h)*60 + int(i)

                m4_swim.append(swim2)
                m4_bike.append(bike2)
                m4_run.append(run2)
            except:
                continue

        elif division == "M25-29":

            try:
                swim = str(row.get("Swim"))
                bike = str(row.get("Bike"))
                run = str(row.get("Run"))
                a,b,c = swim.split(":")
                d,e,f = bike.split(":")
                g,h,i = run.split(":")
                swim2 = int(a)*3600 + int(b)*60 + int(c)
                bike2 = int(d)*3600 + int(e)*60 + int(f)
                run2 = int(g)*3600 + int(h)*60 + int(i)

                m2_swim.append(swim2)
                m2_bike.append(bike2)
                m2_run.append(run2)
            except:
                continue

        elif division == "M18-24":
            try:
                swim = str(row.get("Swim"))
                bike = str(row.get("Bike"))
                run = str(row.get("Run"))
                a,b,c = swim.split(":")
                d,e,f = bike.split(":")
                g,h,i = run.split(":")
                swim2 = int(a)*3600 + int(b)*60 + int(c)
                bike2 = int(d)*3600 + int(e)*60 + int(f)
                run2 = int(g)*3600 + int(h)*60 + int(i)

                m1_swim.append(swim2)
                m1_bike.append(bike2)
                m1_run.append(run2)
            except:
                continue
    
    
    mp_swim_s = sum(mp_swim)
    mp_bike_s = sum(mp_bike)
    mp_run_s = sum(mp_run)
    promedio_mps = mp_swim_s / len(mp_swim)
    promedio_mpb = mp_bike_s / len(mp_bike)
    promedio_mpr = mp_run_s / len(mp_run)
    promedio_mp = mp_bike_s + mp_run_s + mp_swim_s

    tpo_max_mpswim = max(mp_swim)
    tpo_max_mpbike = max(mp_bike)
    tpo_max_mprun = max(mp_run)

    print("Promedio MPRO swim:",promedio_mps)
    print("Promedio MPRO bike:",promedio_mpb)
    print("Promedio MPRO run:",promedio_mpr)
    print("promedio MPRO:", promedio_mp)
    print("Tiempo maximo MPRO swim:", tpo_max_mpswim)
    print("Tiempo maximo MPRO bike:", tpo_max_mpbike)
    print("Tiempo maximo MPRO run:", tpo_max_mprun)


    m4_swim_s = sum(m4_swim)
    m4_bike_s = sum(m4_bike)
    m4_run_s = sum(m4_run)
    promedio_m4s = m4_swim_s / len(m4_swim)
    promedio_m4b = m4_bike_s / len(m4_bike)
    promedio_m4r = m4_run_s / len(m4_run)
    promedio_m4 = m4_bike_s + m4_run_s + m4_swim_s

    tpo_max_m4swim = max(m4_swim)
    tpo_max_m4bike = max(m4_bike)
    tpo_max_m4run = max(m4_run)

    print("Promedio M45-49 swim:",promedio_m4s)
    print("Promedio M45-49 bike:",promedio_m4b)
    print("Promedio M45-49 run:",promedio_m4r)
    print("promedio M45-49:", promedio_m4)
    print("Tiempo maximo M45-49 swim:", tpo_max_m4swim)
    print("Tiempo maximo M45-49 bike:", tpo_max_m4bike)
    print("Tiempo maximo M45-49 run:", tpo_max_m4run)
    
    m2_swim_s = sum(m2_swim)
    m2_bike_s = sum(m2_bike)
    m2_run_s = sum(m2_run)
    promedio_m2s = m2_swim_s / len(m2_swim)
    promedio_m2b = m2_bike_s / len(m2_bike)
    promedio_m2r = m2_run_s / len(m2_run)
    promedio_m2 = m2_bike_s + m2_run_s + m2_swim_s

    tpo_max_m2swim = max(m2_swim)
    tpo_max_m2bike = max(m2_bike)
    tpo_max_m2run = max(m2_run)

    print("Promedio M25-29 swim:",promedio_m2s)
    print("Promedio M25-29 bike:",promedio_m2b)
    print("Promedio M25-29 run:",promedio_m2r)
    print("promedio M25-29:", promedio_m2)
    print("Tiempo maximo M25-29 swim:", tpo_max_m2swim)
    print("Tiempo maximo M25-29 bike:", tpo_max_m2bike)
    print("Tiempo maximo M25-29 run:", tpo_max_m2run)
    

    m1_swim_s = sum(m1_swim)
    m1_bike_s = sum(m1_bike)
    m1_run_s = sum(m1_run)
    promedio_m1s = m1_swim_s / len(m1_swim)
    promedio_m1b = m1_bike_s / len(m1_bike)
    promedio_m1r = m1_run_s / len(m1_run)
    promedio_m1 = m1_bike_s + m1_run_s + m1_swim_s

    tpo_max_m1swim = max(m1_swim)
    tpo_max_m1bike = max(m1_bike)
    tpo_max_m1run = max(m1_run)
    print("Promedio M18-24 swim:",promedio_m1s)
    print("Promedio M18-24 bike:",promedio_m1b)
    print("Promedio M18-24 run:",promedio_m1r)
    print("promedio M18-24:", promedio_m1)
    print("Tiempo maximo M18-24 swim:", tpo_max_m1swim)
    print("Tiempo maximo M18-24 bike:", tpo_max_m1bike)
    print("Tiempo maximo M18-24 run:", tpo_max_m1run)

    
    
    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    '''


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
