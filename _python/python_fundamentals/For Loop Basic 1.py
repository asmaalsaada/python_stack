# basic 
for x in range (150): 
	print (x)
# Multiples of Five 
for x in range (5, 1000, 5):
	print (x)
#Counting, The Dojo Way 
for x in range (1, 100): 
    if x%5==0:
    	print("Coding")
    elif  x%10==0:
    	print("Dojo") 
    else:
        print(x) 
#That Sucker is Huge 
for x in range (0, 500000): 
    if x%2!=0:
    	print(x)
#Countdown by Fours
for x in range (2018, 0,-4) :
    if x >0 : 
        print (x)
#Flexible Counter
lowNum =2
highNum =9
mult =3
for x in range (lowNum, highNum+1): 
    if x%mult==0:
        print (x) 