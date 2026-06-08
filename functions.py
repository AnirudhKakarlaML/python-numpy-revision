'''def greet():
    print("Welcome to Python")
greet()'''

'''def greet(name = "guest"):
    print(f"hell0 {name}")
greet("Anirudh")'''

'''def sum(a , b):
    return a+b
x = sum(1 , 2)
print(x)'''

'''def square(n):
    return n*n
x = square(11)
print(x)'''

'''def evenOrodd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
z = evenOrodd(8)
print(z)'''

'''def largest(a , b):
    if a>b:
        return a
    elif a==b:
        return "Equal"
    else:
        return b
x = largest(1 , 1)
print(x)'''

'''def factorial(n):
    fact = 1
    for i in range(1 , n+1):
        fact*=i
    return fact
x = factorial(5)
print(x)'''

'''def vowelsInstring(x):
    count = 0
    count_2 = 0
    for ch in x:
        if ch in "aeiou":
            count+=1
        else:
            count_2+=1
    return f"The No Of Vowels Is {count} and No.of Consonants is count {count_2}"
x = vowelsInstring("anirudh")#Edge case can be handled by making all lower by using lower function 
print(x)
'''

'''def isPalindrome(x):
    y = x.lower()
    rev = y[-1::-1]
    if(rev == y):
        return "Palindrome"
    else:
        return "Not Palindrome"
y = isPalindrome("MoM")
print(y)
'''

#Lambda Functions
'''square = lambda x:x*x
print(square(5))'''

'''cube = lambda x : x * x *x
print(cube(2))'''

'''add = lambda x , y : x+y
print(add(1 , 3))'''

'''larger = lambda x , y: x if x>y else y
print(larger(1 , 2))'''

'''even_odd = lambda x , y : x if x % 2 == 0 else y
print(even_odd(1 , 2))'''