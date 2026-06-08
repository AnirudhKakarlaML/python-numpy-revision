#Lists
'''a = [1 , 2 , 4 , 5 , 5]
for x in a:
    print(x)'''

'''a = [1 , 2 , 3 , 4 , 5]
sum = 0
for x in a:
    sum+=a
print(sum)'''

'''a = [1,  2 , 3 , 4 , 5]
largest = 0
for x in a:
    if x>largest:
        largest = x
print(largest)'''

'''a = [1 , 2 , 3 , 4 , 5 , 6]
e_a = []
for x in a:
    if x%2==0:
        e_a.append(x)
print(e_a)'''


'''
a = [4 , 3 , 2 , 1]
rev = []
for x in range(len(a) - 1 , -1 , -1):
    rev.append(a[x])
print(rev)'''

'''a = [1 , 2 , 4 , 5 ,6, ]
a.append(2)
a.insert(2 , 100)
a.remove(2)
print(a)
'''
#Printing Each Element With Index:
'''a = [1 , 2 , 3 , 4 , 5]
for x in range( 0 , len(a)):
    print(f"{x} :{a[x]} ")
'''
'''a = [1 , 2 , 3 , 4 , 5 , -5 , -4 , -3 , -2 , -1]
count_p= 0
zeros = 0
count_n = 0
for x in a:
    if x>0:
        count_p+=1
    elif x==0:
        zeros+=1
    else:
        count_n+=1
print(count_p , count_n , zeros)
        '''
#Second Largest Element In The List
'''a = [1 , 2 , 3 , 4 , 5]
largest = float('-inf')
largest_2 = float('-inf')
for x in a:
    if x>largest:
        largest = x
for x in a:
    if x<largest and x>largest_2:
        largest_2 = x
print(largest_2 , largest)
'''

'''#Tuples
a = (1,2,1,1,1,1,1)
print(a.count(1))
print(a.index(2))'''

'''a = {
    "Name":"Anirudh",
    "CLG":"SRMIST",
    "CGPA":9.8
}
for keys , values in a.items():
    print(keys , values)
count_keys = 0
for keys in a.keys():
    count_keys+=1
print(count_keys)'''

'''marks = {
    "A": 80,
    "B": 95,
    "C": 70
}
Max_Marks = 0
for values in marks.values():
    if values>Max_Marks:
        Max_Marks = values
print(Max_Marks)
for keys in marks.keys():
    if marks[keys] == Max_Marks:
        print(keys)'''

'''a = [1, 1, 2, 2, 3, 3, 4]
b = set(a)
print(b)
'''

'''a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.intersection(b)
print(c)'''

'''a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))'''