'use client';

import React from 'react';

interface RulesInputProps {
  rules: string[];
  onChange: (rules: string[]) => void;
}

export const RulesInput: React.FC<RulesInputProps> = ({ rules, onChange }) => {
  const handleRuleChange = (index: number, value: string) => {
    const newRules = [...rules];
    newRules[index] = value;
    onChange(newRules);
  };

  const exampleRules = [
    "The document must have a purpose section.",
    "The document must mention at least one date.",
    "The document must define at least one term.",
  ];

  return (
    <div className="w-full space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-semibold text-gray-800">
          Validation Rules
        </h3>
        <span className="text-xs text-gray-500">Required: 3 rules</span>
      </div>

      {[0, 1, 2].map((index) => (
        <div key={index} className="space-y-1">
          <label
            htmlFor={`rule-${index}`}
            className="block text-sm font-medium text-gray-700"
          >
            Rule {index + 1}
          </label>
          <input
            id={`rule-${index}`}
            type="text"
            value={rules[index] || ''}
            onChange={(e) => handleRuleChange(index, e.target.value)}
            placeholder={exampleRules[index]}
            className="
              w-full px-4 py-2 border border-gray-300 rounded-lg
              focus:ring-2 focus:ring-blue-500 focus:border-transparent
              transition-all duration-200
              placeholder:text-gray-500 placeholder-opacity-100
            "
            required
          />
        </div>
      ))}

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-3 mt-4">
        <p className="text-xs text-blue-800 font-medium mb-1">
          💡 Example Rules:
        </p>
        <ul className="text-xs text-blue-700 space-y-1 ml-4 list-disc">
          {exampleRules.map((rule, i) => (
            <li key={i}>{rule}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};
