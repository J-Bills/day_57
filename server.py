from flask import Flask, render_template
import random
import datetime as dt

app = Flask(__name__)

@app.route('/')
def home():
    rand_number = random.randint(1,10)
    result = dt.datetime.now()
    result = result.year
    return render_template('index.html', num=rand_number, time=result)

if __name__ == "__main__":
    app.run(debug=True)