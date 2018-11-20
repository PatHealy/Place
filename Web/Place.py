# main.py
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack
import json
from threading import Lock

app = Flask(__name__)

if __name__ == "__main__":
    start_grid = [[0 for x in range(15)] for y in range(15)]
    start_grid[0][0] = [[[0 for x in range(3)] for y in range(32)] for z in range(32)]
    outFile = open("grid_data", "w")
    outFile.write(json.dumps(start_grid))
    outFile.close()

lock = Lock()
lock_history = Lock()

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/spimewrangler")
def wrangle():
    return render_template("wrangle.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/set_shape/<shape>", methods=['POST'])
def set_shape(shape):
    #shape is a list of tuples, index of each active panel
    data = json.loads(shape)
    print(data)
    #TODO
    with lock:
        inFile = open("grid_data")
        active_grid = json.loads(inFile.readline())
        inFile.close()
        for x in range(15):
            for y in range(15):
                if [x,y] in data:
                    if active_grid[y][x] == 0:
                        active_grid[y][x] = [[[0 for x in range(3)] for y in range(32)] for z in range(32)]
                else:
                    active_grid[x][y] = 0
        outFile = open("grid_data", "w")
        outFile.write(json.dumps(active_grid))
        outFile.close()
    return "Good"
    
@app.route("/set_pixel/<grid_data>/<coordinate>/<rgb>", methods=['POST'])
def set_pixel(grid_data, coordinate, rgb):
    #sets a pixel to a given color
    #coordinate is a tuple of tuples
    grid = [int(x) for x in grid_data.split(",")]
    cord = [int(x) for x in coordinate.split(",")]
    with lock:
        inFile = open("grid_data")
        active_grid = json.loads(inFile.readline())
        inFile.close()
        active_grid[grid[1]][grid[0]][cord[0]][cord[1]] = [int(x) for x in rgb.split(",")]
        outFile = open("grid_data", "w")
        outFile.write(json.dumps(active_grid))
        outFile.close()
    with lock_history:
        outFile = open("grid_history", "a")
        outFile.write(grid_data + "/" + coordinate + "/" + rgb)
        outFile.close()
    return "Good"

@app.route("/get_history")
def get_history():
    inFile = open("grid_history")
    data = str(inFile.readlines())
    inFile.close()
    return data

@app.route("/get_grid")
def get_grid():
    #returns the grid config and data
    inFile = open("grid_data")
    active_grid = inFile.readline()
    inFile.close()
    return active_grid
