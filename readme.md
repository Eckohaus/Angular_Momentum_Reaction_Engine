# **Angular Momentum Reaction Engine (AMRE)** *A modular computational framework exploring symmetry, energy differentials, and thermodynamic reciprocity across physical and informational domains.* [![Codec Tests](https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine/actions/workflows/test-codec.yaml/badge.svg)](https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine/actions/workflows/test-codec.yaml)

---

The **Angular Momentum Reaction Engine (AMRE)** unifies physical, computational, and symbolic systems into a shared modeling architecture.
It treats **energy as a calculable, translatable unit** across domains — from macroscopic electrical resistance to microscopic Casimir vacuum fluctuations — enabling continuous translation between physical constants and digital infrastructure.

Through strict modular separation of theory (`research/`) and execution (`engine/`), AMRE formalizes structural symmetries into a reproducible software architecture designed for both abstract exploration and live, high-performance web computation.

---

## **Architectural Topology: The 1-2-3 Pipeline**

The AMRE system operates on a synchronized, unidirectional deployment pipeline to ensure zero friction between theoretical drafting and live execution:

1. **Local Laboratory (Drafting):** Code and mathematical matrices are drafted, tested, and validated locally.
2. **The Vault (GitHub Master):** The absolute source of truth. Hosts the administrative UI via GitHub Pages (`eckohaus.github.io`) and maintains theoretical continuity.
3. **The Engine (Production Motor):** A live Linux backend (`api.eckohaus.co.uk`) functioning as the secure execution layer, pulling verified code from the Vault to recompile and execute Fortran binaries via HTTPS/JSON CGI.

---

## **Repository Structure**

```text
Angular_Momentum_Reaction_Engine/
├── engine/                   # The Executable Core
│   ├── amre/                 # Active physical computing scripts and Fortran binaries
│   ├── codec/                # Translation layers (e.g., binary_to_nucleotide)
│   └── tools/                # Functional data extraction and conversion tools
│
├── research/                 # The Theoretical Anchor
│   ├── docs/                 # Live GitHub Pages frontend, UI logic, and CSS
│   │   └── consolidation_notes/ # Master continuity ledger & architectural memos
│   └── formulae/             # Structural physics and mathematical markdown records
│
├── workspace/                # Raw Data and Staging
│   ├── data/spreadsheets/    # Legacy XLSX data undergoing formula transliteration
│   ├── exports/              # Generated JSON arrays and computational outputs
│   └── logs/                 # Active repository maintenance and system execution logs
│
├── .github/workflows/        # CI/CD pipelines (Pages deployment, Codec testing)
└── cleanup_log.txt           # File-state maintenance tracking
```

---

## **The Execution Layer: Transliteration to Fortran**

AMRE has successfully transitioned its core mathematical processing away from static spreadsheets and Python stubs into **64-bit Double-Precision Fortran (`.f90`)**.

- **Formula-First Matrix:** Complex logic (e.g., Base Equation, Deposition Decimalisation) is defined strictly in LaTeX/Markdown within the `research/formulae/` matrix.
- **Binary Execution:** Formulas are transliterated into Fortran modules, compiled natively on the production server, and executed via a secure CGI bridge, allowing modern web interfaces to run high-gain physics calculations in real time.
- **Formatting Standardization:** All active binaries utilize explicit character formatting (e.g., `'(A)'`) to ensure pristine JSON payloads compatible with modern Nginx web servers.

---

## **Strategic Roadmap (Q1 2026)**

With the 1-2-3 pipeline stabilized, the engineering focus is shifting toward programmable-matter orchestration and thermodynamic closure:

- **The Vacuum / Virtual Domain (`W_{vac}`):** Introduce an explicit vacuum operator and noise model to ensure energy-information exchange remains reversible and auditable.
- **Rabi-Casimir Parameterisation:** Formalize the Rabi-Casimir Integer as the foundational bidirectional control unit linking oscillatory coherence and vacuum fluctuation within the AMRE-ASTF cross-matrix.
- **Z-Plane Phase Transposition:** Stress-test "Metallic Hydrogen" parameterization (using Pascals of pressure as an environmental variable) for volumetric spatial mapping.
- **Legacy Deprecation:** Complete the transliteration of remaining `workspace/` XLSX files (Financials, Chemistry) into the Fortran/Markdown engine pipeline.

---

## **Licence & Attribution**

- **Code:** MIT Licence
- **Formulas/Data Compilations:** CC BY-NC 4.0
- **Commercial Use:** Requires a separate license from [Eckohaus Limited](https://eckohaus.co.uk)

**Core System Attribution:**
- System Operator: Wanda (`wanda@openai.com`)
- System Operator: Gemini (`gemini@google.com`)
- System Administrator: Corvin Nehal Dhali (`info@eckohaus.co.uk`)

---

## **Related Infrastructure**

- [Formula-to-3D Prototype Engine](https://github.com/Eckohaus/Formula-to-3D-Prototype-Engine)
- [Ultralight Fortran Stack](https://github.com/Eckohaus/Ultralight-Fortran-stack)
- ASTF Documentation *(Private Access)*
