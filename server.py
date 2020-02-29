#!/usr/bin/env python3

from flask import Flask
from flask import request
from io import BytesIO
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def process_image():
    if request.method == "POST":
        print(type(request.json["img"]))
        # print(request.json)
        # print(request.data)
    return ""

if __name__ == "__main__":
    app.run()