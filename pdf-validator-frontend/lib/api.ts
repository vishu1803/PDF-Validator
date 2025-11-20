import axios from 'axios';
import { ValidationResponse } from '@/types';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const validatePDF = async (
  file: File,
  rules: string[]
): Promise<ValidationResponse> => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('rule1', rules[0]);
  formData.append('rule2', rules[1]);
  formData.append('rule3', rules[2]);

  try {
    const response = await axios.post<ValidationResponse>(
      `${API_BASE_URL}/api/validate`,
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }
    );

    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.detail || 'Validation failed');
    }
    throw error;
  }
};
