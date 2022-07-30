"""Inserción de datos por parte del usuario"""
go = "si"
while go == "Si" or go == "SI" or go == "si" or go == "sI" or go == "S" or go == "s":
    while True:
        try:
            id = int(input("Escribe tu número de cédula\n"))
        except ValueError:
            print("Debes escribir un número.")
            continue
        if id < 0:
            print("Debes escribir un número positivo.")
            continue
        if id > 10**15:
            print("Debes escribir un número que contenga menos de 16 digitos")
            continue
        if id <10**8:
            print("No hay números de identificación tan cortos, por favor ingresa un número válido")
            continue
        else:
            break

#Inserción de los nombres con validación de información

    name1 = ""
    while name1.isalpha() != True or name1.__len__() >= 36 or name1.__len__() == 1:
        name1 = input("Ingresa tu primer nombre:\n")
        if name1.__len__() == 0:
            print("Por favor llena el espacio con tu primer nombre.")
        elif name1.isalpha() != True:
            print("El texto ingresado no es válido, por favor digita tu primer nombre sin simbolos, caracteres especiales o espacios.")
        elif name1.__len__() >= 36:
            print("La cadena de carácteres ingresada es muy elevada, por favor ingresa solo 36 caracteres alfabéticos sin espacios")
        elif name1.__len__() < 2:
            print("La cadena de carácteres ingresada es muy pequeña, por favor ingresa tu nombre hasta 36 carácteres sin espacios.")
    
    name2 = ""
    while name2.isalpha() != True or name2.__len__() >= 36 or name2.__len__() == 1:
        name2 = input("Ingresa tu segundo nombres (si no tienes un segundo nombre deja el espacio en blanco dandole a la tecla enter):\n")
        if name2.__len__() == 0:
            name2 = ""
            break
        elif name2.isalpha() != True:
            print("El texto ingresado no es válido, por favor digita tu nombre sin simbolos, caracteres especiales o espacios.")
        elif name2.__len__() >= 36:
            print("La cadena de carácteres ingresada es muy elevada, por favor ingresa solo 36 caracteres alfabéticos sin espacios.")
        elif name2.__len__() == 1:
            print("La cadena de carácteres ingresada es muy pequeña, por favor ingresa tu nombre hasta 36 carácteres sin espacios.")

#Inserción de apellidos con validación de información
    last_name1 = ""
    while last_name1.isalpha() != True or last_name1.__len__() >= 36 or last_name1.__len__() == 1:
        last_name1 = input("Ingresa tu primer apellido:\n")
        if last_name1.__len__() == 0:
            print("Por favor llena el espacio con tu primer apellido.")
        elif last_name1.isalpha() != True:
            print("El texto ingresado no es válido, por favor digita tu primer apellido sin simbolos, caracteres especiales o espacios.")
        elif last_name1.__len__() >= 36:
            print("La cadena de carácteres ingresada es muy elevada, por favor ingresa solo 36 caracteres alfabéticos sin espacios.")
        elif last_name1.__len__() == 1:
            print("La cadena de carácteres ingresada es muy pequeña, por favor ingresa tu primer apellido hasta 36 carácteres incluyendo espacios.")
    last_name2 = ""
    while last_name2.isalpha() != True or last_name2.__len__() >= 36 or last_name2.__len__() == 1:
        last_name2 = input("Ingresa tu segundo apellido:\n")
        if last_name2.__len__() == 0:
            print("Por favor llena el espacio con tu segundo apellido.")
        elif last_name2.isalpha() != True:
            print("El texto ingresado no es válido, por favor digita tu segundo apellido sin simbolos, caracteres especiales o espacios.")
        elif last_name2.__len__() >= 36:
            print("La cadena de carácteres ingresada es muy elevada, por favor ingresa solo 36 caracteres alfabéticos sin espacios.")
        elif last_name2.__len__() == 1:
            print("La cadena de carácteres ingresada es muy pequeña, por favor ingresa tu segundo apellido hasta 36 carácteres incluyendo espacios.")
#inserción del sueldo base con restricciones según la ley.
    while True:
        try:
            salary = int(input("Escribe tu sueldo básico (Recuerda que debe de ser igual o mayor al salario mínimo legal vigente)\n"))
        except ValueError:
            print("Debes escribir un número.")
            continue
        if salary < 0:
            print("Debes escribir un número positivo.")
            continue
        if salary > 10**50:
            print("Debes escribir un valor que sea menor")
            continue
        if salary < 10**6:
            print("El valor ingresado es menor al salario mínimo legal vigente, recuerda que el SMLV es 1000000")
            continue
        else:
            break
#Días trabajados
    while True:
        try:
            worked = int(input("Digita tus días trabajados\n"))
        except ValueError:
            print("Debes escribir un número.")
            continue
        if worked < 0 or worked == 0:
            print("Debes escribir un número positivo y diferente a cero.")
            continue
        elif worked > 30:
            print("La cantidad de días máximos que puedes trabajar por mes es 30, por favor digita un número que que sea igual o inferior.")
            continue
        else:
            break
#Pregunta sobre el si el trabajador es independiente o depende de un empleador
    independent = " "
    while independent.isalpha() != True or independent.__len__() > 2:
        independent = input("¿Eres trabajador independiente?\n")
        if independent.__len__() == 0:
            print("Por favor llena el espacio")
        elif independent.__len__() > 2:
            print("Por favor ingresa solo 2 caracteres un si o un no")
        elif independent == "Si" or independent == "SI" or independent == "si" or independent == "sI" or independent == "S" or independent == "s":
            health = (12.5 * salary)/100
            pension = 0.16 * salary
        elif independent == "No" or independent == "NO" or independent == "no" or independent == "nO" or independent == "n" or independent =="N" :
            health = 0.04 * salary
            pension = 0.04 * salary
        elif independent != "Si" or independent != "SI" or independent != "si" or independent != "sI" or independent != "S" or independent != "s" or independent != "No" or independent != "NO" or independent != "no" or independent != "nO" or independent != "n" or independent !="N":
            print("Por favor introduce un si o un no")
            independent = "  "
    if salary >= 2000000:
        sub = 0
        salaryarr = salary*(worked/30) - health - pension
    else:
        sub = 117172
        salaryarr = salary*(worked/30) - health - pension + sub

    """Graficación de los datos del usuario"""
    if name2 == "":
        print(f"Tu nombre completo es: {name1} {last_name1} {last_name2}\nTu número de identificación es: {id}\nTu subsidio de transporte es: {sub}\nLo que debes de aportar a salud es: {health}\nTu aporte a pensión es: {pension}\nTus días trabajados son: {worked}\nTu paga por los días que trabajaste es: {salary*(worked/30)}\nTu sueldo total es {salaryarr}")
    else:
        print(f"Tu nombre completo es: {name1} {name2} {last_name1} {last_name2}\nTu número de identificación es: {id}\nTu subsidio de transporte es: {sub}\nLo que debes de aportar a salud es: {health}\nTu aporte a pensión es: {pension}\nTus días trabajados son: {worked}\nTu paga por los días que trabajaste es: {salary*(worked/30)}\nTu sueldo total es {salaryarr}")
    go = ""
    while go.isalpha() != True or go.__len__() > 2:
        go = input("¿Deseas realizar otra nómina? responde con un si o un no\n")
        if go.__len__() == 0:
            print("Por favor llena el espacio")
        elif go.__len__() > 2:
            print("Por favor ingresa solo 2 caracteres un, si o un no")
        elif go == "Si" or go == "SI" or go == "si" or go == "sI" or go == "S" or go == "s":
            health = (12.5 * salary)/100
            pension = 0.16 * salary
        elif go == "No" or go == "NO" or go == "no" or go == "nO" or go == "n" or go =="N" :
            health = 0.04 * salary
            pension = 0.04 * salary
        elif go != "Si" or go != "SI" or go != "si" or go != "sI" or go != "S" or go != "s" or go != "No" or go != "NO" or go != "no" or go != "nO" or go != "n" or go !="N":
            print("Por favor introduce un si o un no como respuesta")
            go = "  "
