def add(*args):
  print(args[1])
  sum = 0
  for n in args:
    sum +=n
  return sum





print(add(3,5,6,9,7,6,4))

def calculate(***kwarga):
  print(*args, **kwargs)
