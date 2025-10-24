try: 
  a = float(input("enter your first number: "))
  b = float(input("enter your seond number: "))
  print(f"addition: {a + b}")
  print(f"subtraction: {a - b}")
except ValueError:
  print("please enter valid numbers.")
