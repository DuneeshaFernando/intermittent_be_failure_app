from flask import Flask, Response
from random import choices

app = Flask(__name__)


@app.route('/hello',methods=['POST'])
def hello():
    random_numbers = [1, 2, 3, 4, 5, 6]
    weights = [0.1, 0.15, 0.05, 0.1, 0.5, 0.1]
    random_number = choices(random_numbers, weights)
    if random_number[0] == 5:
        # Return a 404
        status_code = Response(status=500)
        return status_code
    else:
        # Return a 200
        status_code = Response(status=200)
        return status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
