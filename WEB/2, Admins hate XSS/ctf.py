from flask import Flask, jsonify, render_template, abort, request, Response, Markup
import os
import time

app = Flask(__name__)

template_dir = os.path.abspath('./templates')
app.template_folder = template_dir

@app.route('/', methods=['GET'])
def home():
    messages = open('messages.txt', 'r').read().replace('\n', '<br>')
    messages = Markup(messages)
    return render_template('message.html', messages=messages)

@app.route('/', methods=['POST'])
def message():
    username = request.form.get("username", None)
    message = request.form.get("message", None)
    message = message.replace('\n', '<br>')
    time.sleep(1)
    with open('messages.txt', 'a') as f:
        f.write(f'{username}:{message}\n')

    if not username or not message:
        return jsonify({'error': 'you need a message and a username'})

    messages = open('messages.txt', 'r').read().replace('\n', '<br>')
    messages = Markup(messages)
    return render_template('message.html', messages=messages)

@app.route('/flag', methods=['GET'])
def flag():
    if request.cookies.get('admin') == 'X5S_A_C0ok1e':
        return render_template('flag.html')
    else:
        return render_template('noflag.html')

if __name__ == "__main__":
    app.run(port=3000)
