from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="My Flask App", message="Welcome to my Flask app!")

@app.route("/hello")
def hello():
    return (f"<h1>Hello, Flask!</h1>"
            f"<p>This is a simple Flask application.</p>")

if __name__ == "__main__":
    app.run(debug=True)