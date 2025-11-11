# XLSX Pipeline Integration Guide

**Version**: 1.0  
**Last Updated**: November 2025  
**Module**: Data Processing & Transformation

---

## Overview

The XLSX Pipeline is a critical component of the Angular Momentum Reaction Engine v2, enabling the transformation of spreadsheet-based theoretical calculations into multiple output formats for computational processing, validation, and visualization.

---

## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    XLSX Input Layer                         │
│  data/spreadsheets/in_development/                         │
│    ├── electrical_resistance/                               │
│    ├── financials/                                         │
│    ├── formulae/                                           │
│    └── infinities/                                         │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│              Processing Layer                                │
│  scripts/convert_xlsx.py                                    │
│    ├── XLSX Reading (pandas.ExcelFile)                     │
│    ├── Multi-sheet Processing                              │
│    ├── HTML Generation                                     │
│    └── JSON Transformation                                 │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ├──────────────┬─────────────┐
                   ▼              ▼             ▼
          ┌─────────────┐  ┌──────────┐  ┌──────────────┐
          │ HTML Preview│  │   JSON   │  │ Python Exec  │
          │ docs/previews│  │transforms/│  │ (modules)   │
          └─────────────┘  └──────────┘  └──────────────┘
                   │              │             │
                   └──────────────┴─────────────┘
                                  │
                                  ▼
                   ┌──────────────────────────────┐
                   │  GitHub Pages (Published)    │
                   │  docs/index.html             │
                   └──────────────────────────────┘
```

---

## XLSX Structure Requirements

### File Organization

**Directory Structure**:
```
data/spreadsheets/in_development/
├── [domain]/                    # e.g., electrical_resistance, formulae
│   ├── [module]/               # e.g., lambda_sequencer, unit_(ac)
│   │   ├── [file].xlsx        # Calculation spreadsheets
│   │   └── readme.md          # Module documentation
│   └── readme.md              # Domain documentation
```

### Spreadsheet Design Patterns

#### Pattern 1: Single Calculation Sheet
**Use Case**: Base equations, simple transformations

```
Sheet: "Calculating Variables"
├── Inputs (Cells A1:B5)
│   ├── high: [value]
│   ├── low: [value]
│   └── lambda_factor: 1.14
├── Calculations (Cells C1:C10)
│   └── [intermediate steps]
└── Output (Cell C11)
    └── target: [result]
```

**Example**: `Base_Equation.xlsx`

#### Pattern 2: Multi-Stage Processing
**Use Case**: Deposition, decimalisation, lambda projections

```
Sheet 1: "INPUT"
├── Raw data values
└── Boundary conditions

Sheet 2: "PROCESSING"
├── Iterative calculations
├── Lambda projections
└── Differential steps

Sheet 3: "OUTPUT"
├── Final results
├── Validation checks
└── Export-ready data
```

**Example**: `deposition_within_decimalisation.xlsx`

#### Pattern 3: Multi-File Cartography
**Use Case**: Lambda cartography, boundary momentum

```
File Set:
├── cartography_1.xlsx  → First projection layer
├── cartography_2.xlsx  → Second projection layer
└── cartography_3.xlsx  → Third projection layer

Each file:
├── Sheet: "Data"       → Raw/processed values
└── Sheet: "Metadata"   → Context, parameters, timestamps
```

**Example**: Lambda cartography sets in financials and chemistry modules

### Naming Conventions

**File Names**:
- Use snake_case: `base_equation.xlsx`, `differential_inversions.xlsx`
- Version suffixes: `_v1`, `_v2` for historical tracking
- Descriptive names: avoid single letters except in cartography series (A, B, C)

**Sheet Names**:
- Use UPPERCASE for standard sheets: `INPUT`, `OUTPUT`, `PROCESSING`
- Use Title Case for domain-specific: `Calculating Variables`, `Lambda Projection`
- Consistency within a module

---

## Conversion Process

### Script: `scripts/convert_xlsx.py`

#### Core Functions

##### 1. XLSX to HTML Conversion

```python
def convert_xlsx(src_path, rel_path):
    """
    Converts XLSX to HTML preview
    
    Process:
    1. Read XLSX with pandas.ExcelFile
    2. Parse each sheet into DataFrame
    3. Generate HTML tables with styling
    4. Link to repository source
    5. Export to docs/previews/
    
    Returns:
        (source_url, None, None)
    """
```

**Output Location**: `docs/previews/[domain]/[module]/[file].html`

**Features**:
- Multi-sheet support (one HTML section per sheet)
- CSS styling via `docs/style.css`
- Automatic table formatting
- Error handling with logging

##### 2. XLSX to JSON Transformation

```python
# Embedded in convert_xlsx()
json_export[sheet] = df.to_dict(orient="records")
```

**Output Location**: `transforms/[domain]/[module]/[file].json`

**Format**:
```json
{
  "Sheet1": [
    {"column1": value1, "column2": value2},
    {"column1": value3, "column2": value4}
  ],
  "Sheet2": [...]
}
```

**Use Cases**:
- Programmatic data access
- API endpoints (future)
- Python module integration

##### 3. Python Module Preview

```python
def convert_py(src_path, rel_path):
    """
    Executes Python module and captures output
    
    Process:
    1. Run Python file via subprocess
    2. Capture stdout/stderr
    3. Format as HTML preview
    4. Link in index
    
    Returns:
        (None, preview_html_path, None)
    """
```

**Output Location**: `docs/previews/[domain]/[module]/[file].html`

##### 4. Index Generation

```python
def build_index(entries):
    """
    Builds hierarchical navigation index
    
    Features:
    - Nested folder structure
    - Links to: source XLSX, previews, interactives
    - Collapsible sections via <details>
    - Automatic sorting
    """
```

**Output**: `docs/index.html`

---

## GitHub Actions Integration

### Workflow: `.github/workflows/xlsx-to-html.yaml`

**Trigger Events**:
- Push to `data/spreadsheets/in_development/**`
- Changes to `scripts/convert_xlsx.py`
- Manual trigger via `workflow_dispatch`

**Process Flow**:

```yaml
1. Checkout repository
2. Setup Python 3.x
3. Clean old previews (rm -rf docs/previews/*)
4. Run conversion pipeline
   ├── Execute convert_xlsx.py
   ├── Log to logs/[timestamp]_convert.log
   └── Rotate logs (keep last 7)
5. Display summary
   ├── List HTML previews
   ├── List interactive files
   └── List Python code previews
6. Commit and push
   ├── Add docs/previews
   ├── Add transforms
   ├── Add logs
   └── Push to repository
```

**Permissions**: `contents: write` (required for commit/push)

**Monitoring**: Check workflow status via GitHub Actions badge in README

---

## Integration with Python Modules

### Current State

**Gap**: JSON transforms are generated but not yet consumed by Python modules.

**Existing Pattern**:
```python
# amre/electrical_resistance/base_equation.py
def base_equation(high: float, low: float, lambda_factor: float = 1.14, depth: int = 4):
    """Replicates Base_Equation.xlsx -> Calculating Variables sheet"""
    # Manual reimplementation
```

### Recommended Integration Pattern

#### Step 1: Create Data Loader Module

```python
# amre/io/xlsx_loader.py
import json
import os
from pathlib import Path

TRANSFORMS_DIR = Path(__file__).parent.parent.parent / "transforms"

def load_xlsx_transform(domain: str, module: str, filename: str, sheet: str = None):
    """
    Load processed XLSX data from JSON transform
    
    Args:
        domain: e.g., 'electrical_resistance', 'formulae'
        module: e.g., 'lambda_sequencer', 'unit_(ac)'
        filename: e.g., 'base_equation.json'
        sheet: Optional sheet name, returns all if None
    
    Returns:
        dict or list: Transformed data
    """
    filepath = TRANSFORMS_DIR / domain / module / filename
    
    if not filepath.exists():
        raise FileNotFoundError(f"Transform not found: {filepath}")
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    if sheet:
        return data.get(sheet, [])
    return data

def validate_transform(data, schema):
    """
    Validate transform data against expected schema
    
    Args:
        data: Loaded transform data
        schema: Expected structure definition
    
    Returns:
        bool: True if valid, raises ValueError if not
    """
    # Implementation for schema validation
    pass
```

#### Step 2: Use in Computational Modules

```python
# amre/electrical_resistance/base_equation.py
from amre.io.xlsx_loader import load_xlsx_transform

def base_equation_from_xlsx(transform_file="base_equation.json"):
    """
    Execute base equation using data from XLSX transform
    """
    data = load_xlsx_transform(
        domain="electrical_resistance",
        module="lambda_sequencer",
        filename=transform_file,
        sheet="Calculating Variables"
    )
    
    # Extract values from transform
    inputs = data[0]  # First row typically contains inputs
    high = inputs.get('high')
    low = inputs.get('low')
    
    return base_equation(high, low)
```

#### Step 3: Validation and Testing

```python
# tests/test_xlsx_integration.py
import pytest
from amre.electrical_resistance import base_equation_from_xlsx

def test_xlsx_transform_integration():
    """Verify XLSX transform loads correctly"""
    result = base_equation_from_xlsx("base_equation.json")
    assert result is not None
    assert 'target' in result

def test_xlsx_schema_validation():
    """Ensure transform matches expected structure"""
    from amre.io.xlsx_loader import load_xlsx_transform, validate_transform
    
    data = load_xlsx_transform("electrical_resistance", "lambda_sequencer", "base_equation.json")
    schema = {
        "Calculating Variables": ["high", "low", "lambda_factor"]
    }
    assert validate_transform(data, schema)
```

---

## Data Quality and Validation

### Pre-Conversion Validation

**Recommended Addition to `convert_xlsx.py`**:

```python
def validate_xlsx_structure(src_path):
    """
    Validate XLSX before conversion
    
    Checks:
    1. File is valid XLSX format
    2. Contains expected sheets
    3. Numerical data is within bounds
    4. No circular references (where detectable)
    5. Formulas evaluate correctly
    
    Returns:
        (bool, list of warnings/errors)
    """
    warnings = []
    errors = []
    
    try:
        xls = pd.ExcelFile(src_path)
    except Exception as e:
        errors.append(f"Invalid XLSX format: {e}")
        return False, errors
    
    # Check for empty sheets
    for sheet in xls.sheet_names:
        df = xls.parse(sheet)
        if df.empty:
            warnings.append(f"Sheet '{sheet}' is empty")
        
        # Check for numerical consistency
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if df[col].isnull().all():
                warnings.append(f"Column '{col}' in sheet '{sheet}' has all null values")
    
    return len(errors) == 0, warnings + errors
```

### Post-Conversion Validation

```python
def validate_json_transform(json_path, xlsx_path):
    """
    Ensure JSON transform accurately represents XLSX
    
    Checks:
    1. All sheets present
    2. Row counts match
    3. Data types preserved
    4. No data loss in transformation
    """
    pass
```

---

## Troubleshooting

### Common Issues

#### 1. Conversion Fails Silently

**Symptom**: XLSX file present but no HTML/JSON output

**Diagnosis**:
```bash
# Check conversion logs
cat logs/[latest]_convert.log | grep -i error
```

**Solutions**:
- Verify XLSX is not corrupted (open in Excel/LibreOffice)
- Check for special characters in sheet names
- Ensure pandas can parse all data types

#### 2. HTML Preview Empty

**Symptom**: Preview file exists but shows no data

**Cause**: Sheet parsing failed

**Fix**:
```python
# Check DataFrame content during conversion
df = xls.parse(sheet)
print(f"Sheet '{sheet}': {len(df)} rows, {len(df.columns)} columns")
```

#### 3. JSON Transform Incomplete

**Symptom**: Missing sheets or data in JSON

**Cause**: orient="records" may not handle all structures

**Alternative**:
```python
json_export[sheet] = df.to_dict(orient="split")  # Preserves index
# or
json_export[sheet] = df.to_dict(orient="index")  # For keyed data
```

#### 4. GitHub Action Fails

**Symptom**: Workflow shows red X

**Check**:
1. Workflow logs in Actions tab
2. Python dependencies installed (pandas, openpyxl)
3. File permissions (needs write access)
4. Git configuration (user.name, user.email set)

---

## Best Practices

### For XLSX Authors

1. **Use Consistent Structure**:
   - Define inputs clearly
   - Separate processing from outputs
   - Include metadata sheet when useful

2. **Document Formulas**:
   - Add comments to complex cells
   - Use named ranges for clarity
   - Include formula documentation in README

3. **Version Control**:
   - Save new versions as separate files
   - Update version suffix (v1, v2)
   - Document changes in commit messages

4. **Test Before Commit**:
   - Verify formulas calculate correctly
   - Check for #REF! or #VALUE! errors
   - Ensure data types are correct

### For Pipeline Developers

1. **Error Handling**:
   - Log all errors with context
   - Don't fail silently
   - Provide actionable error messages

2. **Performance**:
   - Process files in parallel when possible
   - Cache results when appropriate
   - Monitor conversion times

3. **Extensibility**:
   - Make conversion functions modular
   - Support plugin architecture for new formats
   - Keep processing logic separate from I/O

---

## Future Enhancements

### Planned Features

1. **Schema Validation**:
   - Define JSON schemas for expected structures
   - Validate on conversion
   - Reject invalid files with clear errors

2. **Interactive Previews**:
   - JavaScript-based calculators
   - Real-time parameter adjustment
   - Visualization of results

3. **API Endpoints**:
   - RESTful access to transforms
   - Query by domain/module/file
   - Real-time conversion on demand

4. **Data Lineage**:
   - Track source XLSX → transform → module usage
   - Version control for transforms
   - Change detection and alerts

5. **Performance Monitoring**:
   - Track conversion times
   - Identify bottlenecks
   - Optimize slow transformations

---

## Related Documentation

- **Main Repository Analysis**: `docs/repository_analysis.md`
- **V3 Readiness**: `docs/v3_readiness.md`
- **PONG Integration**: `formulae/pong_algorithm/integration_guide.md`
- **Workflow Configuration**: `.github/workflows/xlsx-to-html.yaml`
- **Conversion Script**: `scripts/convert_xlsx.py`

---

## Support and Contribution

For issues, questions, or contributions to the XLSX pipeline:

1. Check existing documentation
2. Review conversion logs
3. Test with sample files
4. Open issue with reproduction steps
5. Submit PR with tests for enhancements

**Contact**: [Eckohaus Limited](https://eckohaus.blog)
