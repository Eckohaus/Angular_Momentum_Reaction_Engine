import json
import os

# Load codec map
CODEC_MAP_PATH = os.path.join(os.path.dirname(__file__), "codec_map.json")

with open(CODEC_MAP_PATH, "r", encoding="utf-8") as f:
    CODEC_MAP = json.load(f)

# Invert mapping for reverse translation
REVERSE_MAP = {v: k for k, v in CODEC_MAP.items()}


def translate(binary_input: str) -> str:
    """
    Converts a binary string (e.g., '0101') into its corresponding
    nucleotide sequence (e.g., 'ATCG') based on codec_map.json.
    """
    return "".join(CODEC_MAP.get(bit, "?") for bit in binary_input)


def reverse_translate(nucleotide_sequence: str) -> str:
    """
    Converts a nucleotide sequence (e.g., 'ATCG') back into binary form.
    """
    return "".join(REVERSE_MAP.get(nt, "?") for nt in nucleotide_sequence)


def codec_roundtrip(binary_input: str) -> bool:
    """
    Runs a validation loop to confirm translation coherence.
    """
    return binary_input == reverse_translate(translate(binary_input))


if __name__ == "__main__":
    test_input = "010110"
    encoded = translate(test_input)
    decoded = reverse_translate(encoded)
    print(f"Binary → Nucleotide: {encoded}")
    print(f"Nucleotide → Binary: {decoded}")
    print("✅ Roundtrip success:", codec_roundtrip(test_input))
