from flask import Flask, request, render_template, redirect, url_for
import os
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = 'uploaded_pitch.txt'
            file.save(os.path.join(app.root_path, filename))
            return redirect(url_for('teleprompter'))
    return render_template('index.html')

@app.route('/teleprompter')
def teleprompter():
    filename = os.path.join(app.root_path, 'uploaded_pitch.txt')
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().replace('\n', ' ')  # replace newline characters with spaces
    return render_template('teleprompter.html', text=text, speed=0.5)
if __name__ == '__main__':
    app.run(debug=True)