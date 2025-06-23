#import the % library
for number in range(1, 100):
  if number % 3 == 0 and number % 5 >= 0:
    print("Fizz")
  elif number % 5 == 0 and number % 3 >= 0:
    print("Buzz")
  elif number % 5 == 0 and number % 3 == 0:
    print("FizzBizz")
  else:
    print(f"Your number, {number}, cannot be divided evenly by the number 3 or the number 5.")
