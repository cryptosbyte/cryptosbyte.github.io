from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cryptos.db"
db = SQLAlchemy(app)
db.create_all()


class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_content = db.Column(db.String(99999999), nullable=False)
    post_creation_date = db.Column(db.String(60), nullable=False)
    post_name = db.Column(db.String(200), nullable=False)
    post_short_desc = db.Column(db.String(300), nullable=True)

    def __repr__(self):

        return "<Blog %r>" % self.id


@app.get("/")
def index():
    return render_template("index.html", props={
        "count": db.session.query(Posts).count()
    }, blogs=Posts.query.order_by(Posts.post_creation_date).all())


@app.get("/blog/<int:blog_id>")
def blog(blog_id):
    blog = Posts.query.get_or_404(blog_id)

    try:

        return render_template("blog.html", blog_props=blog)

    except:

        return render_template("404.html")


if __name__ == "__main__":
    app.run(
        # host="0.0.0.0", port=8080
        # debug=True
    )
