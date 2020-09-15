# 1. Install the Python environment
# (1) Anaconda (Version 3.7)
# (2) PyCharm (Community Version)
# Done

# 2. Console input / output
# Ask the user to input: (1) a text, (2) an integer, and
# (3) a floating-point number. Output the values and types of the three input.

input_text = str(input("How should I call you?"))
input_int = int(input("How old are you?"))
input_float =float(input("Please type your lucky float number: "))

print ("%s, %d years old, has %s dollars in the pocket!" % (input_text,input_int,input_float))

# 3. Types, variables and operators
# Define variables of different types (int, float, bool, str).
# Process these variables using various operators (where applicable).
a = 1
b = 2.2
c = True
d = "a plus b equals:"

if c:
    print ("a is",a,"b is",b)
    print (d,a+b)
else:
    print ("You shall not pass!")

# 4. Selection statement
# Ask the user to input an exam score, and the program will output the corresponding grade of the score.
# The grade and corresponding score range is:
# A ~ [90, 100]; B ~ [80, 89]; C ~ [70, 79]; D ~ [60, 69]; E ~ [0, 59]

while True:
    score = eval(input("What is your score, honey? (please type between 0 and 100) "))
    if score >100:
        print ("Oh man, I'm sure you are pretty HIGH, lets try again")
        continue

    elif score <0:
        print ("Hey man cheer up, you are too NEGATIVE, lets try again")
        continue
    else:
        if score > 0 and score <= 59:
            print ("It's an E, you shall not pass my friend")
        elif score >= 60 and score <= 69:
            print ("It's a D, you barely pass it honey")
        elif score >= 70 and score <= 79:
            print ("It's a C, you better try harder my comrade")
        elif score >= 80 and score <= 89:
            print ("Your hardwork earned you a B, good job!")
        elif score >= 90 and score <= 100:
            print ("You A'ced this class! ")
        else:
            print ("Man, you are falling between grades, I dun know what to do with you cuz my prof. didnt tell me abt it.")
        break

# 5. Iteration statement
# Ask the user to input two integers a and b (a < b). Compute and output the sum:
# sum = a+(a+1)+(a+2)+…+（b-2）+（b-1）+b

a = int(input("please enter your first integer"))
b = int(input("Please enter second integer (must be greater than the first integer): "))
c = 0
while a <= b:
    c += a
    a += 1
print ("sum = a+(a+1)+(a+2)+…+（b-2）+（b-1）+b =",c)
