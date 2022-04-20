from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User

# index route. sends us to users page
@app.route('/')
def index():
    return redirect('/users')

# users route. displays all users
@app.route('/users')
def users():
    return render_template('users.html', users = User.get_all())

# displays new user creation page
@app.route('users/new')
def new():
    return render_template('new.html')

# send created user data to database
@app.route('users/create', methods=['POST'])
def create():
    # prints form data to terminal
    print(request.form)
    # creates instance of user
    User.save(request.form)
    # redirects back to display all users page
    return redirect('/users')

# displays edit user page
@app.route('/users/edit/<int:id>')
def edit(id):
    # saves id to pass to query
    data = {
        'id' : id
    }
    return render_template('edit.html', user = User.get_one(data))

# displays show user page
@app.route('/users/show/<int:id>')
def show(id):
    # saves id to pass to query
    data = {
        'id' : id
    }
    return render_template('show.html', user = User.get_one(data))

# send updated data to database
@app.route('users/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

# deletes user data
@app.route('users/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    User.delete(data)
    return redirect('/users')

if __name_ == "__main__":
    app.run(debug=True)