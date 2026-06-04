class Cita:
    """Representa una cita registrada en el taller mecanico."""

    def __init__(self, id, cliente, placa, marca, color, servicio, estado):
        self.id = id
        self.cliente = cliente
        self.placa = placa
        self.marca = marca
        self.color = color
        self.servicio = servicio
        self.estado = estado

    def convertir_a_diccionario(self):
        """Devuelve los datos de la cita en formato de diccionario."""
        return {
            "id": self.id,
            "cliente": self.cliente,
            "placa": self.placa,
            "marca": self.marca,
            "color": self.color,
            "servicio": self.servicio,
            "estado": self.estado,
        }
