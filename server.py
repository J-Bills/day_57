from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

@app.route('/')
def home():
    rand_number = random.randint(1,10)
    result = dt.datetime.now()
    result = result.year
    return render_template('index.html', num=rand_number, time=result)

@app.route('/guess/<name>')
def name_apis(name):
    genderize = requests.api.get(url='https://api.genderize.io', params={'name':name})
    genderize.raise_for_status()
    gender_data = genderize.json()
    
    agify = requests.api.get(url='https://api.agify.io', params={'name':name})
    agify.raise_for_status()
    age_data = agify.json()
    return render_template('names.html', gender=gender_data, age=age_data, users_name=name)

@app.route('/blog')
def blog():
    response = requests.api.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    status = response.raise_for_status()
    all_posts = response.json()
    
    return render_template('blog.html', posts=all_posts, stat=status)

if __name__ == "__main__":
    app.run(debug=True)