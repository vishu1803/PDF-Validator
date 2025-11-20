# app/main.py
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import time
import shutil
from pathlib import Path

from app.config import get_settings
from app.models import ValidationResponse
from app.services.pdf_service import PDFService
from app.services.llm_service import LLMService

# Load configuration
settings = get_settings()

# Initialize FastAPI
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description=settings.api_description
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM service based on provider
if settings.llm_provider == "lmstudio":
    print("🚀 Using LM Studio (Local LLM)")
    llm_service = LLMService(
        api_key="lm-studio",  # Not validated by LM Studio
        base_url=settings.lmstudio_base_url,
        model=settings.lmstudio_model
    )
else:
    print("🌐 Using OpenAI API")
    llm_service = LLMService(
        api_key=settings.openai_api_key,
        model="gpt-4o-mini"
    )

pdf_service = PDFService()

# Create uploads directory
UPLOAD_DIR = Path(settings.upload_dir)
UPLOAD_DIR.mkdir(exist_ok=True)

# ... rest of your endpoints (same as before)
@app.post("/api/validate", response_model=ValidationResponse)
async def validate_pdf(
    file: UploadFile = File(..., description="PDF file to validate"),
    rule1: str = Form(..., description="First validation rule"),
    rule2: str = Form(..., description="Second validation rule"),
    rule3: str = Form(..., description="Third validation rule")
):
    """Validate a PDF document against three custom rules using LLM"""
    start_time = time.time()
    
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    temp_file_path = UPLOAD_DIR / f"temp_{int(time.time())}_{file.filename}"
    
    try:
        with temp_file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        pdf_data = pdf_service.extract_text_from_pdf(str(temp_file_path))
        
        rules = [rule1, rule2, rule3]
        validation_results = llm_service.validate_document(
            document_text=pdf_data["text"],
            rules=rules
        )
        
        return ValidationResponse(
            results=validation_results,
            pdf_pages=pdf_data["pages"],
            processing_time=round(time.time() - start_time, 2)
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        if temp_file_path.exists():
            temp_file_path.unlink()

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": settings.api_title,
        "llm_provider": settings.llm_provider
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "PDF Validator API",
        "llm_provider": settings.llm_provider,
        "docs": "/docs"
    }
