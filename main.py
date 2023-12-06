from flask import Flask, request, jsonify, render_template, redirect, url_for
from openai_chat import get_output_for_doubt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/doubt_response',methods=['POST'])
def doubt_response():
    text = request.form['doubt']
    output_value = get_output_for_doubt(text)
    return render_template('video.html',output_text=output_value)

if __name__ == '__main__':
    app.run(debug=True,port=4000)
