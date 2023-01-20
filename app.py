from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def first_page():
    if request.method == "POST":
       name = request.form.get("name")
       designation = request.form.get("desig")
       if designation=="admin":
           return "Welcome admin"
       return "Welcome user"
    return render_template("index.html")

if __name__ == "__app__":
    app.run()
