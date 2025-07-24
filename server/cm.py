from flask import render_template

def render_cm(user):
  return render_template('cm.html', user=user)
