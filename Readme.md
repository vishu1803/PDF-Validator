
```markdown
# PDF Document Validator 📄✅

An AI-powered PDF validation system that checks documents against custom rules using Large Language Models (LLMs). This project validates PDF documents by extracting text and analyzing them against user-defined compliance rules with evidence-based results.

## 🎯 Project Overview

This application allows users to:
- Upload PDF documents (2-10 pages)
- Define 3 custom validation rules
- Receive AI-powered validation results with evidence, reasoning, and confidence scores

Built as part of the NIYAMR AI Full-Stack Developer Assignment.
## 📸 Screenshots

### Application Interface
![PDF Validator Interface](screenshots/app-interface.png)
*Main interface showing PDF upload, rule inputs, and validation button*

### Validation Results
![Validation Results](screenshots/results-table.png)
*Results table displaying pass/fail status, evidence, reasoning, and confidence scores*

## ✨ Features

- **PDF Upload**: Support for PDF documents up to 10MB
- **Custom Rule Validation**: Define any 3 rules to check against your document
- **AI-Powered Analysis**: Uses LLM to intelligently validate documents
- **Structured Results**: Returns pass/fail status with evidence quotes and confidence scores
- **Local LLM Support**: Works with both OpenAI API and local LLM (LM Studio)
- **Clean UI**: Responsive interface built with Next.js and Tailwind CSS

## 🛠️ Tech Stack

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API calls

### Backend
- **FastAPI** - Modern Python web framework
- **PyMuPDF (fitz)** - Fast PDF text extraction
- **OpenAI API / LM Studio** - LLM for document validation
- **Pydantic** - Data validation
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.10+
- **OpenAI API Key** OR **LM Studio** for local LLM
- Git

## 🚀 Installation & Setup

### Backend Setup

1. **Clone the repository**
```

git clone <your-repo-url>
cd pdf-validator-backend

```

2. **Create virtual environment**
```

python -m venv venv

# On Windows:

venv\Scripts\activate

# On macOS/Linux:

source venv/bin/activate

```

3. **Install dependencies**
```

pip install -r requirements.txt

```

4. **Configure environment variables**
```


# Copy example env file

cp .env.example .env

# Edit .env and add your configuration

```

Example `.env` file:
```


# Choose LLM provider: 'openai' or 'lmstudio'

LLM_PROVIDER=lmstudio

# LM Studio Configuration (if using local LLM)

LMSTUDIO_BASE_URL=http://localhost:1234/v1
LMSTUDIO_MODEL=local-model

# OpenAI Configuration (if using OpenAI)

OPENAI_API_KEY=your-api-key-here

# Application Settings

MAX_FILE_SIZE_MB=10

```

5. **Run the backend server**
```

uvicorn app.main:app --reload

```

The API will be available at `http://127.0.0.1:8000`

### Frontend Setup

1. **Navigate to frontend directory**
```

cd ../pdf-validator-frontend

```

2. **Install dependencies**
```

npm install

```

3. **Configure environment variables**
```


# Create .env.local file

echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

```

4. **Run the development server**
```

npm run dev

```

The application will be available at `http://localhost:3000`

## 🔧 Using LM Studio (Local LLM)

If you want to use a local LLM instead of OpenAI:

1. **Download LM Studio** from https://lmstudio.ai/download
2. **Download a model** (recommended: llama-3.2-3b-instruct or phi-3-mini)
3. **Load the model** in LM Studio
4. **Start the local server** (default: http://localhost:1234)
5. **Set `LLM_PROVIDER=lmstudio`** in your `.env` file

### Recommended Models
- `llama-3.2-3b-instruct` - Fast, good for structured output (~2GB)
- `phi-3-mini-4k-instruct` - Efficient, Microsoft model (~2.3GB)
- `mistral-7b-instruct-v0.3` - Better accuracy (~4.1GB)

## 📖 Usage

1. **Access the application** at `http://localhost:3000`

2. **Upload a PDF document** (2-10 pages)

3. **Enter 3 validation rules**, for example:
   - "The document must have a purpose section."
   - "The document must mention at least one date."
   - "The document must define at least one term."

4. **Click "Check Document"**

5. **View results** in the table with:
   - Rule text
   - Pass/Fail status
   - Evidence from the document
   - Reasoning
   - Confidence score (0-100)

## 📁 Project Structure

```

pdf-validator/
├── pdf-validator-backend/
│   ├── app/
│   │   ├── main.py              \# FastAPI application
│   │   ├── config.py            \# Configuration management
│   │   ├── models.py            \# Pydantic models
│   │   └── services/
│   │       ├── pdf_service.py   \# PDF text extraction
│   │       └── llm_service.py   \# LLM validation logic
│   ├── uploads/                 \# Temporary PDF storage
│   ├── requirements.txt         \# Python dependencies
│   ├── .env                     \# Environment variables
│   └── README.md
│
└── pdf-validator-frontend/
├── app/
│   ├── page.tsx             \# Main application page
│   └── layout.tsx
├── components/
│   ├── PDFUploader.tsx      \# File upload component
│   ├── RulesInput.tsx       \# Rules input form
│   └── ResultsTable.tsx     \# Results display
├── lib/
│   └── api.ts               \# API client functions
├── types/
│   └── index.ts             \# TypeScript types
└── package.json

```

## 🧪 Testing

### Create Test PDFs
A script is provided to generate sample PDFs for testing:

```

cd pdf-validator-backend
python create_test_pdf.py

```

This creates:
- `test_document_pass.pdf` - Contains all required elements
- `test_document_fail.pdf` - Missing key elements

### API Endpoints

**Health Check:**
```

GET http://127.0.0.1:8000/health

```

**Validate PDF:**
```

POST http://127.0.0.1:8000/api/validate
Content-Type: multipart/form-data

file: <PDF file>
rule1: "The document must have a purpose section."
rule2: "The document must mention at least one date."
rule3: "The document must define at least one term."

```

**API Documentation:**
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🎨 Example Output

```

{
"results": [
{
"rule": "The document must have a purpose section.",
"status": "pass",
"evidence": "Found in page 1: 'The purpose of this project is to create...'",
"reasoning": "Document contains a clearly labeled PURPOSE section",
"confidence": 95
}
],
"pdf_pages": 3,
"processing_time": 2.45
}

```

## 🔍 Key Implementation Details

### PDF Text Extraction
- Uses **PyMuPDF** for fast and accurate text extraction
- Preserves page numbers for evidence citations
- Handles multi-page PDFs efficiently

### LLM Integration
- Supports both **OpenAI API** and **local LLMs** via LM Studio
- Uses structured prompts for consistent JSON output
- Low temperature (0.2) for deterministic results
- Extracts evidence with page references

### Error Handling
- Validates file types (PDF only)
- Checks file size limits
- Graceful error messages for users
- Automatic cleanup of temporary files

## 📝 Assignment Requirements

This project fulfills all requirements from the NIYAMR AI assignment:

✅ Upload PDF button  
✅ 3 text inputs for validation rules  
✅ "Check Document" button  
✅ Results table with pass/fail status  
✅ Evidence sentences from document  
✅ Reasoning for each validation  
✅ Confidence scores (0-100)  
✅ Frontend: Next.js + Tailwind CSS  
✅ Backend: FastAPI + Python  
✅ PDF text extraction  
✅ LLM integration  
✅ GitHub repository  
✅ README with instructions  

## 🤝 Contributing

This is an assignment project, but suggestions are welcome:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is created for educational purposes as part of a job assignment.

## 👤 Author

**[Your Name]**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- NIYAMR AI for the assignment opportunity
- FastAPI framework for excellent documentation
- OpenAI and LM Studio for LLM capabilities
- PyMuPDF for reliable PDF processing

---

**Note**: This project was built in 48 hours as part of a full-stack developer assignment. It demonstrates proficiency in modern web development, API design, AI integration, and document processing.
```
