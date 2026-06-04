from src.application.use_cases.atender_cita import AtenderCitaUseCase
from src.application.use_cases.buscar_cita import BuscarCitaUseCase
from src.application.use_cases.cancelar_cita import CancelarCitaUseCase
from src.application.use_cases.crear_cita import CrearCitaUseCase
from src.application.use_cases.listar_citas import ListarCitasUseCase
from src.infrastructure.repositories.cita_repository_memory import CitaRepositoryMemory
from src.presentation.console.menu import Menu


def main():
    """Punto de entrada del sistema."""
    # Se arma la aplicación conectando infraestructura, casos de uso y presentación.
    cita_repository = CitaRepositoryMemory()
    menu = Menu(
        crear_cita_use_case=CrearCitaUseCase(cita_repository),
        listar_citas_use_case=ListarCitasUseCase(cita_repository),
        buscar_cita_use_case=BuscarCitaUseCase(cita_repository),
        cancelar_cita_use_case=CancelarCitaUseCase(cita_repository),
        atender_cita_use_case=AtenderCitaUseCase(cita_repository),
    )
    menu.iniciar()


if __name__ == "__main__":
    main()
