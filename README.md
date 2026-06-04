# Sistema de Citas - Taller Mecánico

## 📋 Información General

**Rama actual:** `codigo-espagueti`

**Lenguaje:** Python 3

**Tipo de aplicación:** Aplicación de consola (terminal)

**Autor:** Evaluación Sumativa - Arquitectura de Software

---

## 🎯 Objetivo Académico

Este proyecto es un **estudio comparativo de tres estilos de arquitectura de software**. Cada rama implementa el **mismo sistema funcional** usando un enfoque arquitectónico diferente:

1. **`codigo-espagueti`** (rama actual) → Código mal organizado, todo mezclado
2. **`monolitico-capas`** (rama futura) → Arquitectura en capas (presentación, negocio, datos)
3. **`enfoque-ddd`** (rama futura) → Domain-Driven Design con ubiquitous language

El objetivo es **comparar ventajas y desventajas** de cada enfoque en un proyecto académico.

---

## 🍝 ¿Qué es Código Espagueti?

**Código Espagueti** es un término que describe código con una estructura **muy pobre**, donde:

- El flujo de control es **difícil de seguir** (como seguir un espagueti enredado)
- No hay **separación de responsabilidades**
- La lógica está **dispersa y repetida** en múltiples lugares
- Es **difícil de mantener, testear y extender**
- Las dependencias entre componentes son **confusas**

### Características típicas:

```
❌ Todo en un archivo
❌ Sin clases ni módulos
❌ Variables globales compartidas
❌ Funciones con múltiples responsabilidades
❌ Validación dispersa en varias funciones
❌ Lógica de búsqueda repetida
❌ Difícil de reutilizar código
❌ Difícil de escribir pruebas unitarias
```

---

## 🔴 Por qué esta versión es Código Espagueti

En la rama `codigo-espagueti`:

✗ **Todo está en un único archivo** (`main.py`)  
✗ **No hay clases** – Solo funciones globales  
✗ **Variables globales** – `citas` y `proximo_id` compartidas globalmente  
✗ **Mezcla de responsabilidades** – Cada función hace entrada, validación, lógica y presentación  
✗ **Validaciones dispersas** – Reglas de negocio esparcidas en varias funciones  
✗ **Búsqueda repetida** – La iteración sobre `citas` ocurre en múltiples funciones  
✗ **Sin separación de capas** – No hay distinction entre presentación, negocio o datos  
✗ **Sin patrones de diseño** – Código procedural simple

### Ejemplo de Spaghetti:

```python
# En crear_cita() está TODO mezclado:
def crear_cita():
    # 1. ENTRADA - Input del usuario
    cliente = input("Nombre: ").strip()
    
    # 2. VALIDACIÓN - Reglas de negocio
    if not cliente:
        print("Error")
        return
    
    # 3. BÚSQUEDA - Lógica de acceso a datos
    for cita in citas:
        if cita["fecha"] == fecha...
    
    # 4. LÓGICA - Cambiar estado
    nueva_cita = {...}
    
    # 5. PRESENTACIÓN - Mostrar resultado
    print("Creado")
```

Todas estas responsabilidades en UNA función = **SPAGHETTI CODE**

---

## 📱 Funcionalidades del Sistema

El programa muestra un menú interactivo con las siguientes opciones:

### **Menú Principal**

```
========================================
 SISTEMA DE CITAS - TALLER MECÁNICO
========================================

1. Crear cita
2. Ver todas las citas
3. Buscar cita por ID
4. Cancelar cita
5. Marcar cita como atendida
6. Salir

Seleccione una opción:
```

### **Opción 1: Crear Cita**

Solicita:
- Nombre del cliente
- Placa del vehículo
- Servicio solicitado
- Fecha (YYYY-MM-DD)
- Hora (HH:MM)

**Validaciones:**
- ✓ Campos no pueden estar vacíos
- ✓ No permitir dos citas activas en la misma fecha y hora
- ✓ Se asigna ID automáticamente
- ✓ Estado inicial: `PENDIENTE`

### **Opción 2: Ver Todas las Citas**

Muestra todas las citas con formato legible:
```
----------------------------------------
ID: 1
Cliente: Juan Pérez
Placa: PBA-1234
Servicio: Cambio de aceite
Fecha: 2026-06-05
Hora: 10:00
Estado: PENDIENTE
----------------------------------------
```

Si no hay citas: `No existen citas registradas.`

### **Opción 3: Buscar Cita por ID**

Solicita el ID y muestra los detalles si existe.

**Validaciones:**
- ✓ ID no puede estar vacío
- ✓ ID debe ser numérico
- ✓ Cita debe existir

### **Opción 4: Cancelar Cita**

Cancela una cita por su ID.

**Validaciones:**
- ✓ ID no puede estar vacío y debe ser numérico
- ✓ Cita debe existir
- ✓ Solo se pueden cancelar citas en estado `PENDIENTE`
- ✓ Si ya está `CANCELADA`: mensaje informativo
- ✓ Si está `ATENDIDA`: no se puede cancelar (error)

### **Opción 5: Marcar Cita como Atendida**

Marca una cita como atendida por su ID.

**Validaciones:**
- ✓ ID no puede estar vacío y debe ser numérico
- ✓ Cita debe existir
- ✓ Solo se pueden atender citas en estado `PENDIENTE`
- ✓ Si ya está `ATENDIDA`: mensaje informativo
- ✓ Si está `CANCELADA`: no se puede atender (error)

### **Opción 6: Salir**

Muestra mensaje de despedida y termina el programa.

---

## 📊 Datos de una Cita

Cada cita es un diccionario con estos campos:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador único (autoincremental) |
| `cliente` | str | Nombre del cliente |
| `placa` | str | Placa del vehículo |
| `servicio` | str | Tipo de servicio solicitado |
| `fecha` | str | Fecha en formato YYYY-MM-DD |
| `hora` | str | Hora en formato HH:MM |
| `estado` | str | `PENDIENTE`, `CANCELADA` o `ATENDIDA` |

### Ejemplo:

```python
{
    "id": 1,
    "cliente": "Juan Pérez",
    "placa": "PBA-1234",
    "servicio": "Cambio de aceite",
    "fecha": "2026-06-05",
    "hora": "10:00",
    "estado": "PENDIENTE"
}
```

---

## 🔄 Estados de una Cita

Una cita tiene **tres estados posibles**:

| Estado | Descripción |
|--------|-------------|
| `PENDIENTE` | Cita creada, esperando ser atendida |
| `ATENDIDA` | El servicio ya fue completado |
| `CANCELADA` | La cita fue cancelada antes de ser atendida |

**Transiciones válidas:**

```
PENDIENTE → ATENDIDA (marcar como atendida)
PENDIENTE → CANCELADA (cancelar cita)
(Las demás transiciones no son permitidas)
```

---

## 💾 Almacenamiento de Datos

- **NO usa base de datos** ✗
- **NO usa archivos JSON** ✗
- **Almacenamiento:** Solo en memoria (lista de diccionarios)
- **Duración:** Los datos se pierden al cerrar el programa

```python
citas = []  # Lista global
proximo_id = 1  # Contador para IDs
```

---

## 📁 Estructura del Proyecto

```
evaluacion-taller-mecanico-arquitecturas/
├── main.py              # Archivo único con TODO el código
├── README.md            # Este archivo
└── .gitignore           # Ignorados de Git
```

**Nota:** Intencionalmente NO hay carpetas ni módulos separados (característica del spaghetti code).

---

## 🚀 Cómo Ejecutar el Programa

### Requisitos

- Python 3.7 o superior

### Pasos

1. **Navega a la carpeta del proyecto:**
   ```bash
   cd evaluacion-taller-mecanico-arquitecturas
   ```

2. **Ejecuta el programa:**
   ```bash
   python main.py
   ```

3. **Sigue las instrucciones del menú interactivo**

---

## 📝 Ejemplo de Uso

```
✨ Bienvenido al Sistema de Citas del Taller Mecánico ✨

========================================
 SISTEMA DE CITAS - TALLER MECÁNICO
========================================

1. Crear cita
2. Ver todas las citas
3. Buscar cita por ID
4. Cancelar cita
5. Marcar cita como atendida
6. Salir

Seleccione una opción: 1

--- CREAR NUEVA CITA ---
Nombre del cliente: Juan Pérez
Placa del vehículo: PBA-1234
Servicio solicitado: Cambio de aceite
Fecha de la cita (YYYY-MM-DD): 2026-06-05
Hora de la cita (HH:MM): 10:00
✅ Cita creada exitosamente con ID: 1

========================================
 SISTEMA DE CITAS - TALLER MECÁNICO
========================================

1. Crear cita
2. Ver todas las citas
3. Buscar cita por ID
4. Cancelar cita
5. Marcar cita como atendida
6. Salir

Seleccione una opción: 2

--- TODAS LAS CITAS ---

----------------------------------------
ID: 1
Cliente: Juan Pérez
Placa: PBA-1234
Servicio: Cambio de aceite
Fecha: 2026-06-05
Hora: 10:00
Estado: PENDIENTE
----------------------------------------

========================================
 SISTEMA DE CITAS - TALLER MECÁNICO
========================================

1. Crear cita
2. Ver todas las citas
3. Buscar cita por ID
4. Cancelar cita
5. Marcar cita como atendida
6. Salir

Seleccione una opción: 6

========================================
Gracias por usar el sistema de citas
del taller mecánico.
========================================
```

---

## ✅ Reglas de Negocio Implementadas

1. **Creación de citas**
   - ID es autoincremental
   - Todas las citas comienzan en estado `PENDIENTE`
   - No se permiten dos citas activas en la misma fecha y hora
   - Todos los campos son obligatorios

2. **Búsqueda y visualización**
   - Se puede buscar cita por ID
   - Se pueden ver todas las citas
   - Se mostrará "No existen citas registradas" si la lista está vacía

3. **Cancelación de citas**
   - Solo se pueden cancelar citas en estado `PENDIENTE`
   - No se puede cancelar una cita `ATENDIDA`
   - Si una cita ya está `CANCELADA`, se muestra mensaje informativo

4. **Atención de citas**
   - Solo se pueden marcar como `ATENDIDA` citas en estado `PENDIENTE`
   - No se puede atender una cita `CANCELADA`
   - Si una cita ya está `ATENDIDA`, se muestra mensaje informativo

---

## ⚖️ Ventajas y Desventajas

### Ventajas de esta versión

✅ **Simple** – Fácil de entender a primera vista  
✅ **Rápido de desarrollar** – Todo en un archivo  
✅ **Funciona** – Cumple con los requisitos  
✅ **Sin dependencias externas** – Solo Python puro  
✅ **Sirve para enseñanza** – Muestra qué NO hacer  

### Desventajas de esta versión

❌ **Difícil de mantener** – Cambios afectan múltiples lugares  
❌ **Difícil de testear** – Funciones con múltiples responsabilidades  
❌ **Difícil de extender** – Añadir nuevas funcionalidades requiere modificar código existente  
❌ **Código repetido** – Lógica de búsqueda aparece varias veces  
❌ **Mala separación de responsabilidades** – Todo mezclado  
❌ **No reutilizable** – Código específico del menú  
❌ **Variables globales** – Difícil de rastrear cambios  
❌ **Escalabilidad** – No puede crecer sin volverse inmantenible  

---

## 📚 Comparación con otras ramas

Este proyecto tiene **tres ramas** con diferentes arquitecturas del **mismo sistema**:

### 1. **`codigo-espagueti`** (rama actual)
- ❌ Todo en un archivo
- ❌ Sin estructura
- ✅ Funciona correctamente
- 📊 **Conclusión:** Fácil de hacer, difícil de mantener

### 2. **`monolitico-capas`** (rama futura)
- ✅ Separación en capas
- ✅ Models, Services, Repositories
- ✅ Mejor estructura
- 📊 **Conclusión:** Mejor organización, intermedio en complejidad

### 3. **`enfoque-ddd`** (rama futura)
- ✅ Domain-Driven Design
- ✅ Agregados, Value Objects, Repositories
- ✅ Muy bien estructurado
- 📊 **Conclusión:** Máxima flexibilidad, más complejo

---

## 🎓 Conclusión Académica

La rama `codigo-espagueti` **demuestra por qué la arquitectura es importante:**

- Aunque el código es **funcional**, es **inmantenible**
- La falta de **estructura** genera **problemas** a medida que crece
- En **equipos grandes**, esto sería un **desastre**
- Las siguientes ramas mostrarán cómo **mejorar** con arquitectura

**Lección clave:** *"La mala arquitectura es cara a largo plazo."*

---

## 📞 Contacto

Proyecto académico - Evaluación Sumativa  
Asignatura: Arquitectura de Software  
Fecha: 2026-06-04

---

**Recuerda:** Este código es un **anti-patrón intencional**. No lo uses en proyectos reales. 🚫