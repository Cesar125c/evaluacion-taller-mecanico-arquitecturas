class Menu:
    """Interfaz de consola para el sistema de citas."""

    def __init__(self, cita_service):
        self.cita_service = cita_service

    def iniciar(self):
        """Ejecuta el ciclo principal del menu."""
        print("\nBienvenido al Sistema de Citas del Taller Mecanico\n")

        while True:
            self.mostrar_menu_principal()
            opcion_usuario = input().strip()

            if opcion_usuario == "1":
                self.crear_cita()
            elif opcion_usuario == "2":
                self.listar_todas_citas()
            elif opcion_usuario == "3":
                self.buscar_cita()
            elif opcion_usuario == "4":
                self.cancelar_cita()
            elif opcion_usuario == "5":
                self.marcar_cita_como_atendida()
            elif opcion_usuario == "6":
                self.mostrar_despedida()
                break
            else:
                print("Error: Opcion invalida. Seleccione entre 1 y 6.")

    def mostrar_menu_principal(self):
        """Muestra las opciones disponibles."""
        print("\n" + "=" * 40)
        print(" SISTEMA DE CITAS - TALLER MECANICO")
        print(" ARQUITECTURA MONOLITICA POR CAPAS")
        print("=" * 40)
        print("\n1. Crear cita")
        print("2. Ver todas las citas")
        print("3. Buscar cita por ID")
        print("4. Cancelar cita")
        print("5. Marcar cita como atendida")
        print("6. Salir")
        print("\nSeleccione una opcion: ", end="")

    def crear_cita(self):
        """Solicita los datos para crear una cita."""
        print("\n--- CREAR NUEVA CITA ---")
        cliente = input("Nombre del cliente: ").strip()
        placa = input("Placa del vehiculo: ").strip()
        marca = input("Marca del vehiculo: ").strip()
        color = input("Color del vehiculo: ").strip()
        servicio = input("Servicio solicitado: ").strip()

        respuesta = self.cita_service.crear_cita(
            cliente=cliente,
            placa=placa,
            marca=marca,
            color=color,
            servicio=servicio,
        )
        self.mostrar_mensaje(respuesta)

    def listar_todas_citas(self):
        """Muestra todas las citas registradas."""
        print("\n--- TODAS LAS CITAS ---")
        respuesta = self.cita_service.listar_citas()
        citas = respuesta["data"]

        if not citas:
            print("No existen citas registradas.")
            return

        for cita in citas:
            self.mostrar_datos_cita(cita)

    def buscar_cita(self):
        """Busca y muestra una cita por ID."""
        print("\n--- BUSCAR CITA ---")
        id_cita = input("ID: ").strip()
        respuesta = self.cita_service.buscar_cita(id_cita)

        if respuesta["success"]:
            self.mostrar_datos_cita(respuesta["data"])
            return

        self.mostrar_mensaje(respuesta)

    def cancelar_cita(self):
        """Solicita el ID y cancela una cita."""
        print("\n--- CANCELAR CITA ---")
        id_cita = input("ID: ").strip()
        respuesta = self.cita_service.cancelar_cita(id_cita)
        self.mostrar_mensaje(respuesta)

    def marcar_cita_como_atendida(self):
        """Solicita el ID y marca una cita como atendida."""
        print("\n--- MARCAR CITA COMO ATENDIDA ---")
        id_cita = input("ID: ").strip()
        respuesta = self.cita_service.marcar_cita_como_atendida(id_cita)
        self.mostrar_mensaje(respuesta)

    def mostrar_datos_cita(self, cita):
        """Muestra una cita en formato legible."""
        datos_cita = cita.convertir_a_diccionario()

        print("\n" + "-" * 40)
        print(f"ID: {datos_cita['id']}")
        print(f"Cliente: {datos_cita['cliente']}")
        print(f"Placa: {datos_cita['placa']}")
        print(f"Marca: {datos_cita['marca']}")
        print(f"Color: {datos_cita['color']}")
        print(f"Servicio: {datos_cita['servicio']}")
        print(f"Estado: {datos_cita['estado']}")
        print("-" * 40)

    def mostrar_mensaje(self, respuesta):
        """Muestra el mensaje devuelto por el servicio."""
        print(respuesta["message"])

    def mostrar_despedida(self):
        """Muestra el mensaje de salida."""
        print("\n" + "=" * 40)
        print("Gracias por usar el sistema de citas")
        print("del taller mecanico.")
        print("=" * 40 + "\n")
