# For Loops Challenges
For this set of challenges, we are going to teach our AI:Bot some basic maths skills such as how to count in 5 from 0 to 500 or how to count down from 100 to 0. We are also going to make our AI:Bot practise the times tables and recite the alphabet from A to Z.

## Writing Lines!
First we need to make sure that our AI:Bot is fully focused and willing to complete the work when asked to. So let him learn our expectations by making the AI:Bot copy the following lines on the screen:

“I will listen to my teacher and complete my work on time.”

## Counting in 5
We are now going to use a step in our for loop to count in 5.

## Counting down
Tweak the code from the previous task to train your AI:Bot to count down from 100 to 0! (Tip: you will have to use a negative step of -1)

## Times Tables
Train your AI:Bot to display the 12 times table as follows:
1 x 12 = 12
2 x 12 = 24
3 x 12 = 36
4 x 12 = 48
5 x 12 = 60
6 x 12 = 72
7 x 12 = 84
8 x 12 = 96
9 x 12 = 108
10 x 12 = 120

Once done, tweak your code so that it starts by asking for a number. It will then display the times table for this given number.

## The Alphabet
We are now going to train our AI:Bot to recite the 26 letters of the Alphabet from A to Z.
To do so we will use the ASCII code which give a unique integer value to each character that appears on your keyboard, including the 26 uppercase letters of the alphabet.

You can for instance try the following code to display the first three letters of the alphabet:

'''python
    # Using the ASCII code to display letters of the alphabet
    print(chr(65))
    print(chr(66))
    print(chr(67))
'''

Combine the above code with a For loop to train your AI:Bot to recite the entire alphabet from A (ASCII code 65) to Z (ASCII code 90).

## Iterative Sum

Let’s look at the following code that can be used to find the iterative sum for number 5 using the following calculation:
Iterative sum for 5 = 5 + 4 + 3 + 2 + 1

#Iterative Sum for number 5
sum = 0
for i in range(1,6): 
   sum = sum + i
print("Iterative Sum for 5 = " + str(sum))

Your task is to tweak the above code to get the computer to ask for a positive integer value and calculate the iterative sum for this given number.

## Factorial!

We are now going to train our AI:Bot to calculate a factorial of a number! Your program will ask for the user to enter a positive integer value and return its factorial value as follows:

You can complete this program by tweaking the code used to calculate the iterative sum as the two calculations are quite similar.