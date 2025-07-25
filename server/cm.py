from flask import render_template

def render_cm(user, token):
  return render_template('cm.html', user=user, token=token)
