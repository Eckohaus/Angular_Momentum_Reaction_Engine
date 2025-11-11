---
title: Base Equation (Electrical Resistance)
version: 1.0
last_updated: 2025-11-11
module: electrical_resistance
dependencies: []
status: stable
related_formulae:
  - differential_inversions.md
  - deposition_decimalisation.md
---

# Base Equation (Electrical Resistance)

The Base Equation models an attenuation cycle between a **high** ($H$) and **low** ($L$) value.  
It was originally expressed in spreadsheet form (`Base_Equation.xlsx`) as part of the *Electrical Resistance* module.  
The construct captures the progressive reduction of a differential through sequential steps.  

---

## General Formula (Compact Form)

Let:

- $H$ = upper boundary input  
- $L$ = lower boundary input  
- $n$ = iteration step  

**Difference:**

$$
D = H - L
$$

**Attenuation sequence:**

$$
A_n = \frac{D}{n!}
$$

**Target (after $N$ steps):**

$$
T = A_N
$$

---

## Expanded Staging (Spreadsheet Behaviour)

The spreadsheet implements this sequentially:

1. Compute differential:  
   $D = H - L$

2. Iteratively divide by each step index:  
   - Step 1: $A_1 = D / 1$  
   - Step 2: $A_2 = A_1 / 2$  
   - Step 3: $A_3 = A_2 / 3$  
   - …  
   - Step $n = A_{n-1} / n$

3. Output target:  
   $T = A_N$

---

## Notes

- The Base Equation is **data-agnostic**: $H$ and $L$ are generic boundary values.  
- Attenuation is modeled as a **sequential dampening process** (factorial decay).  
- In spreadsheet form, this corresponds to chained cell references ($C2 \dots C13$).  
- Within the **Electrical Resistance module**, it functions as a **general operator**:  
  - Any two boundary values can be supplied as inputs.  
  - The output $T$ represents the cumulative effect of progressive resistance.  
- This neutrality enables its use as a **building block** inside larger formulae, modules, or simulations.  
