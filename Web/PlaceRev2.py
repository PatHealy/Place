# main.py
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack
import json
from threading import Lock
import datetime

app = Flask(__name__)

if __name__ == "__main__":
    start_grid = [[(0,0,0) for x in range(128)] for y in range(2)]
    with open("grid_data", "w") as outFile:
        outFile.write(json.dumps(start_grid))

lock = Lock()

@app.route("/")
def home():
    return render_template("homeRev2.html")

@app.route("/set_pixels", methods=['POST'])
def set_pixels():
    #sets pixels based on set data
    #data in format: [(x,y), (0,0,0)]
    change_data = json.loads(request.data)
    grid_data = []
    with lock:
        with open("grid_data") as dataFile:
            grid_data = json.loads(dataFile.readlines())
            for pix in change_data:
                grid_data[pix[0][0]][pix[0][1]] = pix[1];
        with open("grid_data", "w") as dataFile:
            dataFile.writelines(json.dumps(grid_data))
    return "Set Pixels"

@app.route("/get_grid")
def get_grid():
    #returns the grid config and data
    with open("grid_data") as inFile:
        active_grid = inFile.readline()
    return active_grid