# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:29:40 2023

@author: Sergio dominguez

"""
# importar librerias
import pandas as pd
import seaborn as sns
import scipy.stats as st
import numpy as np
import statsmodels.api as sm

def prueba_hipotesis(columna,media_hipotetica,significancia,tipo_cola,media_poblacional,media_muestral):
    """
    Realizar una prueba de hipótesis para comparar media de muestra aleatoria de columna earn con media_hipotetica    
    Args:
        columna (Pandas.Serie): Nombre de columna.
        media_hipotetica (integer): valor de media a evaluar
        significancia (float): porcentale de error permitido
        tipo_cola (string): define la hipotesis alternativa
        ‘two-sided’: the mean of the underlying distribution of the sample is different 
            than the given population mean (popmean)

        ‘less’: the mean of the underlying distribution of the sample is less than 
            the given population mean (popmean)

        ‘greater’: the mean of the underlying distribution of the sample is greater than 
            the given population mean (popmean)
        media_poblacional (integer): valor de media poblacional para comparar
        
    Returns:
        none
       
    """
    # Realizar una prueba de hipótesis para comparar media de muestra aleatoria de columna earn con media_hipotetica
    t_stat, p_value = st.ttest_1samp(columna,media_hipotetica,alternative=tipo_cola)
    
    # Comprobar si el valor p es menor que alfa para rechazar la hipótesis nula
    print("---------------------------------------------------------------------------")
    if p_value < significancia:
        # print("Resultado: Se rechaza la hipótesis nula")
        # segun tipo de cola, genero la descripcion respectiva
        if tipo_cola == "two-sided":
            print(f"Resultado: Con nivel de confianza {round((1 - significancia)*100,2)}%, se acepta la hipotesis alternativa -> la media muestral es diferente a la media hipotetica")
        if tipo_cola == "less":
            print(f"Resultado: Con nivel de confianza {round((1 - significancia)*100,2)}%, se acepta la hipotesis alternativa -> la media muestral es menor a la media hipotetica")
        if tipo_cola == "greater":
            print(f"Resultado: Con nivel de confianza {round((1 - significancia)*100,2)}%, se acepta la hipotesis alternativa -> la media muestral es mayor a la media hipotetica")
    else:
        print(f"Resultado: Con nivel de confianza {round((1 - significancia)*100,2)}%, se acepta la hipotesis nula")

    print("---------------------------------------------------------------------------")
    # Imprimir el valor t y el valor p
    print(f"Valor t (estadistico): {t_stat}")
    print(f"Valor p (p_value)    : {p_value}")
    print(f"nivel significancia  : {significancia}")
    print(f"nivel de confianza   : {round((1 - significancia)*100,2)}%")
    print(f"media hipotetica     : {media_hipotetica}")
    print(f"media muestral       : {media_muestral}")
    print(f"media poblacional    : {round(media_poblacional,2)}")

    
    # crear un intervalo de confinza, calculo el margen de error y confiabilidad
    a,b=st.t.interval(confidence= (1 - significancia), df = len(columna) -1, loc = media_hipotetica, scale = st.sem (columna))
    error=round(b-media_hipotetica,2)
   
    print("---------------------------------------------------------------------------")
    print(f'La media hipotetica es {media_hipotetica}, con un margen de error de {error} y confiabilidad del {round((1 - significancia)*100,2)}%')
    print("---------------------------------------------------------------------------")

    print(f"diferencias en las medias muestral e hipotetica    : {round((media_muestral - media_hipotetica), 2)}")
    print(f"porcentaje de diferencia: {round((((media_muestral - media_hipotetica)/media_muestral) * 100), 2)}%")
    print(f"diferencias en las medias poblacional e hipotetica : {round((media_poblacional - media_hipotetica), 2)}")
    print(f"porcentaje de diferencia: {round((((media_poblacional - media_hipotetica)/media_poblacional) * 100), 2)}%")
    print("---------------------------------------------------------------------------")


def estima_proporcion(significancia,n,cantidad,que_valor):
    """
    Realizar una estomacion de proporcionalidad de variable    
    Args:
        significancia (float): porcentale de error permitido
        n (integer): total de registros
        cantidad (integer): total de que_columna (en este caso hombres)
        que_valor (string): que valor de columna (hombre/mujer)
        
    Returns:
        none
       
    """    
    # Proporción muestral de "x" en la muestra
    proporcion_muestral = cantidad / n

    # nivel de significancia
    #nivel_significancia=1 - confianza

    # Nivel de confianza (por ejemplo, 95%)
    confianza = 1 - significancia

    # Calcular el intervalo de confianza utilizando statsmodels
    intervalo_confianza = sm.stats.proportion_confint(cantidad, n, alpha=significancia)

    # Imprimir el resultado
    print(f"Intervalo de confianza del {confianza * 100}% para la proporción de {que_valor} con la cantidad de {n} registros:")
    print(f"({intervalo_confianza[0]}, {intervalo_confianza[1]})")
    print(f"nivel de significancia: {significancia}")

    
    
    

