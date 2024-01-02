from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    responce = requests.get(blog_url)
    all_posts = responce.json()
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<number>')
def post(number):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    responce = requests.get(blog_url)
    all_posts = responce.json()
    number = int(number)
    return render_template("post.html", posts=all_posts, number=number)

if __name__ == "__main__":
    app.run(debug=True)
