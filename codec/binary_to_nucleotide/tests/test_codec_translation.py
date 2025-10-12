import pytest
from amre.codec.binary_to_nucleotide.codec_translation_engine import (
    translate,
    reverse_translate,
    codec_roundtrip,
)

# --- Basic validation dataset ---
TEST_CASES = [
    ("0101", "ATCG"),   # Example direct mapping test
    ("111000", None),   # Stress pattern (depends on map length)
    ("000111", None),   # Complementary input pattern
]


def test_translation_symmetry():
    """Ensure binary → nucleotide → binary yields the same output."""
    for binary_input, _ in TEST_CASES:
        assert codec_roundtrip(binary_input), f"Roundtrip failed for {binary_input}"


def test_forward_translation_non_empty():
    """Ensure that forward translation produces a non-empty nucleotide string."""
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
