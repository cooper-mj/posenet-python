#!/usr/bin/env python3
"""Send a POST request to server,
pass in an image as the data. """
import requests
import json
from PIL import Image
import binascii
from io import BytesIO

def main():
    # Sending to localhost for now
    filename = "test_image.jpg"
    with open(filename, "rb") as f:
        im = Image.open(f)
        imgByteArr = BytesIO()
        im.save(imgByteArr, format="PNG")
        imgByteArr = imgByteArr.getvalue()
    url = "http://127.0.0.1:5000/"
    print(imgByteArr)
    requests.post(url, data = {'req_img' : imgByteArr})
    
if __name__ == '__main__':
    main()