# codec/binary_to_nucleotide/codec_translation_engine.py

import json
import os
from datetime import datetime

# Paths
CODEC_MAP_PATH = os.path.join(os.path.dirname(__file__), "codec_map.json")
LOG_PATH = os.path.join(os.path.dirname(__file__), "codec_translation.log")

# --- Load Codec Map ---
with open(CODEC_MAP_PATH, "r", encoding="utf-8") as f:
    _data = json.load(f)
    CODEC_MAP = _data.get("codec", {})

# --- Build Reverse Map ---
REVERSE_MAP = {v["symbol"]: k for k, v in CODEC_MAP.items()}


def log(message: str):
    """Append timestamped log messages (for CI & local testing)."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(entry + "\n")


def translate(binary_input: str) -> str:
    """
    Converts a binary string (e.g., '010110') into its corresponding
    nucleotide sequence (e.g., 'ATGC') using codec_map.json.
    Reads input in 2-bit pairs.
    """
    seq = []
    for i in range(0, len(binary_input), 2):
        pair = binary_input[i:i+2]
        symbol = CODEC_MAP.get(pair, {}).get("symbol", "?")
        seq.append(symbol)
    result = "".join(seq)
    log(f"Translated binary→nucleotide: {binary_input} → {result}")
    return result


def reverse_translate(nucleotide_sequence: str) -> str:
    """
    Converts a nucleotide sequence (e.g., 'ATGC') back into its binary equivalent.
    """
    bits = []
    for nt in nucleotide_sequence:
        bits.append(REVERSE_MAP.get(nt, "??"))
    result = "".join(bits)
    log(f"Reversed nucleotide→binary: {nucleotide_sequence} → {result}")
    return result


def codec_roundtrip(binary_input: str) -> bool:
    """
    Executes a full roundtrip (binary→nucleotide→binary) to verify symmetry.
    Returns True if perfectly reversible.
    """
    encoded = translate(binary_input)
    decoded = reverse_translate(encoded)
    success = binary_input == decoded
    status = "✅ Success" if success else "❌ Mismatch"
    log(f"Roundtrip: {binary_input} → {encoded} → {decoded} [{status}]")
    return success


if __name__ == "__main__":
    test_input = "00101111"
    encoded = translate(test_input)
    decoded = reverse_translate(encoded)
    print(f"Binary → Nucleotide: {encoded}")
    print(f"Nucleotide → Binary: {decoded}")
    print("Roundtrip valid:", codec_roundtrip(test_input))
