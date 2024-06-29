from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"Name: {name}, Email: {email}, Message: {message}"
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
