# **Angular Momentum Reaction Engine v2 (2020)**  
*Statistical Modeling Tools for Energy-As-A-Unit Calculus*  

---

## **Overview**  
**Angular_Momentum_Reaction_Engine_v2** is the structured continuation of the 2020 project.  
It transitions the original formula arrays and spreadsheet workflows into a **reproducible, testable, and documented codebase.**  

This repository is part of the **ASTF project**  
(*Applied Scientific & Theoretical Frameworks / August Sixth, Twenty Fifteen*).  

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
├── previews/                 # Auto-generated HTML previews
│   └── electrical_resistance/
│       ├── base_equation.html
│       ├── base_equation_interactive.html
│       ├── deposition_decimalisation.html
│       └── deposition_decimalisation_interactive.html
│
├── docs/                     # Project documentation (GitHub Pages root)
│   ├── index.html            # Auto-generated previews index
│   └── style.css             # Styling for previews
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
- **Basic test coverage** (`tests/test_lambda.py`)  
  → Confirms Lambda projections grow monotonically.  
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
- Finalise **AC Deposition** formulas → Python module with unit checks.  
- Create **dataset loaders** (`amre/io/datasets.py`) with schema validation.  
- Provide **examples/** notebooks for quick start.  
- Deploy **MkDocs documentation** to GitHub Pages.  

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
