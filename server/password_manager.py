from flask import render_template

def render_passwords(user):
  return render_template('passwords.html', user=user)