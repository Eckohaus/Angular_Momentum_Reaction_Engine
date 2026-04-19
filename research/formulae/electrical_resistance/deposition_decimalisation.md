# Deposition Decimalisation (Electrical Resistance)

The *Deposition Decimalisation* describes the subdivision of an initial input value into progressively finer partitions.  
It originated in spreadsheet form (`deposition_within_decimalisation.xlsx`) under the *Electrical Resistance* module.

The construct explores how a deposition $X$ is reduced, step by step, through decimal subdivisions and accumulations.

---

## General Formula (Compact Form)

Let:

- $X$ = initial deposition (boundary input)  
- $n$ = decimalisation level (iteration step)  
- $k$ = number of subdivisions per level  

**Subdivision at level $n$:**

$$
d_n = \frac{X}{10^n}
$$

**Accumulated output:**

$$
A_n = \sum_{i=1}^{k} d_n = k \cdot \frac{X}{10^n}
$$

---

## Expanded Staging (Spreadsheet Behaviour)

The spreadsheet implements this sequentially:

1. Begin with input $X$.  
2. At level $n$, subdivide $X$ by $10^n$.  
3. Accumulate across $k$ subdivisions (often $k = 10$).  
4. Record the result as $A_n$.  
5. Repeat for $n = 1, 2, \dots, N$.  

The output sequence is:

$$
[A_1, A_2, \dots, A_N]
$$

---

## Notes

- $X$ can be combined with additional inputs (e.g. $A_3$ in spreadsheet experiments) to adjust the subdivision baseline.  
- In spreadsheet form, each *tab* may represent a stage of chained decimalisation.  
- Outputs $A_1, \dots, A_N$ correspond to columns in the **OUTPUT** sheet.  
- Within the *Electrical Resistance* module, this provides a **stepwise dampening operator** distinct from the Base Equation.  

---

## Implementation Links

- Formula: [`formulas/electrical_resistance/deposition_decimalisation.md`](./deposition_decimalisation.md)  
- Python: [`amre/electrical_resistance/deposition_decimalisation.py`](../../amre/electrical_resistance/deposition_decimalisation.py)  
- Preview: [`previews/electrical_resistance/deposition_decimalisation.html`](../../previews/electrical_resistance/deposition_decimalisation.html)
