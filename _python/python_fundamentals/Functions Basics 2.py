# Countdown
def countdown(num):
    count=[] 
    for x in range (num, -1, -1):
        count.append(x)
    return count
countdown(5)
Print and Return 
Print and Return 

def printAndReturn(list):
    print (list[0])
    return list[1]
printAndReturn([5, 6])
# First Plus Length

def firstPlusLength(list):
    return list[0]+len(list)
firstPlusLength([1,2,3,4,5])
Values Greater than Second
def values_greater_than_second(list):
    newL=[]
    counter=0
    for x in range(len(list)):
        if len(list)<2:
            return False
        elif(list[x]>list[1]):
            newL.append(list[x])
            counter+=1
    print (counter)
    print (newL)
values_greater_than_second([5,2,3,2,1,4])
def length_and_value(size, value):
    newL=[]
    for x in range(size):
        newL.append(value)
    print(newL)
    
length_and_value(4,7)









