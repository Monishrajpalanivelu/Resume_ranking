Resume Shortlisting & Ranking Web App

A web-based application to upload multiple resumes, provide a job description, and automatically rank resumes based on similarity using NLP embeddings.

Features

Upload multiple resumes (.pdf, .docx, .txt).

Provide a job description.

Rank resumes based on relevance to the job description.

Show matching keywords and similarity scores.

User-friendly web interface with upload form and results display.

Technologies Used

Backend: Python, Flask

NLP: Sentence Transformers (all-MiniLM-L6-v2)

Frontend: HTML, CSS, JavaScript


Installation (Local)
1. Clone the repository
git clone <https://github.com/Nitheeshfanus/Resume_ranking>
cd Resume_shortlist

2. Create and activate virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

3. Install required packages
pip install -r requirements.txt


Note: If you don’t have requirements.txt, you can install manually:

pip install flask sentence-transformers docx2txt PyPDF2

Run the Application Locally
# Make sure your virtual environment is activated
python backend/app.py


By default, Flask runs at: http://127.0.0.1:5000/

Open in your browser.
