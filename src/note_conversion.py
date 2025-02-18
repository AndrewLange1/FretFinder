import librosa

def freq_to_note(frequencies):
    """Convert frequency values to musical note names."""
    return [librosa.hz_to_note(freq) for freq in frequencies]
