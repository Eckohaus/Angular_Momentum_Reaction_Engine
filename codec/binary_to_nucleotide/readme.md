# Binary → Nucleotide Codec Initialization

**Module:** `amre/codec/binary_to_nucleotide/`  
**Stage:** Initialization (v1)  
**Project:** Angular Momentum Reaction Engine v2  

---

## Overview

This module defines a **translation codec** between **binary logic**  
(energy quantisation, digital symmetry) and **nucleotide logic**  
(biological sequencing, entropic symmetry).

Unlike `base_equation.xlsx` — which defines *field induction and bandgap behaviour* —  
the codec operates *downstream* of that layer, at the point where field symmetry  
stabilises into discrete dual-states (the precondition of binary logic).

The codec aims to express how digital dualities (0 / 1) can emerge as  
genetic quartets (A / T / G / C), maintaining conservation of energy  
and information across both regimes.

---

## Conceptual Basis

| Domain | Function | Structural Substrate | Analogue Reference |
|--------|-----------|----------------------|--------------------|
| Base Equation | Inductive / Continuous | Bandgap field | Electrical Resistance equations |
| Codec Process | Translative / Discrete | Binary ↔ Nucleotide grammar | Codec symmetries |

The codec thus begins where **induction stabilises**, not where it originates.  
It uses `base_equation.xlsx` only as a **reference for initialization constants**  
(e.g., potential differences, resistance ratios) exported into  
`induction_reference/base_equation_reference.json`.

---

## Files

| File | Purpose |
|------|----------|
| `induction_reference/base_equation_reference.json` | Simplified constants imported from AMRE base equations. |
| `codec_process.xlsx` | Core working sheet defining binary↔nucleotide translation logic. |
| `codec_init.py` | Python prototype of translation map and schema. |
| `readme.md` | This documentation file. |

---

## Development Sequence

1. Extract relevant constants from `base_equation.xlsx` → `induction_reference/base_equation_reference.json`.  
2. Define binary↔nucleotide grammar in `codec_process.xlsx`.  
3. Implement reversible mapping prototype (`codec_init.py`).  
4. Validate with Lambda Projection Engine harmonics.  
