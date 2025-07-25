from flask import render_template

def render_fis(user, token):
  return render_template('fis.html', user=user, token=token)