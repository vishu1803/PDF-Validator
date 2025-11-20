import fitz  # PyMuPDF
from pathlib import Path

class PDFService:
    """Service for PDF text extraction"""
    
    @staticmethod
    def extract_text_from_pdf(pdf_path: str) -> dict:
        """
        Extract text from PDF with page-level detail
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            dict with 'text', 'pages', and 'page_contents'
        """
        try:
            doc = fitz.open(pdf_path)
            
            # Extract text from all pages
            full_text = ""
            page_contents = []
            
            for page_num, page in enumerate(doc, start=1):
                page_text = page.get_text()
                full_text += f"\n--- Page {page_num} ---\n{page_text}"
                page_contents.append({
                    "page_number": page_num,
                    "text": page_text
                })
            
            doc.close()
            
            return {
                "text": full_text,
                "pages": len(page_contents),
                "page_contents": page_contents
            }
            
        except Exception as e:
            raise ValueError(f"Error extracting text from PDF: {str(e)}")
