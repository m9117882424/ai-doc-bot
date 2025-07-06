# AI Document Processing Telegram Bot 🤖📄

A powerful Telegram bot built with Python that automates document handling:
- 🧾 Extracts text from scanned PDFs or images using OCR (Tesseract)
- 🧠 Identifies document type (invoice, bill, contract, etc.) using GPT
- 📊 Parses key fields (date, ID, total, etc.) into structured format
- 📥 Supports multiple file uploads per session
- 📤 Exports results to Excel (CSV or Google Sheets-ready)

## 🛠 Tech Stack
- Python 3.11+
- aiogram (Telegram bot)
- Tesseract OCR
- GPT (OpenAI API or DeepSeek)
- Pandas + OpenPyXL
- FastAPI / Flask (optional API backend)

## ✅ Features
- Auto-classify document type
- Multi-language OCR (English, Turkish, Russian)
- Export to Excel
- Stateless or session-based processing
- Works with Telegram polling or webhook mode

## 📦 Example Use Cases
- Logistics and shipping waybills
- Utility bills and receipts
- Contracts and reports
- Field data digitization

## 🚀 Demo
Ask the bot to:
1. Upload 1 or more scanned files
2. Type `/finish` to receive structured results in Excel
3. Optionally: deploy to your server with webhook support

## 📁 Repo Structure
```
ai_doc_bot/
├── bot.py                  # Entry point
├── handlers/               # Telegram logic
├── prompts/                # GPT templates
├── ocr_utils.py            # OCR logic
├── gpt_parser.py           # AI parsing
├── document_types.py       # Type → prompt map
└── requirements.txt
```

## 🧑‍💻 Author
Built by a Python developer specializing in automation, AI, and Telegram bot solutions.

Feel free to fork, clone, or contact me for freelance work.
