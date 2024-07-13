from statistics import mean, geometric_mean
from random import randint
opc = 0   
trabajadores = [], [] 
while True:
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opc = input("Ingrese la Opción: ")
    if opc == "1":           
        trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"], [] 
        for trabajador in trabajadores[0]:
            sueldorandom = (str(randint(300000, 2500000)).ljust(10))
            trabajadores[1].append(f"{sueldorandom}") 
            print(f"trabajador: {trabajador}, Sueldo: {sueldorandom}")
    if opc == "2":      
        datosmenor = [], []
        datos800_2m = [], []
        datosmayor_2m = [], []
        sueldomenor  = int(0)
        sueldo800_2m = int(0)
        sueldomayor_2m = int(0)
        total = int(0)
        for trabajador in trabajadores[1] :
            if trabajador < str(800000):  
                sueldomenor = sueldomenor + 1 
                print(trabajador)
                datosmenor[0].append(trabajador)
                # datosmenor[1].append(trabajador[1])
            if trabajador > str(799999) and trabajador[1] < str(1999999):
                sueldo800_2m = sueldo800_2m + 1 
                datos800_2m[0].append(trabajador)            
                # datos800_2m[1].append(trabajador[1])            
            if trabajador > str(2000000):
                sueldomayor_2m = sueldomayor_2m + 1
                datosmayor_2m[0].append(trabajador)          
                # datosmayor_2m[1].append(trabajador[1])          
        print("Clasificación de Sueldos: ")                          
        print(f"Sueldos menores a $800.000 TOTAL: {sueldomenor} ")
        print (datosmenor)            
        print(f"Sueldos entre $800.000 y $2.000.000: TOTAL: {sueldo800_2m}")            
        print (datos800_2m)            
        print(f"Sueldos superiores a $2.000.000: TOTAL: {sueldomayor_2m}")     
        print (datosmayor_2m) 
       
        # print(f"TOTAL SUELDOS: {total}")
        # sueldomenor  = int(0)
        # sueldo800_2m = int(0)
        # sueldomayor_2m = int(0)
            
    