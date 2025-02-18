from audio_processing import load_audio
from pitch_detection import detect_notes
from note_conversion import freq_to_note
from tab_generator import generate_tabs
from display import print_tab

# Load audio
audio_path = "recordings/example_riff.wav"
y, sr = load_audio(audio_path)

# Detect notes
frequencies, timestamps = detect_notes(y, sr)

# Convert frequencies to notes
notes = freq_to_note(frequencies)

# Generate tab
guitar_tab = generate_tabs(notes, timestamps)

# Display tab
print_tab(guitar_tab)
