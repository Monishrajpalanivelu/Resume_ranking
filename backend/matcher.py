from sentence_model import model
from sentence_transformers import util

import docx2txt, PyPDF2

from PyPDF2 import PdfReader
from io import BytesIO

def extract_text(file):
    if file.filename.endswith(".pdf"):
        # read PDF from the in-memory file object
        file_stream = BytesIO(file.read())  # convert uploaded file to a BytesIO stream
        reader = PdfReader(file_stream)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip() if text else None
    else:
        # handle txt / docx files
        return file.read().decode("utf-8", errors="ignore").strip()
from sentence_transformers import util

from sentence_transformers import util
import re

def extract_keywords(text, top_n=10):
    """
    Extract the top N keywords from a text.
    Simple approach: take unique words longer than 3 letters.
    """
    words = re.findall(r'\b\w{6,}\b', text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_words[:top_n]]

def match_resumes(job_description, resumes, top_n_results=3):
    if not job_description or job_description.strip() == "":
        raise ValueError("Job description is empty or missing")

    print("Job Description:", job_description[:100])  # debug first 100 chars

    # Encode job description
    jd_embedding = model.encode(job_description, convert_to_tensor=True)
    jd_keywords = extract_keywords(job_description, top_n=100)
    results = []

    for file in resumes:
        resume_text = extract_text(file)
        if not resume_text:
            print(f"Warning: File {file.filename} could not be read or is empty")
            continue

        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        score = util.cos_sim(jd_embedding, resume_embedding).item()

        # Extract keywords from resume that also appear in JD
        resume_keywords = extract_keywords(resume_text, top_n=20)
        matching_keywords = list(set(jd_keywords) & set(resume_keywords))

        results.append({
            "filename": file.filename,
            "score": round(score, 3),
            "matching_keywords": matching_keywords
        })

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    # Return only top N results
    return results[:top_n_results]


