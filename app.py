from flask import Flask, render_template, request
from parser import analyze_header

app = Flask(__name__)
analysis_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyzer", methods=["GET", "POST"])
def analyzer():
    result = None
    if request.method == "POST":
        header_data = request.form["header"]
        result = analyze_header(header_data)

        if result:
            analysis_history.insert(0, result)
            if len(analysis_history) > 5:
                analysis_history.pop()

    return render_template("analyzer.html", result=result, history=analysis_history)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
