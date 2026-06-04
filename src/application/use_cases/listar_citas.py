class ListarCitasUseCase:
    """Caso de uso para listar citas."""

    def __init__(self, cita_repository):
        self.cita_repository = cita_repository

    def execute(self):
        return {
            "success": True,
            "message": "Citas obtenidas correctamente.",
            "data": self.cita_repository.listar(),
        }
