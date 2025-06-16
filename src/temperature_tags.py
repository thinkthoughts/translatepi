# Thermodynamic Token Tagger

def temperature_tag(token):
    """Assign thermodynamic tag to a token."""
    mapping = {
        "stop": "plasma",
        "pause": "liquid",
        "resist": "solid",
    }
    return mapping.get(token.lower(), "unknown")
