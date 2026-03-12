from flask import Flask, render_template, request, jsonify
import json
from transformers import pipeline

app = Flask(__name__)

# Load AI model (no API key needed)
generator = pipeline("text2text-generation", model="google/flan-t5-base")

DATA_FILE = "patients.json"


def load_patients():
    with open(DATA_FILE) as f:
        return json.load(f)


def save_patients(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.route("/")
def index():
    data = load_patients()
    return render_template("index.html", patients=data["patients"])


@app.route("/patient/<pid>")
def get_patient(pid):
    data = load_patients()

    for p in data["patients"]:
        if p["id"] == pid:
            return jsonify(p)

    return jsonify({"error": "Patient not found"})


@app.route("/ask_ai", methods=["POST"])
def ask_ai():

    question = request.json["question"]
    patient = request.json["patient"]

    prompt = f"""
    Patient Details:
    Name: {patient['name']}
    Age: {patient['age']}
    Condition: {patient['condition']}
    Medication: {patient['medication']}

    Question: {question}

    Give answer in 3 steps.
    """

    result = generator(prompt, max_length=120)

    return jsonify({"response": result[0]["generated_text"]})


@app.route("/update_condition", methods=["POST"])
def update_condition():

    pid = request.json["id"]
    condition = request.json["condition"]

    data = load_patients()

    for p in data["patients"]:
        if p["id"] == pid:
            p["condition"] = condition

    save_patients(data)

    return jsonify({"status": "updated"})


if __name__ == "__main__":
    app.run(debug=True)
