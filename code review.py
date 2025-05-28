#MIlo Bastyr

#Initialize
#Functions

#Challenge 1

def double_num(num):
    return(num*2)


#Returns true if
#Challenge 2

def is_even(num):
    if num %2 == 0:
       return True
    else:
       return False

print(is_even(9))

#Challenge 3

def last_item(list):
    return list [len(list)-1] #Accessing items

last_item([1,2,3,4,5])
