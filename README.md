# Sistema de Citas para Taller Mecánico

Aplicación de consola desarrollada en Python para registrar y administrar citas de un taller mecánico.

Este proyecto forma parte de una evaluación académica de Arquitectura de Software. La rama actual implementa el sistema con un enfoque de código espagueti, es decir, con la lógica concentrada en un solo archivo para analizar sus limitaciones frente a otros estilos de arquitectura.

## Funcionalidades

El sistema permite:

- Crear citas para clientes.
- Ver todas las citas registradas.
- Buscar una cita por ID.
- Cancelar una cita pendiente.
- Marcar una cita como atendida.
- Salir del programa desde el menú principal.

## Datos de una cita

Cada cita registra la siguiente información:

| Campo | Descripción |
|------|-------------|
| `id` | Identificador único generado automáticamente. |
| `cliente` | Nombre del cliente. |
| `placa` | Placa del vehículo. |
| `marca` | Marca del vehículo. |
| `color` | Color del vehículo. |
| `servicio` | Servicio solicitado. |
| `estado` | Estado actual de la cita. |

Estados disponibles:

```text
PENDIENTE
ATENDIDA
CANCELADA
```

## Reglas principales

- Todos los campos de la cita son obligatorios.
- Toda cita nueva inicia en estado `PENDIENTE`.
- Solo una cita pendiente puede cancelarse.
- Solo una cita pendiente puede marcarse como atendida.
- Una cita cancelada no puede ser atendida.
- Una cita atendida no puede ser cancelada.
- El ID ingresado debe ser numérico.

## Código espagueti aplicado

En esta rama se aplica código espagueti de forma intencional. Este término se usa para describir código con poca organización interna, donde varias responsabilidades se mezclan dentro de los mismos archivos o funciones.

En este proyecto se refleja de la siguiente manera:

- Toda la aplicación está desarrollada en un solo archivo: `main.py`.
- El menú, las validaciones, la lógica de negocio y la presentación en consola están juntos.
- Las citas se manejan mediante variables globales.
- No existen capas, clases, módulos separados ni una estructura de dominio.

El sistema funciona, pero esta organización puede dificultar el mantenimiento si el proyecto crece. Por eso se usa como ejemplo académico para comparar este enfoque con arquitecturas más ordenadas.

## Estructura del proyecto

```text
evaluacion-taller-mecanico-arquitecturas/
├── main.py
├── README.md
└── .gitignore
```

### Archivos principales

- `main.py`: contiene el menú, las validaciones y toda la lógica del sistema.
- `README.md`: documentación del proyecto.
- `.gitignore`: archivos y carpetas excluidos del control de versiones.

## Requisitos

- Python 3.7 o superior.
- Terminal o consola de comandos.

No se necesitan librerías externas.

## Cómo ejecutar el programa

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

```bash
python main.py
```

Si el comando anterior no funciona, usar:

```bash
python3 main.py
```

## Instrucciones de uso

Al iniciar el programa se muestra el menú principal:

```text
========================================
 SISTEMA DE CITAS - TALLER MECANICO
========================================

1. Crear cita
2. Ver todas las citas
3. Buscar cita por ID
4. Cancelar cita
5. Marcar cita como atendida
6. Salir
```

Para usar el sistema:

1. Escribir el número de la opción deseada.
2. Presionar `Enter`.
3. Completar los datos solicitados por la consola.
4. Revisar los mensajes de confirmación o error.
5. Seleccionar la opción `6` para finalizar el programa.

## Almacenamiento

Las citas se guardan únicamente en memoria mientras el programa está abierto. Al cerrar la aplicación, los datos registrados se pierden.

## Nota académica

Esta versión mantiene una estructura simple e intencionalmente poco separada para representar código espagueti. Su objetivo es servir como punto de comparación frente a implementaciones más organizadas, como arquitectura en capas o Domain-Driven Design.
