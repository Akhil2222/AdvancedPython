#import the mod library
if number MOD 3 == 0 and number MOD 5 >= 0:
  print("Fizz")
elif number MOD 5 == 0 and number MOD 3 >= 0:
  print("Buzz")
elif number MOD 5 == 0 and number MOD 3 == 0:
  print("FizzBizz")
else:
  print(f"Your number, {number}, cannot be divided evenly by the number 3 or the number 5.")
