"""Minimal experimental pipeline; not AGI. Standard library only."""
import cmath
import hashlib
import json
import math

def run(values):
    x = [float(v) for v in values]
    if not x or not all(math.isfinite(v) for v in x):
        raise ValueError("expected nonempty finite numeric input")
    n = len(x)
    spectrum = [abs(sum(v * cmath.exp(-2j * math.pi * k * j / n)
                        for j, v in enumerate(x))) for k in range(n//2+1)]
    key = hashlib.sha256(json.dumps(x, separators=(",", ":")).encode()).hexdigest()
    return {"input_id": key, "spectrum": spectrum, "status": "experimental"}
