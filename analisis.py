print("Analisis estadistico de datos") 
datos = [10, 20, 30, 40, 50] 
print("Datos:", datos) 
 
print("\n--- Resultados del analisis ---") 
 
def maximo(datos): 
    return max(datos) 
 
def minimo(datos): 
    return min(datos) 
 
def rango(datos): 
    return maximo(datos) - minimo(datos) 
