from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return '<h1>Hello World<h1/>'
    
    #returning the html template that we created
    return render_template('index.html')

if __name__ == "__main__":
    app.run()