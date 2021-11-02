from flask import Flask, render_template, Response
from random import choices

app = Flask(__name__)


@app.route('/')
def hello():
    random_numbers = [1, 2, 3, 4, 5, 6]
    weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]
    random_number = choices(random_numbers, weights)
    if random_number == 5:
        # Return a 404
        status_code = Response(status=404)
        return status_code
        # return render_template('404.html', title = '404'), 404
    else:
        # Return a 200
        status_code = Response(status=200)
        return status_code
        # return 'Hello, World!'

if __name__ == '__main__':
    app.run()
