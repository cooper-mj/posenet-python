#!/usr/bin/env python3

from flask import Flask
from flask import request
from io import BytesIO
from PIL import Image
from image_demo import return_keypoints
import struct
# from skimage.color import yuv2rgb

app = Flask(__name__)

@app.route('/', methods=["GET","POST", "PUT"])
def process_image():
	if request.method == "PUT":
		image = Image.open(BytesIO(request.data))
		# image = yuv2rgb(Image.open(BytesIO(request.data)))
		keypoints = return_keypoints(image)
		print(keypoints)
		return bytearray(
			struct.pack("f", keypoints['leftShoulder'][0]) + 
			struct.pack("f", keypoints['leftShoulder'][1]) + 
			struct.pack("f", keypoints['rightShoulder'][0]) + 
			struct.pack("f", keypoints['rightShoulder'][1]) + 
			struct.pack("f", keypoints['leftHip'][0]) + 
			struct.pack("f", keypoints['leftHip'][1]) + 
			struct.pack("f", keypoints['rightHip'][0]) + 
			struct.pack("f", keypoints['rightHip'][1])
		)

	elif request.method == "GET":
		return "Hello! :)"

if __name__ == "__main__":
    app.run()