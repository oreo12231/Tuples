# Create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

# Create a Tuple
tuple = (4,6,2,8,3,1)
print(tuple)

# Tuples are immutable, so you can not add new elements
# Using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)

# Counts the number of occurrences of item 50 from a tuple
tuple1 = (50,10,60,70,50)
print(tuple1.count(50))

# Create a Tuple
tuplex = (2,4,3,5,4,6,7,8,6,1)
# Used tuplex[start:stop] the start index is inclusive and the stop index

_slice = tuplex[3:5]

# Is exclusive
print(_slice)

# If the start index isn't defined, is taken from the begining of the tuple
_slice = tuplex[:6]
print(_slice)

# Function to check whether palindrome or not
def palid(r):
    e = len(r) -1
    s = 0
    while(s<e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r = (1,2,3,3,2,1)

if (palid(r)):
    print("The Tuple is Flip-Flop")
else:
    print("The Tuple is not Flip-Flop")
    
weather=(1,0,0,0,1,1,0)
sunny=0
rainy=0
for i in range(0,7):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1
        
if (sunny>rainy):
    print("Good Weather")
else:
    print("Bad Weather")
