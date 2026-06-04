from abc import ABC, abstractmethod


class CitaRepository(ABC):
    """Puerto del dominio para acceder a citas."""

    # Define lo que necesita el dominio sin depender de una forma concreta de almacenamiento.

    @abstractmethod
    def guardar(self, cita):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def buscar_por_id(self, id_cita):
        pass

    @abstractmethod
    def existe_placa_activa(self, placa):
        pass

    @abstractmethod
    def siguiente_id(self):
        pass
