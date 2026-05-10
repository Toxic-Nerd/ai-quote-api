from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Keep learning DevOps",
    "Automation saves time",
    "Consistency creates mastery",
    "Small progress every day",
    "Embrace failure as feedback",
    "Life is Hello World",
    "Life is hell"
]

@app.route("/")
def home():
    return {"message": "AI Quote Generator API Running"}

@app.route("/quote")
def quote():
    return {
        "quote": random.choice(quotes)
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)