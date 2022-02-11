# Program to depict else clause with try-except
  
# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) // (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
  
# Driver program to test above function
AbyB(8.0, 3.0)
AbyB(3.0, 3.0)

print("จิรภัทร แก่นคำ")
