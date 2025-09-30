# amre/lambda_seq/base_equation.py
import json

def base_equation(high: float, low: float, lambda_factor: float = 1.14, depth: int = 4):
    """
    Replicates Base_Equation.xlsx -> Calculating Variables sheet.

    Formula:
        target = (high + low)/2 + (high - low) * (lambda_factor ** depth)

    Args:
        high: Closing high (e.g. from currency pair).
        low: Closing low.
        lambda_factor: Growth multiplier (Excel used 1.14).
        depth: Number of iterations (Excel applied 1.14 four times).

    Returns:
        dict with inputs, intermediate steps, and final target.
    """
    diff = high - low
    avg = (high + low) / 2
    c9 = diff * (lambda_factor ** depth)
    target = avg + c9

    return {
        "inputs": {"high": high, "low": low},
        "parameters": {"lambda_factor": lambda_factor, "depth": depth},
        "difference": diff,
        "average": avg,
        "c9": c9,
        "target": target
    }

# Example usage
if __name__ == "__main__":
    # Same test you ran in Excel
    result = base_equation(1.0536, 1.0247)
    print(json.dumps(result, indent=2))
