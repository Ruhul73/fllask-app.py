from flask import Flask, request, render_template
from transformers import pipeline
import os

app = Flask(__name__)

# Load model from Hugging Face
generator = pipeline("text-generation", model="gpt2")

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if prompt:
            response = generator(prompt, max_length=100, num_return_sequences=1)
            result = response[0]['generated_text']
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
