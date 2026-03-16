# Controlador: intermediario entre capa Presentación y Capa de servicio

from .service import UserService

class UserController:
    def __init__(self, service: UserService):
        self.service = service

    # Simula un controlador sin servidor web
    def get_user_full_name(self, user_id: int) -> str:
        full = self.service.get_full_name(user_id)
        return "404 NOT_FOUND" if full is None else full
