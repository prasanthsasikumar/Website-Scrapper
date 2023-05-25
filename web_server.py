from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    python_interpreter = './.venv/Scripts/python.exe'  # Specify the desired Python interpreter path
    output = subprocess.check_output([python_interpreter, 'main.py'])
    return render_template('output.html', output=output.decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)

