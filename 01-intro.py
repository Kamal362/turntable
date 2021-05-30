#  recap rules of iteration
#  parallel coding
#  processing items within a list in the same time 
names = ["Sam","James","Jemima","STaphnie"]

for name in names:
    print(len(name))

print("individual execution")    
    
# use map function to process multiple items within the list a the same time

length = map(len,names)
print(*length)  

print ("parallel execution")

def sqr(x): return len(x)**2
lengthsqr = map (sqr, names)
print(*lengthsqr)

#  principle of list surprising
# each code does seperate thing

sqrlens = map(sqr, lengthsqr)
print(*sqrlens)

# scope of the function
# use lambda to restrict accessiblility
# function with no name
sqrlens = map((lambda x : x**2), lengthsqr)
print(*sqrlens)
print("print lambda function")

# filter return result base on condition
# comprhensive 
age = [20,15,12,18,19,22]

def can_vote(x): return x>=18
voters = filter(can_vote, age)
