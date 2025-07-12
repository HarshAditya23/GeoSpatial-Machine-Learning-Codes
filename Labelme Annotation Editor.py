import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def json_to_pdf(json_file, pdf_file):
    # Load JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create a canvas for PDF
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    y = height - 50  # start from top

    # Write content
    c.setFont("Helvetica", 12)
    c.drawString(50, y, "JSON to PDF Output")
    y -= 30

    def write_dict(d, indent=0):
        nonlocal y
        for key, value in d.items():
            line = " " * (indent * 4) + f"{key}: {value if not isinstance(value, dict) else ''}"
            if y < 50:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 12)
            c.drawString(50, y, line)
            y -= 20
            if isinstance(value, dict):
                write_dict(value, indent + 1)

    if isinstance(data, dict):
        write_dict(data)
    else:
        c.drawString(50, y, str(data))

    # Save PDF
    c.save()
    print(f"PDF saved as {pdf_file}")

# Example usage
json_to_pdf("dataset2.json", "output.pdf")
