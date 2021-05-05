# 1. 
print( "Hello World!" )
#2.
name = "Asma"
print( "Hello ", name )	# Hello Asma
print( "Hello "+ name )	# HelloAsma
#3.
name = 23
print( "Hello", name )	# Hello 23
print( "Hello"-- name )
print( "Hello" + name )	# with a + , -- TypeError: can only concatenate str (not "int") to str
# 4.
fave_food1 = "fettuccine" 
fave_food2 = "steak"
print("I love to eat {} and {} .".format(fave_food1, fave_food2))
print("I love to eat %s and %s ."  % (fave_food1, fave_food2))  
print (f"I love to eat {fave_food1} and {fave_food2}." )
