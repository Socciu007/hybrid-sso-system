import json

# Get all users
def get_users():
  try:
    with open('../mock/users.json', 'r') as f:
      users = json.load(f)
      return users
  except Exception as e:
    print('error', e)
    return []

# Get user by username
def get_user(username):
  users = get_users()
  for user in users:
    if user['username'] == username:
      return user
  return None