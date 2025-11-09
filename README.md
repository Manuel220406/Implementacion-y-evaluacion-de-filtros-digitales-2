Implementación y Evaluación de Filtros Digitales

Autor: Manuel Banda González
Materia: Señales y Sistemas
Fecha: 09/11/2025

#Objetivo
Diseñar, implementar y evaluar filtros digitales pasa bajos, pasa altos y pasa banda utilizando Python y las librerías SciPy y Matplotlib.
El propósito es analizar el comportamiento de señales con ruido antes y después del filtrado, observando los efectos de cada tipo de filtro en el dominio del tiempo y la frecuencia.
Conceptos clave

#Filtros digitales FIR (Finite Impulse Response) y IIR (Infinite Impulse Response).
*Tipos de filtros:
  Pasa bajos (Butterworth)
  Pasa altos (Chebyshev tipo I)
  Pasa banda (FIR con ventana)
*Respuesta en frecuencia
*Filtrado de señales con ruido blanco
*Transformada rápida de Fourier (FFT)

#Requerimientos
Asegúrar de tener instaladas las siguientes librerías antes de ejecutar el código:
  pip install numpy scipy matplotlib

#Desarrollo del proyecto
1. Generación de la señal de entrada
Se genera una señal compuesta por tres componentes sinusoidales de 5 Hz, 50 Hz y 200 Hz, además de agregarse ruido blanco gaussiano para simular una señal contaminada.

2. Diseño e implementación de filtros
Se diseñaron tres filtros digitales utilizando SciPy:
| Tipo de Filtro | Método        | Frecuencia(s) de corte | Orden     | Observaciones                       |
| -------------- | ------------- | ---------------------- | --------- | ----------------------------------- |
| Pasa Bajos     | Butterworth   | 30 Hz                  | 4         | Atenúa frecuencias superiores       |
| Pasa Altos     | Chebyshev I   | 100 Hz                 | 4         | Ripple de 1 dB en banda de paso     |
| Pasa Banda     | FIR (ventana) | 40–100 Hz              | 101 coef. | Permite paso de un rango intermedio |

3. Aplicación de los filtros
Cada filtro se aplica a la señal ruidosa usando el método filtfilt() (filtrado en avance y retroceso), evitando desfases en la señal filtrada.

4. Visualización
Se generan y guardan gráficas en la carpeta resultados/ para analizar:
*Señal original vs. con ruido
*Señales filtradas (por tipo de filtro)
*Respuesta en frecuencia de cada filtro
*Comparación del espectro (FFT) entre todas las señales

#Resultados obtenidos
| Tipo de filtro               | Efecto observado                                                         |
| ---------------------------- | ------------------------------------------------------------------------ |
| **Pasa bajos (Butterworth)** | Suaviza la señal, eliminando las componentes de alta frecuencia y ruido. |
| **Pasa altos (Chebyshev I)** | Resalta las frecuencias altas, suprimiendo las bajas.                    |
| **Pasa banda (FIR)**         | Conserva solo el rango de 40–100 Hz, eliminando el resto.                |

1.Gráficas generadas:
  *senal_original_ruido.png
  *filtro_pasa_bajos.png
  *filtro_pasa_altos.png
  *filtro_pasa_banda.png
  *espectro_comparacion.png
  *respuesta_pasa_bajos.png, respuesta_pasa_altos.png, respuesta_pasa_banda.png

#Análisis
  *El filtro Butterworth mostró una respuesta en frecuencia suave y estable, ideal para eliminar ruido de alta frecuencia.
  *El Chebyshev tipo I tuvo una transición más abrupta, aunque con ligera ondulación en la banda de paso.
  *El filtro FIR con ventana demostró gran estabilidad y fase lineal, conservando adecuadamente el rango de frecuencias deseado.
  *El análisis de FFT confirmó que cada filtro atenúa o deja pasar las frecuencias esperadas, cumpliendo con su propósito teórico.

#Conclusiones
  *Los filtros digitales son herramientas esenciales para el procesamiento de señales ruidosas.
  *Cada tipo de filtro ofrece ventajas distintas: estabilidad (Butterworth), selectividad (Chebyshev) y control de banda (FIR).
  *Python, mediante SciPy, permite una implementación flexible y precisa para el diseño y evaluación de filtros.
  *La comparación visual entre los resultados demuestra cómo el filtrado digital mejora significativamente la calidad de las señales.

#Estructura del repositorio
Implementacion-y-evaluacion-de-filtros-digitales-2/
│
├── resultados/
│   ├── senal_original_ruido.png
│   ├── filtro_pasa_bajos.png
│   ├── filtro_pasa_altos.png
│   ├── filtro_pasa_banda.png
│   ├── respuesta_pasa_bajos.png
│   ├── respuesta_pasa_altos.png
│   ├── respuesta_pasa_banda.png
│   └── espectro_comparacion.png
│
├── filtros_digitales.py
└── README.md
