# **Angular Momentum Reaction Engine v2 (2020)**  
*A modular, physics-inspired computational framework exploring symmetry,  
energy differentials, and translational grammars across domains.*  

*Statistical Modeling Tools for Energy-As-A-Unit Calculus*  

[![Codec Tests](https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/actions/workflows/test-codec.yaml/badge.svg)](https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/actions/workflows/test-codec.yaml)

---

The **Angular Momentum Reaction Engine (AMRE)** unifies physical, computational, and symbolic systems into a shared modeling architecture.  
It treats **energy as a calculable unit** across domains — from electrical resistance and field induction to binary and nucleotide grammars — enabling continuous translation between physical constants and informational structures.  
Through modular builds (core, lambda, boundary, codec), AMRE v2 formalises this symmetry within a reproducible software framework designed for both theoretical exploration and experimental computation.

---

## **Repository Structure**
```
Angular_Momentum_Reaction_Engine_v2/
├── amre/                     # Core package
│   ├── core/                 # Base constants, ratios, unit handling
│   ├── lambda_seq/           # Lambda Projection Engine
│   ├── infinities/           # Assigned vs Continuous models (future)
│   ├── boundary/             # Growth-in-division calculators (future)
│   ├── electrochem/          # AC deposition models (future)
│   ├── finance/              # Currency differential tools (future)
│   ├── io/                   # Dataset loaders & validators
│   └── viz/                  # Plotting & visualisation tools
│
├── codec/                    # Cross-domain translation layer
│   └── binary_to_nucleotide/ # Codec initialization module (v1)
│       ├── codec_map.json
│       ├── codec_translation_engine.py
│       ├── codec_validation_framework.md
│       ├── test_codec_map.py
│       └── readme.md
│
├── formulas/                 # Formula-first definitions (Markdown + LaTeX)
│   └── electrical_resistance/
│       ├── base_equation.md
│       └── deposition_decimalisation.md
│
├── amre/                     # Python implementations (mirroring formulas)
│   └── electrical_resistance/
│       ├── base_equation.py
│       └── deposition_decimalisation.py
│
├── docs/                     # GitHub Pages root
│   ├── index.html            # Auto-generated previews index
│   ├── style.css             # Styling for previews
│   ├── previews/             # Auto-generated static previews
│   │   └── electrical_resistance/
│   │       ├── base_equation.html
│   │       └── deposition_decimalisation.html
│   └── interactive/          # Auto-generated interactive previews
│       └── electrical_resistance/
│           ├── base_equation_interactive.html
│           └── deposition_decimalisation_interactive.html
│
├── data/                     # Example datasets (CSV/XLSX)
├── examples/                 # Jupyter notebooks & usage demos
├── tests/                    # Pytest suite
├── pyproject.toml            # Project configuration
├── mkdocs.yml                # Documentation site config
└── README.md                 # We are here
```

---

## **Formula → Code → Preview Pipeline**

The **Electrical Resistance** modules are being transitioned away from direct XLSX  
into a formula-first workflow:

- `formulas/` → Markdown + LaTeX expressions  
- `amre/` → Python implementations (mirroring formulas)  
- `previews/` → HTML renderings (auto-generated)  

Interactive previews (`*_interactive.html`) are generated where applicable, providing richer inspection alongside static previews.  

**Example: Base Equation**  
- Formula: `formulas/electrical_resistance/base_equation.md`  
- Python: `amre/electrical_resistance/base_equation.py`  
- Preview: `previews/electrical_resistance/base_equation.html`  

This creates a reproducible chain:  
1. **Formulas** → General + expanded staging (preserve spreadsheet behaviour).  
2. **Computational Layer** → Python/Fortran execution.  
3. **Preview Layer** → HTML for inspection & communication.  

---

## **Current Status**

- **Lambda Projection Engine** (`amre/lambda_seq/engine.py`)  
  → Forecasts energy as discrete units mapped by eigenvalue scaling.  
- **Core constants** (`amre/core/constants.py`)  
  → Base power ratios, unit registry, physical constants.  
- **Binary → Nucleotide Codec** (`codec/binary_to_nucleotide/`)  
  → Defines reversible translation grammar between digital and biological logic.  
- **Basic test coverage** (`tests/test_lambda.py`, `codec/.../test_codec_translation.py`)  
  → Confirms Lambda growth and Codec roundtrip symmetry.  
- **Electrical Resistance (in progress):**  
  → Migrating `Base_Equation.xlsx` and `Deposition_Decimalisation.xlsx`  
  into formula-first + Python modules with live previews.  

---

## **Integration with Fortran Stack**

- Python modules here can be swapped for accelerated Fortran implementations.  
- The **Ultralight Fortran Stack** is intended as a runtime layer for this project.  
- This keeps the Angular Momentum repo as the conceptual + prototype space,  
  while Fortran provides performance + portability.  

---

## **Live Pages**

- **Previews Index**: [Angular Momentum v2 GitHub Pages](https://eckohaus.github.io/Angular_Momentum_Reaction_Engine_v2)  

*(Browse the `formulas/`, `amre/`, and `previews/` chains — auto-updated via GitHub Actions.)*  

---

## **Roadmap**

- Port **Boundary Momentum** calculators (growth-in-division).  
- Encode **Infinities Framework** (assigned vs continuous).  
- Expand **Binary → Nucleotide Codec** into probabilistic field grammar.  
- Finalise **AC Deposition** formulas → Python module with unit checks.  
- Create **dataset loaders** (`amre/io/datasets.py`) with schema validation.  
- Provide **examples/** notebooks for quick start.  
- Deploy **MkDocs documentation** to GitHub Pages.

**For detailed analysis and V3 roadmap, see**:
- [Repository Analysis](docs/repository_analysis.md) - Comprehensive analysis of all four focus areas
- [V3 Readiness Assessment](docs/v3_readiness.md) - Migration roadmap and gap analysis
- [Formula Index](docs/formula_index.md) - Complete cross-referenced formula catalog
- [XLSX Pipeline Guide](docs/xlsx_pipeline_guide.md) - Data processing workflow documentation
- [PONG Integration Guide](formulae/pong_algorithm/integration_guide.md) - Theoretical integration examples

---

## **Licence**

- **Code**: MIT Licence  
- **Formulas/Data Compilations**: CC BY-NC 4.0  
- **Commercial Use**: Requires separate license from [Eckohaus Limited](https://eckohaus.blog)  

---

## **Related Repositories**

- [Formula-to-3D Prototype Engine](https://github.com/Eckohaus/Formula-to-3D-Prototype-Engine)
- [Ultralight Fortran Stack](https://github.com/Eckohaus/Ultralight-Fortran-stack)  
- ASTF Documentation *(private repo)*  
