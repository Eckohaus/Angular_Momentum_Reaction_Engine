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
- The construct emphasises how inversion behaves differently across domains that sit **close to or far from zero**.  
- The **scaling coefficient ($S$)** is explicitly defined as a **zero-bound parameter**:  
  - It encodes how far a system is positioned from the zero threshold.  
  - It governs stability/instability of inversion as magnitude shrinks or grows.

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

1. **Square Root (Recursive Marker):**  
Captures iterative dampening/amplification across steps:

$$
I_{t+1} = \pm \sqrt{I(X_t, S)}
$$

2. **Holographic Rotation (Subset Transition):**  
Each inversion layer rotates forward into the next subset:

$$
I^{(k+1)} = e^{\pm i\theta} \, \sqrt{I^{(k)}}
$$

---

## Notes

- $S$ is **not arbitrary**: it anchors inversion to the zero-bound, ensuring behaviour is scale-aware.  
- Whole and real number regimes only differ in their **distance from zero**, not in their fundamental operator.  
- The construct acts as a **bridge** between discrete and continuous interpretations.  

---

## Open Questions

- Should Regimes A and B be unified under a single zero-bound operator, with $S$ as the binding factor?  
- Would renaming the spreadsheets to `differential_inversions_integer.xlsx` and `differential_inversions_real.xlsx` better reflect their zero-bound positions?
