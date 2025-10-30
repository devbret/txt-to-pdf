import os
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

input_dir = "input"
output_dir = "output"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        txt_path = os.path.join(input_dir, filename)
        pdf_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".pdf")
        
        with open(txt_path, "r", encoding="utf-8") as f:
            content = f.readlines()
        
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
        print(f"Converted: {filename} → {os.path.basename(pdf_path)}")

print("All .txt files converted to .pdf")
