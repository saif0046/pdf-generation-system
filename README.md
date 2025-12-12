
# Automated PDF Generation System (100 PDFs Daily)
### Using Local HTML Template Exported from Google Docs

---

## Overview

This project automates the daily generation of **100 unique PDF documents** using an **HTML template exported from Google Docs**.  
The template includes placeholders like:

```
{{name}}, {{email}}, {{date}}, {{id}}, {{notes}}
```

Each PDF is filled with randomized values, converted into a PDF, and saved into a structured folder.

Automation is handled via **Windows Task Scheduler**, enabling hands‑free, daily execution.

---

## Features

- Generates **100 unique PDFs** per run  
- Dynamically fills placeholders with random data  
- Converts HTML template → PDF  
- Stores output in structured format  
- Fully automated using **Task Scheduler**  
- Clean OOP architecture  

---

## Project Requirements Fulfilled

### 1. Template Processing
- Google Docs was used to design the original layout.
- The Google Doc was exported as **template.html**.
- PDF generation now uses a **local HTML template** for maximum stability.

### 2. Generating 100 Unique PDFs
- Script runs in a loop for the configured number of files.
- Each file receives unique random data.
- Files saved as:

```
output_pdfs/document_001.pdf
output_pdfs/document_002.pdf
...
```

### 3. Automation with Task Scheduler
- A `.bat` file executes the Python script.
- Task Scheduler triggers it daily.
- Runs silently without user involvement.

---

##  Why We Do NOT Use Google Docs API for Editing

Google Docs API has a strict limit:

### **Max 60 write operations per minute**

Generating 100 PDFs with 5–10 placeholders results in:

- 500+ write requests
- Frequent failures like:

```
429 RATE_LIMIT_EXCEEDED
QuotaExceeded: WriteRequestsPerMinutePerUser
```

### Final decision:
Use a **local HTML template** → Zero API limits, very fast, fully reliable.

---

## Benefits of Local HTML Template Approach

| Google API Problems | Local HTML Solution |
|---------------------|---------------------|
| 60 writes/min limit | No limits |
| 429 quota errors | Zero failures |
| Requires authentication | No authentication |
| Slow network speed | Instant local processing |
| Template restoration needed | No restoration required |
| Hard to scale | Highly scalable |

---

# Project Structure

```
innobot-automation/
│
├── main.py                     # Application entry point
├── config.json                 # Settings & placeholder rules
├── template.html               # HTML template with placeholders
├── generate_pdfs.bat           # Script for scheduled execution
├── output_pdfs/                # Auto-generated PDFs
│
└── src/
    ├── core/
    │   ├── orchestrator.py         # Main workflow controller
    │   ├── template_processor.py   # Template loader + PDF exporter
    │   ├── random_generator.py     # Random value generation
    │
    ├── infrastructure/
    │   ├── storage.py              # Directory utilities
    │
    └── utils/
        ├── logger.py               # Logging configuration
```

---

# How It Works

### **1️. Load the HTML Template**
Contains placeholders:

```
Name: {{name}}
Email: {{email}}
Date: {{date}}
ID Number: {{id}}
Notes: {{notes}}
```

### **2️. Generate Random Values**
RandomDataGenerator creates:
- Names  
- Emails  
- Dates  
- Numeric IDs  
- Notes sentences  

### **3️. Replace Placeholders**
Each placeholder is replaced with dynamic content.

### **4️. Convert HTML → PDF**
`xhtml2pdf` handles rendering.

### **5️. Save file into output_pdfs/**
Repeat for 100 files.

---

# Setup Instructions

## **1. Create Virtual Environment**

```
python -m venv .venv
```

### Windows:
```
.venv\Scriptsctivate
```

### Mac/Linux:
```
source .venv/bin/activate
```

---

## **2. Install Dependencies**

```
pip install -r requirements.txt
```

---

## **3. Run Script Manually**

```
python main.py
```

---

# Automating with Task Scheduler

## **Step 1 — Create generate_pdfs.bat (Pass the venv your python.exe path and main.py file path)**

```
F:\Python_Saif\innobot-automation\.venv\Scripts\python.exe F:\Python_Saif\innobot-automation\main.py
```

---

## **Step 2 — Create Scheduled Task**

1. Open **Task Scheduler**
2. Select **Create Basic Task**
3. Task Name: *Daily PDF Generator*
4. Trigger: **Daily**
5. Action: **Start a Program**
6. Program/script:

```
Pass generate_pdfs.bat after copy your path locally this is my system path.

F:\Python_Saif\innobot-automation\generate_pdfs.bat
```

7. Start in:

```
Pass root folder path

F:\Python_Saif\innobot-automation
```

8. Select: Run whether user is logged on or not and Run with highest privileges 

9. Enter your Windows password  
10. Finish

---

## **Step 3 — Validate Automation**

- Right-click → **Run**  
- Check "Last Run Result" → **0x0 (Success)**  
- Verify new PDFs appear in `output_pdfs/`

---

# Final Outcome

We now have:

- 100 PDFs generated daily  
-  Fully automated system  
-  No Google API quota issues  
-  Clean OOP architecture  
-  Professional and reliable workflow  

---

