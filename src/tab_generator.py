# Mapping of notes to common guitar fret positions
fretboard = {
    "E": [0, 5, 10],
    "A": [0, 5, 10],
    "D": [0, 5, 10],
    "G": [0, 5, 9],
    "B": [0, 5, 8],
    "E_high": [0, 5, 12]
}

def generate_tabs(notes, timestamps):
    """Generate a guitar tab from detected notes and timestamps."""
    tab_lines = {string: ["-"] * len(notes) for string in ["E", "A", "D", "G", "B", "E_high"]}

    for i, note in enumerate(notes):
        note_letter = note[:-1]  # Extract pitch letter (e.g., "A", "G", etc.)
        if note_letter in fretboard:
            fret = fretboard[note_letter][0]  # Pick first available position
            tab_lines["E"][i] = str(fret) if "E" in note else "-"
            tab_lines["A"][i] = str(fret) if "A" in note else "-"
            tab_lines["D"][i] = str(fret) if "D" in note else "-"
            tab_lines["G"][i] = str(fret) if "G" in note else "-"
            tab_lines["B"][i] = str(fret) if "B" in note else "-"
            tab_lines["E_high"][i] = str(fret) if "E_high" in note else "-"

    return tab_lines
