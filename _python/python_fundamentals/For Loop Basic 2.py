def biggie_size(list):
    for x in range(len(list)):
        if list[x] > 0 :
            list[x] = "big"
    print(list) # for test
    return list

biggie_size([-1, 3, 5, -8,-9]) 

def count_positives(list):
    counter = 0 
    for x in range (len(list)):
        if list[x] > 0 :
            counter += 1
            list[-1] = counter
    print (list) # for test
    return list

count_positives([-1,1,1,1])

def sum_total(list) :
    sum = 0
    for x in range (len(list)) :
        sum += list[x] 
    print (sum) # for test
    return sum
sum_total([6,3,-2]) #output 7

def average(list) :
    sum = 0
    avg = None
    for x in range (len(list)) :
        sum += list[x] 
    avg = sum / len(list)
    print(avg) # for test
    return avg
average([6,3,-2])  #output 2.3333333333333335

def length(list) :
    print (len(list)) # for test
    return len(list)
length([37,2,1,-9]) # output 4

def minimum(list):
    min = 0
    for x in range (len(list)):
        if len(list) == 0: 
            return 
        if list[x]<min :
            min = list[x]
    print (min) # for test 
    return min
minimum([37,2,1,-9]) # output -9

def maximum(list):
    max = 0
    for x in range (len(list)):
        if len(list) == 0: 
            return 
        if list[x]>max :
            max = list[x]
    print (max)        # for test 
    return max
maximum([37,2,1,-9]) # output 37

def ultimate_analysis(list) :
    d = dict()
    d['sumTotal'] = sum_total(list)
    d['average'] = average(list)
    d['minimum'] = minimum(list)
    d['maximum'] = maximum(list)
    d['length'] =length(list)
    print (d) # for test
    return d
ultimate_analysis([37,2,1,-9]) 

def reverse_list(list):
    list.reverse() # a built in function for reversing a list 
    print (list)
    return list
reverse_list([37,2,1,-9]) 