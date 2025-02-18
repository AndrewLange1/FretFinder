import librosa

'''File_path imports file, sr = sample rate which is sound quality, higher is better but uses more memory'''
def load_audio(file_path, sr="44100"):
    '''y is an array of the wave form values (audio samples), sr is the sample rate used'''
    y, sr = librosa.load(file_path, sr=sr)
    return y, sr
