from flask import Flask, request, jsonify,render_template
import google.generativeai as genai
from flask_cors import CORS
# Initialize Gemini
genai.configure(api_key="AIzaSyAPj8VvcpdN4-SSd91E4e5IMdIGctN4dQY")

model = genai.GenerativeModel("gemini-2.0-flash")

app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = model.generate_content(user_input)
    return jsonify({"response": response.text})

if __name__ == "__main__":
        app.run(host='10.75.51.145', port=5000, debug=True)

