#!/usr/bin/env python3
"""
tools/export_formulas.py

Exports AMRE-derived formula datasets as JSON for downstream engines
(e.g. Formula-to-3D Prototype Engine).

First implementation:
- "pong_phase_overlap": a phase-lattice inspired by the Pong Algorithm
  notes in formulas/pong_algorithm/readme.md

JSON schema (v1):

{
  "meta": {
    "id": "amre_pong_phase_overlap_v1",
    "source_repo": "Eckohaus/Angular_Momentum_Reaction_Engine_v2",
    "source_path": "formulas/pong_algorithm/readme.md",
    "description": "...",
    "generated_utc": "...",
    "version": "1.0.0"
  },
  "points": [
    {
      "x": ...,
      "y": ...,
      "r": ...,
      "theta": ...,
      "phase": ...,
      "amplitude": ...,
      "overlap_real": ...,
      "overlap_imag": ...
    },
    ...
  ]
}
"""

import json
import math
import os
from datetime import datetime
from pathlib import Path


def generate_pong_phase_overlap(
    n_radial: int = 12,
    n_angular: int = 96,
    r_min: float = 0.1,
    r_max: float = 1.0,
):
    """
    Construct a simple phase lattice inspired by the Pong Algorithm notes:

      ∇² φ → -4πρ      (Poisson-style potential)
      ⟨ψ₁ | ψ₂⟩ = e^{iφ}  (phase overlap channel)

    We don't attempt a full PDE solve here – this is a *schematic* numerical
    playground:

      - r: radial coordinate
      - θ: angular coordinate
      - phase φ ≈ θ (wrapped into [-π, π])
      - amplitude A(r) = exp(-r²)  (Gaussian envelope)
      - overlap: A(r) * e^{iφ}

    Output format: list of point dicts, suitable for JSON.
    """
    points = []

    if n_radial <= 0 or n_angular <= 0:
        return points

    for i in range(n_radial):
        # Radial sampling between r_min and r_max
        if n_radial == 1:
            r = (r_min + r_max) / 2.0
        else:
            t = i / (n_radial - 1)
            r = r_min + t * (r_max - r_min)

        for j in range(n_angular):
            theta = 2.0 * math.pi * j / n_angular

            # Cartesian embedding
            x = r * math.cos(theta)
            y = r * math.sin(theta)

            # Phase ≈ θ wrapped into [-π, π]
            phase = ((theta + math.pi) % (2.0 * math.pi)) - math.pi

            # Simple Gaussian amplitude
            amplitude = math.exp(-r * r)

            # Complex overlap
            overlap_real = amplitude * math.cos(phase)
            overlap_imag = amplitude * math.sin(phase)

            points.append(
                {
                    "x": x,
                    "y": y,
                    "r": r,
                    "theta": theta,
                    "phase": phase,
                    "amplitude": amplitude,
                    "overlap_real": overlap_real,
                    "overlap_imag": overlap_imag,
                }
            )

    return points


def build_pong_payload() -> dict:
    """
    Wrap the Pong phase lattice into a JSON-ready payload with metadata.
    """
    points = generate_pong_phase_overlap()

    return {
        "meta": {
            "id": "amre_pong_phase_overlap_v1",
            "source_repo": "Eckohaus/Angular_Momentum_Reaction_Engine_v2",
            "source_path": "formulas/pong_algorithm/readme.md",
            "description": (
                "Phase-lattice inspired by the Pong Algorithm: "
                "coherence transport via overlap ⟨ψ₁ | ψ₂⟩ = e^{iφ}, "
                "encoded on a polar grid (r, θ) with Gaussian envelope."
            ),
            "generated_utc": datetime.now().astimezone().isoformat(),
            "version": "1.0.0",
        },
        "points": points,
    }


def save_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def main():
    repo_root = Path(__file__).resolve().parents[1]
    out_path = repo_root / "exports" / "formulas" / "pong_phase_overlap.json"

    payload = build_pong_payload()
    save_json(out_path, payload)

    print(f"[export_formulas] Wrote Pong phase dataset → {out_path}")


if __name__ == "__main__":
    main()
