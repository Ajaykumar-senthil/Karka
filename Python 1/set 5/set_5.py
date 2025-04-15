# for i in range(1,11):
#     print(i)

# 2

# for i in range(1,21):
#     if i%2==0:
#         print(i,"even number:")

# 3

# for i in range(1,21):
#     if i % 2 != 0:
#         print("odd number",i)

# # 4

# num =8
# factorial = 1
# for i in range(1,num+1):
#     factorial *=i
# print(num,factorial)    

# 5

# total = 0
# for i in range(1, 101):
#     total += i
# print("The sum of numbers from 1 to 100 is:", total)

# 6

# numbers = [10, 20, 30, 40, 50,60]
# total = 0
# for num in numbers:
#     total += num
# average = total / len(numbers)
# print("The average of the list is:", average)


# 7

# rows = 5
# for i in range(rows):
#     for j in range(rows):
#         print("*", end=" ")
#     print()


# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# 8

# for i in range(1,6):
#     print(i)

# 9

# for i in range(1, 11):
#     print(i)

# 10

# number=[10,20,30,40,10]
# if len(number)>0 and (number)[0]==number[4]:
#     print("it is true")
# else:
#     print("false")    

# 11

# number=[5,6,10,11,15,16,20,22,17]
# for num in number:
#      if num %5==0:
#           print(num)

# 12

# char = input("Enter a single alphabet character: ")

# if len(char) == 1 and char.isalpha():
#     if char in ['a', 'e', 'i', 'o', 'u']:
#         print(char,"is a vowel.")
#     else:
#         print(char," is a consonant.")
# else:
#     print("Invalid input.")

# 13

# even_count = 0
# odd_count = 0
# for num in range(10, 56):
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Count of even numbers:", even_count)
# print("Count of odd numbers:", odd_count)

# 14
# for num in range(1,26):
#     if num%5==0:
#         print(num)

# 15

# numbers = [3, 5, 7]
# for num in numbers:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print(num,factorial)

# 16

# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))
# product = num1 * num2

# if product > 500:
#     result = num1 + num2
#     print("The product is greater than 500. Returning the sum:",result )
# else:
#     print("The product is:",product)

# 17

# a=40
# b=80
# if a > b:
#     print("the greater number is",a)
# elif b>a:
#     print("the greater number is",b)   
# else:
#     print("both numbers are equal")     


# 18

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# if num1 >= num2 and num1 >= num3:
#     print("The greatest number is:",num1)
# elif num2 >= num1 and num2 >= num3:
#     print("The greatest number is:", num2)
# else:
#     print("The greatest number is:" ,num3)


# 19

# x = [23, 4, -6, 23, -9, 21, 3, -45, -8]

# positive_numbers = []
# negative_numbers = []

# for num in x:
#     if num >= 0:
#         positive_numbers.append(num)
#     else:
#         negative_numbers.append(num)

# print("Positive numbers:", positive_numbers)
# print("Negative numbers:", negative_numbers)

