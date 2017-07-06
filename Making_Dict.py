"""
Charachters project for coding dojo
"""
# pylint: disable=c0103
arr1 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"] #name
arr2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"] #favorite_animal

def make_dict(arr1, arr2):
    dictionary = {}
    for i in range(len(arr1)):
        key = arr1[i]
        value = arr2[i]
            #        print key, value
        dictionary[key] = value
    print dictionary
    return dictionary
make_dict(arr1, arr2)

def make_dict(arr1, arr2):
    dictionary = zip(arr1,arr2)
    print dictionary
    return dictionary
make_dict(arr1, arr2)
