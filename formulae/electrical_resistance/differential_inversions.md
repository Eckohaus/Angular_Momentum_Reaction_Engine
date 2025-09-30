# Differential Inversions (Electrical Resistance)

The *Differential Inversions* construct originated in two spreadsheets:

- `differential_Inversions.xlsx`
- `differential_inversions_1.xlsx`

Both apply the same inversion logic but differ in their **scaling regimes**:

- **Regime A (Whole Numbers):** integer-scale values (±1 … ~17).  
- **Regime B (Real Numbers):** fractional-scale values (1e−05 … up to ~200,000+).  

---

## General Aim

To formalise **differential inversion** as a transformation within the *Electrical Resistance* module:

- Inputs are treated as **numerical signals**, agnostic to external context.  
- Behaviour is stabilised by reference to a **zero-bound state**.  
- The **scaling coefficient ($S$)** is defined as the **zero-bound parameter**:  
  - Encodes distance from the zero threshold.  
  - Governs whether inversion is *stable* (macro regime) or *sensitive* (micro regime).  

---

## Core Formula (Conceptual)

Let:

- $X$ = input value  
- $S$ = scaling coefficient (zero-bound parameter)  

**Differential inversion:**

$$
I(X, S) = \frac{S}{X}
$$

- If $|X| \gg S$: inversion flattens → low sensitivity.  
- If $|X| \approx S$: inversion amplifies → high sensitivity, near zero-bound.  

---

## Extensions

1. **Square Root (Limitation / Recursive Marker):**  
   Encodes internal constraint, acting as the *physics stabiliser*:  

   $$
   I_{t+1} = \pm \sqrt{I(X_t, S)}
   $$  

2. **Holographic Principle (Rotation Vector):**  
   Encodes projection into the next subset, acting as the *chemistry / biology transformer*:  

   $$
   I^{(k+1)} = e^{\pm i\theta} \, \sqrt{I^{(k)}}
   $$  

Together, the **square root** and **holographic rotation** describe how inversions both **constrain** and **propagate** into new layers.  

---

## Parameterised Operators

- **Square Root Parameter ($\alpha$):**  
  - Default: $\alpha = 1$  
  - $\alpha = 0$ → ignore square root (linear inversion only)  
  - $\alpha = 1$ → include $\pm \sqrt{}$ as QCD-like marker  
  - $\alpha > 1$ → amplify recursive weighting of the square root  

- **Holographic Rotation Parameter ($\theta$):**  
  - Default: $\theta = \pi/2$ (quarter rotation)  
  - $\theta = 0$ → no rotation (static subset)  
  - $\theta = \pi$ → inversion + reflection (mirrored subset)  

---

## Transposition and Positioning

- **Transposition** = shifting values between macro (whole number) and micro (fractional) regimes while maintaining zero-bound reference.  
- **Positioning** = whether inversion resolves on the **limitation vector** (square root, physics) or the **rotation vector** (holographic, chemistry/biology).  

---

## Notes

- Regimes A and B differ only in **scale**, not in operator.  
- $S$ is the universal **binding factor**, ensuring scale-aware behaviour.  
- The construct bridges **discrete** (integer) and **continuous** (real/decimal) regimes.  
- In spreadsheets, realised as chains of inversions with explicit scaling coefficients.  

---

## Open Questions

- Should Regimes A and B be unified under a **single operator**, with $S$ as determinant of behaviour?  
- Would renaming the source spreadsheets to:  
  - `differential_inversions_integer.xlsx`  
  - `differential_inversions_real.xlsx`  
  make their intent clearer in the repository structure?  
