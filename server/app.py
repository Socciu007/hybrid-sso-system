from flask import Flask, render_template, request, redirect, make_response
from auth import generate_token, login_required
from cm import render_cm
from fis import render_fis
from password_manager import render_passwords
from users import get_user
from middleware import LifespanMiddleware
from asgiref.wsgi import WsgiToAsgi # type: ignore
import uvicorn

app = Flask(__name__, template_folder='../website', static_folder='../website/css')

# Fake user
USERS = {'admin': '123456'}

@app.route('/')
@login_required
def home(user, token):
  return render_template('home.html', user=user, token=token)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    user = request.form['username']
    pwd = request.form['password']
    user_data = get_user(user)
    if user_data and user_data['password'] == pwd:
      token = generate_token(user)
      resp = make_response(redirect('/'))
      resp.set_cookie('token', token)
      return resp
    return "Login failed"
  return render_template('login.html')

@app.route('/logout')
def logout():
  resp = make_response(redirect('/login'))
  resp.delete_cookie('token')
  return resp

@app.route('/cm')
@login_required
def cm(user, token):
  return render_cm(user, token)

@app.route('/fis')
@login_required
def fis(user, token):
  return render_fis(user, token)

@app.route('/passwords')
@login_required
def passwords(user, token):
  return render_passwords(user, token)

asgi_app = LifespanMiddleware(WsgiToAsgi(app))
if __name__ == '__main__':
  uvicorn.run("app:asgi_app", port=8000, reload=True)