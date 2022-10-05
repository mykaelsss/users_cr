from flask import Flask, render_template,redirect, request
app= Flask(__name__)

from models.users import Users

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

if __name__=="__main__":
    app.run(debug=True, port=5001)
