import pdfplumber
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path


def load_pdf(file_path: str) -> str:
    """
    Load and extract text from a PDF.
    1️⃣ Try pdfplumber (fast, text-based PDFs)
    2️⃣ Fallback to OCR (for scanned/image-based PDFs like resumes)
    """

    text = ""

    pdf_path = Path(file_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    # -------- 1️⃣ Normal text extraction --------
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    # -------- 2️⃣ OCR fallback if text is too small --------
    if len(text.strip()) < 200:
        print("⚠️ Low text detected — running OCR fallback")

        images = convert_from_path(pdf_path)
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"

    print(f"✅ Final extracted text length: {len(text)}")

    return text
