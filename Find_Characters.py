"""
Charachters project for coding dojo
"""
# pylint: disable=c0103
world_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'
newlist = []
for word in world_list:
    for each_letter in word:
        if each_letter == char:
            newlist.append(word)
print newlist
