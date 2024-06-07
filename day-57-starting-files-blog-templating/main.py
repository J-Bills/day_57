from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    posts_data = Post()
    return render_template("index.html", blog_posts = posts_data)

@app.route('/blog/<number>')
def read_blog(number):
    posts_data = Post()
    number =int(number)
    page = posts_data.get_blog(number)
    return render_template("post.html",page=page, number=number)



if __name__ == "__main__":
    app.run(debug=True)
