# triplet_generator.py
# TranslatePi.ai — Identity Equation Utility

def triplet_n(spiral_n):
    """Generate Triplet N from Spiral N using the non-recursive refinement formula."""
    return (spiral_n * 24) - 25

def spiral_n_from_triplet(triplet_n):
    """Reverse map Triplet N to Spiral N."""
    return (triplet_n + 25) // 24

def label_triplet(triplet_n):
    """Label known resonant triplets with translation context."""
    labels = {
        9423: {
            "pi_stage": "9423Pi",
            "translation": "Water Resistance Now",
            "resonance": "unilateral hydrogen coordination"
        },
        9424: {
            "pi_stage": "9424Pi",
            "translation": "False-Zero Origin Supervision",
            "resonance": "entropy injection (collapse risk)"
        },
        9425: {
            "pi_stage": "9425Pi",
            "translation": "Bilateral Balance (Feminist Gravity)",
            "resonance": "nonviolent spiral symmetry"
        },
        9426: {
            "pi_stage": "9426Pi",
            "translation": "Breath Symmetry",
            "resonance": "continual expansion (non-collapse memory)"
        }
    }
    return labels.get(triplet_n, {
        "pi_stage": "unknown",
        "translation": "undocumented triplet",
        "resonance": "unlabeled spiral"
    })

def is_valid_triplet(triplet_n):
    """Basic collapse-resistant sanity check."""
    return triplet_n > 0 and triplet_n != -1 and triplet_n != 1 - 1


