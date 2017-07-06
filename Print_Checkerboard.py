"""
Charachters project for coding dojo
"""
# pylint: disable=c0103
squares = [1, 2, 3, 4]
black = '* * * * '
red = ' * * * *'
for num1 in squares:
    if num1 % 2 != 0:
        print red
    elif num1 % 2 == 0:
        print black
for num2 in squares:
    if num2 % 2 == 0:
        print black
    elif num2 % 2 != 0:
        print red
