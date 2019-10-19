from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    week = ['月', '火', '水', '木', '金']
    #duties = {'月': '佐藤', '火': '鈴木', '水': '清水', '木': '中村', '金': '高橋'}
    return render_template('index.html', week=week)


if __name__ == "__main__":
    app.run()
