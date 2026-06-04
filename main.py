from repositories.cita_repository import CitaRepository
from services.cita_service import CitaService
from views.menu import Menu


def main():
    """Punto de entrada del sistema."""
    cita_repository = CitaRepository()
    cita_service = CitaService(cita_repository)
    menu = Menu(cita_service)
    menu.iniciar()


if __name__ == "__main__":
    main()
