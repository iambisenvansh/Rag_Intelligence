import pdfplumber
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path


def load_pdf(file_path: str) -> str:
    """
    Load and extract text from a PDF.
    1. Try pdfplumber for normal PDFs.
    2. Use OCR page-by-page for scanned PDFs.
    """

    text = ""

    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    # -------- 1. Normal text extraction --------
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    # -------- 2. OCR fallback --------
    if len(text.strip()) < 200:
        print("⚠️ Low text detected — running OCR fallback")

        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)

        for page_number in range(1, total_pages + 1):

            images = convert_from_path(
                pdf_path,
                dpi=100,
                first_page=page_number,
                last_page=page_number,
                fmt="jpeg"
            )

            if images:
                text += pytesseract.image_to_string(images[0]) + "\n"
                images[0].close()

            del images

    print(f"✅ Final extracted text length: {len(text)}")

    return text