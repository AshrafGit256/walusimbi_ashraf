# Example four try to divide 5 / 0 (cause ZeroDivisionError)

try:
    result = 5 / 2
    
except ZeroDivisionError:
    print('cannot divide by zero')
    
else:
    print('Division successfull', result)
    
finally:
    print('Execution completed')
    
# Exercise