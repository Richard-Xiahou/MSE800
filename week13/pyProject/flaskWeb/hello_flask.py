from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="My Flask App", message="Welcome to my Flask app!")

@app.route("/hello")
def hello():
    return (f"<h1>Hello, Flask!</h1>"
            f"<p>This is a simple Flask application.</p>")

# frontend code for login.html
@app.route("/login")
def login():
    data = {"username": "testuser", "password": "testpass"}
    return render_template("login.html", title="Login Page", data=data)
# backend code for login.html
@app.route("/loginwithdata", methods=["POST"])
def login_with_data():
    username = request.form.get("username")
    password = request.form.get("password")
    return f"Received login data: Username: {username}, Password: {password}"

@app.route("/bmi")
def bmi():
    return render_template("bmi.html", title="BMI Calculator")

@app.route("/calculate_bmi", methods=["POST"])
def calculate_bmi():
    height = float(request.form.get("height"))
    weight = float(request.form.get("weight"))
    bmi = weight / (height ** 2)
    return render_template("bmi_result.html", title="BMI Result", bmi=bmi)

if __name__ == "__main__":
    app.run(debug=True)