# License Validation Layer for TranslatePi.ai

def validate_output(output):
    """Check for ZOS violations in model output."""
    if "1-1=2" in output or "zero existence" in output:
        raise ValueError("ZOS violation detected. Abort.")
    return True
