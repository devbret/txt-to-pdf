import logging
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")
FONT_NAME = "Helvetica"
FONT_SIZE = 12
LINE_HEIGHT = 15
MARGIN = 72
PAGE_WIDTH, PAGE_HEIGHT = LETTER
USABLE_WIDTH = PAGE_WIDTH - 2 * MARGIN


def break_long_word(word, max_width):
    pieces = []
    current = ""
    for char in word:
        if current and stringWidth(current + char, FONT_NAME, FONT_SIZE) > max_width:
            pieces.append(current)
            current = char
        else:
            current += char
    return pieces + [current]


def wrap_line(line):
    line = line.rstrip().expandtabs()
    stripped = line.lstrip(" ")
    if not stripped:
        return 0, [""]

    indent = line[: len(line) - len(stripped)]
    indent_width = min(stringWidth(indent, FONT_NAME, FONT_SIZE), USABLE_WIDTH / 2)
    available = USABLE_WIDTH - indent_width

    fragments = []
    for fragment in simpleSplit(stripped, FONT_NAME, FONT_SIZE, available):
        if stringWidth(fragment, FONT_NAME, FONT_SIZE) > available:
            fragments.extend(break_long_word(fragment, available))
        else:
            fragments.append(fragment)
    return indent_width, fragments


def convert_txt_to_pdf(txt_path, pdf_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    c = canvas.Canvas(str(pdf_path), pagesize=LETTER)
    c.setFont(FONT_NAME, FONT_SIZE)
    y_position = PAGE_HEIGHT - MARGIN

    for line in lines:
        indent_width, fragments = wrap_line(line)
        for fragment in fragments:
            if y_position < MARGIN:
                c.showPage()
                c.setFont(FONT_NAME, FONT_SIZE)
                y_position = PAGE_HEIGHT - MARGIN
            c.drawString(MARGIN + indent_width, y_position, fragment)
            y_position -= LINE_HEIGHT

    c.save()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("conversion.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    try:
        OUTPUT_DIR.mkdir(exist_ok=True)
        logging.info(f"Output directory ready: {OUTPUT_DIR}")
    except Exception as e:
        logging.error(f"Failed to create output directory: {e}")
        return 1

    try:
        txt_files = sorted(
            p for p in INPUT_DIR.iterdir()
            if p.is_file() and p.suffix.lower() == ".txt"
        )
    except FileNotFoundError:
        logging.critical(f"Input directory not found: {INPUT_DIR}")
        return 1

    if not txt_files:
        logging.warning(f"No .txt files found in {INPUT_DIR}")
        return 0

    converted = 0
    failed = 0
    for txt_path in txt_files:
        pdf_path = OUTPUT_DIR / txt_path.with_suffix(".pdf").name
        logging.info(f"Processing file: {txt_path.name}")
        try:
            convert_txt_to_pdf(txt_path, pdf_path)
        except Exception as e:
            logging.error(f"Failed to convert {txt_path.name}: {e}")
            failed += 1
            continue
        logging.info(f"Converted: {txt_path.name} → {pdf_path.name}")
        converted += 1

    if failed:
        logging.warning(f"Finished with errors: {converted} converted, {failed} failed")
        return 1

    logging.info(f"Finished: {converted} .txt file(s) converted to .pdf")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
