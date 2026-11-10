#!/usr/bin/env python3
"""Ensure all eight approved brand HEX values are unchanged."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "navy": "#081727",
    "tech_blue": "#174765",
    "cyan": "#24CDDF",
    "electric_blue": "#4C85D7",
    "champagne_gold": "#DFC48C",
    "cool_white": "#F1F6FA",
    "alert_red": "#D62832",
    "verified_green": "#28AA83",
}
actual = json.loads((ROOT / "assets/design-tokens.json").read_text(encoding="utf-8"))["canonical_palette"]
assert actual == EXPECTED, f"Palette mismatch: expected {EXPECTED}, found {actual}"
print("PASS: all eight canonical HEX colors matched")
