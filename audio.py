from scipy.io import wavfile
import numpy as np
fs, a = wavfile.read('./audio.wav')
fs1, b = wavfile.read('./audio3.wav')

n = min(len(a), len(b))
out_idx = np.flatnonzero(a[:n] == b[:n])
x= out_idx.size

total_elements = np.multiply(*a.shape)
percentage = x/total_elements
print('{:.5f}% Match'.format(percentage*100))