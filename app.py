from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/usa")
def usa():
    return render_template("extra/uae-us/us.html")

@app.route("/uae")
def uae():
    return render_template("extra/uae-us/use.html")

@app.route("/comparison")
def comparison():
    return render_template("extra/comparison.html")

@app.route("/conclusion")
def conclusion():
    return render_template("extra/conclusion.html")

@app.route("/citations")
def citations():
    return render_template("extra/citations.html")

if __name__ == "__main__":
    app.run()
