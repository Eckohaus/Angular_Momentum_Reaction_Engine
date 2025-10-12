# codec/binary_to_nucleotide/test_codec_map.py
import json
import os
from datetime import datetime

# === Path & Logging Setup ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "codec_validation.log")

os.makedirs(LOG_DIR, exist_ok=True)

def log(message):
    """Write message to both console and persistent log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")


# === Core I/O ===
def load_codec_map(path=None):
    """Load the JSON codec mapping."""
    if path is None:
        path = os.path.join(BASE_DIR, "codec_map.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# === Validation Routines ===
def validate_codec_structure(codec_map):
    """Ensure all required bit-pair mappings exist and are valid."""
    codec = codec_map.get("codec", {})
    required = ["00", "01", "10", "11"]
    assert all(pair in codec for pair in required), f"❌ Missing required mappings: {required}"
    for key, value in codec.items():
        assert "symbol" in value and len(value["symbol"]) == 1, f"❌ Invalid symbol entry for {key}"
    log("✅ Codec structure validated successfully.")


def translate(binary_str, codec_map):
    """Translate a binary string into nucleotide symbols."""
    codec = codec_map["codec"]
    return "".join(codec.get(binary_str[i:i+2], {"symbol": "?"})["symbol"] for i in range(0, len(binary_str), 2))


def reverse_translate(nucleotide_str, codec_map):
    """Translate a nucleotide sequence back to binary."""
    codec = codec_map["codec"]
    reverse = {v["symbol"]: k for k, v in codec.items()}
    return "".join(reverse.get(nuc, "??") for nuc in nucleotide_str)


def test_round_trip(codec_map):
    """Confirm binary → nucleotide → binary round-trip symmetry."""
    binary_input = "00101111"
    nucleotide_seq = translate(binary_input, codec_map)
    binary_output = reverse_translate(nucleotide_seq, codec_map)
    assert binary_input == binary_output, f"❌ Round-trip failed: {binary_input} → {nucleotide_seq} → {binary_output}"
    log(f"🔁 Round-trip successful: {binary_input} → {nucleotide_seq} → {binary_output}")


# === Entry Point ===
if __name__ == "__main__":
    codec_map = load_codec_map()
    validate_codec_structure(codec_map)
    test_round_trip(codec_map)
    log("🏁 Codec validation completed.\n")
