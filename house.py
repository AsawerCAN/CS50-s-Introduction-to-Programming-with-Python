name = input("What's your name? ")

match name:
  case "Harry" | "Hermionie" | "Ron":
    print("Griffindor")
  case "Daraco":
    print("Slytherin")
  case _:
    print("Who?")