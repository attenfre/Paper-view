import os
import glob
try:
    import fitz  # PyMuPDF
    from PIL import Image
except ImportError:
    print("Please install PyMuPDF and Pillow")
    exit(1)

# Extract PDF
pdf_path = "public/pdfs/sn-article.pdf"
out_txt = "pdf_extracted.txt"

if os.path.exists(pdf_path):
    print(f"Extracting text from {pdf_path}...")
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Saved text to {out_txt}")
else:
    print(f"PDF not found: {pdf_path}")

# Convert TIFFs
figs_dir = "public/figs"
tiff_files = glob.glob(os.path.join(figs_dir, "*.tiff")) + glob.glob(os.path.join(figs_dir, "*.tif"))
for tiff in tiff_files:
    try:
        img = Image.open(tiff)
        out_path = os.path.splitext(tiff)[0] + ".webp"
        img.save(out_path, "WEBP", quality=85)
        print(f"Converted {tiff} to {out_path}")
    except Exception as e:
        print(f"Failed to convert {tiff}: {e}")
