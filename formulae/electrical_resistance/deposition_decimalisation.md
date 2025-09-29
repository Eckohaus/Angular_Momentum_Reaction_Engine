# Deposition Decimalisation (Electrical Resistance)

The *Deposition Decimalisation* construct extends the **Electrical Resistance module**.  
It describes the progressive subdivision of an initial boundary value into finer decimalised steps,  
followed by accumulation into an **output sequence**.

Originally expressed in spreadsheet form (`deposition_within_decimalisation.xlsx`),  
this formulation captures staged attenuation across multiple decimalisation levels.  

---

## General Formula (Compact Form)

Let:

- $X$ = initial deposition input  
- $n$ = decimalisation level (e.g., first, second, …, $n$-th)  
- $k$ = index within each level  

**Decimal subdivision:**

$$
d_{n,k} = \frac{X}{10^n}
$$

**Output accumulation (per level):**

$$
A_n = \sum_{k=1}^{m} d_{n,k}
$$

Where:

- $d_{n,k}$ is the $k$-th subdivision at decimalisation level $n$  
- $A_n$ is the aggregated value across that level  

---

## Expanded Staging (Spreadsheet Behaviour)

The spreadsheet implements this as chained sheets/tabs:  

1. Begin with deposition input $X$ at level $n=0$  
2. Apply successive decimalisation:  
   - Level 1: $d_{1,k} = X / 10$  
   - Level 2: $d_{2,k} = d_{1,k} / 10$  
   - …  
   - Level $n$: $d_{n,k} = d_{n-1,k} / 10$  
3. For each level, accumulate subdivisions into $A_n$  
4. Final **OUTPUT sheet** reports values $(A_1, A_2, \dots, A_N)$  

---

## Notes

- The construct is **sequential and cumulative**, mimicking chained spreadsheet tabs.  
- Each decimalisation stage attenuates the initial deposition by an additional order of magnitude.  
- The **OUTPUT vector** represents progressive resistance effects under subdivision.  
- Can be generalised to bases other than 10, but the original implementation uses decimalisation.  
- In practice, this functions as a **complement** to the *Base Equation*:  
  - *Base Equation* → attenuation by factorial steps  
  - *Deposition Decimalisation* → attenuation by decimal subdivision  
