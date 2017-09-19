import os
from flask import Flask, g, render_template


app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(
    DATABASE=os.path.join(app.root_path, 'myfridge.db'),
    SECRET_KEY=b'asdfasfsaf',
    username='admin',
    password='admin',
)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/user/<int:id>')
def show_user_profile(id):
    # show the user profile for that user
    return 'User %s' % id
