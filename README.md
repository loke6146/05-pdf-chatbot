# 🤖 Chat With Your PDF

Try yourself: https://loke-pdf-chatbot.streamlit.app/

An AI-powered PDF chatbot built with **Streamlit + OpenRouter + DeepSeek**.

Upload any PDF, get an **AI-generated summary**, and **ask questions directly from the document**.

---

## 🚀 Features

✅ Upload PDF files
✅ Extract text from PDF
✅ AI-powered document summarization
✅ Ask questions about uploaded PDF
✅ Context-aware answers from document
✅ Clean Streamlit browser UI

---

## 🛠️ Tech Stack

* **Python 3.12**
* **Streamlit** (UI)
* **OpenRouter API**
* **DeepSeek Chat Model**
* **PyPDF2** (PDF text extraction)
* **python-dotenv** (.env support)

---

## 📌 How It Works

1. Upload a PDF file
2. Text is extracted using **PyPDF2**
3. AI summarizes the document
4. Ask questions based on the uploaded PDF
5. Get context-aware responses

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/loke6146/05-pdf-chatbot.git
```

Move into project folder:

```bash
cd 05-pdf-chatbot
```

Create virtual environment:

```bash
py -3.12 -m venv venv
```

Activate virtual environment:

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
OPENAI_API_KEY=your_openrouter_api_key
```

Run the app:

```bash
streamlit run app.py
```

---

## 📷 Demo

### Upload PDF

* Upload any PDF document

### Summarize PDF

* Get concise AI-generated summaries

### Ask Questions

Examples:

```text
What are the key concepts?
Explain softmax simply.
What skills are listed in this resume?
Summarize the important topics.
```

---

## 🔮 Future Improvements

* Chat memory for PDFs
* Better handling of formula-heavy documents
* OCR support for scanned PDFs
* Download summary feature
* Multiple summary styles

---

## 📚 Learning Outcome

This project helped me learn:

* File uploads in Streamlit
* PDF text extraction
* Prompt engineering
* LLM integration using APIs
* Context-aware document Q&A
* Building real AI applications

```
```

<img width="1902" height="902" alt="Screenshot 2026-06-14 215342" src="https://github.com/user-attachments/assets/03a4afda-1a66-4330-85b0-765f667f021f" />
<img width="1343" height="723" alt="Screenshot 2026-06-14 215552" src="https://github.com/user-attachments/assets/a4f9162c-9761-4f17-bae1-4295f643fac7" />
<img width="1042" height="758" alt="Screenshot 2026-06-14 215612" src="https://github.com/user-attachments/assets/c98923b9-edbc-417c-8c24-daa591d262e6" />
<img width="1445" height="627" alt="Screenshot 2026-06-14 215642" src="https://github.com/user-attachments/assets/882e7e8b-186b-49c3-a39e-1a055498fdc8" />

