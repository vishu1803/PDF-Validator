'use client';

import React, { useState } from 'react';
import { PDFUploader } from '@/components/PDFUploader';
import { RulesInput } from '@/components/RulesInput';
import { ResultsTable } from '@/components/ResultsTable';
import { validatePDF } from '@/lib/api';
import { ValidationResponse } from '@/types';

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [rules, setRules] = useState<string[]>(['', '', '']);
  const [results, setResults] = useState<ValidationResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleValidate = async () => {
    // Validation
    if (!file) {
      setError('Please upload a PDF file');
      return;
    }

    if (rules.some(rule => !rule.trim())) {
      setError('Please fill in all 3 validation rules');
      return;
    }

    setLoading(true);
    setError(null);
    setResults(null);

    try {
      const response = await validatePDF(file, rules);
      setResults(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Validation failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4">
      <div className="max-w-6xl mx-auto space-y-8">
        {/* Header */}
        <div className="text-center">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            PDF Document Validator
          </h1>
          <p className="text-gray-600">
            Upload a PDF and define rules to validate document compliance
          </p>
        </div>

        {/* Main Card */}
        <div className="bg-white rounded-2xl shadow-xl p-8 space-y-6">
          {/* Step 1: Upload PDF */}
          <div>
            <h2 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-3">
              Step 1: Upload Document
            </h2>
            <PDFUploader onFileSelect={setFile} />
          </div>

          {/* Step 2: Enter Rules */}
          <div>
            <h2 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-3">
              Step 2: Define Validation Rules
            </h2>
            <RulesInput rules={rules} onChange={setRules} />
          </div>

          {/* Validate Button */}
          <button
            onClick={handleValidate}
            disabled={loading}
            className="
              w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold
              py-3 px-6 rounded-lg transition-colors duration-200
              disabled:bg-gray-400 disabled:cursor-not-allowed
              focus:ring-4 focus:ring-blue-300
            "
          >
            {loading ? (
              <span className="flex items-center justify-center gap-2">
                <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                    fill="none"
                  />
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                  />
                </svg>
                Validating Document...
              </span>
            ) : (
              'Check Document'
            )}
          </button>

          {/* Error Display */}
          {error && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4">
              <p className="text-sm text-red-800">❌ {error}</p>
            </div>
          )}
        </div>

        {/* Results */}
        {results && (
          <div className="bg-white rounded-2xl shadow-xl p-8">
            <ResultsTable data={results} />
          </div>
        )}
      </div>
    </main>
  );
}
