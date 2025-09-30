# Differential Inversions (Electrical Resistance)

The *Differential Inversions* construct originated in two spreadsheets:

- `differential_Inversions.xlsx`
- `differential_inversions_1.xlsx`

Both apply the same inversion logic but differ in their **scaling regimes**:

- **Regime A (Whole Numbers):** operates with values on an integer scale (±1 … ~17).  
- **Regime B (Real Numbers):** operates across fractional values (1e−05 … up to ~200,000+).  

---

## General Aim

To formalise **differential inversion** as a transformation consistent with the *Electrical Resistance* module:

- Inputs are treated as **numerical signals**, independent of their external origin.  
- Behaviour is anchored to a **zero-bound state**, which stabilises cross-scale comparisons.  
- The **scaling coefficient ($S$)** is defined as the **zero-bound parameter**:  
  - It encodes how far a system is positioned from the zero threshold.  
  - It governs whether inversion appears *stable* (macro regime) or *sensitive* (micro regime).  

---

## Core Formula (Conceptual)

Let:

- $X$ = input value  
- $S$ = scaling coefficient (zero-bound parameter)  

**Differential inversion:**

$$
I(X, S) = \frac{S}{X}
$$

- If $|X| \gg S$, inversion tends to flatten (low sensitivity).  
- If $|X| \approx S$, inversion amplifies (high sensitivity, near zero-bound).  

---

## Extensions

1. **Square Root (Limitation / Recursive Marker):**  
Encodes constraint within the system, acting as the *physics* stabiliser:  

$$
I_{t+1} = \pm \sqrt{I(X_t, S)}
$$  

2. **Holographic Principle (Rotation Vector):**  
Encodes projection into the next subset, acting as the *chemistry / biology* transformer:  

$$
I^{(k+1)} = e^{\pm i\theta} \, \sqrt{I^{(k)}}
$$  

- Together, the square root + holographic rotation describe how inversions both **constrain** and **propagate** into new layers.  

---

## Transposition and Positioning

- **Transposition** = shifting values between macro (whole number) and micro (fractional) regimes while maintaining reference to the zero-bound.  
- **Positioning** = determining whether the inversion resolves on the **limitation vector** (square root, physics) or the **rotation vector** (holographic, chemistry/biology).  

---

## Notes

- Regimes A and B differ only in **scale**, not in fundamental operator.  
- $S$ acts as the universal **binding factor**, ensuring scale-aware behaviour.  
- This construct bridges **discrete** (integer) and **continuous** (real/decimal) interpretations.  
- In spreadsheet form, this is implemented through chains of inversions with explicit scaling coefficients.  

---

## Open Questions

- Should Regimes A and B be unified under a **single operator**, with $S$ as the determinant of behaviour?  
- Would renaming the source spreadsheets to:  
  - `differential_inversions_integer.xlsx`  
  - `differential_inversions_real.xlsx`  
  make their intent clearer within the repository structure?  
