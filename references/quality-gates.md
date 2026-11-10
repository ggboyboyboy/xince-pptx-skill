# Quality Gates

## Hard requirements
- 16:9 widescreen; no accidental cropping, overlaps, or out-of-bounds text.
- Editable title, labels, shapes, charts and tables; never flatten entire slide into one image.
- Exact eight canonical colors from `assets/design-tokens.json`.
- No fabricated clients, proof, patents, experimental results, financial numbers, or product capabilities.
- Every chart: label the units, period, key comparison conditions and sources.
- Body text preferably 16pt or larger; dense labels 13–14pt minimum; footnotes ~10–11pt minimum.
- Readable contrast on projection; cyan, gold, red and green have clear semantic functions.
- Consistent navigation, cards, headings, margins, and final takeaways across the deck.
- No embedded proprietary fonts or unlicensed original-deck page images.

## Three-second test
A person looking at any slide for three seconds should know:
1. Its main argument.
2. Which single chart, photo, or metric proves it.
3. The conclusion to remember.

If any answer is unclear, remove information blocks; do not add glowing elements.

## Validation
1. Run `python scripts/check_palette.py`.
2. Generate the editable sample using `python scripts/build_starter.py`.
3. Run `python scripts/validate_style.py assets/editable-starter.pptx`.
4. Render to images and manually verify readability, alignment, chart labels, object placement and photo cropping.
5. Check at 1920×1080 projected presentation size.

The script only performs structural checks. It cannot determine whether a diagram is factually true, visually elegant, or free from every overlap.
