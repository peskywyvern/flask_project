from flask import Flask
from people.route import people
from posts.route import posts

app = Flask(__name__)
app.register_blueprint(people)
app.register_blueprint(posts)


@app.route('/version')
def version():
    return "1.0"


if __name__ == "__main__":
    app.run()