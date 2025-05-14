from flask import Flask, redirect
import os

app = Flask(__name__)
counter = 0
urls = [
    "https://google.com",
    "https://yahoo.com",
    "https://x.com",
]

@app.route("/")
def redirect_url():
    global counter
    url = urls[counter % len(urls)]
    counter += 1
    return redirect(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
