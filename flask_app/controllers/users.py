from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import Users


@app.route('/users/new')
def new_user():
    return render_template("create.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.form
    Users.create_user(data)
    return redirect('/users')

@app.route('/users')
def all_users():
    users = Users.get_all_users()
    print(users)
    return render_template("read.html", every_users = users)

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id": id
    }
    return render_template("update.html", user=Users.show_user(data))

@app.route('/user/update/<int:id>', methods=['POST'])
def update(id):
    print(request.form)
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "id":id
    }
    Users.update(data)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    Users.delete_user(data)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def one_user(id):
    data ={
        "id":id
    }
    Users.show_user(data)
    return render_template("show_user.html", user=Users.show_user(data))
