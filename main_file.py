print('hello')


def get_term(n1, n2 ,N): 

	# n1=0
	# n2=1

	temp=0

	# N=int(input('Enter N to get Nth term of series : '))

	if N==1:
	    print(n1)
	    return n1
	    
	    
	else:
	    for i in range(3,N+1,1):
	        temp=n2
	        n2=temp+n1
	        n1=temp
	        
	        
	    print(n2)
	    return n2
	# enter validations on client side
	# make variable ficonnaci sequence


get_term(1,1,6)



from flask import Flask, render_template, request, redirect 

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello():
	if request.method=="POST":
		f=int(request.form["first"])
		s=int(request.form["second"])
		q=int(request.form["quantity"])
		a=get_term(f,s,q)
		return render_template("home.html",ans=a)


	a=0
	return render_template("home.html",ans=a)


app.run(debug=True)


