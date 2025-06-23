#import the % library
#for number in range(1, 100):
 # if number % 3 == 0 and number % 5 >= 0:
  #  print("Fizz")
  #elif number % 5 == 0 and number % 3 >= 0:
   # print("Buzz")
  #elif number % 5 == 0 and number % 3 == 0:
   # print("FizzBizz")
  #else:
   # print(f"Your number, {number}, cannot be divided evenly by the number 3 or the number 5.")
foo = 2
fizz = 3
buzz = 5
bazz = 7
list = [foo, fizz, buzz, bazz]
name = ""
for number in range(1, 100):
  for item in list:
    if number % item == 0:
      name += f"{item}"
