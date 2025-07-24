from flask import render_template

def render_fis(user):
  return render_template('fis.html', user=user)