
def main():
  number = int(input("Enter number "))
  if is_even(number):
    print("Even")
  else:
    print("Odd")


def is_even(x):
  # if x % 2 == 0:
  #   return True
  # else: 
  #   return False

  # return True if x % 2 ==0 else False

  return x % 2 == 0

main()

