import matplotlib.pylab as plt
import numpy as np
import scipy
from scipy import signal
from pydub import AudioSegment

INPUT_PATH = 'characters/sayori.chr'
OUTPUT_PATH = 'decoded/sayori.png'

def main():
    sound = AudioSegment.from_file(INPUT_PATH)
    samples = np.array(sound.get_array_of_samples())
    frequencies, times, spectrogram = scipy.signal.spectrogram(samples, nperseg=2048)

    plt.pcolormesh(times, frequencies, spectrogram, cmap='binary')
    plt.savefig(OUTPUT_PATH)
    plt.show()

    print(OUTPUT_PATH)

if __name__ == "__main__":
    main()
