### Formulation Notes 

This document provides a **mathematical and conceptual foundation** for the Angular Momentum Reaction Engine (v2).
It transitions the 2020 formulations into a structured, testable form.

## 1. Lambda Projections

### Concept:
Energy is modeled as a discrete unit sequence, scaled by eigenvalue-like ratios.
This reflects how fields evolve under repeated multiplicative transformations.

### Notation:
Let $E_0$ be the base energy unit.
For ratio $r$ and step $n$:

$$
E_n = E_0 \cdot r^n
$$

- **Default ratio:** $r = 1.14$ (statistically validated optimum).  
- Series growth is monotonic under $r > 1$.  

**Use in code:** implemented in `amre/lambda_seq/engine.py` as `project_lambda`.

---

## 2. Infinities Framework

**Concept:**
Two modes of representing infinities:
	- **Assigned Infinities:** transport models, based on discrete allocations across vectors.
	- **Continuous Infinities:** lossless ratios, nuclear scaling regimes.

### Notation (placeholder):

  - **Assigned form:**

$$
I_{\text{assigned}}(x) = f(x_1, x_2, \dots, x_n)
$$

  - **Continuous form:**

$$
I_{\text{continuous}}(t) = \int f(t) \, dt
$$

These will be formalized in amre/infinities/.

---

## 3. Boundary Momentum

**Concept:**
Models of division-driven growth, where state evolution is governed by splitting or branching processes.

**Notation (placeholder):**
If $N(t)$ is the entity count at time t:

$$
\frac{dN}{dt} = \alpha N - \beta N^2
$$

  -	\alpha: growth parameter
  -	\beta: limiting / division parameter

Future implementation in amre/boundary/.

---

## 4. Base Power Ratios

**Concept:**
Ratios near $1.14$ provide optimal fit when scaling nuclear/energy systems.

**Example values:**
  -	$1.14$ (default, validated optimum)
  -	$1.15$
  -	$1.16$

To be stored in amre/core/constants.py.

---

## 5. Future Extensions
	- Electrochemical models (AC deposition): redox attenuation, probability distributions.
	- Currency Differentials: economic analogues of transport models.
	- Integration with ASTF: feeding outputs into Formula-to-3D Prototype Engine for visualization.
