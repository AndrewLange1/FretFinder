def print_tab(tab_lines):
    """Formats and prints guitar tabs in a readable way."""
    print("\nGenerated Guitar Tab:\n")
    for string in ["E", "B", "G", "D", "A", "E_high"]:
        print(f"{string}|", "—".join(tab_lines[string]), "|")
    print("\n")
