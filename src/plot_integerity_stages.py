import json
import matplotlib.pyplot as plt

# Load JSON matrix
with open("integerity_matrix.json", "r") as f:
    data = json.load(f)

tokens = [entry["token"] for entry in data["integerity_matrix"]]
pi_stages = list(range(1, len(tokens) + 1))  # just label 1, 2, 3...

# Simple visual plot
plt.figure(figsize=(10, 6))
plt.barh(pi_stages, range(len(tokens)), tick_label=tokens, color="skyblue")
plt.xlabel("Token Index")
plt.title("Integerity Matrix — Pi-stage Token Visual")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
