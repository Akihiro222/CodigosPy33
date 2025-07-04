#JEREMI JOSUE FLORES VEGA ESTUDIANTE ANALISTA PROGRAMADOR

# Importamos deepcopy desde el módulo copy lo que permite hacer copias independientes y no tener problemas de memoria
# de estructuras como listas añadidas sin compartir referencias en memoria
from copy import deepcopy

# Creamos un diccionario vacío para almacenar usuarios registrados junto con sus contraseñas correspondientes y no hayan errore
usuarios_registrados = {}

# esta función que permite crear un nuevo usuario y usarlo
def crear_usuario():
    """Registra un nuevo usuario solicitando nombre de usuario y contraseña."""

    # Muestra encabezado visual para separar esta sección del programa.
    print("=== Registro de Usuario ===")
    
    # Esto solicita al usuario que ingrese un nombre de usuario
    # Esto será usado como clave única dentro del diccionario 
    usuario = input("Ingrese un nombre de usuario: ")
    
    # esto verefica si el nombre de usuario ya existe en el dec
    # esto previene la duplicación y asegura unicidad del registro
    if usuario in usuarios_registrados:
        print("El usuario ya existe. Intente con otro nombre.")
        return False  # Si ya existe se interrumpe el proceso de registro y lo regresa
    
    # Si el nombre es nuevo se solicita una contraseña para el usuario
    # asta contraseña será vinculada al usuario y se almacenará en la memoria
    contraseña = input("Ingrese una contraseña segura: ")
    
    # Almacena el usuario y su contraseña en el diccionario global usuario
    # Esto permite validar credenciales durante el proceso de inicio de sesión
    usuarios_registrados[usuario] = contraseña
    
    # Informa al usuario que el proceso de registro fue exitoso sin error
    print("Usuario creado exitosamente.\n")
    
    # Retorna True como indicador de que el registro se completó correctamente
    return True

# Función que permite a un usuario iniciar sesión en el sistema
def login():
    """Valida credenciales de usuario para permitir acceso al sistema."""

    # Muestra un encabezado indicando que comienza el proceso de autenticación
    print("=== Inicio de Sesión ===")
    
    # Solicita al usuario que ingrese su nombre de usuario que habia creado
    usuario = input("Usuario: ")
    
    # Solicita la contraseña correspondiente al usuario creado
    contraseña = input("Contraseña: ")
    
    # Compara las credenciales ingresadas con el contenido del diccionario usuario
    # get(usuario) obtiene la contraseña asociada al usuario Si coincide con la ingresada, se otorga acceso a las 3 ramas
    if usuarios_registrados.get(usuario) == contraseña:
        # Si las credenciales son correctas se muestra un mensaje de bienvenida.
        print("Acceso concedido.\n")
        return True  # El retorno True indica que el login fue exitoso
    else:
        # Si las credenciales no coinciden, se informa al usuario que no coinciden
        print("Credenciales incorrectas.\n")
        return False  # El retorno False indica fallo en la autenticación

# Función principal del Ejercicio 1: Gestión de Tareas Pendientes
def ejercicio_tareas_pendientes():
    """Permite agregar, visualizar y actualizar tareas con estado mediante una lista de diccionarios."""

    # Se inicializa una lista vacía llamada `tareas_pendientes`, donde se almacenarán las tareas
    # Cada tarea será representada como un diccionario con claves 'nombre' y 'estado'
    tareas_pendientes = []

    # Definición de una función interna que se encargará de mostrar el contenido de la lista de tareas.
    # Esta función recibe como parámetro una lista de tareas (esperada en formato de diccionarios)
    def mostrar_tareas(lista):
        # Encabezado visual para identificar la sección de tareas en pantalla
        print("--- Lista de Tareas ---")

        # Condicional que evalúa si la lista está vacía
        # Si no hay tareas registradas se notifica al usuario
        if not lista:
            print("No hay elementos en la lista.")
        else:
            # Si la lista contiene elementos se imprime cada tarea en formato: [estado] - nombre
            print("Estado      -   Tarea")
            for t in lista:
                # Accede a los valores de las claves 'estado' y 'nombre' de cada tarea y los muestra
                print(f"[{t['estado']}] - {t['nombre']}")
        
        # Imprime una línea vacía para mejorar la legibilidad visual tras mostrar la lista
        print()

    # Función que marca como completada una tarea específica utilizando deepcopy para mantener la integridad de la lista original
     # Función interna que marca como completada una tarea específica en la lista
    # Se utiliza deepcopy para no modificar directamente la lista original
    def completar_tarea(lista, nombre):
        # Se crea una copia profunda de la lista lo que permite modificar la copia
        # sin alterar la lista original (buena práctica de seguridad y control de estado).
        copia = deepcopy(lista)

        # Variable de control que indica si la tarea fue encontrada y modificada con exito
        completada = False

        # Se recorre cada tarea de la copia
        for t in copia:
            # Si el nombre de la tarea coincide con el que se busca
            # se actualiza su estado a "completada"
            if t["nombre"] == nombre:
                t["estado"] = "completada"
                completada = True  # Se marca como exito la operación

        # La función retorna la nueva lista modificada y un valor booleano indicando si se completó la tarea
        return copia, completada

    # Se muestra inicialmente la lista vacía de tareas al usuario
    mostrar_tareas(tareas_pendientes)

    # Se agregan tres tareas a la lista principal Cada una es un diccionario con nombre y estado
    # Después de agregar cada tarea se muestra la lista actualizada
    for nombre in ["Hacer la cama", "Estudiar Python", "Hacer la compra"]:
        tareas_pendientes.append({"nombre": nombre, "estado": "pendiente"})
        mostrar_tareas(tareas_pendientes)

    # Se utiliza la función `completar_tarea` para marcar "Estudiar Python" como completada
    # Se reciben dos valores: la nueva lista y un booleano indicando si hubo cambio
    tareas_modificadas, cambio = completar_tarea(tareas_pendientes, "Estudiar Python")

    # Se informa al usuario si la tarea fue efectivamente completada
    print(f"Se logró completar la Tarea Estudiar Python?: {cambio}\n")

    # Se muestra la lista después de haber modificado la tarea
    mostrar_tareas(tareas_modificadas)

    # Se agrega una nueva tarea llamada "Preparar la cena" a la lista modificada
    tareas_modificadas.append({"nombre": "Preparar la cena", "estado": "pendiente"})

    # Finalmente, se imprime la lista con todas las tareas, incluyendo la nueva agregada
    mostrar_tareas(tareas_modificadas)

# Función principal del Ejercicio 2: Información de Producto Inmutable
def ejercicio_productos_tuplas():
    """Gestiona productos utilizando tuplas inmutables y demuestra un intento de modificación prohibida."""

    # Se definen dos tuplas que representan productos
    # Cada tupla contiene: (nombre del producto categoría precio código del producto)
    # Las tuplas son estructuras de datos inmutables es decir sus valores no se pueden modificar una vez creadas
    tupla1 = ("Laptop", "Electrónica", 1200000, "ABC123XYZ")
    tupla2 = ("Mouse", "Electrónica", 12000, "XYHA12812312")

    # Se agrupan ambas tuplas dentro de una tupla mayor llamada `productos_info`
    # Esto simula un catálogo de productos donde cada elemento es inmutable
    productos_info = (tupla1, tupla2)

    # Se imprime un encabezado indicando que se mostrará información de productos
    print("--- Producto ---")

    # Se accede al primer producto dentro de `productos_info específicamente a su nombre (índice 0)
    print("Nombre:", productos_info[0][0])

    # Se accede al precio del mismo producto (índice 2 de la primera tupla
    print("Precio: $", productos_info[0][2])

    # A continuación se intenta modificar el precio del primer producto
    # lo cual es incorrecto, ya que las tuplas no permiten modificar sus valores
    try:
        # Esta línea generará una excepción TypeError porque las tuplas son inmutables
        productos_info[0][2] = 1150000
    except TypeError as e:
        # Se captura el error y se muestra al usuario para evidenciar la naturaleza inmutable de las tuplas
        print("Error al intentar modificar el precio:", e)

# Función principal del Ejercicio 3: Registro de Estudiantes
def ejercicio_registro_estudiantes():
    """Permite ingresar y validar calificaciones de estudiantes utilizando diccionarios y manejo de errores."""

    # Se inicializa un diccionario vacío que almacenará estudiantes y sus calificaciones
    # La clave será el nombre del estudiante y el valor su nota
    registro_estudiantes = {}

    # Función interna que permite agregar un estudiante o actualizar su calificación
    def agregar_estudiante():
        # Se solicita el nombre del estudiante por teclado
        nombre = input("Ingrese el nombre del estudiante: ")

        try:
            # Se solicita la nota como número decimal (float).
            nota = float(input("Ingrese la calificación (decimal entre 1.0 y 7.0): "))

            # Se valida que la nota esté dentro del rango permitido (1.0 a 7.0 inclusive
            if nota < 1.0 or nota > 7.0:
                print("La nota debe estar entre 1.0 y 7.0")
                return  # Si la nota no es válida se detiene la función

            # Si el estudiante ya existe se informa y se actualizará su calificación
            if nombre in registro_estudiantes:
                print(f"El estudiante {nombre} ya está registrado. Se actualizará su calificación.")
            else:
                # Si es un nuevo estudiante se muestra mensaje de registro exitoso
                print(f"Registrando al estudiante {nombre}...")

            # Se almacena o actualiza la calificación en el diccionario
            registro_estudiantes[nombre] = nota

        except ValueError:
            # Si el usuario ingresa algo que no puede convertirse a float, se captura la excepción
            print("Error: La calificación debe ser un número decimal válido.")

    # Función interna que permite mostrar todos los estudiantes registrados junto con sus notas
    def mostrar_estudiantes():
        print("\nRegistro de Estudiantes:")

        # Si el diccionario está vacío se informa que no hay datos
        if not registro_estudiantes:
            print("No hay estudiantes registrados.")

        # Se recorre el diccionario y se imprime cada par nombre-nota
        for nombre, nota in registro_estudiantes.items():
            print(f"{nombre}: {nota}")

    # Ciclo principal del módulo que actúa como menú de interacción para el usuario
    while True:
        # Opciones disponibles para el usuario
        print("\nMenú de Registro de Estudiantes")
        print("1. Agregar o Actualizar estudiante")
        print("2. Mostrar lista de estudiantes")
        print("3. Volver al menú principal")

        # Se recibe la opción seleccionada
        opcion = input("Seleccione una opción: ")

        # Se ejecuta la acción correspondiente según la opción ingresada
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            # Se rompe el bucle para volver al menú principal general
            break
        else:
            # Mensaje en caso de que la opción ingresada no sea válida
            print("Opción inválida.")

# Menú principal que conecta los tres ejercicios
def menu_principal():
    """Despliega un menú para seleccionar entre los tres ejercicios disponibles."""

    # Ciclo infinito que mantiene activo el menú hasta que el usuario decida salir
    while True:
        # Se muestran las opciones disponibles para el usuario
        print("=== Menú Principal ===")
        print("1. Gestión de Tareas Pendientes")
        print("2. Información de Producto Inmutable")
        print("3. Registro de Estudiantes")
        print("4. Salir del sistema")

        # Se solicita al usuario que seleccione una opción del menú
        opcion = input("Seleccione una opción: ")

        # Según la opción ingresada se llama a la función correspondiente:
        
        # Opción 1: Ejecuta el ejercicio que gestiona tareas usando listas y diccionarios
        if opcion == "1":
            ejercicio_tareas_pendientes()

        # Opción 2: Ejecuta el ejercicio que utiliza tuplas para almacenar datos inmutables
        elif opcion == "2":
            ejercicio_productos_tuplas()

        # Opción 3: Ejecuta el ejercicio que registra estudiantes y valida sus calificaciones
        elif opcion == "3":
            ejercicio_registro_estudiantes()

        # Opción 4: Finaliza el ciclo del menú y retorna al nivel superior del sistema
        elif opcion == "4":
            print("Cerrando sesión...")
            break

        # En caso de que el usuario ingrese una opción inválida se muestra un mensaje de advertencia
        else:
            print("Opción inválida. Intente nuevamente.")


# Flujo inicial del programa con autenticación
def iniciar_sistema():
    """Controla el flujo principal de la aplicación: creación de usuario, login y acceso al menú principal."""

    # Ciclo principal que mantiene activo el sistema hasta que el usuario decida salir
    while True:
        # Se presenta el encabezado del sistema y el menú de opciones de inicio
        print("=== Sistema Seguro de Evaluación ===")
        print("1. Crear usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        # Se solicita al usuario que seleccione una de las opciones del sistema
        seleccion = input("Seleccione una opción: ")

        # Opción 1: Permite crear un nuevo usuario. Llama a la función `crear_usuario
        if seleccion == "1":
            crear_usuario()

        # Opción 2: Inicia sesión con credenciales Si el login es exitoso se accede al menú principal
        elif seleccion == "2":
            if login():  # Solo si las credenciales son válidas se continúa con el uso del sistema
                menu_principal()

        # Opción 3: Finaliza el programa completamente saliendo del bucle principal
        elif seleccion == "3":
            print("Programa finalizado.")
            break  # Se rompe el ciclo while cerrando la aplicación

        # Cualquier otra entrada no válida es capturada y se muestra un mensaje de advertencia
        else:
            print("Opción inválida.")


# Ejecutamos todo el sistema llamando a la función principal
iniciar_sistema()
## Esta línea ejecuta la función `iniciar_sistema()` al final del script
# Su propósito es lanzar el sistema completo una vez que todas las funciones y estructuras han sido definidas
# Desde aquí se controla el flujo de toda la aplicación: registro, inicio de sesión y acceso a los ejercicios
# Es una práctica estándar en Python llamar a la función principal al final del archivo para iniciar el programa

# Pausa para evitar que la consola se cierre inmediatamente
input("Presiona Enter para salir...")