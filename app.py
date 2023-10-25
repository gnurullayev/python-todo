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
@app.route("/delete/<int:id>", methods=["GET","POST"])
def delete_post(id):
    if request.method == "GET":
        userId = id
        for user in users:
            if user["id"] == userId:
                print(userId)
                print(user)
                users.remove(user)
        return redirect("/")

    return render_template("index.html")

@app.route("/edit-post/<int:id>", methods=["GET","POST"])
def edit_post(id):
    if request.method == "POST":
        print(id, request.form)
        for num in range(len(users)):
            if users[num]['id'] == id:
                newUser = {
                    "id": users[num]['id'],
                    "name": request.form['name'],
                    "job": request.form['job'],
                    "email":request.form['email']
                }
                users.remove(users[num])
                users.insert(num,newUser)
    
        return redirect("/")
    user = None
    if id:
        user = next((user for user in users if user["id"] == id),None)
    return render_template("edit-post.html", user = user)


if __name__ == '__main__':
    app.run(port=8000)
    app.run(debug=True)