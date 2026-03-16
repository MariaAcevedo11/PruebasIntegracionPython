# Controlador: intermediario entre capa Presentación y Capa de servicio

from .service import UserService

class UserController:
    def __init__(self, service: UserService):
        self.service = service

    # Simula un controlador sin servidor web
    def get_user_full_name(self, user_id: int) -> str:
        full = self.service.get_full_name(user_id)
        return "404 NOT_FOUND" if full is None else full

# Si cambias el formato de salida del controlador. ¿Qué otras capas tendrías que adaptar?
'''
Es depende de qué se cambie en la salida, 
se debería de cambiar entonces el servicio porque el controlador depende de el 
y el servicio depende del respositorio

'''
