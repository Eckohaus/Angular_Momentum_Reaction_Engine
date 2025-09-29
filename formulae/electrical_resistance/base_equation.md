# Base Equation (Electrical Resistance)

The Base Equation models the attenuation cycle between a **high** ($H$) and **low** ($L$) value.  
It defines a differential and then applies a sequential attenuation process,  
making it a general framework independent of any specific dataset or domain.

---

## General Formula (Compact Form)

Let:

- $H$ = high input (a chosen reference value, e.g. from observed data)  
- $L$ = low input (a paired reference value, e.g. from observed data)  
- $n$ = iteration step  

Difference:

$$
D = H - L
$$

Attenuation sequence:

$$
A_n = \frac{D}{n!}
$$

Target (after $N$ steps):

$$
T = A_N
$$

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

---

## Notes
- $H$ and $L$ are externally provided (imported data).  
- The attenuation behaves like a daisy-chained division (factorial decay).  
- In spreadsheet form, this corresponds to chained cell references ($C2 \dots C13$).
