# main.py
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack
import json
from threading import Lock

app = Flask(__name__)

if __name__ == "__main__":
    start_grid = [[0 for x in range(15)] for y in range(15)]
    start_grid[0][0] = [[[255 for x in range(3)] for y in range(32)] for z in range(32)]
    start_grid[0][1] = [[[255 for x in range(3)] for y in range(32)] for z in range(32)]
    with open("grid_data", "w") as outFile:
        outFile.write(json.dumps(start_grid))

lock = Lock()
lock_history = Lock()

@app.route("/")
def home():
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
        with open("grid_data") as inFile:
            active_grid = json.loads(inFile.readline())
        
        for x in range(15):
            for y in range(15):
                if [x,y] in data:
                    if active_grid[y][x] == 0:
                        active_grid[y][x] = [[[255 for x in range(3)] for y in range(32)] for z in range(32)]
                else:
                    active_grid[y][x] = 0
        with open("grid_data", "w") as outFile:
            outFile.write(json.dumps(active_grid))
    return "Good"

@app.route("/set_pixels/<data>", methods=['POST'])
def set_pixels(data):
    #sets a pixels to a given color
    changeData = json.loads(data)
    historyString = ""
    
    with lock:
        with open("grid_data") as inFile:
            try:
                active_grid = json.loads(inFile.readline())
            except JSONDecodeError:
                active_grid = [[0 for x in range(15)] for y in range(15)]
                active_grid[0][0] = [[[255 for x in range(3)] for y in range(32)] for z in range(32)]
                start_grid[0][1] = [[[255 for x in range(3)] for y in range(32)] for z in range(32)]
                with open("grid_data", "w") as outFile:
                    outFile.write(json.dumps(active_grid))
                print("OOPS")
                return "Big oops"
            except:
                print("oops")
                return "Little oops"
        for entry in changeData:
            try:
                active_grid[entry[1]][entry[0]][entry[2]][entry[3]] = entry[4]
                historyString += json.dumps(entry) + "\n"
            except:
                print(entry)
        with open("grid_data", "w") as outFile:
            outFile.write(json.dumps(active_grid))
    with lock_history:
        with open("grid_history", "a") as outFile:
            outFile.write(historyString)
    return "Good"


@app.route("/get_history")
def get_history():
    with open("grid_history") as inFile:
        data = str(inFile.readlines())
    return data

@app.route("/get_grid")
def get_grid():
    #returns the grid config and data
    with open("grid_data") as inFile:
        active_grid = inFile.readline()
    return active_grid

@app.route("/silicon")
def get_silicon():
    return render_template("silicon.html")
