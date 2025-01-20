# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."
   return message


message = welcome_message("bcamac09@calpoly.edu")
print(message)


def smallest(n: float, m: float) -> float:
   if n < m:
      return n
   else:
      return m


first = smallest(3, 2)  # 2
second = smallest(2, 2)  # 2 NO becuase they have the same value
print(second)