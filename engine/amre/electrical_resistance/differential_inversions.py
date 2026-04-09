# amre/electrical_resistance/differential_inversions.py

import json
import math
from typing import List, Dict


def differential_inversion(
    X: float,
    S: float = 1.0,
    steps: int = 5,
    regime: str = "auto"
) -> Dict:
    """
    Differential Inversions (Electrical Resistance Module)

    Implements the construct described in
    `formulae/electrical_resistance/differential_inversions.md`.

    Mathematical definitions:
        - Core inversion:
              I(X, S) = S / X
        - Square root extension (limitation vector):
              I_{t+1} = ± sqrt(I(X_t, S))
        - Holographic rotation (subset projection):
              I^(k+1) = e^(±iθ) sqrt(I^(k)), θ = π/2

    Extrapolation logic:
        • Iterates the inversion recursively across `steps`.
        • Tracks both integer-scale (whole numbers) and real-scale (fractional)
          behaviour. These are distinguished by `regime`, or auto-detected:
              - "integer": |X| ≥ 1
              - "real":    |X| < 1
        • Outputs per-step inversion, square root, and holographic rotation
          approximated here as ± roots.

    Args:
        X (float): Input value.
        S (float): Scaling coefficient (zero-bound parameter).
        steps (int): Number of recursive iterations.
        regime (str): "integer", "real", or "auto".
            - "integer": interpret as whole-number regime.
            - "real": interpret as fractional regime.
            - "auto": select based on |X|.

    Returns:
        dict: {
            "inputs": {
                "X": float,
                "S": float,
                "steps": int,
                "regime": str
            },
            "iterations": [
                {
                    "step": int,
                    "input": float,
                    "inversion": float,
                    "square_root": float,
                    "holographic_rotation": [float, float]
                },
                ...
            ],
            "notes": str
        }
    """
    if regime == "auto":
        regime = "real" if abs(X) < 1 else "integer"

    iterations: List[Dict] = []
    value = X

    for t in range(steps):
        # Core inversion
        inv = S / value if value != 0 else float("inf")

        # Square root extension
        root = math.sqrt(abs(inv))

        # Holographic rotation (placeholder: ± root)
        rotated = [+root, -root]

        iterations.append({
            "step": t + 1,
            "input": value,
            "inversion": inv,
            "square_root": root,
            "holographic_rotation": rotated
        })

        # Feed-forward
        value = inv

    return {
        "inputs": {"X": X, "S": S, "steps": steps, "regime": regime},
        "iterations": iterations,
        "notes": (
            f"Regime '{regime}' selected. "
            "Square root = limitation vector. "
            "Holographic rotation = subset projection. "
            "s is treated as zero-bound scaling coefficient."
        )
    }


# Example usage
if __name__ == "__main__":
    result_int = differential_inversion(15, S=1.0, steps=5, regime="integer")
    print("Integer regime:\n", json.dumps(result_int, indent=2))

    result_real = differential_inversion(0.0025, S=1.0, steps=5, regime="real")
    print("Real regime:\n", json.dumps(result_real, indent=2))
