# Python Input & Output Questions Solutions

# ✅ Basic Level (1–10)
# 1. Take a number from the user and print it.
num = int(input("Enter a number: "))
print(num)

# 2. Take two numbers and print their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

# 3. Take your name and print a welcome message.
name = input("Enter your name: ")
print(f"Welcome, {name}!")

# 4. Take radius and print the area of a circle.
radius = float(input("Enter radius: "))
print(3.14159 * radius * radius)

# 5. Take a number and print whether it is even or odd.
n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")

# 6. Take marks of 3 subjects and print total and percentage.
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
total = m1 + m2 + m3
percentage = total / 3
print("Total:", total)
print("Percentage:", percentage)

# 7. Take a string and print its length.
s = input("Enter a string: ")
print(len(s))

# 8. Take a number and print its square.
n = int(input("Enter a number: "))
print(n ** 2)

# 9. Take age from user and print “Adult” or “Child”.
age = int(input("Enter age: "))
print("Adult" if age >= 18 else "Child")

# 10. Take 5 numbers and print the average.
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(5)]
avg = sum(numbers) / 5
print("Average:", avg)

# ✅ Medium Level (11–20)
# 11. Take a string and print it in uppercase.
s = input("Enter a string: ")
print(s.upper())

# 12. Take two numbers and print the largest.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(max(a, b))

# 13. Take temperature in Celsius and convert to Fahrenheit.
c = float(input("Enter temperature in Celsius: "))
f = c * 9/5 + 32
print("Fahrenheit:", f)

# 14. Take a number and print its multiplication table.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 15. Take an integer and print whether it is positive or negative.
n = int(input("Enter an integer: "))
print("Positive" if n > 0 else "Negative" if n < 0 else "Zero")

# 16. Take the base and height of a triangle and print the area.
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("Area:", area)

# 17. Take a sentence and print the number of words.
sentence = input("Enter a sentence: ")
print(len(sentence.split()))

# 18. Take a number and print the sum of digits.
n = int(input("Enter a number: "))
sum_digits = sum(int(d) for d in str(abs(n)))
print("Sum of digits:", sum_digits)

# 19. Take two strings and print them combined.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(s1 + s2)

# 20. Take a number and print factorial.
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

# ✅ Advance Level (21–30)
# 21. Take N numbers from user and print the largest.
N = int(input("How many numbers? "))
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(N)]
print("Largest:", max(numbers))

# 22. Take N numbers and print the smallest.
N = int(input("How many numbers? "))
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(N)]
print("Smallest:", min(numbers))

# 23. Take a list of numbers and print the sum using sum().
numbers = [float(x) for x in input("Enter numbers separated by space: ").split()]
print("Sum:", sum(numbers))

# 24. Take 10 numbers and count how many are even.
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
even_count = sum(1 for n in numbers if n % 2 == 0)
print("Even count:", even_count)

# 25. Take a number and check if it is prime.
n = int(input("Enter a number: "))
if n < 2:
    print("Not prime")
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

# 26. Take two numbers and swap them (without third variable).
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swap:", a, b)

# 27. Take a name and check if it is a palindrome.
name = input("Enter a name: ")
print("Palindrome" if name == name[::-1] else "Not palindrome")

# 28. Take a number and reverse it.
n = int(input("Enter a number: "))
print(str(n)[::-1])

# 29. Take a string and count vowels.
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for c in s if c in vowels)
print("Vowel count:", vowel_count)

# 30. Take marks of 5 subjects and print grade.
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
avg = sum(marks) / 5
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)
