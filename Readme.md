


# 📄 PDF Document Validator

An AI-powered PDF validation system that checks documents against custom rules using Large Language Models (LLMs). This project validates PDF documents by extracting text and analyzing them against user-defined compliance rules with evidence-based results.

---

## 🎯 Project Overview

This application allows users to:

- Upload PDF documents (2–10 pages)
- Define 3 custom validation rules
- Receive AI-powered validation results with evidence, reasoning, and confidence scores

Built as part of the **NIYAMR AI Full-Stack Developer Assignment**.


## 📸 Screenshots

### 🖥️ Application Interface
<p align="center">
  <img src="./screenshots/app-interface.png" alt="PDF Validator Interface" width="850">
</p>

### 📊 Validation Results
<p align="center">
  <img src="./screenshots/results-table.png" alt="Validation Results Table" width="850">
</p>




## ✨ Features

- **PDF Upload** — Supports documents up to 10MB  
- **Custom Rule Validation** — Define any 3 rules to validate against your PDF  
- **AI-Powered Analysis** — Works with OpenAI API or LM Studio  
- **Structured Results** — Pass/Fail, evidence, reasoning, confidence  
- **Local LLM Support** — Compatible with LM Studio  
- **Modern UI** — Built with Next.js + Tailwind CSS  

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
- Git
- OpenAI API Key **or** LM Studio

---

## 🚀 Installation & Setup

#️⃣ Backend Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd pdf-validator-backend
````

### 2. Create virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

**Example `.env`:**

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

### 5. Run backend server

```bash
uvicorn app.main:app --reload
```

API runs at → **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

#️⃣ Frontend Setup

### 1. Navigate to frontend

```bash
cd ../pdf-validator-frontend
```

### 2. Install dependencies

```bash
npm install
```

### 3. Configure environment variables

```bash
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
```

### 4. Start development server

```bash
npm run dev
```

The frontend runs at → **[http://localhost:3000](http://localhost:3000)**

---

## 🔧 Using LM Studio (Local LLM)

1. Download LM Studio
2. Download a recommended model (llama-3.2-3b, phi-3-mini, mistral-7b)
3. Load and run the model
4. Ensure server runs at `http://localhost:1234`
5. Set `LLM_PROVIDER=lmstudio` in `.env`

---

## 📖 Usage

1. Open the web app
2. Upload a PDF (2–10 pages)
3. Enter 3 validation rules
4. Click **Check Document**
5. View structured results with evidence + confidence

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

Validate PDF:

```bash
POST http://127.0.0.1:8000/api/validate
```

Swagger Docs → `http://127.0.0.1:8000/docs`
ReDoc → `http://127.0.0.1:8000/redoc`

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

* Uses PyMuPDF for accurate extraction
* Maps text with page numbers
* Handles multi-page documents efficiently

### LLM Integration

* Supports OpenAI API and LM Studio
* Deterministic low-temperature prompts
* Structured JSON output for reliability

### Error Handling

* Validates file type & size
* Clean error messages
* Auto cleanup of temporary files

---

## 📝 Assignment Requirements (Completed)

* PDF upload
* 3 rule inputs
* AI validation with evidence
* Pass/Fail
* Reasoning
* Confidence (0–100)
* Next.js + Tailwind
* FastAPI backend
* LLM integration
* Complete README

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch
3. Commit and push
4. Create a PR

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


* FastAPI
* OpenAI & LM Studio
* PyMuPDF



**Built in 48 hours as part of a full-stack developer assignment.**




