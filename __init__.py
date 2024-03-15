from flask import Flask, render_template, request
from main import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    bot_response = get_response(user_input)
    return {'bot_response': bot_response}



if __name__ == '__main__':
    app.run(port=5556,debug=True)
