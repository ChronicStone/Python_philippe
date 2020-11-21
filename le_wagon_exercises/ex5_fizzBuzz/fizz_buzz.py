# Start with some pseudo-code!
for val in range(1, 101):
    if(val % 3 == 0 and  val % 5 == 0):
        print("fizzbuzz")
    elif(val % 3 == 0):
        print("fizz")
    elif(val % 5 == 0):
        print("buzz")
    else:
        print(val)
        
# We should check if the current value can be divided by 3 and 5 in first, otherwise we have
# a bug : some values will be declared as fizz or buzz instead of fizzbuzz, because asserting
# that val can be divided by 3 does not prove that it cant also be divided by 5