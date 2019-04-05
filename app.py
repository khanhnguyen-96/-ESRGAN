import os
import sys
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import test
import utils.util as util

UPLOAD_FOLDER = "../Dataset/uploaded/LR"
RESULT_FOLDER = "./results/RRDB_ESRGAN_x4/demo"
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = SECRET_KEY

util.mkdirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        # Get the name of the uploaded files
        uploaded_files = request.files.getlist("file[]")

        for file in uploaded_files:

            # Check if the file is one of the allowed types/extensions
            if file and allowed_file(file.filename):
                # Make the filename safe, remove unsupported chars
                filename = secure_filename(file.filename)
                # Move the file form the temporal folder to the upload
                # folder we setup
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                # Save the filename into a list, we'll use it later
                # filenames.append(filename)
                # Redirect the user to the uploaded_file route, which
                # will basicaly show on the browser the uploaded file
        # Load an html page with a link to each uploaded file

        test.main("./options/test/test_ESRGAN.json")

        lrFiles = [UPLOAD_FOLDER + file for file in os.listdir(UPLOAD_FOLDER)]
        hrFiles = [RESULT_FOLDER + file for file in os.listdir(RESULT_FOLDER)]

        return render_template("result.html", lrFiles=lrFiles, hrFiles=hrFiles)
