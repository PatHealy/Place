# main.py
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack
import json
from threading import Lock
import datetime

app = Flask(__name__)

#if __name__ == "__main__":

grid = [[(0,0,0) for x in range(64)] for y in range(64)]

@app.route("/")
def home():
    return render_template("homeRev2.html")

@app.route("/set_pixels", methods=['POST'])
def set_pixels():
    change_data = json.loads(request.data)
    for pix in change_data:
        grid_data[pix[0][0]][pix[0][1]] = pix[1]
    return "Set Pixels"

@app.route("/get_grid")
def get_grid():
    return json.dumps(grid)