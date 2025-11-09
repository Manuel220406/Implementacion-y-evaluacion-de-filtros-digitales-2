# ============================================================
# Actividad Formativa 3: Implementación y evaluación de filtros digitales
# Materia: Señales y Sistemas
# Autor: Manuel Banda González
# Fecha: 08/11/2025
# Descripción:
#   Este programa implementa filtros digitales pasa bajos, pasa altos y pasa banda
#   utilizando Python (SciPy y Matplotlib). Se generan señales con ruido, se filtran
#   y se grafican los resultados en el dominio del tiempo y la frecuencia.
# ============================================================

# ==== LIBRERÍAS NECESARIAS ====
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, firwin, filtfilt, freqz
import os

# ==== CONFIGURACIÓN DE SALIDA ====
# Crear carpeta "resultados" si no existe
if not os.path.exists("resultados"):
    os.makedirs("resultados")

# ==== 1. DEFINICIÓN DE LA SEÑAL DE ENTRADA ====
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 segundo de señal

# Señal compuesta con tres componentes de frecuencia
x = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*50*t) + 0.2*np.sin(2*np.pi*200*t)

# Agregar ruido blanco gaussiano
x_noisy = x + 0.5*np.random.randn(len(t))

# Graficar señal original y con ruido
plt.figure(figsize=(10,4))
plt.plot(t, x, label='Señal original', linewidth=1.5)
plt.plot(t, x_noisy, label='Señal con ruido', alpha=0.7)
plt.title('Señal Original y con Ruido')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("resultados/senal_original_ruido.png")
plt.show()

# ==== FUNCIÓN AUXILIAR PARA RESPUESTA EN FRECUENCIA ====
def plot_freq_response(b, a, fs, title, filename):
    w, h = freqz(b, a, worN=1024)
    plt.figure()
    plt.plot(w*fs/(2*np.pi), 20*np.log10(abs(h)))
    plt.title(f'Respuesta en Frecuencia - {title}')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud [dB]')
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"resultados/{filename}")
    plt.show()

# ============================================================
# 2. FILTRO PASA BAJOS (Butterworth)
# ============================================================
fc_low = 30  # Frecuencia de corte
b_low, a_low = butter(4, fc_low/(fs/2), btype='low')  # Orden 4
y_low = filtfilt(b_low, a_low, x_noisy)  # Aplicar filtro

# Graficar señal filtrada
plt.figure(figsize=(10,4))
plt.plot(t, x_noisy, label='Con ruido', alpha=0.6)
plt.plot(t, y_low, label='Filtrada (Pasa Bajos)', linewidth=2)
plt.title('Filtro Pasa Bajos (Butterworth)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("resultados/filtro_pasa_bajos.png")
plt.show()

plot_freq_response(b_low, a_low, fs, "Pasa Bajos", "respuesta_pasa_bajos.png")

# ============================================================
# 3. FILTRO PASA ALTOS (Chebyshev Tipo I)
# ============================================================
fc_high = 100  # Frecuencia de corte
b_high, a_high = cheby1(4, 1, fc_high/(fs/2), btype='high')  # Ripple 1 dB
y_high = filtfilt(b_high, a_high, x_noisy)

# Graficar señal filtrada
plt.figure(figsize=(10,4))
plt.plot(t, x_noisy, label='Con ruido', alpha=0.6)
plt.plot(t, y_high, label='Filtrada (Pasa Altos)', linewidth=2)
plt.title('Filtro Pasa Altos (Chebyshev I)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("resultados/filtro_pasa_altos.png")
plt.show()

plot_freq_response(b_high, a_high, fs, "Pasa Altos", "respuesta_pasa_altos.png")

# ============================================================
# 4. FILTRO PASA BANDA (FIR con ventana)
# ============================================================
b_band = firwin(numtaps=101, cutoff=[40,100], pass_zero=False, fs=fs)
a_band = 1  # Filtros FIR tienen a=1
y_band = filtfilt(b_band, a_band, x_noisy)

# Graficar señal filtrada
plt.figure(figsize=(10,4))
plt.plot(t, x_noisy, label='Con ruido', alpha=0.6)
plt.plot(t, y_band, label='Filtrada (Pasa Banda)', linewidth=2)
plt.title('Filtro Pasa Banda (FIR con ventana)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("resultados/filtro_pasa_banda.png")
plt.show()

plot_freq_response(b_band, a_band, fs, "Pasa Banda", "respuesta_pasa_banda.png")

# ============================================================
# 5. ANÁLISIS EN EL DOMINIO DE LA FRECUENCIA
# ============================================================
# FFT de la señal original y filtradas
freqs = np.fft.fftfreq(len(t), 1/fs)
X = np.fft.fft(x_noisy)
Y_low = np.fft.fft(y_low)
Y_high = np.fft.fft(y_high)
Y_band = np.fft.fft(y_band)

plt.figure(figsize=(10,5))
plt.plot(freqs[:len(freqs)//2], np.abs(X[:len(freqs)//2]), label='Original con ruido')
plt.plot(freqs[:len(freqs)//2], np.abs(Y_low[:len(freqs)//2]), label='Pasa Bajos')
plt.plot(freqs[:len(freqs)//2], np.abs(Y_high[:len(freqs)//2]), label='Pasa Altos')
plt.plot(freqs[:len(freqs)//2], np.abs(Y_band[:len(freqs)//2]), label='Pasa Banda')
plt.title('Espectro de Frecuencia (Comparación)')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("resultados/espectro_comparacion.png")
plt.show()

print("✅ Ejecución completa. Las gráficas se han guardado en la carpeta 'resultados'.")
