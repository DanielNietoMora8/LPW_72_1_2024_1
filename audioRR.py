import librosa
import numpy as np
import librosa.display
import matplotlib.pyplot as plt
import time

def set_default(figsize=(10,10), dpi=100):
    plt.style.use(['dark_background', 'bmh'])
    plt.rc('axes', facecolor='k')
    plt.rc('figure', facecolor='k')
    plt.rc('figure', figsize=figsize, dpi=dpi)

set_default(figsize=(16,8))

audio='/Users/Usuario/Downloads/prueba.mp3'
y,sampling_rate=librosa.load(audio)
sampling_rate

T=y.size/sampling_rate
dt=1/sampling_rate
t=np.r_[0:T:dt]

print(
    f'y[t] tiene {y.size} muestras',
    f'La frecuencia de muestreo es {sampling_rate*1e-3}KHz',
    f'y(t) tiene {T:.1f}s',
    sep='\n')
#mostramos la grafica de la cancion
plt.plot(t, y);
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud[/]')
plt.title(r'$y(t)$', size=20)
plt.figure()
#muentra la imagen del tratamiento del audio
plt.show()

X = librosa.stft(y)
X_dB = librosa.amplitude_to_db(np.abs(X))
X = librosa.stft(y)

from librosa.display import specshow
#Esta linea cargamos la funcion specshow con las variables de interes, la amplitud en decibeles X_db y la frecuencia demuestreo
specshow(X_dB, sr=sampling_rate, x_axis='time', y_axis='hz')

plt.xlabel('tiempo [s]')
plt.ylabel('frecuencia [Hz]')
plt.ylim(top=12000)
plt.colorbar()
plt.grid(True)
plt.figure()
plt.show()

