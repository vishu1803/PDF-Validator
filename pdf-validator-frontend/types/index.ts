export interface RuleResult {
  rule: string;
  status: 'pass' | 'fail';
  evidence: string;
  reasoning: string;
  confidence: number;
}

export interface ValidationResponse {
  results: RuleResult[];
  pdf_pages: number;
  processing_time: number;
}

export interface ValidationRequest {
  file: File;
  rules: string[];
}
