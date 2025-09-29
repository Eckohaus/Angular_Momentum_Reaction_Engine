# Base Equation (Electrical Resistance)

The Base Equation models the attenuation cycle between a **high** ($H$) and **low** ($L$) value.  
It defines a differential and then applies a sequential attenuation process.  
This framework is general and independent of any particular dataset or context.

---

## General Formula (Compact Form)

Let:

- $H$ = high input  
- $L$ = low input  
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

- $H$ and $L$ are externally provided.  
- The attenuation behaves like a daisy-chained division (factorial decay).  
- In spreadsheet form, this corresponds to chained cell references ($C2 \dots C13$).  
- Within the **electrical resistance module**, this equation is treated as a structural element,  
  not tied to any specific application domain.
