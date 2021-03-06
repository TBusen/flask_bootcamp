from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    myname = 'Travis'
    mylist = [1,2,3,4]
    return render_template('basic.html', myname=myname, mylist=mylist)


@app.route('/information')
def info():
    return "<h1> Here is some information</h1>"

# dynamic routes


@app.route('/puppy_latin/<name>')
def latinConvert(name):
    if name[-1].lower() == 'y':
        puppname = f'{name[:-1].lower()}iful'
    else:
        puppname = f'{name[:-1].lower()}y'
    return f'<h1> My latin name is {puppname} </h1>'


if __name__ == "__main__":
    app.run(debug=True)
