from flask import Flask, render_template, request
import string
 


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    user = request.args.get('username')

    requirements = [lambda user: any(l.isupper() for l in user),  # build all rules to pass
                    lambda user: any(l.islower() for l in user),
                    lambda user: user[-1] in string.digits]

    if all(rule(user) for rule in requirements): # apply all the rules
        return render_template('success.html', username=user)
    else:
        return render_template('failure.html', username=user)


if __name__ == '__main__':
    app.run(debug=True)
