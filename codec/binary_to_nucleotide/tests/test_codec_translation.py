import os
import pytest
import json
from codec.binary_to_nucleotide.codec_translation_engine import (
    translate,
    reverse_translate,
    codec_roundtrip,
)

# --- Load codec map dynamically for contextual validation ---
CODEC_MAP_PATH = os.path.join(
    os.path.dirname(__file__), "codec_map.json"
)
if os.path.exists(CODEC_MAP_PATH):
    with open(CODEC_MAP_PATH, "r", encoding="utf-8") as f:
        CODEC_MAP = json.load(f)
else:
    CODEC_MAP = None


# --- Base test cases ---
TEST_CASES = [
    ("00", "A"),
    ("01", "T"),
    ("10", "C"),
    ("11", "G"),
    ("00011011", None),  # Extended sequence test
]


def test_translation_symmetry():
    """Ensure binary → nucleotide → binary yields identical output."""
    for binary_input, _ in TEST_CASES:
        assert codec_roundtrip(binary_input), f"❌ Roundtrip failed for {binary_input}"


def test_forward_translation_non_empty():
    """Forward translation should produce a valid nucleotide string."""
    for binary_input, _ in TEST_CASES:
        nucleotide_output = translate(binary_input)
        assert nucleotide_output.strip() != "", f"❌ Empty output for {binary_input}"


def test_reverse_translation_non_empty():
    """Reverse translation should return a valid binary sequence."""
    for binary_input, _ in TEST_CASES:
        nucleotide_output = translate(binary_input)
        binary_output = reverse_translate(nucleotide_output)
        assert binary_output.strip() != "", f"❌ Empty reverse output for {binary_input}"


def test_codec_map_integrity():
    """Check codec_map.json structural integrity and expected fields."""
    assert CODEC_MAP is not None, "❌ codec_map.json missing"
    assert "codec" in CODEC_MAP, "❌ codec section missing"
    for k, v in CODEC_MAP["codec"].items():
        assert "symbol" in v, f"❌ Missing symbol in entry {k}"
        assert isinstance(v["symbol"], str), f"❌ Non-string symbol in {k}"


def test_consistency_across_random_inputs():
    """Run randomized checks to ensure consistent mapping."""
    import random
    for _ in range(10):
        rand_bin = "".join(random.choice("01") for _ in range(8))
        assert codec_roundtrip(rand_bin), f"❌ Codec failed for random input {rand_bin}"
