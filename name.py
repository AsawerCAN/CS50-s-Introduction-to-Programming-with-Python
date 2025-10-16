import sys

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


if len(sys.argv) < 2:
  sys.exit("too few argument")

# for argv in sys.argv[1:]:
for argv in sys.argv[1:-1]:
  print("my name is", argv)