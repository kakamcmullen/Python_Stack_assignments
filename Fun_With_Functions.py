"""
Charachters project for coding dojo
"""
# pylint: disable=c0103
#def odd_even(start, end, step):
    #for i in range(start, end, step):
        #if i % 2 != 0:
            #print "number is " + str(i + 1) + ".  This is an odd number."
        #else:
            #print "number is " + str(i + 1) + ".  This is an even number."

#odd_even(0, 0, 0) #enter start point, end point and step to run function


def Multiplying(li, multiplier): #input list and multiplier when calling function
    newli = []
    for i in range(len(li)):
        x = li[i] * multiplier
        newli.append(x)
    print newli
Multiplying([1, 2, 3, 4], [1, 2])





