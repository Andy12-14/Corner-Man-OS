import os
from flask import Flask, render_template, request, jsonify
from headhunter import run_headhunter
from smoke_detector import run_smoke_detector
from The_plug import run_the_plug

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/headhunter', methods=['GET', 'POST'])
def headhunter():
    if request.method == 'POST':
        user_input = request.json.get('message')
        response = run_headhunter(user_input)
        return jsonify({'response': response})
    return render_template('agent.html', agent_name="Headhunter", catchphrase="I find everything about everyone.", agent_id="headhunter")

@app.route('/smoke_detector', methods=['GET', 'POST'])
def smoke_detector():
    if request.method == 'POST':
        user_input = request.json.get('message')
        response = run_smoke_detector(user_input)
        return jsonify({'response': response})
    return render_template('agent.html', agent_name="Smoke Detector", catchphrase="Where there's smoke, there's a fight!", agent_id="smoke_detector")

@app.route('/the_plug', methods=['GET', 'POST'])
def the_plug():
    if request.method == 'POST':
        user_input = request.json.get('message')
        response = run_the_plug(user_input)
        return jsonify({'response': response})
    return render_template('agent.html', agent_name="The Plug", catchphrase="Everybody knows the plug has the goods (;)", agent_id="the_plug")

if __name__ == '__main__':
    app.run(debug=True)
