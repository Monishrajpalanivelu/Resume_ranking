from sentence_model import model
from sentence_transformers import util
import PyPDF2
from PyPDF2 import PdfReader
from io import BytesIO
import re

def extract_text(file):
    if file.filename.endswith(".pdf"):
        file_stream = BytesIO(file.read())
        reader = PdfReader(file_stream)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip() if text else None
    else:
        return file.read().decode("utf-8", errors="ignore").strip()

# --- NEW FUNCTION: Scan resume for skills from a master list ---
def find_skills_in_resume(resume_text):
    """
    Scans the resume text to find which skills from a predefined
    master list are present.
    """
    # This is your master list of keywords. You can expand it with any
    # skills you want to track.
    master_skill_list = [
        'java', 'spring boot', 'react', 'react.js', 'javascript', 'sql', 'mysql',
        'postgresql', 'docker', 'git', 'rest api', 'microservices', 'python',
        'aws', 'azure', 'gcp', 'html', 'css', 'django', 'node.js', 'redis',
        'hibernate', 'maven', 'jenkins', 'postman', 'oop', 'dbms'
    ]

    found_skills = []
    # Loop through the master list to see which skills are in the resume
    for skill in master_skill_list:
        # re.search() looks for a match anywhere in the text.
        # r'\b' ensures we match whole words only (e.g., 'api' not 'captain').
        # re.IGNORECASE makes the search case-insensitive ('Java' and 'java' match).
        if re.search(r'\b' + re.escape(skill) + r'\b', resume_text, re.IGNORECASE):
            found_skills.append(skill)
            
    return found_skills

# --- UPDATED MAIN FUNCTION ---
def match_resumes(job_description, resumes, top_n_results=3):
    if not job_description or job_description.strip() == "":
        raise ValueError("Job description is empty or missing")

    jd_embedding = model.encode(job_description, convert_to_tensor=True)
    results = []

    for file in resumes:
        resume_text = extract_text(file)
        if not resume_text:
            print(f"Warning: File {file.filename} could not be read or is empty")
            continue

        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        score = util.cos_sim(jd_embedding, resume_embedding).item()

        # <-- UPDATED: Call our new function to get skills from the predefined list
        matching_keywords = find_skills_in_resume(resume_text)

        results.append({
            "filename": file.filename,
            "score": round(score, 4),
            "matching_keywords": matching_keywords
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_n_results]
