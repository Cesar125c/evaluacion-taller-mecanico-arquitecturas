from src.domain.repositories.cita_repository import CitaRepository


class CitaRepositoryMemory(CitaRepository):
    """Implementacion en memoria del repositorio de citas."""

    def __init__(self):
        self.citas = []
        self.proximo_id = 1

    def guardar(self, cita):
        # Si la cita ya existe, se reemplaza para conservar el cambio de estado.
        cita_existente = self.buscar_por_id(cita.id)
        if cita_existente:
            indice = self.citas.index(cita_existente)
            self.citas[indice] = cita
            return cita

        self.citas.append(cita)
        return cita

    def listar(self):
        return self.citas

    def buscar_por_id(self, id_cita):
        for cita in self.citas:
            if cita.id == id_cita:
                return cita
        return None

    def existe_placa_activa(self, placa):
        # Evita registrar dos citas activas para el mismo vehículo.
        placa_normalizada = placa.lower()
        for cita in self.citas:
            if cita.placa.lower() == placa_normalizada and cita.esta_activa():
                return True
        return False

    def siguiente_id(self):
        id_disponible = self.proximo_id
        self.proximo_id += 1
        return id_disponible
