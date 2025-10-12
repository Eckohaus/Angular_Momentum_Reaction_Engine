# codec/binary_to_nucleotide/tests/test_codec_translation.py
import os
import json
import pytest
from codec.binary_to_nucleotide.codec_translation_engine import (
    translate,
    reverse_translate,
    codec_roundtrip,
)

# === Safe path resolution ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CODEC_PATH = os.path.join(BASE_DIR, "..", "codec_map.json")

# Load codec map (CI-safe)
CODEC_MAP = None
if os.path.exists(CODEC_PATH):
    with open(CODEC_PATH, "r", encoding="utf-8") as f:
        CODEC_MAP = json.load(f)

# --- Basic validation dataset ---
TEST_CASES = [
    ("0101", None),   # Example direct mapping test
    ("111000", None), # Stress pattern
    ("000111", None), # Complementary input pattern
]


def test_codec_map_integrity():
    """Check codec_map.json structural integrity and expected fields."""
    assert CODEC_MAP is not None, "❌ codec_map.json missing"
    assert "codec" in CODEC_MAP, "❌ Missing 'codec' key in map"
    for pair in ["00", "01", "10", "11"]:
        assert pair in CODEC_MAP["codec"], f"❌ Missing mapping for bit-pair {pair}"


def test_translation_symmetry():
    """Ensure binary → nucleotide → binary yields the same output."""
    for binary_input, _ in TEST_CASES:
        assert codec_roundtrip(binary_input), f"Roundtrip failed for {binary_input}"


def test_forward_translation_non_empty():
    """Ensure forward translation produces a non-empty nucleotide string."""
    for binary_input, _ in TEST_CASES:
        nucleotide_output = translate(binary_input)
        assert len(nucleotide_output) > 0, f"No output for {binary_input}"


def test_reverse_translation_non_empty():
    """Ensure reverse translation produces a valid binary sequence."""
    for binary_input, _ in TEST_CASES:
        nucleotide_output = translate(binary_input)
        binary_output = reverse_translate(nucleotide_output)
        assert len(binary_output) > 0, f"No reverse output for {binary_input}"


def test_consistency_across_random_inputs():
    """Run randomized checks to ensure consistent mapping for random binary patterns."""
    import random
    for _ in range(10):
        rand_bin = "".join(random.choice("01") for _ in range(8))
        assert codec_roundtrip(rand_bin), f"Codec failed at random input {rand_bin}"
