from flask import Flask, render_template, request, jsonify, send_file
from subprocess import Popen, PIPE
import threading
import time

app = Flask(__name__)

# Global variable to store the output
output = []
status = []
stop_flag = False

def run_main():
    global output, stop_flag
    # Run the main.py script
    process = Popen(["python", "main.py"], stdout=PIPE)
    while True:
        if stop_flag:
            print(stop_flag)
            process.terminate()  # Terminate the subprocess if stop flag is True
            break
        line = process.stdout.readline().decode().strip()
        if line == '':
            break

        # If the line does not have atleast five commas, that means, it is a status message
        if line.count(',') < 5:
            status.append(line)
        else:
            output.append(line.split(','))  # Splitting the line into columns and appending as a list
    #output = output[-10:]  # Keep the last 10 rows

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output")
def get_output():
    return jsonify(output)

@app.route("/status")
def get_status():
    return jsonify(status)

@app.route("/run_main", methods=["POST"])
def run_main_route():
    global stop_flag
    stop_flag = False
    #if output is empty, start the thread
    if not output:
        threading.Thread(target=run_main).start()
    return ""

@app.route("/stop_main")
def stop_execution():
    global stop_flag, output
    stop_flag = True
    output = []
    print("Stop flag set to True")
    return ""

@app.route('/download')
def download():
    return send_file('car_data.csv', as_attachment=True)

if __name__ == "__main__":
    # Start the Flask development server
    app.run(debug=True)
