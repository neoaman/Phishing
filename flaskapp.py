from flask import Flask, request, render_template
from web import classifier
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def classifierA():
    if request.method == "POST":
        url = request.form.get("url")
        out = classifier(url)
        return render_template("index.html",out=out)

    return render_template("index.html",out="")

if __name__ == "__main__":
    app.run(debug=True)