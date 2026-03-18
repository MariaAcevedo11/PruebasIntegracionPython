
# Introducción a Pruebas de Integración (Python) — 4 partes

Este repositorio contiene un ejercicio práctico en **Python** para evidenciar 4 tipos de integración:

1) **Por capas** (Controller → Service → Repository in-memory)  
2) **Modular** (un módulo usa a otro)  
3) **Con API externa** (cliente HTTP real contra servidor simulado)  
4) **Con base de datos** (SQLite en memoria)

## Requisitos
- Python 3.11+
- `pip install -r requirements.txt`

## Ejecutar
```bash
pytest -q
```
O por parte:
```bash
pytest -q tests/test_part1_layers.py
pytest -q tests/test_part2_modules.py
pytest -q tests/test_part3_external_api.py
pytest -q tests/test_part4_database.py
```

## Estructura
```
src/
  layers/ (modelo, repositorio in-memory, servicio, controlador)
  modules/ (discount, order)
  external/ (cliente http)
  db/ (repositorio sqlite)
```

## Estructura detallada
.devcontainer/ para abrir en GitHub Codespaces con Python 3.11 y extensiones.
.github/workflows/ci.yml: workflow de Actions que instala deps y ejecuta pytest.
requirements.txt: pytest, httpx, pytest-httpserver.
pytest.ini: configuración para descubrir tests desde src/ y tests/.
src/ con el código de producción:

layers/: modelo User, InMemoryUserRepository, UserService, UserController.
modules/: DiscountEngine + OrderCalculator.
external/: UserClient con httpx.
db/: SQLiteUserRepository con sqlite3 en memoria.


tests/ con 4 archivos:

test_part1_layers.py — por capas.
test_part2_modules.py — modular.
test_part3_external_api.py — API externa con pytest-httpserver.
test_part4_database.py — base de datos (SQLite in‑memory).


README.md con instrucciones ejecutables.

# ACTIVIDAD
## Parte 1 — Integración por capas (Controller → Service → Repository)
**Si cambias el formato de salida del controlador, ¿qué otras capas tendrías que adaptar?**
Si se cambia el formato de salida del controlador, principalmente habría que adaptar la capa de servicio, ya que el controlador depende de funciones como get_user_full_name, que a su vez llama a service.get_full_name.
El impacto principal estaría en el controlador y el servicio, mientras que el repositorio y el modelo solo se verían afectados si cambia la estructura interna de los datos.

## Parte 2 — Integración modular (Módulo A usa Módulo B)
**Explica por qué esta es una prueba de integración (y no solo unitaria)**
Porque el módulo order se conecta con discount para poder obtener el descuento dentro de la función final_total. Esto significa que order depende directamente de discount para calcular el valor final.
Se considera una prueba de integración, ya que se está verificando cómo interactúan ambos módulos en conjunto. No es una prueba unitaria porque no se está evaluando una parte aislada del sistema, sino la conexión y el funcionamiento entre múltiples módulos.

##  Parte 3 — Integración con API externa (cliente HTTP + servidor simulado)
** Cuál es la diferencia entre mockear la librería HTTP vs. levantar un servidor simulado**
Mockear la librería es más rápido y enfocado a pruebas unitarias porque aísla el código, solo verifica cómo el código maneja la respuesta, mientras que el servidor simulado es más realista y se usa en pruebas de integración porque valida cómo interactúan los componentes a través de HTTP, el código hace una petición HTTP real (aunque local), y el servidor responde como lo haría una API externa asi probando la integración completa de la llamada HTTP.
