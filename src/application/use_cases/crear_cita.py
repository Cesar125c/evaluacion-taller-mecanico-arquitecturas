from src.domain.entities.cita import Cita


class CrearCitaUseCase:
    """Caso de uso para registrar una nueva cita."""

    def __init__(self, cita_repository):
        self.cita_repository = cita_repository

    def execute(self, cliente, placa, marca, color, servicio):
        # El caso de uso valida la entrada antes de crear la entidad del dominio.
        campos = {
            "cliente": cliente,
            "placa": placa,
            "marca": marca,
            "color": color,
            "servicio": servicio,
        }
        for nombre, valor in campos.items():
            if not valor:
                return self._respuesta(False, f"Error: El campo {nombre} es obligatorio.")

        if self.cita_repository.existe_placa_activa(placa):
            return self._respuesta(False, "Error: Ya existe una cita activa para la misma placa.")

        # El repositorio entrega el ID; la entidad nace con estado pendiente por defecto.
        cita = Cita(
            id=self.cita_repository.siguiente_id(),
            cliente=cliente,
            placa=placa,
            marca=marca,
            color=color,
            servicio=servicio,
        )
        self.cita_repository.guardar(cita)
        return self._respuesta(True, f"Cita creada correctamente con ID: {cita.id}.", cita)

    def _respuesta(self, success, message, data=None):
        return {
            "success": success,
            "message": message,
            "data": data,
        }
