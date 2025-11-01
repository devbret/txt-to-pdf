import os
import logging
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("conversion.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

input_dir = "input"
output_dir = "output"

try:
    os.makedirs(output_dir, exist_ok=True)
    logging.info(f"Output directory ready: {output_dir}")
except Exception as e:
    logging.error(f"Failed to create output directory: {e}")
    raise

try:
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            txt_path = os.path.join(input_dir, filename)
            pdf_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".pdf")
            
            logging.info(f"Processing file: {filename}")
            
            try:
                with open(txt_path, "r", encoding="utf-8") as f:
                    content = f.readlines()
            except Exception as e:
                logging.error(f"Failed to read {txt_path}: {e}")
                continue
            
            try:
                c = canvas.Canvas(pdf_path, pagesize=LETTER)
                width, height = LETTER
                y_position = height - 72
                
                for line in content:
                    c.drawString(72, y_position, line.strip())
                    y_position -= 15
                    if y_position < 72:
                        c.showPage()
                        y_position = height - 72
                
                c.save()
                logging.info(f"Converted: {filename} → {os.path.basename(pdf_path)}")
            except Exception as e:
                logging.error(f"Failed to convert {filename} to PDF: {e}")
except FileNotFoundError:
    logging.critical(f"Input directory not found: {input_dir}")
except Exception as e:
    logging.critical(f"Unexpected error: {e}")

logging.info("All .txt files converted to .pdf")
