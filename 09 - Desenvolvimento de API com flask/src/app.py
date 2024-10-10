from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
  return {
    "user": usuario,
    "age": idade,
    "height": "{:.2f}".format(altura)
  }

@app.route("/bemvindo")
def bem_vindo():
  return {
    "message": "Hello World"
  }

@app.route("/projects/")
def projects():
  return "The project page"

@app.route("/about", methods=["GET", "POST"])
def about():
  if request.method == "GET":
    return "This is a GET"
  else:
    return "This is a POST"
  return "The about page"

with app.test_request_context():
  print(url_for("bem_vindo"))
  print(url_for("projects"))
  print(url_for("about", next="/"))
