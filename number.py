#exceptions

# try:
#   x= int(input("What's x? "))
# except ValueError:
#   print("x is not integer")
# else:
#   print(f"x is {x}")


# def main():
#     # Call get_int to get the value, and store the result in x
#     x = get_int() 
#     # Print the result from main()
#     print(f'x is {x}')

# def get_int():
#     while True:
#         try:
#             # The loop gets the integer and assigns it to x
#             x = int(input("what's x? ")) 
#         except ValueError:
#             print('x is not integer')
#         else:
#             # If successful, break the loop and return the value
#             return x # Return the successfully received integer, return is more stronger then break it breaks and return value as well

# # Standard convention to run the main function when the script executes
# if __name__ == "__main__":
#     main()



def main():
  x = get_int("what's x? ")
  print(f"x is {x}")

def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      pass

main()

