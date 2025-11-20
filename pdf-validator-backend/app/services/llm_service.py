# app/services/llm_service.py
from openai import OpenAI
import json
from typing import List
from app.models import RuleResult

class LLMService:
    """Service for LLM-based document validation - supports OpenAI and local LLMs"""
    
    def __init__(self, api_key: str = "lm-studio", base_url: str = None, model: str = None):
        """
        Initialize LLM service
        
        Args:
            api_key: OpenAI API key or 'lm-studio' for local
            base_url: API base URL (for LM Studio: http://localhost:1234/v1)
            model: Model name to use
        """
        if base_url:
            # Use local LM Studio or other OpenAI-compatible API
            self.client = OpenAI(
                api_key=api_key,  # LM Studio doesn't validate this
                base_url=base_url
            )
            self.is_local = True
            # For LM Studio, model name comes from loaded model
            self.model = model or "local-model"
        else:
            # Use OpenAI
            self.client = OpenAI(api_key=api_key)
            self.is_local = False
            self.model = model or "gpt-4o-mini"
    
    def validate_document(self, document_text: str, rules: List[str]) -> List[RuleResult]:
        """
        Validate document against rules using LLM
        
        Args:
            document_text: Extracted PDF text
            rules: List of validation rules
            
        Returns:
            List of RuleResult objects
        """
        
        # Construct the prompt
        prompt = self._build_validation_prompt(document_text, rules)
        
        try:
            # Call LLM API (works with both OpenAI and LM Studio)
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a document compliance expert. Analyze documents against rules and provide structured validation results."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,
                # Note: LM Studio may not support response_format, so we handle both
                **({"response_format": {"type": "json_object"}} if not self.is_local else {})
            )
            
            # Parse the response
            content = response.choices[0].message.content
            
            # Try to extract JSON if wrapped in markdown code blocks
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content: # Fallback for other markdown code blocks
                content = content.split("```")[1].strip()
            
            result_data = json.loads(content)
            
            # Convert to Pydantic models
            results = [RuleResult(**item) for item in result_data["results"]]
            
            return results
            
        except Exception as e:
            raise ValueError(f"LLM validation error: {str(e)}")
    
    def _build_validation_prompt(self, document_text: str, rules: List[str]) -> str:
        """Build the validation prompt for the LLM"""
        
        rules_formatted = "\n".join([f"{i+1}. {rule}" for i, rule in enumerate(rules)])
        
        prompt = f"""
You are validating a document against specific rules. For each rule, determine if the document PASSES or FAILS.

DOCUMENT TEXT:
{document_text}

RULES TO VALIDATE:
{rules_formatted}

For each rule, provide:
1. status: "pass" or "fail"
2. evidence: One specific sentence or phrase from the document (include page number if found in "--- Page X ---" markers)
3. reasoning: Brief explanation of why it passes or fails
4. confidence: Score from 0-100 indicating your certainty

IMPORTANT: Return your response as valid JSON in this exact format (no markdown, just pure JSON):
{{
  "results": [
    {{
      "rule": "exact rule text here",
      "status": "pass",
      "evidence": "Found in page 2: 'specific quote from document'",
      "reasoning": "Brief explanation",
      "confidence": 85
    }}
  ]
}}

Be precise and quote directly from the document for evidence.
"""
        return prompt