# 🌡️ Conversión de Celsius a Fahrenheit con TensorFlow

Este proyecto utiliza TensorFlow para crear y entrenar una red neuronal que predice temperaturas en grados Fahrenheit a partir de grados Celsius.

## 📁 Estructura del Proyecto

- 🔎 **Definición de Datos:**
  - Datos de entrada: Temperaturas en grados Celsius.
```python3
celcius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
```

  - Datos de salida: Temperaturas en grados Fahrenheit.
```python3
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)
```
---

# 🤖 **Modelo de Red Neuronal:**
🧠 Consiste en una capa **densa**, es decir, que se conecta con todas las neuronas posibles y la iniciamos con una neurona (units=1).
<p align="center">
  <img src="https://github.com/user-attachments/assets/8b15d513-c4c0-44b7-b24d-8e1ec1f06fc1" alt="image" heig="350" width="350">
</p>

```python
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
```
  - 🧮 La función de pérdida utilizada es el Error Cuadrático Medio (`mean_squared_error`).
  - 🌐 El optimizador utilizado es Adam con una tasa de aprendizaje de 0.1
```python3
optimizer = tf.keras.optimizers.Adam(0.1),
```
---

# 📈 **Entrenamiento:**
  - El modelo se entrena durante 1000 épocas. (epochs=1000)
```python3
historial = modelo.fit(celcius, fahrenheit, epochs=1000, verbose=False)
```
  - 📖 Se registra el historial de pérdida para su visualización.

# **Evaluación:**
  - 📈 Se genera una gráfica que muestra cómo disminuye el error a lo largo del entrenamiento.
<p align="center">
  <img src="https://github.com/user-attachments/assets/db9135e5-1a04-43ee-ba62-bc152a6a0fc8" alt="image" heig="350" width="350">
</p>

```python3
import matplotlib.pyplot as plt
plt.xlabel('# Epoca')
plt.ylabel('Magnitud de perdida')
plt.plot(historial.history["loss"])
```
---

# 🧭 **Predicción:**
  - El modelo predice una temperatura en Fahrenheit a partir de un valor en Celsius ingresado por el usuario.
<p align="center">
  <img src="https://github.com/user-attachments/assets/2f97225e-bb76-4202-95f4-ce6ecd1edf36" alt="image" heig="350" width="350">
</p>

```python3
resultado = modelo.predict(np.array([dato]))
```

[![GitHub Issues](https://img.shields.io/github/issues/username/repo.svg)](https://github.com/74lg0/machine-learning/issues)
[![GitHub Forks](https://img.shields.io/github/forks/username/repo.svg)](https://github.com/74lg0/machine-learning/network)
[![GitHub Stars](https://img.shields.io/github/stars/username/repo.svg)](https://github.com/74lg0/machine-learning/stargazers)


