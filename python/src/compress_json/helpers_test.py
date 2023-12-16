from helpers import trim_undefined, trim_undefined_recursively


def assertion(condition: bool):
  if not condition:
    raise Exception("Assertion failed")

user = {
  'name': 'Alice',
  'role': None,
}
trim_undefined(user)
if 'role' in user:
  print("undefined field is not removed")
  exit(1)
assertion(user['name'] == 'Alice')

a = {
  'name': 'a',
  'b': None,
  'extra': None 
}
b = {
  'name': 'b',
  'a': a
}
a['b'] = b

trim_undefined_recursively(b)
if 'extra' in b['a']:
  print("undefined field is not removed recursively")
  exit(1)

assertion(a['name'] == 'a')
assertion(a['b'] == b)
assertion(b['name'] == 'b')
assertion(b['a'] == a)

print("pass: helpers.py")
