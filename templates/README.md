# 💡 AI Text Generator

This project is a simple web application that generates text using a Hugging Face transformer model. It allows users to input a prompt and receive an AI-generated text response. The backend is built with Flask, and the frontend uses HTML and CSS for a clean, responsive interface.

---

## 🚀 Project Features

- ✅ Text generation using Hugging Face's `gpt2` model
- ✅ Flask-based API to handle requests
- ✅ HTML frontend with prompt input and output display
- ✅ Integration between UI and model
- ✅ Ready for deployment and GitHub upload

---

## 🧠 Model Used

- **Model:** [GPT-2](https://huggingface.co/gpt2)
- **Library:** `transformers` by Hugging Face
- The model is accessed using the `pipeline` API from `transformers`.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python     | Backend logic |
| Flask      | Web framework / API |
| HTML & CSS | Frontend interface |
| Hugging Face Transformers | Model loading and inference |

---

## 📁 Project Structure

ai-text-generator/
│
├── app.py # Flask application
├── requirements.txt # Required packages
├── templates/
│ └── index.html # Frontend HTML file
└── README.md # Project documentation

---

## 🖥️ How It Works

1. User opens the web interface.
2. User enters a text **prompt** in the textarea.
3. On clicking **Generate**, the prompt is sent to the Flask backend.
4. The `gpt2` model generates text based on the prompt.
5. The generated response is displayed on the web page.

---

## ✅ Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-text-generator.git
cd ai-text-generator

### 2. Create and Activate Virtual Environment (optional but recommended)

python -m venv venv
source venv/bin/activate       # For macOS/Linux
venv\Scripts\activate          # For Windows

### 3. Install Requirements

pip install -r requirements.txt

### 4. Run the Application

python app.py

The app will be live at:
➡️ http://127.0.0.1:5000/

