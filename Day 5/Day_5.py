#1) Write a program to create a list of n integer values and do the following
#• Add an item in to the list (using function)
#• Delete (using function)
#• Store the largest number from the list to a variable
#• Store the Smallest number from the list to a variable

L = [1,2,3,4,5,6,7]
print(L)

L.append(8)
print(L)

del L[4]
print(L)

hi = min(L)
lo = max(L)
print(lo)
print(hi)

#2) Create a tuple and print the reverse of the created tuple
my_tuple = (9, "red", 5.8)
print(my_tuple)
print(tuple(reversed(my_tuple)))

#3)Create a tuple and convert tuple into list
tuple1 = ('red','blue','green')
print(tuple1)
H = list(tuple1)
print(H)
