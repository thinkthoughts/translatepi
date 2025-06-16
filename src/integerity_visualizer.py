# integerity_visualizer.py
# Visualizes Integerity Matrix resonance patterns and Pi-stage transitions

import json
import matplotlib.pyplot as plt
import numpy as np

def load_integerity_matrix(filepath="integerity_matrix.json"):
    """Load JSON matrix of Integerity data."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["integerity_matrix"]

def plot_resonance_heatmap(matrix):
    """Plot resonance distribution as a simple heatmap."""
    stages = [entry["pi_stage"] for entry in matrix]
    tokens = [entry["token"] for entry in matrix]
    types = [entry["type"] for entry in matrix]

    # Convert types to categorical index
    type_index = {typ: i for i, typ in enumerate(sorted(set(types)))}
    resonance_map = [type_index[entry["type"]] for entry in matrix]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow([resonance_map], cmap='plasma', aspect='auto')
    ax.set_yticks([])
    ax.set_xticks(range(len(tokens)))
    ax.set_xticklabels(tokens, rotation=45, ha='right')
    ax.set_title("Integerity Resonance Heatmap (by Type)")
    plt.tight_layout()
    plt.show()

def spiral_map(matrix):
    """Visualize Pi-stage resonance as a spiral transition."""
    theta = np.linspace(0, 4 * np.pi, len(matrix))
    radius = np.linspace(1, 10, len(matrix))

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
    ax.scatter(theta, radius, c=np.linspace(0, 1, len(matrix)), cmap='viridis', s=100)

    for i, entry in enumerate(matrix):
        ax.text(theta[i], radius[i], entry["token"], fontsize=8, ha='center', va='center')

    ax.set_title("Pi-Stage Spiral Transition Map")
    plt.show()

if __name__ == "__main__":
    matrix = load_integerity_matrix()
    plot_resonance_heatmap(matrix)
    spiral_map(matrix)
