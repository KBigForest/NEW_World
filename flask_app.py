
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/experience/')
def page1():
    return render_template('experience.html')
if __name__ == '__main__':
    app.run(debug=True)