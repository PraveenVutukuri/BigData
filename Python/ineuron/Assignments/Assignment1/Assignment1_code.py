
#Task 1 
#2
newLine=[]
for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        newLine.append(str(x))
print (','.join(newLine))

#3
fname="praveen"
lname ="kumar"
fullname = fname + ' ' + lname
print(fullname)
reversename = fullname[::-1]
print(reversename)

#4
Pi=3.14
diameter =12
radius = diameter/2
Volume=4/3*Pi*radius*radius*radius
print(Volume)


#Task 2
#1
inputnumber = input()
list = inputnumber.split(",")
print(list)

#2
n=int(input("input a number"))
for i in range(1,n+1):
 print('* '*i)
for m in range(1,n):
 print('* '*(n-m))

#3
inputword = input()
reverseword = inputword[::-1]
print(reverseword)

#4

input = """WE, THE PEOPLE OF INDIA, \n having solemnly resolved to constitute India into a SOVEREIGN, \n SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n and to secure to all its citizens"""
print(input)
