from flask import Flask
app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return "This is the first route."

app.run(use_reloader=True)
