ESTADO_PENDIENTE = "PENDIENTE"
ESTADO_CANCELADA = "CANCELADA"
ESTADO_ATENDIDA = "ATENDIDA"


class CitaService:
    """Contiene las reglas de negocio del sistema de citas."""

    def __init__(self, cita_repository):
        self.cita_repository = cita_repository

    def crear_cita(self, cliente, placa, marca, color, servicio):
        """Valida y registra una nueva cita."""
        campos = {
            "cliente": cliente,
            "placa": placa,
            "marca": marca,
            "color": color,
            "servicio": servicio,
        }
        error = self._validar_campos_obligatorios(campos)
        if error:
            return self._respuesta(False, error)

        cita = self.cita_repository.guardar(
            cliente=cliente,
            placa=placa,
            marca=marca,
            color=color,
            servicio=servicio,
            estado=ESTADO_PENDIENTE,
        )
        return self._respuesta(True, f"Cita creada correctamente con ID: {cita.id}.", cita)

    def listar_citas(self):
        """Devuelve todas las citas registradas."""
        return self._respuesta(True, "Citas obtenidas correctamente.", self.cita_repository.listar_todas())

    def buscar_cita(self, id_cita):
        """Busca una cita por ID."""
        respuesta_id = self._validar_id(id_cita)
        if not respuesta_id["success"]:
            return respuesta_id

        cita = self.cita_repository.buscar_por_id(respuesta_id["data"])
        if not cita:
            return self._respuesta(False, f"Error: No existe cita con ID {respuesta_id['data']}.")

        return self._respuesta(True, "Cita encontrada.", cita)

    def cancelar_cita(self, id_cita):
        """Cancela una cita pendiente."""
        return self._cambiar_estado(
            id_cita=id_cita,
            estado_destino=ESTADO_CANCELADA,
            estado_bloqueado=ESTADO_ATENDIDA,
            mensaje_estado_actual="La cita {id} ya estaba cancelada.",
            mensaje_estado_bloqueado="Error: No se puede cancelar una cita que ya fue atendida.",
            mensaje_exito="Cita {id} cancelada exitosamente.",
        )

    def marcar_cita_como_atendida(self, id_cita):
        """Marca una cita pendiente como atendida."""
        return self._cambiar_estado(
            id_cita=id_cita,
            estado_destino=ESTADO_ATENDIDA,
            estado_bloqueado=ESTADO_CANCELADA,
            mensaje_estado_actual="La cita {id} ya estaba marcada como atendida.",
            mensaje_estado_bloqueado="Error: No se puede atender una cita que fue cancelada.",
            mensaje_exito="Cita {id} marcada como atendida exitosamente.",
        )

    def _cambiar_estado(
        self,
        id_cita,
        estado_destino,
        estado_bloqueado,
        mensaje_estado_actual,
        mensaje_estado_bloqueado,
        mensaje_exito,
    ):
        respuesta = self.buscar_cita(id_cita)
        if not respuesta["success"]:
            return respuesta

        cita = respuesta["data"]
        if cita.estado == estado_destino:
            return self._respuesta(False, mensaje_estado_actual.format(id=cita.id), cita)

        if cita.estado == estado_bloqueado:
            return self._respuesta(False, mensaje_estado_bloqueado, cita)

        cita.estado = estado_destino
        return self._respuesta(True, mensaje_exito.format(id=cita.id), cita)

    def _validar_campos_obligatorios(self, campos):
        for nombre, valor in campos.items():
            if not valor:
                return f"Error: El campo {nombre} es obligatorio."
        return None

    def _validar_id(self, id_cita):
        if not id_cita:
            return self._respuesta(False, "Error: El ID no puede estar vacio.")

        if not id_cita.isdigit():
            return self._respuesta(False, "Error: El ID debe ser un numero.")

        return self._respuesta(True, "ID valido.", int(id_cita))

    def _respuesta(self, success, message, data=None):
        return {
            "success": success,
            "message": message,
            "data": data,
        }
