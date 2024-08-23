def evaluar_persona(nombre, apellido, edad, sexo):
    
    if edad >= 18:
        print(f"{nombre} {apellido} es mayor de edad.")
    else:
        print(f"{nombre} {apellido} es menor de edad.")


    if sexo.lower() == "masculino":
        print(f"{nombre} {apellido} es un Hombre.")
    else:
        print(f"{nombre} {apellido} es una Mujer.")

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (Masculino/Femenino): ")

evaluar_persona(nombre, apellido, edad, sexo)