import os
import fitz
from app.config import UPLOAD_DIR

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        print(f"failed to read {pdf_path}: {e}")
    return text

def load_all_documents() -> list:
    documents = []
    for filename in os.listdir(UPLOAD_DIR):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(UPLOAD_DIR, filename)
            content = extract_text_from_pdf(file_path)
            if content.strip():
                documents.append({
                    "filename": filename,
                    "content": content
                })
    return documents