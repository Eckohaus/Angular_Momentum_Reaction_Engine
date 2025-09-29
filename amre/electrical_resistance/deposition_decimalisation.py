# amre/electrical_resistance/deposition_decimalisation.py

import json

def deposition_decimalisation(X: float, levels: int = 5, subdivisions: int = 10):
    """
    Implements the Deposition Decimalisation construct:
    - Sequentially subdivides an initial deposition X by powers of 10 (or chosen base).
    - At each level, accumulates the subdivisions into an output sequence.

    Args:
        X (float): Initial deposition input (boundary value).
        levels (int): Number of decimalisation levels (default: 5).
        subdivisions (int): Number of subdivisions per level (default: 10).

    Returns:
        dict: {
            "input": X,
            "levels": levels,
            "subdivisions": subdivisions,
            "outputs": [A1, A2, ..., An]
        }
    """

    outputs = []
    value = X

    for n in range(1, levels + 1):
        d_n = value / (10 ** n)   # decimal subdivision
        A_n = sum(d_n for _ in range(subdivisions))  # accumulate across k subdivisions
        outputs.append(A_n)

    return {
        "input": X,
        "levels": levels,
        "subdivisions": subdivisions,
        "outputs": outputs
    }


# Example usage
if __name__ == "__main__":
    result = deposition_decimalisation(1.0, levels=5, subdivisions=10)
    print(json.dumps(result, indent=2))
