# **Angular Momentum Reaction Engine v2 (2020)**  
*Statistical Modeling Tools for Energy-As-A-Unit Calculus*  

### **Overview**  
**Angular_Momentum_Reaction_Engine_v2** is the structured continuation of the 2020 project.
It transitions the original formula arrays and spreadsheet workflows into a **reproducible, testable, and documented codebase.**

This repository is part of the **ASTF project** (Applied Scientific & Theoretical Frameworks / August Sixth, Twenty Fifteen).

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
├── data/                     # Example datasets (CSV/Parquet)
├── docs/                     # Project documentation (MkDocs)
├── examples/                 # Jupyter notebooks & usage demos
├── tests/                    # Pytest suite
├── pyproject.toml            # Project configuration
├── mkdocs.yml                # Documentation site config
└── README.md                 # We are here```  
``` 
---

## Current Status
- **Lambda Projection Engine** (`amre/lambda_seq/engine.py`)  
  → Forecasts energy as discrete units mapped by eigenvalue scaling.  
- **Core constants** (`amre/core/constants.py`)  
  → Base power ratios, unit registry, physical constants.  
- **Basic test coverage** (`tests/test_lambda.py`)  
  → Confirms Lambda projections grow monotonically.  

### Roadmap
- Port **Boundary Momentum** calculators (growth-in-division).
- Encode **Infinities Framework** (assigned vs continuous).
- Convert **AC Deposition** XLSX → Python module with unit checks.
- Create **dataset loaders** (amre/io/datasets.py) with schema validation.
- Provide **examples/** notebooks for quick start.
- Deploy **MkDocs documentation** to GitHub Pages.

### Licence
- **Code** MIT Licence
- **Formulas/Data Compilations** CC BY-NC 4.0
- **Commercial Use** : Requires separate license from [Eckohaus Limited](https://eckohaus.blog)

### Related Repositories
- [Formula-to-3D Prototype Engine](https://github.com/Eckohaus/Formula-to-3D_Prototype_Engine)  
- ASTF Documentation (private repo)  
