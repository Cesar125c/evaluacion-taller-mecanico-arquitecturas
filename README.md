# Sistema de Citas - Taller Mecanico

**Rama actual:** `enfoque-ddd`

Proyecto academico en Python para gestionar citas de un taller mecanico desde consola. Permite crear citas, listarlas, buscarlas por ID, cancelarlas y marcarlas como atendidas. La informacion se guarda en memoria, sin base de datos ni librerias externas.

## Objetivo

Aplicar **Domain-Driven Design (DDD)** para organizar el sistema alrededor del dominio del taller mecanico. A diferencia de una separacion solo tecnica, esta version ubica las reglas importantes en la entidad `Cita` y en los casos de uso.

## Estructura

```text
evaluacion-taller-mecanico-arquitecturas/
├── main.py
├── README.md
├── .gitignore
└── src/
    ├── domain/
    │   ├── entities/cita.py
    │   ├── value_objects/estado_cita.py
    │   └── repositories/cita_repository.py
    ├── application/use_cases/
    │   ├── crear_cita.py
    │   ├── listar_citas.py
    │   ├── buscar_cita.py
    │   ├── cancelar_cita.py
    │   └── atender_cita.py
    ├── infrastructure/repositories/cita_repository_memory.py
    └── presentation/console/menu.py
```

## Responsabilidades

- `main.py`: punto de entrada; crea dependencias e inicia el menu.
- `domain/entities/cita.py`: entidad principal con datos y comportamientos como `cancelar()` y `atender()`.
- `domain/value_objects/estado_cita.py`: define `PENDIENTE`, `CANCELADA` y `ATENDIDA`.
- `domain/repositories/cita_repository.py`: contrato del repositorio, sin almacenamiento real.
- `application/use_cases`: coordina acciones del sistema: crear, listar, buscar, cancelar y atender citas.
- `infrastructure/repositories/cita_repository_memory.py`: implementa el almacenamiento en memoria.
- `presentation/console/menu.py`: muestra el menu, pide datos y presenta resultados.

## Flujo

```text
Usuario -> Presentation -> Application -> Domain -> Infrastructure
```

## Datos de una Cita

Cada cita contiene:

- `id`
- `cliente`
- `placa`
- `marca`
- `color`
- `servicio`
- `estado`

## Funcionalidades

```text
1. Crear cita
2. Ver todas las citas
3. Buscar cita por ID
4. Cancelar cita
5. Marcar cita como atendida
6. Salir
```

## Reglas de Negocio

- Todos los campos son obligatorios.
- El ID debe ser numerico.
- Toda cita nueva inicia como `PENDIENTE`.
- No se permite otra cita activa para la misma placa.
- Una cita activa es una cita que no esta `CANCELADA`.
- No se puede cancelar una cita `ATENDIDA`.
- No se puede atender una cita `CANCELADA`.
- Si la cita no existe, se muestra un error.

## Ejecucion

```bash
python main.py
```

## Diferencia con Versiones Anteriores

En `codigo-espagueti`, todo estaba mezclado en un solo archivo. En `monolitico-capas`, el sistema se separaba por capas tecnicas como modelos, servicios y repositorios. En esta version DDD, la organizacion se centra en el dominio: entidad `Cita`, estados, contrato de repositorio y casos de uso.

## Conclusion

Esta version mantiene una aplicacion simple de consola, pero con una estructura mas clara: el dominio contiene las reglas principales, la aplicacion coordina casos de uso, la infraestructura guarda datos en memoria y la presentacion maneja la consola.
