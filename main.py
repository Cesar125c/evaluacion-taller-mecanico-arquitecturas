# Sistema de Citas - Taller Mecánico (código-espagueti)
# NOTA ACADÉMICA: Código intencionalmente desordenado para demostrar anti-patrones

# Lista global donde se almacenan las citas mientras el programa está abierto.
citas_registradas = []

# Controla el siguiente ID disponible para asignarlo a una nueva cita.
proximo_id_disponible = 1

# Ciclo de vida de una cita: PENDIENTE → ATENDIDA o CANCELADA
ESTADO_PENDIENTE = "PENDIENTE"
ESTADO_CANCELADA = "CANCELADA"
ESTADO_ATENDIDA = "ATENDIDA"

def mostrar_menu_principal():
    """Presenta el menú interactivo al usuario."""
    print("\n" + "="*40)
    print(" SISTEMA DE CITAS - TALLER MECÁNICO")
    print("="*40)
    print("\n1. Crear cita\n2. Ver todas las citas\n3. Buscar cita por ID")
    print("4. Cancelar cita\n5. Marcar cita como atendida\n6. Salir")
    print("\nSeleccione una opción: ", end="")

def obtener_id_ingresado():
    """Solicita y valida el ID de una cita."""
    id_ingresado = input("ID: ").strip()
    
    if not id_ingresado:
        print("❌ Error: El ID no puede estar vacío.")
        return None
    
    if not id_ingresado.isdigit():
        print("❌ Error: El ID debe ser un número.")
        return None
    
    return int(id_ingresado)

def buscar_cita_por_identificador(id_cita):
    """Busca una cita en el registro por su identificador."""
    # Recorre la lista de citas hasta encontrar una con el ID solicitado.
    for cita in citas_registradas:
        if cita["id"] == id_cita:
            return cita
    return None

def mostrar_datos_cita(cita):
    """Imprime los datos de una cita en formato legible."""
    print("\n" + "-"*40)
    for campo, valor in cita.items():
        print(f"{campo.capitalize()}: {valor}")
    print("-"*40)

def crear_cita():
    """Registra una nueva cita con los datos del cliente y validaciones."""
    global proximo_id_disponible
    
    print("\n--- CREAR NUEVA CITA ---")
    nombre_cliente = input("Nombre del cliente: ").strip()
    placa_vehiculo = input("Placa del vehículo: ").strip()
    marca_vehiculo = input("Marca del vehículo: ").strip()
    color_vehiculo = input("Color del vehículo: ").strip()
    tipo_servicio = input("Servicio solicitado: ").strip()
    
    # Valida que el usuario haya ingresado todos los datos requeridos.
    campos_requeridos = [
        nombre_cliente,
        placa_vehiculo,
        marca_vehiculo,
        color_vehiculo,
        tipo_servicio
    ]
    if not all(campos_requeridos):
        print("❌ Error: Todos los campos son obligatorios.")
        return
    
    # La cita se crea con estado inicial PENDIENTE antes de guardarse.
    nueva_cita = {
        "id": proximo_id_disponible,
        "cliente": nombre_cliente,
        "placa": placa_vehiculo,
        "marca": marca_vehiculo,
        "color": color_vehiculo,
        "servicio": tipo_servicio,
        "estado": ESTADO_PENDIENTE
    }
    
    citas_registradas.append(nueva_cita)
    print(f"✅ Cita creada con ID: {proximo_id_disponible}")
    proximo_id_disponible += 1

def listar_todas_citas():
    """Muestra todas las citas registradas en el sistema."""
    print("\n--- TODAS LAS CITAS ---")
    
    if not citas_registradas:
        print("No existen citas registradas.")
        return
    
    for cita in citas_registradas:
        mostrar_datos_cita(cita)

def buscar_cita():
    """Busca una cita específica por su ID."""
    print("\n--- BUSCAR CITA ---")
    id_cita = obtener_id_ingresado()
    
    if id_cita and (cita := buscar_cita_por_identificador(id_cita)):
        mostrar_datos_cita(cita)
    elif id_cita:
        print(f"❌ Error: No existe cita con ID {id_cita}.")

def cancelar_cita():
    """Cancela una cita que está en estado PENDIENTE."""
    print("\n--- CANCELAR CITA ---")
    id_cita = obtener_id_ingresado()
    
    if not id_cita:
        return
    
    cita = buscar_cita_por_identificador(id_cita)
    if not cita:
        print(f"❌ Error: No existe cita con ID {id_cita}.")
        return
    
    # No se realizan cambios si la cita ya fue cancelada.
    if cita["estado"] == ESTADO_CANCELADA:
        print(f"ℹ️ La cita {id_cita} ya estaba cancelada.")
        return
    
    # Una cita atendida no puede regresar a estado cancelado.
    if cita["estado"] == ESTADO_ATENDIDA:
        print("❌ Error: No se puede cancelar una cita que ya fue atendida.")
        return
    
    # Transición válida: PENDIENTE → CANCELADA.
    cita["estado"] = ESTADO_CANCELADA
    print(f"✅ Cita {id_cita} cancelada exitosamente.")

def marcar_cita_como_atendida():
    """Marca una cita como completada con el servicio realizado."""
    print("\n--- MARCAR CITA COMO ATENDIDA ---")
    id_cita = obtener_id_ingresado()
    
    if not id_cita:
        return
    
    cita = buscar_cita_por_identificador(id_cita)
    if not cita:
        print(f"❌ Error: No existe cita con ID {id_cita}.")
        return
    
    # No se realizan cambios si la cita ya fue atendida.
    if cita["estado"] == ESTADO_ATENDIDA:
        print(f"ℹ️ La cita {id_cita} ya estaba marcada como atendida.")
        return
    
    # Una cita cancelada no puede reactivarse para ser atendida.
    if cita["estado"] == ESTADO_CANCELADA:
        print("❌ Error: No se puede atender una cita que fue cancelada.")
        return
    
    # Transición válida: PENDIENTE → ATENDIDA.
    cita["estado"] = ESTADO_ATENDIDA
    print(f"✅ Cita {id_cita} marcada como atendida exitosamente.")

if __name__ == "__main__":
    print("\n✨ Bienvenido al Sistema de Citas del Taller Mecánico ✨\n")
    
    # Ciclo principal: menú interactivo hasta seleccionar salir (opción 6)
    while True:
        mostrar_menu_principal()
        opcion_usuario = input().strip()
        
        if opcion_usuario == "1":
            crear_cita()
        elif opcion_usuario == "2":
            listar_todas_citas()
        elif opcion_usuario == "3":
            buscar_cita()
        elif opcion_usuario == "4":
            cancelar_cita()
        elif opcion_usuario == "5":
            marcar_cita_como_atendida()
        elif opcion_usuario == "6":
            # Salir del programa
            print("\n" + "="*40)
            print("Gracias por usar el sistema de citas")
            print("del taller mecánico.")
            print("="*40 + "\n")
            break
        else:
            print("❌ Error: Opción inválida. Seleccione entre 1 y 6.")
