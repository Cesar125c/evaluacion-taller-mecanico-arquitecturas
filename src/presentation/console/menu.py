class Menu:
    """Interfaz de consola para el sistema de citas."""

    def __init__(
        self,
        crear_cita_use_case,
        listar_citas_use_case,
        buscar_cita_use_case,
        cancelar_cita_use_case,
        atender_cita_use_case,
    ):
        self.crear_cita_use_case = crear_cita_use_case
        self.listar_citas_use_case = listar_citas_use_case
        self.buscar_cita_use_case = buscar_cita_use_case
        self.cancelar_cita_use_case = cancelar_cita_use_case
        self.atender_cita_use_case = atender_cita_use_case

    def iniciar(self):
        print("\nBienvenido al Sistema de Citas del Taller Mecanico\n")

        while True:
            self._mostrar_menu()
            opcion = input().strip()

            if opcion == "1":
                self._crear_cita()
            elif opcion == "2":
                self._listar_citas()
            elif opcion == "3":
                self._buscar_cita()
            elif opcion == "4":
                self._cancelar_cita()
            elif opcion == "5":
                self._atender_cita()
            elif opcion == "6":
                self._mostrar_despedida()
                break
            else:
                print("Error: Opcion invalida. Seleccione entre 1 y 6.")

    def _mostrar_menu(self):
        print("\n" + "=" * 40)
        print(" SISTEMA DE CITAS - TALLER MECANICO")
        print(" ENFOQUE DDD")
        print("=" * 40)
        print("\n1. Crear cita")
        print("2. Ver todas las citas")
        print("3. Buscar cita por ID")
        print("4. Cancelar cita")
        print("5. Marcar cita como atendida")
        print("6. Salir")
        print("\nSeleccione una opcion: ", end="")

    def _crear_cita(self):
        print("\n--- CREAR NUEVA CITA ---")
        respuesta = self.crear_cita_use_case.execute(
            cliente=input("Nombre del cliente: ").strip(),
            placa=input("Placa del vehiculo: ").strip(),
            marca=input("Marca del vehiculo: ").strip(),
            color=input("Color del vehiculo: ").strip(),
            servicio=input("Servicio solicitado: ").strip(),
        )
        self._mostrar_mensaje(respuesta)

    def _listar_citas(self):
        print("\n--- TODAS LAS CITAS ---")
        citas = self.listar_citas_use_case.execute()["data"]

        if not citas:
            print("No existen citas registradas.")
            return

        for cita in citas:
            self._mostrar_cita(cita)

    def _buscar_cita(self):
        print("\n--- BUSCAR CITA ---")
        respuesta = self.buscar_cita_use_case.execute(input("ID: ").strip())

        if respuesta["success"]:
            self._mostrar_cita(respuesta["data"])
            return

        self._mostrar_mensaje(respuesta)

    def _cancelar_cita(self):
        print("\n--- CANCELAR CITA ---")
        respuesta = self.cancelar_cita_use_case.execute(input("ID: ").strip())
        self._mostrar_mensaje(respuesta)

    def _atender_cita(self):
        print("\n--- MARCAR CITA COMO ATENDIDA ---")
        respuesta = self.atender_cita_use_case.execute(input("ID: ").strip())
        self._mostrar_mensaje(respuesta)

    def _mostrar_cita(self, cita):
        datos = cita.convertir_a_diccionario()
        print("\n" + "-" * 40)
        print(f"ID: {datos['id']}")
        print(f"Cliente: {datos['cliente']}")
        print(f"Placa: {datos['placa']}")
        print(f"Marca: {datos['marca']}")
        print(f"Color: {datos['color']}")
        print(f"Servicio: {datos['servicio']}")
        print(f"Estado: {datos['estado']}")
        print("-" * 40)

    def _mostrar_mensaje(self, respuesta):
        print(respuesta["message"])

    def _mostrar_despedida(self):
        print("\n" + "=" * 40)
        print("Gracias por usar el sistema de citas")
        print("del taller mecanico.")
        print("=" * 40 + "\n")
