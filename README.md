# Sistema de Citas - Taller Mecanico

Proyecto academico desarrollado en Python para gestionar citas de un taller mecanico desde consola.

La aplicacion permite registrar citas, listar todas las citas, buscar por ID, cancelar una cita y marcarla como atendida. Los datos se guardan en memoria, por lo que no se usa base de datos ni archivos persistentes.

## Arquitectura

Esta version usa una arquitectura **monolitica por capas**. El sistema sigue siendo una sola aplicacion, pero el codigo esta separado por responsabilidades para que sea mas claro, mantenible y facil de extender.

Flujo principal:

```text
Usuario -> View/Menu -> Service -> Repository -> Memoria
```

## Estructura del Proyecto

```text
evaluacion-taller-mecanico-arquitecturas/
├── main.py
├── README.md
├── .gitignore
├── models/
│   ├── __init__.py
│   └── cita.py
├── repositories/
│   ├── __init__.py
│   └── cita_repository.py
├── services/
│   ├── __init__.py
│   └── cita_service.py
└── views/
    ├── __init__.py
    └── menu.py
```

## Responsabilidad de Cada Archivo

### `main.py`

Punto de entrada del programa. Crea el repositorio, el servicio y el menu principal.

### `models/cita.py`

Contiene la clase `Cita`, que representa una cita del taller.

Campos principales:

- `id`
- `cliente`
- `placa`
- `marca`
- `color`
- `servicio`
- `estado`

### `repositories/cita_repository.py`

Administra el almacenamiento en memoria.

Funciones principales:

- Guardar citas.
- Listar citas.
- Buscar citas por ID.
- Generar IDs autoincrementales.

### `services/cita_service.py`

Contiene la logica de negocio.

Se encarga de:

- Validar campos obligatorios.
- Crear citas en estado `PENDIENTE`.
- Cancelar citas.
- Marcar citas como `ATENDIDA`.
- Validar que el ID sea correcto.
- Evitar cambios de estado no permitidos.

### `views/menu.py`

Maneja la interaccion con el usuario en consola.

Se encarga de:

- Mostrar el menu.
- Pedir datos con `input()`.
- Mostrar resultados con `print()`.
- Llamar al servicio correspondiente.

## Funcionalidades

El menu principal incluye:

```text
1. Crear cita
2. Ver todas las citas
3. Buscar cita por ID
4. Cancelar cita
5. Marcar cita como atendida
6. Salir
```

Cada cita nueva inicia con estado `PENDIENTE`.

Estados disponibles:

- `PENDIENTE`
- `CANCELADA`
- `ATENDIDA`

## Reglas Principales

- Todos los campos de la cita son obligatorios.
- El ID debe ser numerico.
- No se puede cancelar una cita ya atendida.
- No se puede atender una cita cancelada.
- Si una cita no existe, se muestra un mensaje de error.

## Ejecucion

Desde la carpeta del proyecto:

```bash
python main.py
```

No requiere librerias externas.

## Diferencia con Codigo Espagueti

En la version de codigo espagueti, todo estaba concentrado en un solo archivo: menu, validaciones, reglas de negocio y almacenamiento.

En esta version por capas:

- `main.py` solo inicia el sistema.
- `views` maneja la consola.
- `services` maneja las reglas de negocio.
- `repositories` maneja los datos en memoria.
- `models` representa la estructura de una cita.

Esta separacion hace que el codigo sea mas ordenado, facil de entender y mas sencillo de modificar.
