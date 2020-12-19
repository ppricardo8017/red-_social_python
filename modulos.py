def datos_basicos_ingreso ():
    ano = int (input ("Que ano naciste ? "))
    edad = 2020 - ano
    genero = input("De que genero eres, hombre o mujer ")
    estatura = float (input("Cuentanos un poco mas sobre ti. Cuanto mides de estatura, en metros ? "))
    estatura_m = int (estatura)
    estatura_cm = int ((estatura - estatura_m) * 100)
    num_amigos = int (input("Bueno finalmente. Cuentanos cuantos amigos tienes ? "))
    telefono = int (input("Cual es tu numero de telefono "))
    ciudad = input("En que ciudad vives ")
    pais_nacimiento = input("En que pais naciste ")
    direccion = input("Cual es tu direccion actual ")
    return direccion, pais_nacimiento, ciudad, telefono, num_amigos, estatura, estatura_m, estatura_cm, genero,edad
    
    

