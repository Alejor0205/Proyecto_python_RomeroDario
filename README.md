# Lotería Virtual

# **Descripción del Proyecto**

Este proyecto consiste en la creación de un programa que simula una lotería, permitiendo a los usuarios comprar boletos con combinaciones de números y participar en sorteos virtuales. El programa genera números ganadores aleatorios, compara las combinaciones de los boletos con los números ganadores, y determina si algún boleto es ganador. Los usuarios pueden recibir diferentes premios en función del número de aciertos obtenidos. La simulación tiene funcionalidades adicionales como la compra de múltiples boletos, la automatización de simulaciones, el registro histórico de los juegos, y la visualización de estadísticas de los resultados.



## **Problema**

La mayoría de las loterías reales implican costos, tiempos de espera para los sorteos y una falta de retroalimentación instantánea para el jugador. Además, no siempre se tiene la oportunidad de experimentar con distintas estrategias o jugar múltiples veces sin gastar dinero real. Este proyecto busca abordar estos problemas proporcionando una forma divertida, educativa y sin costo de experimentar la emoción de una lotería. El programa no solo permite participar en sorteos simulados, sino también analizar la probabilidad de ganar y entender mejor cómo funcionan los sistemas de lotería. Además, al incluir un historial de juegos y opciones de simulación automatizada, los usuarios pueden evaluar patrones y tendencias en los resultados para mejorar sus decisiones en futuros sorteos.



## **Funcionalidades Básicas**

1. **Compra de Boleto:**

   - El usuario elige una cantidad de números (por ejemplo, 6 números) dentro de un rango (por ejemplo, del 1 al 49).

   - El programa debe validar que los números sean únicos y estén dentro del rango permitido.

2. **Generación de Números Ganadores:**

   - El programa genera una combinación aleatoria de números ganadores (por ejemplo, 6 números del 1 al 49).

   - Los números ganadores deben ser únicos.

3. **Comparación de Resultados:**

   - El programa compara los números del boleto con los números ganadores y determina cuántos números coinciden.

   - Puede mostrar un mensaje con el resultado, indicando cuántos aciertos tuvo el usuario.

4. **Premios:**
   - Puedes definir diferentes premios según el número de aciertos (por ejemplo, 3 aciertos = premio pequeño, 4 aciertos = premio mediano, 5 aciertos = premio grande, y 6 aciertos = premio mayor).

## **Funcionalidades Adicionales (Requerido)**

1. **Múltiples Boletos:**
   - Permite al usuario comprar varios boletos para la misma lotería y muestra los resultados de cada uno.

2. **Historial de Juegos:**
   - Guarda los resultados de las loterías anteriores en un archivo de texto o CSV para que el usuario pueda ver su historial de juego.

3. **Automatización de Juegos:**
   - Permite que el usuario elija un número de veces para jugar automáticamente (por ejemplo, simular 100 loterías) y muestra estadísticas sobre la frecuencia de aciertos.

4. **Visualización de Resultados:**
   - Utiliza gráficos para mostrar cuántas veces se acierta un número específico en varias simulaciones, o para representar la probabilidad de ganar un premio.



# Tecnologías y Herramientas

- Recurso: https://drive.google.com/drive/folders/1ynoY28Ol34YditVw9CAqjZCTAUJlNlPS?usp=sharing
- GitHub: Para la gestión de versiones del código y colaboración en el desarrollo.
- Bibliotecas sugeridas:
- `random`: Para generar números aleatorios. https://www.w3schools.com/python/module_random.asp
- `json`: Para guardar y cargar archivos de historial.
- `tabulate`: Para visualizar datos si decides agregar gráficos. https://pypi.org/project/tabulate/

﻿﻿

# Pasos básicos para implementar

1. Generar la combinación de números del boleto del usuario: Permite al usuario seleccionar los números manualmente o genera un boleto automático con números aleatorios.
2. Generar los números ganadores: Usa `random.sample()` para obtener una lista de números únicos dentro del rango especificado.
3. Comparar los números del boleto con los números ganadores: Cuenta los aciertos y determina el premio si lo hay.
4. Mostrar los resultados al usuario: Informa sobre los números ganadores, los números del boleto y cuántos coincidieron.

# Resultado esperado

La entrega de este proyecto se realizará grupos de 2 personas (Si el Trainer lo desea lo hará de manera individual), donde se debe anexar un enlace a un repositorio en GitHub privado llamado “Proyecto_Python_ApellidoNombre” (Proyecto_Python_Apellido1Nombre1Apellido2Nombre2 donde aplique) que contenga el código de la aplicación construida en Python. En este mismo repositorio, debe contener los siguientes archivos:

- Archivo principal de ejecución en Python.
- Archivos modularizados que den funcionalidad al programa principal de Python.
- Archivo JSON que almacene la información del programa en sí. 