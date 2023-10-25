from flask import Flask, render_template,request,redirect
import random

app = Flask(__name__)

users = [
    {   
        "id":1,
        "name":"Alisher",
        "job":"Doctr",
        "email":"alisher@gaminl.com"
    },
    {   
        "id":2,
        "name":"Ahmad",
        "job":"Developer",
        "email":"ahmad@gaminl.com"
    }
]

usersId = [1]
def newId (): 
    id = 1
    while id in usersId:
        id = random.randint(1,100)
    usersId.append(id)
    return id

@app.route('/', methods=["GET","POST"])
def home():
    return render_template("index.html", users=users )

@app.route("/add-post", methods=['GET', 'POST'])
def add_post():
    if request.method == "POST":
        newUser = {
            "id": newId(),
            "name": request.form["name"],
            "job": request.form["job"],
            "email": request.form["email"]
        }
        users.append(newUser)
        return redirect("/")
    return render_template("add-post.html")

if __name__ == '__main__':
    app.run(port=8000)
    app.run(debug=True)