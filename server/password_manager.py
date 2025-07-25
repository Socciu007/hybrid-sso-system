from flask import render_template

def render_passwords(user, token):
  return render_template('passwords.html', user=user, token=token)