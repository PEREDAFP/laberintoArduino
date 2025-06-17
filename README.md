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

## 🚀 La versión 2

- El motivo de haber creado un retardo es por la necesidad del envío del json a un arduino vía bluetooth
- Al programa se le pasará el laberinto y enviará, con el retardo oportuno, las líneas json para que Arduino pueda resolver el laberinto sin ningún tipo de senson
- Se utilizarán el shield AF_MOTOR.h y la librería json de Arduino
```
