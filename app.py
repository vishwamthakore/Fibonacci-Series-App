import Flask 

app = Flask(__name__)

@app.route("/")
def hello():
	a=0
	return render_template("home.html",ans=a)


# app.run(debug=True)


