# Formula Index and Cross-Reference Map

**Last Updated**: 2025-11-11  
**Version**: 1.0

---

## Overview

This document provides a comprehensive index of all formulae within the Angular Momentum Reaction Engine v2, organized by module with cross-references showing theoretical and computational relationships.

---

## Formula Categories

### 1. Electrical Resistance Module

Formulae for modeling energy attenuation, field inversions, and deposition processes.

#### 1.1 Base Equation
**Path**: `formulae/electrical_resistance/base_equation.md`  
**Status**: ✅ Stable  
**Python**: `amre/electrical_resistance/base_equation.py`

**Purpose**: Models attenuation cycle between high and low boundary values

**Key Formula**:
$$
A_n = \frac{D}{n!} \quad \text{where} \quad D = H - L
$$

**Dependencies**: None (foundational)  
**Used By**: 
- Differential inversions (scaling reference)
- Lambda projections (boundary definition)

**Related Datasets**:
- `data/spreadsheets/in_development/electrical_resistance/lambda_sequencer/Base_Equation.xlsx`

---

#### 1.2 Differential Inversions
**Path**: `formulae/electrical_resistance/differential_inversions.md`  
**Status**: ✅ Stable  
**Python**: `amre/electrical_resistance/differential_inversions.py`

**Purpose**: Transformation via zero-bound inversion with QCD/holographic extensions

**Key Formulae**:

*Core Inversion*:
$$
I(X, S) = \frac{S}{X}
$$

*QCD Boundary (Peripheral)*:
$$
I_{t+1} = \pm \sqrt{I(X_t, S)}
$$

*Holographic Boundary (Central)*:
$$
I^{(k+1)} = e^{\pm i\theta} \sqrt{I^{(k)}}
$$

**Dependencies**: 
- Base equation (for scaling coefficient reference)

**Related To**:
- PONG Algorithm (Poisson charge density mapping)
- Delta Key (eigenmatrix logic)

**Related Datasets**:
- `differential_inversions.xlsx` (whole numbers, Regime A)
- `differential_inversions_1.xlsx` (real numbers, Regime B)

---

#### 1.3 Deposition Decimalisation
**Path**: `formulae/electrical_resistance/deposition_decimalisation.md`  
**Status**: ✅ Stable  
**Python**: `amre/electrical_resistance/deposition_decimalisation.py`

**Purpose**: Subdivision of input value into progressively finer decimal partitions

**Key Formula**:
$$
A_n = k \cdot \frac{X}{10^n}
$$

where $k$ = number of subdivisions per level

**Dependencies**: None  
**Complements**: Base equation (alternative dampening operator)

**Related Datasets**:
- `deposition_within_decimalisation.xlsx`
- `deposition_within_decimalisation_v1.xlsx`

---

### 2. Physics Module

Advanced theoretical frameworks linking field dynamics to temporal and spatial structures.

#### 2.1 O(3)–Van der Waals Continuum
**Path**: `formulae/physics/o3_vdw_volumetric_continuum.md`  
**Status**: 📝 Theoretical  
**Python**: Not yet implemented

**Purpose**: Temporal actuator framework via Van der Waals potential reversal

**Key Formula**:
$$
\frac{\partial V_{vdW}}{\partial t} < 0  \Rightarrow  \frac{\partial \phi}{\partial t} > 0
$$

**Temporal Actuator**:
$$
T(\text{phase}) = f(\Delta\phi, E, V)
$$

**Dependencies**: 
- PONG Algorithm (phase transport mechanisms)

**Related Concepts**:
- Moiré time crystals (2D materials)
- ABL retrocausality
- Relational time (Barbour, Rovelli)

**Future Integration**: Experimental validation track (optional for V3)

---

### 3. PONG Algorithm Module

Theoretical bridge between Angular Momentum, QCD, and Poisson field calculus.

#### 3.1 Lambda–Poisson QCD Compiler
**Path**: `formulae/pong_algorithm/readme.md`  
**Status**: 📝 Theoretical  
**Python**: Planned in `amre/pong/`  
**Integration Guide**: `formulae/pong_algorithm/integration_guide.md`

**Purpose**: Unified field calculus bridging multiple symmetry domains

**Core Vision**:
$$
\underbrace{\nabla^2 \phi}_{\text{Angular Momentum}}
\;\rightarrow\;
\underbrace{-4\pi\rho}_{\text{Poisson Charge Density}}
$$

**Phase Transport**:
$$
\langle \psi_1 | \psi_2 \rangle = e^{i\phi}
$$

**Pong Operator**:
$$
\hat{P}|\psi\rangle = e^{i\phi}|\psi\rangle
$$

**Dependencies**:
- Hydrogen Equation (binary resonance)
- Lambda Projections (1.5578 resonance mapping)
- Differential Inversions (Poisson integration)

**Integration Points**:
1. **Hydrogen Equation**: Binary frequency encoding (1.14 factor)
2. **Lambda Projections**: Tau-decay resonance (1.5578 ≈ 1.14^3.3)
3. **Differential Inversions**: Poisson field solver analogue
4. **Binary-Nucleotide Codec**: Phase-encoded translation

**Related Datasets**: Financial lambda cartography, Hydrogen equation spreadsheets

---

### 4. Chemistry Module (Formulae)

Theoretical constructs for nuclear resonance and periodic table symmetries.

#### 4.1 Hydrogen Equation
**Path**: `data/spreadsheets/in_development/formulae/chemistry/periodic_table/alkali/the_hydrogen_equation/readme.md`  
**Status**: 📝 Theoretical with data  
**Python**: Not yet implemented

**Purpose**: Nuclear resonance signatures in binary assembly

**Key Concepts**:

*Hydrogen Ion Genesis*:
$$
\Psi_H = \frac{Q}{(\Delta t)^{-3}}
$$

*Oxygen Component*:
$$
\text{O}^{2-} \equiv k^2
$$

**Binary Assembly**:
| Component | Encoding | Frequency Ratio |
|-----------|----------|-----------------|
| H⁺        | 1.14     | 0.11 → 0.88     |
| O²⁻       | k²       | 0.27 → 2.16     |

**Related To**:
- PONG Algorithm (hydrogen binaries → QCD)
- Lambda Projections (1.14 frequency encoding)

**Related Datasets**:
- `e_squared/lambda/cartography_*.xlsx`
- `e_squared/boundary_momentum/a.xlsx`

---

#### 4.2 Neodymium Curvature
**Path**: `data/spreadsheets/in_development/formulae/chemistry/periodic_table/lanthanide_series/neodymium/`  
**Status**: 📝 Data available, no formula doc yet  
**Python**: Not yet implemented

**Available Datasets**:
1. `1_Atomic_number_144.243.xlsx`
2. `2_e_squared_in_binary.xlsx`
3. `3_AC_differentials.xlsx`
4. `4_EM_curvature.xlsx`

**Related To**: PONG Algorithm (neodymium curvature differentials)

**Recommendation**: Create formula documentation extracting theoretical framework from XLSX

---

### 5. Physics Module (Formulae - Additional)

#### 5.1 Delta Key
**Path**: `data/spreadsheets/in_development/formulae/physics/delta_key/readme.md`  
**Status**: 📝 Specification  
**Python**: Not yet implemented

**Purpose**: Energetic constant for nucleated eigenmatrices

**Key Equations**:

*Composition → Frequency*:
$$
\mathscr{F} = \frac{\Delta \cdot \text{Spin Density}}{\text{Vacuum Permittivity}}
$$

*Frequency → Composition*:
$$
\mathscr{C} = \int \frac{\text{Lambda Field Intensity}}{\Delta_{\pm}} \, d(\text{Planar})
$$

**Dirac-Maxwell Synthesis**:
$$
\boxed{\text{Dirac Equation} \supset \text{Delta Key Logic}}
$$

**Related To**:
- PONG Algorithm (eigenmatrix assembler)
- Differential Inversions (polarity fields)

---

#### 5.2 Sulawesi Equation
**Path**: `data/spreadsheets/in_development/formulae/physics/the_sulawesi_equation/readme.md`  
**Status**: 📝 Placeholder  
**Python**: Not yet implemented

**Note**: Documentation exists but content not yet populated. Requires development.

---

### 6. Core Framework Components

#### 6.1 Lambda Projections
**Path**: `docs/formulation.md` (Section 1)  
**Status**: ✅ Implemented  
**Python**: `amre/lambda_seq/engine.py`

**Purpose**: Energy as discrete unit sequence, eigenvalue scaling

**Formula**:
$$
E_n = E_0 \cdot r^n
$$

where $r = 1.14$ (validated optimum)

**Used By**:
- Electrical resistance calculations
- PONG resonance mapping (1.5578)
- Financial data projections
- Hydrogen equation encoding

---

#### 6.2 Infinities Framework
**Path**: `docs/formulation.md` (Section 2)  
**Status**: 📝 Conceptual  
**Python**: Planned in `amre/infinities/`

**Two Modes**:

*Assigned Infinities (transport)*:
$$
I_{\text{assigned}}(x) = f(x_1, x_2, \dots, x_n)
$$

*Continuous Infinities (lossless)*:
$$
I_{\text{continuous}}(t) = \int f(t) \, dt
$$

**Related Datasets**:
- `infinities_continuous.xlsx`
- `infinities_transport.xlsx`

---

#### 6.3 Boundary Momentum
**Path**: `docs/formulation.md` (Section 3)  
**Status**: 📝 Conceptual  
**Python**: Planned in `amre/boundary/`

**Purpose**: Division-driven growth models

**Formula**:
$$
\frac{dN}{dt} = \alpha N - \beta N^2
$$

where:
- $\alpha$ = growth parameter
- $\beta$ = limiting/division parameter

**Related Datasets**: Boundary momentum XLSX files in financial and chemistry datasets

---

### 7. Cross-Domain Integration (Codec)

#### 7.1 Binary → Nucleotide Codec
**Path**: `codec/binary_to_nucleotide/readme.md`  
**Status**: ✅ Operational  
**Python**: `codec/binary_to_nucleotide/codec_translation_engine.py`

**Purpose**: Reversible translation between digital and biological logic

**Mapping**:
| Binary | Nucleotide | Base     | Group      |
|--------|------------|----------|------------|
| 00     | A          | adenine  | purine     |
| 01     | T          | thymine  | pyrimidine |
| 10     | C          | cytosine | pyrimidine |
| 11     | G          | guanine  | purine     |

**Integration with PONG**: Phase-encoded translation (see `integration_guide.md`)

**Related To**:
- PONG phase transport
- Hydrogen binary assembly

---

## Formula Dependency Graph

```
Core Constants (1.14, ratios)
    ↓
    ├─→ Lambda Projections (E_n = E_0 · r^n)
    │       ↓
    │       ├─→ Electrical Resistance (base equation, inversions)
    │       ├─→ Hydrogen Equation (binary encoding)
    │       └─→ PONG Resonance (1.5578 mapping)
    │
    ├─→ Differential Inversions (I = S/X)
    │       ↓
    │       ├─→ PONG Poisson Bridge (∇²φ = -4πρ)
    │       └─→ Delta Key (eigenmatrix logic)
    │
    ├─→ Binary-Nucleotide Codec (translation)
    │       ↓
    │       └─→ PONG Phase Encoding (coherence tracking)
    │
    └─→ PONG Algorithm (meta-framework)
            ↓
            ├─→ Hydrogen Equation integration
            ├─→ Lambda projection resonance
            ├─→ Differential inversion Poisson mapping
            └─→ Phase transport codec extension
```

---

## Formula Status Summary

### By Implementation Status

**✅ Stable & Implemented** (4):
- Base Equation
- Differential Inversions
- Deposition Decimalisation
- Binary-Nucleotide Codec

**⚙️ Partial Implementation** (1):
- Lambda Projections (basic implementation exists)

**📝 Theoretical/Specification** (8):
- PONG Algorithm
- O(3)-VdW Continuum
- Hydrogen Equation
- Neodymium Curvature
- Delta Key
- Sulawesi Equation
- Infinities Framework
- Boundary Momentum

### By Module Coverage

| Module | Formulae | Implemented | Percentage |
|--------|----------|-------------|------------|
| Electrical Resistance | 3 | 3 | 100% |
| Lambda/Core | 3 | 1 | 33% |
| PONG Algorithm | 1 | 0 | 0% |
| Physics | 3 | 0 | 0% |
| Chemistry | 2 | 0 | 0% |
| Codec | 1 | 1 | 100% |
| **Total** | **13** | **5** | **38%** |

---

## Usage Patterns

### For Researchers

1. **Start with Core Framework** (`docs/formulation.md`)
2. **Review Electrical Resistance** (most complete module)
3. **Explore PONG Integration** (`formulae/pong_algorithm/integration_guide.md`)
4. **Check XLSX data** for empirical context

### For Developers

1. **Examine implemented modules** (electrical_resistance, codec)
2. **Review Python implementations** in `amre/`
3. **Check tests** in `codec/binary_to_nucleotide/tests/`
4. **Follow XLSX pipeline** (`docs/xlsx_pipeline_guide.md`)

### For Integration Work

1. **Use this index** to identify dependencies
2. **Check cross-references** for related formulae
3. **Review integration guide** for PONG-AMRE bridges
4. **Validate against datasets** in `data/spreadsheets/`

---

## Recommendations for V3

### Priority 1: Complete Partial Implementations
- [ ] Finish Lambda Projections (decay models)
- [ ] Implement PONG computational layer
- [ ] Port Hydrogen Equation to Python

### Priority 2: Document Data-Only Modules
- [ ] Create formula docs for Neodymium
- [ ] Document Sulawesi Equation
- [ ] Extract Delta Key formal specification

### Priority 3: Implement Theoretical Frameworks
- [ ] Infinities Framework
- [ ] Boundary Momentum
- [ ] O(3)-VdW experimental validation

### Priority 4: Enhance Cross-References
- [ ] Add "See Also" sections to all formula files
- [ ] Create interactive dependency viewer
- [ ] Link to relevant XLSX datasets in each formula doc

---

## Maintenance

This index should be updated when:
- New formulae are added
- Implementation status changes
- Dependencies are identified
- Cross-references are discovered

**Last Review**: 2025-11-11  
**Next Review**: After V2.5 module completion (January 2026)

---

## See Also

- **Comprehensive Analysis**: `docs/repository_analysis.md`
- **XLSX Pipeline Guide**: `docs/xlsx_pipeline_guide.md`
- **PONG Integration**: `formulae/pong_algorithm/integration_guide.md`
- **V3 Roadmap**: `docs/v3_readiness.md`
- **Main README**: `readme.md`
