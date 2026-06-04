class BuscarCitaUseCase:
    """Caso de uso para buscar una cita por ID."""

    def __init__(self, cita_repository):
        self.cita_repository = cita_repository

    def execute(self, id_cita):
        # El ID llega desde consola como texto, por eso se valida antes de buscar.
        respuesta_id = self._validar_id(id_cita)
        if not respuesta_id["success"]:
            return respuesta_id

        cita = self.cita_repository.buscar_por_id(respuesta_id["data"])
        if not cita:
            return self._respuesta(False, f"Error: No existe cita con ID {respuesta_id['data']}.")

        return self._respuesta(True, "Cita encontrada.", cita)

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
