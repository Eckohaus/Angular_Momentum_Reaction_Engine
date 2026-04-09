# amre/electrical_resistance/deposition_decimalisation.py
import json

def deposition_decimalisation(X: float, levels: int = 5, subdivisions: int = 10, a3: float = None):
    """
    Implements the Deposition Decimalisation construct.

    Two possible modes:
    1. Generalised decimal subdivision:
       - Sequentially subdivides an initial deposition X by powers of 10 (or chosen base).
       - At each level, accumulates the subdivisions into an output sequence.

    2. Spreadsheet-like placeholder (if a3 is provided):
       - Combines X (A1) and a3 (A3) to produce outputs A1..An.
       - TODO: refine with real chained-tab behaviour.

    Args:
        X (float): Initial deposition input (boundary value).
        levels (int): Number of decimalisation levels (default: 5).
        subdivisions (int): Number of subdivisions per level (default: 10).
        a3 (float, optional): Secondary input (corresponding to spreadsheet cell A3).

    Returns:
        dict with input values, outputs list, and notes.
    """
    outputs = []

    if a3 is None:
        # Mode 1: general decimalisation
        for n in range(1, levels + 1):
            d_n = X / (10 ** n)   # decimal subdivision
            A_n = sum(d_n for _ in range(subdivisions))  # accumulate across subdivisions
            outputs.append(A_n)
        notes = "General decimalisation mode."
    else:
        # Mode 2: spreadsheet placeholder
        base = (X + a3) / 2
        for i in range(1, levels + 1):
            outputs.append(round(base / i, 10))
        notes = "Spreadsheet placeholder mode (replace with chained-tab logic)."

    return {
        "inputs": {"X": X, "a3": a3, "levels": levels, "subdivisions": subdivisions},
        "outputs": {f"A{i}": val for i, val in enumerate(outputs, start=1)},
        "notes": notes,
    }


# Example usage
if __name__ == "__main__":
    # Generalised mode
    result1 = deposition_decimalisation(1.0, levels=5, subdivisions=10)
    print("Generalised:\n", json.dumps(result1, indent=2))

    # Spreadsheet placeholder mode
    result2 = deposition_decimalisation(1.05, levels=5, subdivisions=10, a3=0.95)
    print("Spreadsheet:\n", json.dumps(result2, indent=2))
