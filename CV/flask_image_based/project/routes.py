import json
import os
import time
import flask
from flask import Blueprint, request, render_template, url_for, redirect
from ..instance import config
import logic as logic
from os import urandom
import io


# here you must load your saved model, when the server starts


conf_obj = config.Config()
bp = Blueprint('routes', __name__, url_prefix='/project')


@bp.route("/")
def start_page():
    return render_template("home.html", start_page="True")


@bp.route("/custom_task")
def custom_task():
    return render_template("image_upload_form.html", task_name="Image Classification")


@bp.route("/image_process", methods=["POST"])
def image_process():
    image = request.files["file"]
    image.save("your_path_to_saving.jpg")

    # open image, and process it

    # return class as text(you can also add image\another images)

    class_ = "classification_result_after_image_processing"
    return render_template("image_process_output.html", task_name="Image Classification Output", class_=class_)
