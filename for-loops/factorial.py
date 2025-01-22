number_to_iterate = int(input("Enter a positive number to get the factorial of: \n>>"))

sum = 1
print(number_to_iterate, "= ", end="")
for i in range(1, number_to_iterate+1): 
   sum = sum * i
   print(number_to_iterate + 1 - i, end="")
   if i < number_to_iterate:
      print(" * ", end="")

print("\nThe factorial for", number_to_iterate, "is", sum)