from flask import Flask

from quiz import *


app = Flask(__name__)

@app.route('/')
def hello():
    sample = quiz_capital()

    sample.display_question()
    sample.check_answer()

    return None

if __name__ == '__main__':
    app.run()