# 🚀 Resume Shortlisting & Ranking Web App

An AI-powered web application that helps recruiters and hiring teams **automatically shortlist resumes** based on a given job description using **Natural Language Processing (NLP)** and semantic similarity.

Upload multiple resumes, provide a job description, and instantly get ranked candidates with **similarity scores** and **matching keywords**.

---

## ✨ Features

✅ Upload multiple resumes (`.pdf`, `.docx`, `.txt`)  
✅ Enter a custom job description  
✅ AI-powered resume ranking using NLP embeddings  
✅ Displays similarity scores for each candidate  
✅ Extracts and highlights matching keywords  
✅ Clean and responsive user interface  
✅ Fast and lightweight Flask backend  

---

## 🧠 How It Works

1. Recruiter uploads multiple resumes
2. User enters the job description
3. Resumes are converted into text
4. NLP embeddings are generated using Sentence Transformers
5. Cosine similarity is calculated between resumes and the job description
6. Resumes are ranked from most relevant to least relevant

---

## 🛠️ Tech Stack

### 🔹 Backend
- Python
- Flask

### 🔹 NLP & AI
- Sentence Transformers
- `all-MiniLM-L6-v2`
- Cosine Similarity

### 🔹 Frontend
- HTML
- CSS
- JavaScript

### 🔹 File Processing
- PyPDF2
- docx2txt

---

## 📂 Project Structure

```bash
Resume_shortlist/
│
├── backend/
│   ├── app.py
│   ├── matcher.py
│   └── ...
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── uploads/
│
├── venv/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd Resume_shortlist
```

---

### 2️⃣ Create Virtual Environment

#### 🔹 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🔹 macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 📌 Manual Installation (if needed)

```bash
pip install flask sentence-transformers docx2txt PyPDF2
```

---

## ▶️ Run the Application

```bash
python backend/app.py
```

The Flask server will start at:

```bash
http://127.0.0.1:5000/
```

Open it in your browser 🚀

---

## 📸 Application Workflow

### 📤 Upload Resumes
Upload multiple candidate resumes in supported formats.

### 📝 Enter Job Description
Provide the required skills, qualifications, and responsibilities.

### 🤖 AI Resume Matching
The system analyzes resumes using NLP embeddings.

### 📊 View Rankings
Get ranked resumes with:
- Similarity scores
- Matching keywords
- Relevance-based ordering

---

## 🧪 Example Use Cases

💼 HR Resume Screening  
🏢 Recruitment Automation  
🎓 Internship Candidate Filtering  
🚀 Startup Hiring Assistance  

---

## 🔥 Future Improvements

- Authentication System
- Resume Skill Visualization
- Export Results to CSV/PDF
- Advanced ATS Scoring
- Dashboard Analytics
- Multi-job comparison support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Monishraj**  
Information Technology Student

---

## ⭐ Support

If you found this project useful:

🌟 Star the repository  
🍴 Fork the project  
📢 Share it with others
