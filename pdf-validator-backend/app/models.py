from pydantic import BaseModel, Field
from typing import Literal

class ValidationRule(BaseModel):
    """Represents a single validation rule"""
    rule: str = Field(..., description="The rule to validate")

class ValidationRequest(BaseModel):
    """Request model for PDF validation"""
    rules: list[str] = Field(..., min_items=3, max_items=3)

class RuleResult(BaseModel):
    """Result for a single rule validation"""
    rule: str
    status: Literal["pass", "fail"]
    evidence: str
    reasoning: str
    confidence: int = Field(..., ge=0, le=100)

class ValidationResponse(BaseModel):
    """Complete validation response"""
    results: list[RuleResult]
    pdf_pages: int
    processing_time: float
