from src.domain.value_objects.estado_cita import EstadoCita


class Cita:
    """Entidad principal del dominio de citas del taller mecanico."""

    def __init__(self, id, cliente, placa, marca, color, servicio, estado=EstadoCita.PENDIENTE):
        self.id = id
        self.cliente = cliente
        self.placa = placa
        self.marca = marca
        self.color = color
        self.servicio = servicio
        self.estado = estado

    def cancelar(self):
        """Aplica la regla de negocio para cancelar una cita."""
        if self.esta_cancelada():
            return self._respuesta(False, f"La cita {self.id} ya estaba cancelada.")

        if self.esta_atendida():
            return self._respuesta(False, "Error: No se puede cancelar una cita que ya fue atendida.")

        self.estado = EstadoCita.CANCELADA
        return self._respuesta(True, f"Cita {self.id} cancelada exitosamente.")

    def atender(self):
        """Aplica la regla de negocio para atender una cita."""
        if self.esta_atendida():
            return self._respuesta(False, f"La cita {self.id} ya estaba marcada como atendida.")

        if self.esta_cancelada():
            return self._respuesta(False, "Error: No se puede atender una cita que fue cancelada.")

        self.estado = EstadoCita.ATENDIDA
        return self._respuesta(True, f"Cita {self.id} marcada como atendida exitosamente.")

    def esta_cancelada(self):
        return self.estado == EstadoCita.CANCELADA

    def esta_atendida(self):
        return self.estado == EstadoCita.ATENDIDA

    def esta_activa(self):
        return self.estado != EstadoCita.CANCELADA

    def convertir_a_diccionario(self):
        return {
            "id": self.id,
            "cliente": self.cliente,
            "placa": self.placa,
            "marca": self.marca,
            "color": self.color,
            "servicio": self.servicio,
            "estado": self.estado.value,
        }

    def _respuesta(self, success, message):
        return {
            "success": success,
            "message": message,
            "data": self,
        }
