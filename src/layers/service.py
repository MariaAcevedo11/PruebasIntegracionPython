#Servicio que contiene la lógica de negocio de usuarios, funciones relacionadas a los usuarios 

from typing import Optional
from .repository import InMemoryUserRepository

class UserService:
    def __init__(self, repo: InMemoryUserRepository):
        self.repo = repo

    #Retorna el nombre completo del usuario por ID
    def get_full_name(self, user_id: int) -> Optional[str]:
        u = self.repo.find_by_id(user_id)
        return None if u is None else f"{u.first} {u.last}"
