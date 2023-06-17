from flask import Flask, render_template, abort, request, Response
import os

app = Flask(__name__)

template_dir = os.path.abspath('./templates')
app.template_folder = template_dir

@app.route('/')
def home():
    resp = Response(render_template('ctf.html'))
    resp.set_cookie('admin', 'false')
    return resp

@app.route('/flag')
def flag():
    if request.cookies.get('admin') == 'true':
        with open(os.path.join(template_dir, "flag.html"), "r") as txt_file:
            content = txt_file.read()
        resp = Response(content)
        resp.headers['Content-Type'] = 'text/html'
        return resp
    else:
        return render_template('noflag.html')

if __name__ == "__main__":
    app.run(port=3000)

