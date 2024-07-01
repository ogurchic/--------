import librosa
import numpy as np
import pipes as pipe
# Загрузите ваш аудиофайл
audio, sample_rate = librosa.load('example.wav', sr=None)

# Преобразуйте аудиофайл в подходящий формат
audio = audio.astype(np.float32)

# Теперь вы можете передать аудио в pipe
result = pipe(audio)
print(result["text"])

