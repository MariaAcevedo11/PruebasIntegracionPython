#Definición de la clase user con sus respectivos atributos 
#Frozen = true, datos inmutables 
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    id: int
    first: str
    last: str
