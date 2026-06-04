from enum import Enum


class EstadoCita(Enum):
    """Estados permitidos para una cita."""

    PENDIENTE = "PENDIENTE"
    CANCELADA = "CANCELADA"
    ATENDIDA = "ATENDIDA"
