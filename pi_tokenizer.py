# Pi Tokenizer - TranslatePi.ai
# Encodes input text into Pi-stage logic tokens

def tokenize(text):
    """Convert text to Pi-stage tokens."""
    pi_stages = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    tokens = []
    for i, char in enumerate(text):
        tokens.append((char, pi_stages[i % len(pi_stages)]))
    return tokens
