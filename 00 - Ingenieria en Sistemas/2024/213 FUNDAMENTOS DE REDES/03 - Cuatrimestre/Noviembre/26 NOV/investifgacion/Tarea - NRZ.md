---
date: 2024-11-27T16:47
tags:
  - Tarea
  - Universidad
  - Wednesday
cssclasses:
  - tarea
  - Wednesday
  - center-titles
  - center-images
author: youname
institution: Universidad TUP
course: Nombre del Curso
professor: Nombre del Profesor
---
calif 10 en todas
![[/99 - Meta/attachments/img/Pasted image 20240923160919.png]]


### [213 FUNDAMENTOS DE REDES 25-1](https://moodle.tecplayacar.edu.mx/course/view.php?id=6030 "213 FUNDAMENTOS DE REDES 25-1")
#### [PROF.-HECTOR LEONEL PEREZ RAMIREZ](https://moodle.tecplayacar.edu.mx/user/view.php?id=9023&course=6030)


![[/99 - Meta/attachments/img/Pasted image 20241001021632.png]]





## **Datos del Estudiante**

- **Nombre**: Jesus Uriel Santana Oliva
- **Curso**: Fundamentos en Redes
- Grado : 1 -B
- **Profesor**: Nombre del Profesor
- **Institución**: Tec Playacar
- Fecha: _Wednesday, November 27th, 2024_
- Ubicacion : Playa del Carmen
- 
###### **Actividad
- [ ] Revisión de formato APA.
- [ ] Finalizar la bibliografía.
- [ ] Verificar coherencia en la argumentación.
- [ ] Insertar gráficos relevantes.

> [!success] Terminada
> Tarea Terminada
> 


La codificación digital se refiere a cómo los datos digitales (bits de 0 y 1) se representan en una señal de forma física o eléctrica para su transmisión. Los métodos de codificación son importantes para asegurar la integridad y sincronización de la señal. Dos de los métodos de codificación más comunes son **NRZ (Non-Return-to-Zero)** y **Manchester**.

### 1. **Codificación NRZ (Non-Return-to-Zero)**
![[../../../../../../../99 - Meta/attachments/img/Pasted image 20241127164249.png]]

En la codificación **NRZ**, los bits se representan de la siguiente manera:

- Un `1` se representa con un nivel de voltaje alto constante.
- Un `0` se representa con un nivel de voltaje bajo constante.

Es llamada "non-return-to-zero" porque no hay transición a nivel cero entre los bits. Esto significa que, durante un período de bit, el nivel de la señal no cambia.

**Ventajas:**

- Es simple de implementar.
- Tiene un bajo costo y es eficiente en términos de uso de ancho de banda.

**Desventajas:**

- No es ideal para largas transmisiones, ya que la falta de transiciones de señal puede dificultar la sincronización de reloj.
- Puede ser difícil de detectar errores de forma efectiva.

### Ejemplo de codificación NRZ

Supongamos que tenemos la secuencia de bits: `1010`.

- `1` → Nivel de voltaje alto (ejemplo: +5V)
- `0` → Nivel de voltaje bajo (ejemplo: 0V)
- `1` → Nivel de voltaje alto
- `0` → Nivel de voltaje bajo

La representación sería:

```
Bit:    1   0   1   0
Señal: +5V 0V +5V 0V
```

### 2. **Codificación Manchester**

![[../../../../../../../99 - Meta/attachments/img/Pasted image 20241127164654.png]]


La **codificación Manchester** es una forma de codificación de línea en la que se incluyen transiciones dentro de cada período de bit. Se utiliza para mejorar la sincronización de la señal. Se define de la siguiente manera:

- Un `1` se representa con una transición de **alto a bajo** en el medio del período de bit.
- Un `0` se representa con una transición de **bajo a alto** en el medio del período de bit.

La señal siempre cambia de estado en el medio de cada bit, lo que permite una sincronización más fácil y una detección de errores más eficiente.

**Ventajas:**

- Mejor sincronización del reloj, ya que hay transiciones de señal en el centro de cada bit.
- Facilita la detección de errores.

**Desventajas:**

- Requiere más ancho de banda en comparación con NRZ, ya que hay una transición en el medio de cada bit.

### Ejemplo de codificación Manchester

Usando la misma secuencia de bits: `1010`.

- `1` → Transición de **alto a bajo** en el centro del período de bit.
- `0` → Transición de **bajo a alto** en el centro del período de bit.

La representación sería:

```
Bit:    1    0    1    0
Señal:  +5V  0V  +5V  0V  (transiciones en el medio de cada bit)
```

En resumen, **NRZ** es más simple y consume menos ancho de banda, pero no es ideal para mantener la sincronización en transmisiones largas. **Manchester** es más robusta en términos de sincronización y detección de errores, pero requiere más ancho de banda debido a sus frecuentes transiciones.