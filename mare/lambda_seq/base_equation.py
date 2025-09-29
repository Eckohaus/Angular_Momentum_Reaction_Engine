# amre/lambda_seq/base_equation.py

def base_equation(high: float, low: float, steps: int = 10):
    """
    Replicates the Base_Equation.xlsx logic:
    - Takes a high and low (closing values of a currency pair).
    - Computes the differential.
    - Runs a daisy-chain attenuation cycle.

    Args:
        high: Closing high (float).
        low: Closing low (float).
        steps: Number of attenuation iterations.

    Returns:
        dict with differential, attenuation cycle, and final target value.
    """
    # Core differential
    diff = high - low

    # Attenuation chain (simple sequential division)
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


# Example usage
if __name__ == "__main__":
    result = base_equation(1.0824, 1.0813)
    print(result)
