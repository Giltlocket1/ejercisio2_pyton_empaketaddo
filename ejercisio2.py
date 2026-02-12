# =========================
# DATOS INICIALES
# =========================
estudiantes = [
    ("Ana", 85, 90, 78, 92),
    ("Luis", 88, 76, 95),
    ("Carlos", 100, 98),
    ("María", 70, 80, 75, 85, 90)
]

# Diccionario donde se almacenarán los resultados finales
# El valor será otro diccionario con promedio, máximo y mínimo
resultados = {}

# =========================
# PROCESAMIENTO DE DATOS
# =========================
# Recorremos cada estudiante en la lista
for estudiante in estudiantes:
    
    # Separación de datos:
    # 'nombre' toma el primer valor
    # 'calificaciones' guarda el resto de los valores
    nombre, *calificaciones = estudiante
    
    # Inicializamos la suma total de calificaciones
    suma_total = 0
    
    # Tomamos la primera calificación como referencia inicial
    # para calcular el máximo y el mínimo
    primera_nota, *otras = calificaciones
    nota_max = primera_nota
    nota_min = primera_nota
    
    # Recorremos todas las calificaciones del estudiante
    for nota in calificaciones:
        
        # Sumamos cada calificación
        suma_total += nota
        
        # Determinamos la calificación máxima
        if nota > nota_max:
            nota_max = nota
            
        # Determinamos la calificación mínima
        if nota < nota_min:
            nota_min = nota
    
    # Calculamos el promedio dividiendo la suma total
    # entre el número de calificaciones
    promedio = suma_total / len(calificaciones)
    
    # Guardamos los resultados en el diccionario
    resultados[nombre] = {
        "promedio": promedio,
        "max": nota_max,
        "min": nota_min
    }

# =========================
# IMPRESIÓN DE RESULTADOS
# =========================
print("--- Diccionario de Resultados ---")

# Recorremos el diccionario de resultados
for nombre, info in resultados.items():
    print(f"{nombre}: {info}")

# =========================
# MEJOR PROMEDIO
# =========================
# Variables para encontrar al estudiante con el mejor promedio
mejor_estudiante = ""
max_promedio = -1

# Recorremos los resultados para comparar promedios
for nombre, datos in resultados.items():
    if datos["promedio"] > max_promedio:
        max_promedio = datos["promedio"]
        mejor_estudiante = nombre

# Mostramos el estudiante con el mejor promedio
print(f"\nEstudiante con mejor promedio: {mejor_estudiante}")
