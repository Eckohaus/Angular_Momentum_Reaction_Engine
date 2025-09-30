# Differential Inversions (Scaling Regimes)

The *Differential Inversions* construct originates from two spreadsheets:

- `differential_Inversions.xlsx`
- `differential_inversions_1.xlsx`

Both apply the same inversion logic but differ in their **scaling coefficients**:

- **Regime A (Whole Numbers):** operates with values on an integer scale (±1 … ~17).  
- **Regime B (Real Numbers):** operates across fractional values (1e−05 … up to ~200,000+).  

---

## General Aim

To formalise **differential inversion** as a transformation consistent with the *Electrical Resistance* module:

- Inputs are treated as **numerical signals**, independent of their origin.  
- The construct emphasises how inversion behaves differently under **integer-scale vs real-scale** domains.  
- Scaling is not tied to external context but defined entirely by the resistance framework.

---

## Core Formula (Conceptual)

Let:

- $X$ = input value  
- $S$ = scaling coefficient (internal parameter)  

**Differential inversion:**

$$
I(X, S) = \frac{S}{X}
$$

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

- The operator is **data-agnostic**: whole and real numbers are both admissible.  
- Behaviour diverges primarily according to **scaling regime**, not source domain.  
- The construct acts as a **bridge** between discrete and continuous interpretations.  

---

## Open Questions

- Should Regimes A and B be unified into a single operator (with $S$ absorbing the scaling difference), or kept distinct as independent cases?  
- Would renaming the spreadsheets to `differential_inversions_integer.xlsx` and `differential_inversions_real.xlsx` better reflect their roles?
