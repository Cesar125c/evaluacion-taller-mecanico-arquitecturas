from src.application.use_cases.buscar_cita import BuscarCitaUseCase


class AtenderCitaUseCase:
    """Caso de uso para marcar una cita como atendida."""

    def __init__(self, cita_repository):
        self.cita_repository = cita_repository
        self.buscar_cita_use_case = BuscarCitaUseCase(cita_repository)

    def execute(self, id_cita):
        # Primero se localiza la cita; luego la entidad decide si puede atenderse.
        respuesta = self.buscar_cita_use_case.execute(id_cita)
        if not respuesta["success"]:
            return respuesta

        cita = respuesta["data"]
        respuesta_atencion = cita.atender()
        self.cita_repository.guardar(cita)
        return respuesta_atencion
