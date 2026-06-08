'''#count digits
n = int(input())
count = 0
while n>0:
    ld = n % 10
    count+=1
    n = n//10
print(count)'''

'''#counting CHAR in string
name = str(input())
count=0
for ch in name:
    count+=1
print(count)'''

#count vowels in string
'''name = str(input())
name_generalized = name.lower()
vowels = 0
consonants = 0
for ch in name_generalized:
    if ch in "aeiou":
        vowels+=1
    else:
        consonants+=1
print(vowels)
print(consonants)
'''
'''#reversing a string using loops
name = "Anirudh"
name_r = ""
for ch in range(len(name)-1 , -1 , -1 ):
    name_r+=name[ch]
print(name_r)
'''

'''#Checking Whether a Name is palindrome or not
name = "Anirudh"
r = ""
for ch in range(len(name)-1 , -1 , -1):
    r+=name[ch]
if name == r:
    print("Palindrome")
else:
    print("not palindrome")'''


