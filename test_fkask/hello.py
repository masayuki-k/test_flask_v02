from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    hello = "こんにちは"
    return render_template('hello.html', hello=hello)

if __name__ == "__main__":
    app.run()