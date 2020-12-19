nombre = input ("Bienvenido a la Red Epsilon, Cual es tu nombre ? ")
print ("hola", nombre, ", que gusto que estes aqui, Bienvenido a mi Epsilon")
print (nombre, ", para poder ser parte de la Epsilon necesitamos algunos datos basicos tuyos")
print ("te agradeceriamos que nos los proporciones")
print ("para disfrutar de una grata experiencia en la Red")




ejecucion = input("Deseas continuar en la Red ?, (s/n) ")
while ejecucion =="s":
    print ("Porfavor, elige una de las opciones del menu")
    print("-----------------------------------")
    print ("1 Escribir un mensaje al publico")
    print ("2 Escribir un mensaje a un amigo")
    print ("3 Cambiar Mi Nombre de usuario")
    print ("4 Cambiar Datos de Perfil")
    print ("5 Publicar datos de Perfil")
    print ("Enter para salir")
    print("----------------------------------")

    menu = input("Escribe el numero de tu eleccion ")
    if menu =="1":
        print ("Has elegido ", menu, "Escribir un mensaje")
        publicar = input("Escribe tu mensaje porfavor ")
        print(nombre ," : ",publicar)
    elif menu =="2":
        cantidad=int(input("cantidad de amigos a los que les quieres escribir "))
        for i in range (cantidad):
            nombre_amigo =input("Escribe el nombre de tu amigo ")
            mensaje= input("Que quieres decirles a tus amigos ")
            print(nombre," dice a ",nombre_amigo," mensaje :", mensaje)
    elif menu =="3":
        print ("Has elegido ", menu, "Cambiar Nombre ")
        nombre = input("Porfavor, Ingresa tu nuevo nombre de Usurio ")
        print ("Has elegido ", nombre, " como nuevo nombre de Usuario ")
    elif menu=="4":
        from modulos import datos_basicos_ingreso 
        datos_basicos_ingreso ()
    elif menu =="5":
        print("Muy bien", nombre, "Ahora podemos crear tu perfil con estos datos que nos proporcionaste")
        print("Nombre   :", nombre)
        print("Edad     :", edad, "anos")
        print("Estatura :", estatura_m, "metro y ", estatura_cm, "centimetros")
        print("Numero de amigos :", num_amigos)
        print("Genero   :", genero)
        print("Telefono :", telefono)
        print("Ciudad   :", ciudad)
        print("Lugar de Nacimiento :", pais_nacimiento)
        print("Direccion :", direccion)
        print("Es tiempo de que saludes a tus nuevos amigos de la Red Epsilon")
        print("Y des un saludo de Bienvenida para que te conozcan")
    print("--------------------------------------------------")
    ejecucion = input("Deseas continuar en la Red ?, (s/n) ")
    print("--------------------------------------------------")
print("Gracias ", nombre, " por participar en La Red")
print ("Vuelve cuando quieras")


