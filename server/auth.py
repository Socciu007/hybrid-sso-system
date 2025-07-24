import jwt # type: ignore
from datetime import datetime, timedelta
from flask import request, redirect, url_for

SECRET_KEY = 'secret-key-demo'

# Generate a JWT token for a user
def generate_token(user_id):
  payload = {
    'sub': user_id,
    'exp': datetime.utcnow() + timedelta(hours=1)
  }
  return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# Verify a JWT token
def verify_token(token):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    return payload['sub']
  except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
    return None

# Decorator to check if a user is logged in
def login_required(f):
  from functools import wraps
  @wraps(f)
  def decorated(*args, **kwargs):
    token = request.cookies.get('token')
    user = verify_token(token)
    if not user:
      return redirect(url_for('login'))
    return f(user, *args, **kwargs)
  return decorated