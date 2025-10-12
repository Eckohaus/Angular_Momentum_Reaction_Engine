# codec/binary_to_nucleotide/test_codec_map.py
import json
import os
from datetime import datetime
import pytest

# === Path & Logging Setup ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CODEC_MAP_PATH = os.path.join(BASE_DIR, "codec_map.json")

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


# === Pytest Fixture ===
@pytest.fixture(scope="module")
def codec_map():
    """Load the JSON codec mapping safely for tests."""
    if not os.path.exists(CODEC_MAP_PATH):
        # Fallback for GitHub Actions path resolution
        fallback_path = os.path.join(
            os.path.dirname(BASE_DIR), "binary_to_nucleotide", "codec_map.json"
        )
        if os.path.exists(fallback_path):
            path = fallback_path
        else:
            raise FileNotFoundError("❌ codec_map.json not found in expected locations.")
    else:
        path = CODEC_MAP_PATH

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
    return "".join(
        codec.get(binary_str[i:i + 2], {"symbol": "?"})["symbol"]
        for i in range(0, len(binary_str), 2)
    )


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
    assert binary_input == binary_output, (
        f"❌ Round-trip failed: {binary_input} → {nucleotide_seq} → {binary_output}"
    )
    log(f"🔁 Round-trip successful: {binary_input} → {nucleotide_seq} → {binary_output}")


# === Entry Point (Manual Run) ===
if __name__ == "__main__":
    codec_map_data = codec_map()  # direct call for local test
    validate_codec_structure(codec_map_data)
    test_round_trip(codec_map_data)
    log("🏁 Codec validation completed.\n")
