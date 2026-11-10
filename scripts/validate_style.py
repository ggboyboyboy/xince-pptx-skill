#!/usr/bin/env python3
"""Simple structural quality control for generated PPTX; render for visual QA."""
from pathlib import Path
import sys
from pptx import Presentation

def validate(path):
    p = Presentation(str(path))
    warnings = []
    ratio = p.slide_width / p.slide_height
    if abs(ratio - 16/9) > 0.015:
        warnings.append("Canvas is not 16:9")
    for index, slide in enumerate(p.slides, 1):
        shapes = list(slide.shapes)
        images = [s for s in shapes if s.shape_type == 13]
        text_shapes = [s for s in shapes if s.has_text_frame and s.text.strip()]
        if len(shapes) == len(images) == 1:
            warnings.append(f"Slide {index}: entirely rasterized")
        if not text_shapes:
            warnings.append(f"Slide {index}: lacks editable text")
        for shape in text_shapes:
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    if run.text.strip() and run.font.size and run.font.size.pt < 10:
                        warnings.append(f"Slide {index}: text smaller than 10pt")
        print(f"Slide {index:02}: shapes={len(shapes)} images={len(images)} editable_text_shapes={len(text_shapes)}")
    print(f"Slides: {len(p.slides)}; canvas ratio: {ratio:.4f}")
    if warnings:
        for warning in warnings:
            print("WARNING:", warning)
        return 1
    print("PASS: basic structural checks")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_style.py <filename.pptx>")
        sys.exit(2)
    sys.exit(validate(Path(sys.argv[1])))
