from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
@app.route("/Home")
def home():
	return render_template("home.html")

app.run(debug=True)


