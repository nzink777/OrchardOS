"""
OrchardOS: 18.08 Hz Resonance Monitor
Purpose: Real-time FFT analysis to detect planetary heartbeat harmonics.
"""

import numpy as np
import scipy.fft
import sounddevice as sd

# Configuration
FS = 44100  # Sampling frequency
DURATION = 2  # Analysis window in seconds
TARGET_FREQ = 18.08  # The Master Heartbeat

def monitor_resonance():
    print(f"Monitoring Orchard frequency at {TARGET_FREQ} Hz...")
    
    while True:
        # Capture raw signal
        audio_data = sd.rec(int(DURATION * FS), samplerate=FS, channels=1, dtype='float32')
        sd.wait()
        
        # Perform FFT
        fft_data = np.abs(scipy.fft.fft(audio_data.flatten()))
        freqs = scipy.fft.fftfreq(len(fft_data), 1/FS)
        
        # Filter for the target range (17 Hz - 19 Hz)
        idx = np.where((freqs >= 17) & (freqs <= 19))
        peak_freq = freqs[idx][np.argmax(fft_data[idx])]
        
        print(f"Detected Peak: {peak_freq:.2f} Hz")

if __name__ == "__main__":
    try:
        monitor_resonance()
    except KeyboardInterrupt:
        print("\nMonitoring stopped by Gardener.")
      
