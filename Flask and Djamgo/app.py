from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

if "__main__" == "__name__":
    app.run(debugger=True)
