#exceptions

# try:
#   x= int(input("What's x? "))
# except ValueError:
#   print("x is not integer")
# else:
#   print(f"x is {x}")

while True:
  try:
    x = int(input("what's x? "))
  except ValueError:
    print('x is not integer')
  else:
    break

print(f'x is {x}')