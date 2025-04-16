#Crear un programa que gestione una lista de tareas pendiente
print (" ʚ♡ɞ Software de gestión de tareas pendientes !! ʚ♡ɞ ") #titulo.

def menu():                   #defino la funcion menu la cual muestra el menu en dato tipo texto, no funciona como boton
    opcionesMenu = '''
                    ◃┊ Estas son las opciones: ┊▹
                       ⤥
                    ·˚ * 1 - Añadir una tarea                              ·˚ ༘
                    ·˚ * 2 - Ver todas las tareas                          ·˚ ༘
                    ·˚ * 3 - Marcar una tarea como completada              ·˚ ༘
                    ·˚ * 4 - Salir                                         ·˚ ༘
                    
                    ◃┊ Acontinuación ingresa el numero
                        de la opción que eligas ┊▹
                    '''
    print(opcionesMenu)

tareas = []

while True:                                      #bucle while para llevar a cabo acada opcion
    menu()                                       #llamo a la funcion menu sino de lo contrario no se puede imprimir
    opcion= int (input("Ingrese la opción: "))   #creo la variable opcion la cual le da el valor el user por el input

    if opcion==1: #si eligio la opcion 1:
        tarea = input("Escribe la nueva tarea que querés añadir: ") #aqui engresa el usuario que tarea quiere añadir
        tareas.append(tarea) #agrega la nueva tarea a la lista tareas 
        print("✓ - Tarea añadida con éxito ⊱┊")

    elif opcion==2: 
        print (f"Estas son todas tus tareas ೃ⁀➷ {tareas}")
    
    elif opcion==3:
        tareaCompletada = input("escribe la tarea que quieres borrar (¡! OJO... tienes que escribirlo tal cual como la ingresaste ❞): ") #el usuario me dice que tarea eliminara
        tareas.remove(tareaCompletada) #saca la tarea
        print("✓ - Tu tarea se marco como completada con éxito ⊱┊")
    
    elif opcion == 4:
        print("Muchas gracias por usar nuestro software ⸜❤︎⸝ ")
        break

print("Haz salido de nuestro sistema, fin.")