# Datos iniciales
estudiantes = [
    ("Ana", 85, 90, 78, 92),
    ("Luis", 88, 76, 95),
    ("Carlos", 100, 98),
    ("María", 70, 80, 75, 85, 90)
]

resultados = {}

for estudiante in estudiantes:
    # separamos el nombre 
    nombre, *calificaciones = estudiante
    
    # Inicializamos variables para los cálculos manuales
    suma_total = 0
    # Usamos el primer elemento de la lista para comparar 
    primera_nota, *otras = calificaciones
    nota_max = primera_nota
    nota_min = primera_nota
    
    # Recorremos la lista calificaciones 
    for nota in calificaciones:
        # Suma 
        suma_total += nota
        
        # Determinar máximo 
        if nota > nota_max:
            nota_max = nota
            
        # Determinar mínimo 
        if nota < nota_min:
            nota_min = nota
            
    # Uso de len() para sumar todo el promedio
    promedio = suma_total / len(calificaciones)
    
    # Guardamos en el diccionario
    resultados[nombre] = {
        "promedio": promedio,
        "max": nota_max,
        "min": nota_min
    }

# Impresión de resultados
print("--- Diccionario de Resultados ---")
for nombre, info in resultados.items():
    print(f"{nombre}: {info}")

# Determinar el promedio más alto 
mejor_estudiante = ""
max_promedio = -1

for nombre, datos in resultados.items():
    if datos["promedio"] > max_promedio:
        max_promedio = datos["promedio"]
        mejor_estudiante = nombre

print(f"\nEstudiante con mejor promedio: {mejor_estudiante}")