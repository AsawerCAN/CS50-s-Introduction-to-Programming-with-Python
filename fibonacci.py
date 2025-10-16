# def feb_sequence(n):
#     if n < 0:
#       print("n should be positive number")
#       return
      
#     a, b= 0, 1

#     print(a, end="")

#     if n==1:
#       return
#     print(f", {b}", end="")
  
#     for i in range(2, n):
#        c=a+b

#        print(f", {c}", end="")
       
#        a,b=b,c

# feb_sequence(100)

def feb_seq(n):
  if n < 0:
    print("value must be positive")
    return
  
  a,b=0,1

  print(a, end="")

  if n==1:
    return
  print(f", {b}", end="")

  for i in range(2,n):
    c = a+b
    print(f", {c}", end="")

    a,b= b, c

feb_seq(50)