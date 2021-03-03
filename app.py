from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/greet')
# def greet():
#     name = "Mavewrick"
#     return render_template('greet.html', name = name)

@app.route('/<name>')
def nameParam(name):
    name = name
    return render_template('greet.html', name = name)

if __name__ == "__main__":
    app.run(debug=True)