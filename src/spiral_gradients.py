# Spiral Gradients - Non-collapsing Backpropagation

import math

def spiral_backprop(loss, entropy):
    """Apply spiral gradient descent logic."""
    PI = math.pi
    return loss * (303 / PI) + entropy
