from flask import Flask, request, jsonify, render_template
from matcher import match_resumes

app = Flask(__name__)

# Serve the frontend
@app.route("/")
def home():
    return render_template("index.html")

# Endpoint for ranking resumes
@app.route("/rank", methods=["POST"])
def rank():
    job_description = request.form.get("job_description")
    resumes = request.files.getlist("resumes")

    if not job_description or job_description.strip() == "":
        return jsonify({"error": "Job description cannot be empty"}), 400

    if not resumes:
        return jsonify({"error": "No resumes uploaded"}), 400

    ranked = match_resumes(job_description, resumes)
    return jsonify(ranked)

if __name__ == "__main__":
    app.run(debug=True)
