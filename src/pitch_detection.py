import aubio
import numpy as np

def detect_notes(y, sr):
    """Detects pitch (frequencies) from an audio signal."""
    win_s = 1024
    hop_s = 512

    pitch_o = aubio.pitch("yin", win_s, hop_s, sr)
    pitch_o.set_unit("Hz")

    pitches = []
    timestamps = []

    for i in range(0, len(y), hop_s):
        pitch = pitch_o(y[i:i+hop_s])[0]
        if pitch > 0:  # Ignore silence
            pitches.append(pitch)
            timestamps.append(i / sr)

    return pitches, timestamps
