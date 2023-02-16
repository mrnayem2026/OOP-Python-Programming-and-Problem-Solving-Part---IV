#! Option 1 is the best 
# takeNumber = float(input('Enter any float number : '))

''' integer_part  = int(takeNumber)
decimal_part = takeNumber - integer_part

print(f'{takeNumber} Floor is {integer_part} and Ceil if {decimal_part}.')
 '''

#! Option 2 is the best 
# number = 123.456
# Split the float number into integer and decimal parts
''' integer_part = int(number)
decimal_part = (number - integer_part) +  1 '''

# Or you can use divmod to get integer and decimal parts
# integer_part, decimal_part = divmod(number, 1)

# Convert decimal part to string and remove the leading '0.'
''' decimal_part_str = str(decimal_part)[2:] '''

# Print the results
''' print('Integer part:', integer_part)
print('Decimal part:', decimal_part_str) '''


#! Option 3 is the best 

takeNumber = float(input('Enter any float number : '))
int_part, frac_part= str(takeNumber).split('.')
print(f'{takeNumber} Floor is {int_part} and Ceil if {frac_part}')

