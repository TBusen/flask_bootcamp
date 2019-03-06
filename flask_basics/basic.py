from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>I love puppies!</h1>"

@app.route('/information')
def info():
    return "<h1> Here is some information</h1>"

# dynamic routes
@app.route('/user/<name>')
def somename(name):
    return f"<h1> This is a page for: {name}"


if __name__ == "__main__":
    app.run()
