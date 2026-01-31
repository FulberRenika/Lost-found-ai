from flask import Flask, request, jsonify
from flask_cors import CORS
from sentence_transformers import SentenceTransformer, util

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load AI model (lightweight, fast, accurate)
model = SentenceTransformer("all-MiniLM-L6-v2")

@app.route("/")
def home():
    return "Lost & Found AI Backend Running"

@app.route("/match", methods=["POST"])
def match_items():
    data = request.get_json()

    lost_text = data.get("lost", "")
    found_text = data.get("found", "")

    # Convert text to embeddings
    embeddings = model.encode(
        [lost_text, found_text],
        convert_to_tensor=True
    )

    # Calculate cosine similarity
    similarity_score = util.cos_sim(
        embeddings[0],
        embeddings[1]
    ).item()

    # Confidence level logic (judge-friendly)
    if similarity_score >= 0.85:
        confidence = "High confidence match"
    elif similarity_score >= 0.70:
        confidence = "Possible match"
    else:
        confidence = "Low confidence"

    return jsonify({
        "similarity": round(similarity_score, 2),
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(debug=True)
