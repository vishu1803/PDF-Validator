
---

````markdown
# 📄 PDF Document Validator

An AI-powered PDF validation system that checks documents against custom rules using Large Language Models (LLMs). This project validates PDF documents by extracting text and analyzing them against user-defined compliance rules with evidence-based results.

---

## 🎯 Project Overview

This application allows users to:

- Upload PDF documents (2–10 pages)
- Define 3 custom validation rules
- Receive AI-powered validation results with evidence, reasoning, and confidence scores

Built as part of the **NIYAMR AI Full-Stack Developer Assignment**.

---

## 📸 Screenshots

### Application Interface
![PDF Validator Interface](screenshots/app-interface.png)
*Main interface showing PDF upload, rule inputs, and validation button.*

### Validation Results
![Validation Results](screenshots/results-table.png)
*Results table displaying pass/fail status, evidence, reasoning, and confidence scores.*

---

## ✨ Features

- **PDF Upload** — Supports documents up to 10MB  
- **Custom Rule Validation** — Define any 3 rules to validate against your PDF  
- **AI-Powered Analysis** — Uses OpenAI API or LM Studio  
- **Structured Results** — Pass/Fail, evidence, reasoning, and confidence  
- **Local LLM Support** — LM Studio compatible  
- **Modern UI** — Next.js + Tailwind CSS  

---

## 🛠️ Tech Stack

### Frontend
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- Axios

### Backend
- FastAPI
- PyMuPDF (fitz)
- OpenAI API / LM Studio
- Pydantic
- python-dotenv

---

## 📋 Prerequisites

- Node.js 18+
- Python 3.10+
- OpenAI API Key **or** LM Studio
- Git

---

## 🚀 Installation & Setup

#️⃣ Backend Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd pdf-validator-backend
````

2. **Create virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

```bash
cp .env.example .env
```

Example `.env`:

```env
LLM_PROVIDER=lmstudio

# LM Studio
LMSTUDIO_BASE_URL=http://localhost:1234/v1
LMSTUDIO_MODEL=local-model

# OpenAI
OPENAI_API_KEY=your-api-key-here

# App Settings
MAX_FILE_SIZE_MB=10
```

5. **Run backend server**

```bash
uvicorn app.main:app --reload
```

API runs at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

#️⃣ Frontend Setup

1. Navigate to frontend:

```bash
cd ../pdf-validator-frontend
```

2. Install dependencies:

```bash
npm install
```

3. Create environment file:

```bash
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
```

4. Run development server:

```bash
npm run dev
```

App runs at **[http://localhost:3000](http://localhost:3000)**

---

## 🔧 Using LM Studio (Local LLM)

1. Download LM Studio
2. Download a model (recommended: llama-3.2-3b-instruct, phi-3-mini, mistral-7b)
3. Load the model
4. Start the server ([http://localhost:1234](http://localhost:1234))
5. Set `LLM_PROVIDER=lmstudio` in `.env`

---

## 📖 Usage

1. Open the app → `http://localhost:3000`
2. Upload a PDF (2–10 pages)
3. Enter 3 custom rules
4. Click **Check Document**
5. View the structured results table

---

## 📁 Project Structure

```plaintext
pdf-validator/
├── pdf-validator-backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models.py
│   │   └── services/
│   │       ├── pdf_service.py
│   │       └── llm_service.py
│   ├── uploads/
│   ├── requirements.txt
│   └── README.md
│
└── pdf-validator-frontend/
    ├── app/
    │   ├── page.tsx
    │   └── layout.tsx
    ├── components/
    │   ├── PDFUploader.tsx
    │   ├── RulesInput.tsx
    │   └── ResultsTable.tsx
    ├── lib/
    │   └── api.ts
    ├── types/
    │   └── index.ts
    └── package.json
```

---

## 🧪 Testing

### Generate Test PDFs

```bash
cd pdf-validator-backend
python create_test_pdf.py
```

Creates:

* `test_document_pass.pdf`
* `test_document_fail.pdf`

### API Endpoints

Health Check:

```bash
GET http://127.0.0.1:8000/health
```

PDF Validation:

```bash
POST http://127.0.0.1:8000/api/validate
Content-Type: multipart/form-data
```

Swagger: `http://127.0.0.1:8000/docs`
ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🎨 Example Output

```json
{
  "results": [
    {
      "rule": "The document must have a purpose section.",
      "status": "pass",
      "evidence": "Found on page 1: 'The purpose of this project is to create...'",
      "reasoning": "Document contains a clearly labeled PURPOSE section",
      "confidence": 95
    }
  ],
  "pdf_pages": 3,
  "processing_time": 2.45
}
```

---

## 🔍 Key Implementation Details

### PDF Extraction

* PyMuPDF for fast, accurate extraction
* Page-aware text mapping
* Handles multi-page PDFs

### LLM Integration

* Works with both OpenAI and LM Studio
* Deterministic low-temperature prompts
* Structured JSON output

### Error Handling

* PDF validation (type, size)
* Detailed error messages
* Cleanup of temporary files

---

## 📝 Assignment Requirements (Completed)

* PDF upload
* 3 rule inputs
* Validation with evidence
* Reasoning
* Confidence score
* Next.js + Tailwind
* FastAPI backend
* LLM integration
* Clean UI
* Complete README

---

## 🤝 Contributing

1. Fork repo
2. Create feature branch
3. Commit and push
4. Open PR

---

## 📄 License

This project is created for educational purposes as part of a job assignment.

---

## 👤 Author

**Your Name**

* GitHub: `@yourusername`
* Email: `your.email@example.com`

---

## 🙏 Acknowledgments

* NIYAMR AI for the assignment
* FastAPI
* OpenAI & LM Studio
* PyMuPDF

---

**Built in 48 hours as part of a full-stack developer assignment.**

```

---


```
