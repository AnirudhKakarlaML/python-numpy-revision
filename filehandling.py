'''f = open("new.txt" , "x")
f.write("My Name Is Anirudh")
f.close()
'''

'''f = open("new.txt" , "r")
print(f.read())
f.close()'''

'''f = open("new.txt" , "r")#counting words
data = f.read()
data_1 = data.split()
count = 0
for ch in data_1:
    count+=1
print(count)
'''

'''f = open("new.txt" , "r")
data = f.read()
count = 0
for ch in range(1 , len(data)+1):
    count+=1
print(count)'''

'''f = open("new.txt" , "r")
data = f.read()
x = open("destination.txt" , "a")
x.write(data)
f.close()
x.close()
with open("destination.txt" , "r") as f:
    print(f.read())
'''

'''f = open("student.txt" , "a")
f.write("Anirudh")
f.write("Anirudh")
f.write("Anirudh")
f.write("Anirudh")
f.write("Anirudh")
f.close()
f = open("student.txt" , "r")
print(f.read())
'''
'''with open("students.txt", "r") as f:
    data = f.read()

words = data.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)'''

'''with open("sample.txt" , "r") as f:
    data = f.read()
    c = data.split()
    count = 0
    content = str(c)
    for ch in content:
        if ch.lower() in "aeiou":
            count+=1
    print(count)
'''
   
