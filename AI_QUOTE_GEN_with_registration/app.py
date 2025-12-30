import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import mysql.connector

load_dotenv()

# Database connection
con = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

API_KEY = os.getenv("NINJA_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")

API_URL = "https://api.api-ninjas.com/v1/quotes"

headers = {
    "X-Api-Key": API_KEY
}

app = Flask(__name__)

def generate_ai_quote():
    response = requests.get(API_URL, headers=headers)
    data = response.json()

    if isinstance(data, list) and len(data) > 0:
        quote = data[0]["quote"]
        author = data[0]["author"]
        return quote, author
    else:
        return "No quote received", "Unknown"

# FIX 1: pass quote and author
@app.route("/")
def home_page():
    quote, author = generate_ai_quote()
    return render_template("home.html", quote=quote, author=author)

@app.route("/index")
def home():
    quote, author = generate_ai_quote()
    return render_template(
        "index.html",
        quote=quote,
        author=author
    )

@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO registration (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)
        )
        con.commit()
        cursor.close()

        return "Registration successful!"

    return render_template("registration.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor = con.cursor()
        cursor.execute(
            "SELECT * FROM registration WHERE email = %s AND password = %s",
            (email, password)
        )
        user = cursor.fetchone()
        cursor.close()

        if user:
            return "Login successful!"
        else:
            return "Invalid email or password."
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
