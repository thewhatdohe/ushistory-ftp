from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/usa")
def USA():
    return render_template("uae-us/us.html")


@app.route("/uae")
def UAE():
    return render_template("uae-us/uae.html")


@app.route("/comparison")
def Comparison():
    return render_template("extra/comparison.html")


@app.route("/conclusion")
def Conclusion():
    return render_template("extra/conclusion.html")


@app.route("/citations")
def Citations():
    return render_template("extra/citations.html")



if __name__ == "__main__":
    app.run(debug=True)