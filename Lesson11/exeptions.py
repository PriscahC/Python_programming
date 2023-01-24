#exceptions
try:
    bills = [1,2,3]
    print(bills[3])

except IndexError:      #(for multiple errors use bracket and comas )
    print("number is out of range")
except:                 #default error
    ("unkown error")

#custom exceptions
class keyError(Exception):
    
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        
try:
    key = input("Enter your keys: ")
    
    if any(char.isalpha() for char in key):
        raise keyError
        
except keyError:
    print("keys can't contain a non number")