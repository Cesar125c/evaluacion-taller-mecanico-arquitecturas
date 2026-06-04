from src.application.use_cases.buscar_cita import BuscarCitaUseCase


class CancelarCitaUseCase:
    """Caso de uso para cancelar una cita."""

    def __init__(self, cita_repository):
        self.cita_repository = cita_repository
        self.buscar_cita_use_case = BuscarCitaUseCase(cita_repository)

    def execute(self, id_cita):
        respuesta = self.buscar_cita_use_case.execute(id_cita)
        if not respuesta["success"]:
            return respuesta

        cita = respuesta["data"]
        respuesta_cancelacion = cita.cancelar()
        self.cita_repository.guardar(cita)
        return respuesta_cancelacion
