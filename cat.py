# loop

# i = 3

# while i != 0:
#   print("meow")
#   i = i - 1

# i = 0

# while i < 3:
#   print("meow") 
#   i += 1

# for i in range(3):
#   print("meow")


# for _ in range(3):
#   print("meow")

# print("meow\n" * 3, end='')

# while True:
#   n = int(input("what's n? "))
#   if n >0:
#     break

# for _ in range(n):
#   print("meow")
#   n -+ 1


def main():
   number= get_number()
   meow(number)

def get_number():
    while True:
      n = int(input("what's n? "))
      if n >0:
        break  
    return n

def meow(n):
   for _ in range(n):
      print("meow")


main()

#3:21 yt