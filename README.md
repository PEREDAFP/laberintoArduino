# 🧭 Navegación en Laberinto con Python

Este proyecto resuelve laberintos representados en texto utilizando el algoritmo **BFS (Breadth-First Search)** y genera instrucciones en formato **JSON** para moverse desde una entrada `E` hasta una salida `S`.

La visualización incluye una representación gráfica del laberinto con el camino resuelto marcado con la letra `I` en color verde.

---

## 📦 Estructura del Laberinto

Cada laberinto es un archivo `.txt` con los siguientes caracteres:

- `X` = Muro (no transitable)
- ` ` (espacio) = Camino libre
- `E` = Entrada
- `S` = Salida

### Ejemplo:

X X X X X

X E X X

X X X X X

X X S X

X X X X X

---

## 🚀 ¿Qué hace este programa?

- Lee el laberinto desde un archivo `.txt`
- Encuentra el camino más corto de `E` a `S`
- Genera una serie de instrucciones en JSON:
  ```json
  {"accion": "avanza", "espacio": 3}
  {"accion": "derecha", "espacio": 0}
  ```

```
## 🚀 Puedes generar laberintos de prueba con

- generaLaberinto
- El programa solicitará el ancho y el alto y creará un fichero `laberinto_generado.txt` para pruebas


```

## 📚 **Librería `RobotMovimiento` - Descripción General**

### 🧠 **¿Qué hace esta librería?**

`RobotMovimiento` es una librería de Arduino diseñada para controlar un robot con **dos motores DC** conectados al **Adafruit Motor Shield v1**, usando la librería `AFMotor.h`.

Permite movimientos precisos en base a:

- Distancia a recorrer.
- RPM individual por motor.
- Radio de rueda.
- Distancia entre ruedas (ancho del robot).

---

## ✨ **Características principales**

- ✅ Movimiento hacia adelante con distancia, RPM y radio de rueda.
- ✅ Giro exacto de 90° a izquierda o derecha, usando distancia entre ruedas.
- ✅ Parámetros configurables para RPM independientes de cada motor.
- ✅ Función de paro inmediato.

---

## 🛠️ **Funciones disponibles**

```cpp
RobotMovimiento(uint8_t motorIzq, uint8_t motorDer, float distancia_ruedas_cm);
```

### Métodos:

```cpp
void adelante(float distancia_cm, int rpmIzq, int rpmDer, float radio_rueda_cm);
```

> Mueve el robot hacia adelante una distancia determinada.

```cpp
void izquierda(int rpmIzq, int rpmDer, float radio_rueda_cm);
void derecha(int rpmIzq, int rpmDer, float radio_rueda_cm);
```

> Gira el robot 90° a izquierda o derecha sobre su eje.

```cpp
void paro();
```

> Detiene ambos motores inmediatamente.

---

## 🚀 **Ejemplo de uso**

```cpp
#include <AFMotor.h>
#include <RobotMovimiento.h>

RobotMovimiento robot(1, 2, 12.0);  // Motores en M1 y M2, distancia entre ruedas: 12 cm

void setup() {
  robot.adelante(50, 60, 60, 3.0);   // Avanza 50 cm
  delay(1000);
  robot.izquierda(50, 50, 3.0);      // Gira 90° izquierda
  delay(1000);
  robot.derecha(50, 50, 3.0);        // Gira 90° derecha
  delay(1000);
  robot.paro();                      // Se detiene
}

void loop() {}
```

---

## 📦 **Cómo crear el archivo `.zip` en Linux**

1. Asegúrate de tener una carpeta con esta estructura:

```
RobotMovimiento/
├── RobotMovimiento.h
├── RobotMovimiento.cpp
```

2. Ejecuta este comando en el terminal (ubicado donde esté la carpeta):

```bash
zip -r RobotMovimiento.zip RobotMovimiento/
```

Esto generará un archivo llamado `RobotMovimiento.zip`.

---

## 🔧 **Cómo instalar la librería en el IDE de Arduino**

1. Abre el **IDE de Arduino**.
2. Ve a **Sketch > Include Library > Add .ZIP Library...**
3. Selecciona el archivo `RobotMovimiento.zip` que creaste.
4. ¡Listo! Ahora puedes incluirla en tus programas:

```cpp
#include <RobotMovimiento.h>
```

---

## 📌 Requisitos

- Arduino Uno R3 (u otro compatible con AFMotor).
- Adafruit Motor Shield v1.
- Librería **AFMotor** instalada en el IDE (usa el Gestor de Bibliotecas).

---
