# Exercise 1: Leap year (闰年)
# ask the user to input a year (YYYY)
# output “Yes” (if it’s a leap year) or “No” (otherwise)
# what is a leap year?
# “四年一闰、百年不闰、四百年又闰”
# divisible by 4 but not by 100, or divisible by 400

input_yr = int(input("Please input a year in YYYY format: "))
if (input_yr%4==0 and input_yr%100!=0) or input_yr%400==0:
    print(input_yr," is leap year")
else:
    print (input_yr," is not a leap year")



# Exercise 2: Double your money
# ask the user to input an amount of money, and the annual interest rate (%)
# output the number of years needed to double the money

# method 1: realistic way

amt = float(input("Please enter your amount of money: "))
r = float(input("Plase enter the interest rate in percentage format(ex. 22 for 22%， 0.1 for 0.1%): "))/100

total_amt = amt
yr = 0
while total_amt < 2*amt:
    yr += 1
    total_amt *= 1 + r
print("It will take %d years to double your money at interest rate: %d" % (yr,r))


# method 2: theoretical way

import math
amt = float(input("Please enter your amount of money: "))
r = float(input("Plase enter the interest rate in percentage format(ex. 22 for 22%， 0.1 for 0.1%): "))/100
yr = math.log(2,1+r)
print("It will take %f years to double your money at interest rate: %d" % (yr,r))



# Exercise 3: Floyd’s triangle
# ask the user to input the number of rows
# output the Floyd’s triangle

row = int(input("Enter the number of rows of Floyd's triangle: "))
itr_number = 1
row_number = []
for i in range(row):
    for j in range(i+1):
        print (itr_number, end="")
        itr_number+=1
    print()



# Exercise 4: Multiplication table (九九乘法表)
# use an iteration (loop) structure to output the multiplication table

row = int(input("How many rows of Multiplication table do you wish to see: "))
for i in range(row):
    for j in range(i+1):
        print (" %d x %d = %d " % (j+1,i+1,(i+1)*(j+1)),end="")
    print()



# Exercise 5: What is the value of m?
# think before you execute to verify
# Answer: 1+80=81

k = 1
m = 1
for i in range(10):
     if i % 5 == 0:
          continue
     for j in range(10):
          if j % 1 == 0:
               m = m + 1
          elif j % 2 == 1:
               m = m - k
          elif j % 3 == 2:
               m = m - 1
          elif j % 4 == 3:
               m = m + k
          else:
               break

print("m =", m)



# Exercise 6: Reversed string
# ask the user to input a string
# e.g., How are you?
# output the string in a reversed order
# e.g., ?uoy era woH

input_str = str(input("Please input a string: "))
for i in range(-1,-len(input_str)-1,-1):
    print(input_str[i],end="")



# Exercise 7： Text file replacement
# read from a text file (E7.txt)
# input 1: the character to be replaced, c1
# input 2: the character to replace with, c2
# write to a text file (E7-Output.txt) with all c1 replaced with c2

import re

old = open("C:\\Users\\Day19\\Dropbox\\Notability\\金融数据分析方法与应用-林志杰\\金融数据分析方法与应用\\Week 3\\E7.txt","r")
old_string = old.read()
c1 = str(input("Please input the character to be replaced: "))
c2 = str(input("Please input the character to place with: "))
pattern = re.compile(c1,re.IGNORECASE)
new_string = pattern.sub(c2,old_string)
new = open("C:\\Users\\Day19\\Dropbox\\Notability\\金融数据分析方法与应用-林志杰\\金融数据分析方法与应用\\Week 3\\E7-Output.txt","w")
new.write(new_string)
old.close()
new.close()
print("New string has been outputed to file: E7-Output.txt")

