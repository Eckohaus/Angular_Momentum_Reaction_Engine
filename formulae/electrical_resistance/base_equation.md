# Base Equation (Electrical Resistance)

The *Base Equation* originated as `Base_Equation.xlsx` under  
`data/spreadsheets/in_development/Electrical_resistance/lambda_sequencer/`.  
It defines a simple attenuation cycle starting from the difference between a high and low input.

---

## General Formula (Compact Form)

Let:

- $H$ = high input (e.g., currency pair closing high)  
- $L$ = low input (e.g., currency pair closing low)  
- $n$ = iteration step  

Then the differential is:

$$
D = H - L
$$

The attenuation sequence is:

$$
A_n = \frac{D}{n!}
$$

Where:

- $D$ is the differential  
- $A_n$ is the attenuated value at step $n$  
- Final target = $A_N$ for chosen $N$ steps  

---

## Expanded Staging (Spreadsheet Behaviour)

The spreadsheet implements this sequentially:

1. Compute differential:  

   $$
   D = H - L
   $$

2. Iteratively divide by each step index:  
   - Step 1: $A_1 = D / 1$  
   - Step 2: $A_2 = A_1 / 2$  
   - Step 3: $A_3 = A_2 / 3$  
   - …  
   - Step $n$: $A_n = A_{n-1} / n$  

3. Output target:  

   $$
   T = A_N
   $$

This matches the daisy-chained cell references in the original `.xlsx`.

---

## Notes

- **Interpretation:** Attenuation = diminishing influence through sequential division.  
- **Implementation:**  
  - Python version: [`amre/electrical_resistance/base_equation.py`](../../amre/electrical_resistance/base_equation.py)  
  - Preview: [`previews/electrical_resistance/base_equation.html`](../../previews/electrical_resistance/base_equation.html)  
- **Future:** Could be generalized beyond simple factorial decay.
