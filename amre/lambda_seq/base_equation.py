# amre/lambda_seq/base_equation.py
import json

def base_equation(high: float, low: float, steps: int = 10):
    """
    Replicates the Base_Equation.xlsx logic:
    - Takes a high and low (for example : the closing values of a currency pair).
    - Computes the differential.
    - Runs a daisy-chain attenuation cycle.

    Args:
        high (float): Closing high.
        low (float): Closing low.
        steps (int): Number of attenuation iterations.

    Returns:
        dict: {
            "inputs": {"high": float, "low": float},
            "differential": float,
            "attenuation_cycle": list of (step, value),
            "target": float
        }
    """
    # Core differential
    diff = high - low

    # Attenuation chain
    attenuation = []
    value = diff
    for i in range(1, steps + 1):
        value = value / i
        attenuation.append((i, value))

    return {
        "inputs": {"high": high, "low": low},
        "differential": diff,
        "attenuation_cycle": attenuation,
        "target": attenuation[-1][1],
    }

# Example usage (only runs if executed directly, not on import)
if __name__ == "__main__":
    result = base_equation(1.0824, 1.0813)
    # Pretty-print JSON for easier HTML preview rendering
    print(json.dumps(result, indent=2))
