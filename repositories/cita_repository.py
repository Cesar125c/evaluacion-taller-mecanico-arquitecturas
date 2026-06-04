from models.cita import Cita


class CitaRepository:
    """Administra el almacenamiento en memoria de las citas."""

    def __init__(self):
        self.citas = []
        self.proximo_id = 1

    def guardar(self, cliente, placa, marca, color, servicio, estado):
        """Crea y guarda una nueva cita en memoria."""
        cita = Cita(
            id=self.proximo_id,
            cliente=cliente,
            placa=placa,
            marca=marca,
            color=color,
            servicio=servicio,
            estado=estado,
        )
        self.citas.append(cita)
        self.proximo_id += 1
        return cita

    def listar_todas(self):
        """Devuelve todas las citas registradas."""
        return self.citas

    def buscar_por_id(self, id_cita):
        """Busca una cita por su identificador."""
        for cita in self.citas:
            if cita.id == id_cita:
                return cita
        return None
