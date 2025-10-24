# import sys

# print("MY NAME IS", sys.argv[1]) #at sys.argv[0] is a file name which there is name.py

# if len(sys.argv) < 2:
#   print("too few argument")
# elif len(sys.argv) > 2:
#   print("too many argument")
# else:
#   print("my name is", sys.argv[1])

# if len(sys.argv) < 2:
#   sys.exit("too few argument")
# elif len(sys.argv) > 2:
#   sys.exit("too many argument")

# print("my name is", sys.argv[1])


# if len(sys.argv) < 2:
#   sys.exit("too few argument")

# # for argv in sys.argv[1:]:
# for argv in sys.argv[1:-1]:
#   print("my name is", argv)

# name = input("What's your name? ")

# file = open("name.txt", "a")
# file.write(f"{name}\n")
# file.close()

# name = input("What's your name? ")

# with open("name.txt", "a") as file:
#   file.write(f"{name}\n")

# with open("name.txt", "r") as file:
#   lines = file.readlines()

#   for line in lines:
#     print("Hello,", line, end="")

# with open("name.txt", "r") as file:
#   for line in file:
#     # print("Hello,", line.rstrip())
#     print("Hello,", line.rstrip().sort())


names = []

with open("name.txt") as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names):
  print(f"Hello, {name}")
    

