from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='')

@app.route('/to/<name>')
def to_name(name):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
