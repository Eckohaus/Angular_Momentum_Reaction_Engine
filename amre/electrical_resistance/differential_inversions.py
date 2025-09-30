# amre/electrical_resistance/differential_inversions.py
import json
import cmath

def differential_inversion(x: float, s: float = 1.0):
    """
    Compute the differential inversion with respect to a zero-bound scaling coefficient.

    Args:
        x (float): Input value.
        s (float): Scaling coefficient (zero-bound parameter). Default = 1.0.

    Returns:
        dict: Contains input, inversion, square root variants, and holographic rotation.
    """
    if x == 0:
        raise ValueError("Input x cannot be zero (division by zero).")

    # Core inversion
    inv = s / x

    # Square root branch (±)
    sqrt_pos = inv**0.5 if inv >= 0 else None
    sqrt_neg = -(inv**0.5) if inv >= 0 else None

    # Complex holographic rotation (subset transition)
    # Here θ = π/2 represents a 90° rotation
    theta = cmath.pi / 2
    holographic = cmath.exp(1j * theta) * cmath.sqrt(inv)

    return {
        "inputs": {"x": x, "s": s},
        "inversion": inv,
        "square_root": {"positive": sqrt_pos, "negative": sqrt_neg},
        "holographic_rotation": holographic,
        "notes": "s is treated as zero-bound scaling coefficient."
    }


# Example usage
if __name__ == "__main__":
    # Test values in both regimes
    results = [
        differential_inversion(10, s=1),      # Whole number regime
        differential_inversion(1e-5, s=1),    # Real number regime near zero
        differential_inversion(200000, s=1),  # Large real number regime
    ]
    print(json.dumps(results, indent=2, default=str))
