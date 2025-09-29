# Deposition within Decimalisation

*Part of the **Electrical Resistance** module in Angular Momentum Reaction Engine v2.*

---

## **Overview**
This document defines the deposition–decimalisation process as developed in the original spreadsheets  
(`deposition_within_decimalisation.xlsx`).  

Unlike the **Base Equation**, which is a direct differential/attenuation chain,  
this process operates through **multiple tab stages**.  
Each stage is a daisy-chained decimalisation, propagating progressively to an **OUTPUT vector**.

---

## **Formula (General Form)**

Let:

- \( D^{(n)} \) = value at the \( n \)-th decimalisation stage.  
- \( f_n \) = transformation applied at stage \( n \).  
- \( \text{OUTPUT}_i \) = final deposition values, indexed by \( i \).

Then:

\[
\text{OUTPUT}(i) = f_{N} \circ f_{N-1} \circ \dots \circ f_1 ( \text{Initial Inputs}[i] )
\]

Where:
- \( N \) = number of decimalisation stages (typically 12 in the current workbook).
- Initial inputs often derive from **high / low values** seeded from `Base_Equation`.

---

## **Expanded Staging**

For each stage \( n \):

\[
D^{(n)} = D^{(n-1)} \; \pm \; \delta_n
\]

- \( \delta_n \) = adjustment factor (simple ± increments, no higher-order operators).  
- Output sheet cells \( A1 \ldots A5 \) aggregate the terminal results.

---

## **Position in the Framework**

- **Base Equation** provides initial differentials (high vs low).  
- **Deposition Decimalisation** propagates those values across multiple stages.  
- Both live under:  
  `formulae/electrical_resistance/`  
  and map to corresponding Python prototypes in:  
  `amre/electrical_resistance/`.

---

## **Next Steps**

- Confirm precise **cell-by-cell mappings** from the workbook (tabs → functions).  
- Translate staged propagation into Python module:  
  `amre/electrical_resistance/deposition_decimalisation.py`.  
- Link results to HTML preview:  
  `previews/electrical_resistance/deposition_decimalisation.html`.  
