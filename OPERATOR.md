# Operadores aritméticos y precedencia en Python

## Objetivo

Aprender a interpretar y resolver expresiones aritméticas en Python comprendiendo el orden en que se ejecutan los operadores.

---

# Operadores utilizados

| Operador | Descripción | Ejemplo |
|----------|-------------|----------|
| `+` | Suma | `5 + 3` |
| `-` | Resta | `8 - 2` |
| `*` | Multiplicación | `4 * 6` |
| `/` | División | `10 / 2` |
| `%` | Módulo (residuo) | `10 % 3` |
| `**` | Potencia | `2 ** 3` |
| `()` | Paréntesis | `(5 + 3) * 2` |

---

# Orden de precedencia

Python sigue el siguiente orden para resolver operaciones:

1. Paréntesis `()`
2. Potencias `**`
3. Multiplicación `*`, división `/` y módulo `%`
4. Suma `+` y resta `-`

Cuando existen operadores con la misma prioridad, se ejecutan de izquierda a derecha (excepto la potencia, que se evalúa de derecha a izquierda).

---

# Desarrollo de los ejercicios

## Ejercicio 1

```python
5 + 3 * 2
```

1. Multiplicación: `3 * 2 = 6`
2. Suma: `5 + 6 = 11`

**Resultado:** `11`

---

## Ejercicio 2

```python
8 / 2 + 4 * 3
```

1. División: `8 / 2 = 4`
2. Multiplicación: `4 * 3 = 12`
3. Suma: `4 + 12 = 16`

**Resultado:** `16.0`

---

## Ejercicio 3

```python
(7 + 3) * 2 - 5
```

1. Paréntesis: `7 + 3 = 10`
2. Multiplicación: `10 * 2 = 20`
3. Resta: `20 - 5 = 15`

**Resultado:** `15`

---

## Ejercicio 4

```python
10 - 4 + 2 * 3
```

1. Multiplicación: `2 * 3 = 6`
2. Operaciones restantes de izquierda a derecha:
   - `10 - 4 = 6`
   - `6 + 6 = 12`

**Resultado:** `12`

---

## Ejercicio 5

```python
(10 / 2) * (3 + 2) - 4
```

1. Paréntesis:
   - `10 / 2 = 5`
   - `3 + 2 = 5`
2. Multiplicación:
   - `5 * 5 = 25`
3. Resta:
   - `25 - 4 = 21`

**Resultado:** `21.0`

---

## Ejercicio 6

```python
2 + 3 * (4 - 1)
```

1. Paréntesis:
   - `4 - 1 = 3`
2. Multiplicación:
   - `3 * 3 = 9`
3. Suma:
   - `2 + 9 = 11`

**Resultado:** `11`

---

## Ejercicio 7

```python
5 * 2 ** 3
```

1. Potencia:
   - `2 ** 3 = 8`
2. Multiplicación:
   - `5 * 8 = 40`

**Resultado:** `40`

---

## Ejercicio 8

```python
6 + 4 / 2 ** 2
```

1. Potencia:
   - `2 ** 2 = 4`
2. División:
   - `4 / 4 = 1`
3. Suma:
   - `6 + 1 = 7`

**Resultado:** `7.0`

---

## Ejercicio 9

```python
10 % 3 + 2 * 5
```

1. Módulo:
   - `10 % 3 = 1`
2. Multiplicación:
   - `2 * 5 = 10`
3. Suma:
   - `1 + 10 = 11`

**Resultado:** `11`

---

## Ejercicio 10

```python
(8 + 2) * 3 ** 2
```

1. Paréntesis:
   - `8 + 2 = 10`
2. Potencia:
   - `3 ** 2 = 9`
3. Multiplicación:
   - `10 * 9 = 90`

**Resultado:** `90`

---

## Ejercicio 11

```python
7 + 2 * (3 + 5) / 4
```

1. Paréntesis:
   - `3 + 5 = 8`
2. Multiplicación:
   - `2 * 8 = 16`
3. División:
   - `16 / 4 = 4`
4. Suma:
   - `7 + 4 = 11`

**Resultado:** `11.0`

---

## Ejercicio 12

```python
2 ** 3 * 4 / 2
```

1. Potencia:
   - `2 ** 3 = 8`
2. Multiplicación:
   - `8 * 4 = 32`
3. División:
   - `32 / 2 = 16`

**Resultado:** `16.0`

---

## Ejercicio 13

```python
9 - 6 + 3 ** 2
```

1. Potencia:
   - `3 ** 2 = 9`
2. Operaciones restantes:
   - `9 - 6 = 3`
   - `3 + 9 = 12`

**Resultado:** `12`

---

## Ejercicio 14

```python
(7 - 2) * 5 + 3 ** 2
```

1. Paréntesis:
   - `7 - 2 = 5`
2. Potencia:
   - `3 ** 2 = 9`
3. Multiplicación:
   - `5 * 5 = 25`
4. Suma:
   - `25 + 9 = 34`

**Resultado:** `34`

---

## Ejercicio 15

```python
4 * 2 ** 3 / 8 + 1
```

1. Potencia:
   - `2 ** 3 = 8`
2. Multiplicación:
   - `4 * 8 = 32`
3. División:
   - `32 / 8 = 4`
4. Suma:
   - `4 + 1 = 5`

**Resultado:** `5.0`

---

# Conclusión

Estos ejercicios permiten comprender la importancia del orden de precedencia de los operadores en Python. Antes de ejecutar cualquier expresión es recomendable identificar primero los paréntesis, luego las potencias, después las multiplicaciones, divisiones y módulos, y finalmente las sumas y restas. Aplicar este procedimiento evita errores y facilita la comprensión del funcionamiento de las expresiones aritméticas.