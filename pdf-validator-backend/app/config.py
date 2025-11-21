
import os
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

class Settings:
    """Application configuration"""
    
    def __init__(self):
        # LLM Provider: 'openai' or 'lmstudio'
        self.llm_provider = os.getenv("LLM_PROVIDER", "lmstudio")  # Default to LM Studio
        
        # OpenAI Configuration (if using OpenAI)
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        
        # LM Studio Configuration (if using local LLM)
        self.lmstudio_base_url = os.getenv("LMSTUDIO_BASE_URL", "http://localhost:1234/v1")
        self.lmstudio_model = os.getenv("LMSTUDIO_MODEL", "local-model")
        
        # File Upload Configuration
        self.max_file_size_mb = int(os.getenv("MAX_FILE_SIZE_MB", "10"))
        self.allowed_extensions = [".pdf"]
        self.upload_dir = "uploads"
        
        # API Metadata
        self.api_title = "PDF Validator API"
        self.api_version = "1.0.0"
        self.api_description = "Validate PDF documents against custom rules using LLM"
        
        # CORS Configuration
        self.cors_origins = ["http://localhost:3000"]

@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
