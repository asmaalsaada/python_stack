x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15 
print ("this is : x\n {} ".format(x))
#Change the last_name of the first student from 'Jordan' to 'Bryant'
students [0]['last_name'] ='Bryant'
print ("this is : students\n   {}  " .format(students))
#In the sports_directory, change 'Messi' to 'Andres'
sports_directory ['soccer'][0]= 'Andres'
print ("this is : sports_directory\n   {}  " .format(sports_directory))
#Change the value 20 in z to 30
z [0]['y'] = 30
print ("this is : z\n   {}  " .format(z))

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name': 'Tonel'}
    ]

def iterateDictionary(some_list):
    index=0
    for index in range(len(some_list)):
        for key  in some_list[index]:
            print(f"{key} - {some_list[index][key]}")
iterateDictionary(students) 

def iterateDictionary2(l):
    for item in range (len(l)):    
        print(l[item]['first_name'])
iterateDictionary2(students)

def iterateDictionary3(l):
    for item in range (len(l)):    
        print(l[item]['last_name'])
iterateDictionary3(students)

def printInfo(dictionary):
    for key, value in dictionary.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
        print("")

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)