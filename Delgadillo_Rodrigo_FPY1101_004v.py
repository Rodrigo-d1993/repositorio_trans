import random
trabajadors = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
                 "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"] 
def generar():
    salarios = {}
    for trabajador in trabajadors:
        salario = random.randint(400000, 1500000)
        salarios[trabajador] = salario
    return salarios
def clasificar():
    menores_600000 = []
    entre_600000_800000=[]
    mayores_1000000 = []
    for trabajador, salario in salarios_trabajadors.items():
        if salario < 600000:
            menores_600000.append((trabajador, salario))
        elif 600000 <= salario <= 800000:
            entre_600000_800000.append((trabajador, salario))
        elif salario > 1000000:
            mayores_1000000.append((trabajador, salario))
    menuClasificar='''
    1. salarios menores a 600000
    2. salarios entre 600000 y 800000
    3. salarios Mayores a 1.000.0000
    4. Salir
    '''
    while True:
        print(menuClasificar)
        op1=int(input('Ingrese opción: '))
        while(op1<1 or op1>4):
            op1=int(input('Ingrese opción del 1 al 3: '))
        if(op1==1):
            print("salarios menores a 600000: ")
            for trabajador, salario in menores_600000:
                print(f"{trabajador}: {salario}")
            continue
        if(op1==2):
            print("\nsalarios Entre 600000 y 800000: ")
            for trabajador, salario in entre_600000_800000:
                print(f"{trabajador}: {salario}")
            continue
        if(op1==3):
            print("\nsalarios Mayores a 1.000.000: ")
            for trabajador, salario in mayores_1000000:
                print(f"{trabajador}: {salario}")
            continue
        if(op1==4):
            break  
def max_salario(diccionario_salarios):
    trabajador_mayor_salario = max(diccionario_salarios, key=diccionario_salarios.get)
    return trabajador_mayor_salario, diccionario_salarios[trabajador_mayor_salario]
def min_salario(diccionario_salarios):
    trabajador_mayor_salario = min(diccionario_salarios, key=diccionario_salarios.get)
    return trabajador_mayor_salario, diccionario_salarios[trabajador_mayor_salario]
def promedio_salario(diccionario_salarios):
    total_salarios = sum(diccionario_salarios.values())  
    cantidad_trabajadors = len(diccionario_salarios) 
    promedio = total_salarios / cantidad_trabajadors 
    return promedio
def media_salario(diccionario_salarios):
    salarios = list(diccionario_salarios.values())
    if not salarios:
        raise ValueError("El diccionario de salarios está vacío")
    producto = 1
    for salario in salarios:
        producto *= salario
    media_geometrica = round(producto ** (1 / len(salarios)))
    return media_geometrica  
def estadistica():
    menu=''''
    1. Salario Maximo
    2. Salario Minimo
    3. Salario Promedio
    4. Media Geometrica
    5. Salir
    '''
    while True:
        print(menu)
        op2= int(input('Ingrese opcion: '))
        while (op2<1 or op2>5):
            op2=int(input('Ingrese opcion del 1 al 5: '))
        if op2 == 1:
            salarios_trabajadors = generar()
            trabajador_max, salario_max = max_salario(salarios_trabajadors)
            print(f"El trabajador con el mayor salario es {trabajador_max} con un salario de {salario_max}")
        if op2 == 2:
            salarios_trabajadors = generar()
            trabajador_min, salario_min = min_salario(salarios_trabajadors)
            print(f"El trabajador con el menor salario es {trabajador_min} con un salario de {salario_min}")
        if op2 == 3:
            salarios_trabajadors = generar()
            salario_promedio = promedio_salario(salarios_trabajadors)
            print(f"El salario promedio es {salario_promedio:.2f}")
        if op2 == 4:
            salarios_trabajadors = generar()
            try:
                media_geo = media_salario(salarios_trabajadors)
                print(f"La media geométrica de los salarios es: {media_geo}")
            except ValueError as e:
                print(f"Error: {e}")
            continue
        if op2 == 5:
            break     
def reportesalario():
    print("")
def cerrarPrograma():
    print("""Cerrando el programa...
Desarrolado por Rodrigo Delgadillo
RUT: 21.753.853-K""") 
while True:
    menuOpcion = input("""Menu de salarios
1. Asignar salario aleatorio
2. Clasificar salarios
3. Ver estadisticas
4. Reporte de salarios
5. Salir del programa
Opción: """)
    if menuOpcion == "1":
        salarios_trabajadors = generar()
        print(salarios_trabajadors)
        continue
    elif menuOpcion == "2":
        clasificar()
    elif menuOpcion == "3":
        estadistica()
    elif menuOpcion == "4":
        reportesalario()
    elif menuOpcion == "5":
        cerrarPrograma()
        break
    else:
        print("Elige una opción del menú valida")