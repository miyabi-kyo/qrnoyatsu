from flask import Flask, redirect
import os

app = Flask(__name__)
counter = 0
urls = [
    "https://miyabinazo.web.fc2.com/kagimplomake/179669.html",
    "https://miyabinazo.web.fc2.com/kagimplomake/279669.html",
    "https://miyabinazo.web.fc2.com/kagimplomake/379669.html",
    "https://miyabinazo.web.fc2.com/kagimplomake/479669.html",
    "https://miyabinazo.web.fc2.com/kagimplomake/579669.html",
    "https://miyabinazo.web.fc2.com/kagimplomake/679669.html",
    "https://miyabinazo.web.fc2.com/kagimplomake/779669.html",
    "https://miyabinazo.web.fc2.com/kagimplomake/879669.html",
    "https://miyabinazo.web.fc2.com/kagimplomake/979669.html",
    
]
# リセット後の遷移先
reset_redirect_url = "https://miyabinazo.web.fc2.com/kagimplomake/079669.html"

@app.route("/")
def redirect_url():
    global counter
    # counterが最大インデックス以上になったら、最後のURLに固定
    if counter >= len(urls) - 1:
    return redirect(urls[-1])
    url = urls[counter]
    counter += 1
    return redirect(url)

@app.route("/reset")
def reset_counter():
    global counter
    counter = 0
    return redirect(reset_redirect_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
