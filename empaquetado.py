datos=[1,2,3,4,5]
print(f"arregglo original:{datos}")

"""copia_datos=[]
for i in datos:
    copia_datos.append(i)"""
#forma adecuada  de hacer una copia de una lista con desempaquetado
copia_datos=[*datos]
print(*datos)
print(f"Lista 2:{copia_datos}")
copia_datos.append(6)
print(f"lista original id{id(datos)}, contenido:{datos}")
print(f"lista 2 id{id(copia_datos)}, contenido:{copia_datos}")

def impresion_nombres(nombres):
    print(f"los nombres son:",*nombres)

impresion_nombres("diego","juan","ana","laura")



def impresion_datos(data):
    print(f"los datos son:{data}")
impresion_datos(nombre="diego",tel=558788878,carrera="sitemas")
diccionario_datos={"marca":"DELL","modelo":"27080","fecha":"hoy"}
copia_dicccionario={**diccionario_datos}
impresion_datos(**copia_dicccionario)