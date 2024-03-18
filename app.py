from flask import Flask, render_template, request, flash


app = Flask (__name__)
app.secret_key = "la que cuelga"
#app.config['SECRET_KEY'] = 'chapalapachala'


@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!" )
    #request.form['name_input'] #match with the name of our input
    return render_template("index.html")
