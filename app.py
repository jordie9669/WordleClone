from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home.html')



# Need to design a form with 5 inputs for letters then check if those letters are in the given word and update the color
# of the words depending on whether a letter is present and if the letter is in the correct position