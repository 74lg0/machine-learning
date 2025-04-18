# -*- coding: utf-8 -*-
"""firts_ia.ipynb

Automatically generated by Colab.

"""

# Importación de las bibliotecas necesarias 
import tensorflow as tf
import numpy as np

# Definimos los datos y las salidas esperadas
celcius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Añadimos la primera "neurona" al modelo
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

# Añadimos un optimizador y la función de pérdida para ajustar los pesos y sesgos
modelo.compile(
    # Tasa de aprendizaje en (0.1)
    optimizer = tf.keras.optimizers.Adam(0.1),

    # Función de pérdida (Error cuadrático medio)
    loss = 'mean_squared_error'
)

# Entrenamiento del modelo, epochs=1000 (Mil vueltas, para entrenar el modelo)
historial = modelo.fit(celcius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado")

# Qué tan mal están los resultados de la red en cada vuelta
import matplotlib.pyplot as plt
plt.xlabel('# Época')
plt.ylabel('Magnitud de pérdida')
plt.plot(historial.history["loss"])

# Fórmula para calcular los grados Fahrenheit
def celcius_a_fahrenheit(c):
  f = c * 1.8 + 32
  return f

# Ejemplo de predicción
print("Hagamos una predicción...")
dato = float(input("Ingresa un grado Celsius: "))
resultado = modelo.predict(np.array([dato]))
print(f'Resultado de la IA: {resultado}\nResultado real: {celcius_a_fahrenheit(dato)}')
