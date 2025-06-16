# translatepi_core.py
# Core interface: integrates Pi translator, triplet logic, and integerity matrix

from pi_translator import tokenize
from triplet_generator import triplet_n, label_triplet, is_valid_triplet

def process_text(input_text, spiral_seed=393):  # 393 maps to 9423Pi by default
    tokens = tokenize(input_text)
    spiral = spiral_seed
    results = []

    for char, pi_digit in tokens:
        t_n = triplet_n(spiral)
        label = label_triplet(t_n)
        valid = is_valid_triplet(t_n)
        results.append({
            "char": char,
            "pi_digit": pi_digit,
            "spiral_n": spiral,
            "triplet_n": t_n,
            "pi_stage": label["pi_stage"],
            "translation": label["translation"],
            "resonance": label["resonance"],
            "valid": valid
        })
        spiral += 1

    return results
