"""
Charachters project for coding dojo
"""
# pylint: disable=c0103
import random

for x in range(10):
    score = random.randint(60, 100)
    if score <= 100 and score >= 90:
        grade = "A"
    elif score <= 89 and score >= 80:
        grade = "B"
    elif score <= 79 and score >= 70:
        grade = "C"
    elif score <= 69 and score >= 60:
        grade = "D"
    print "Score:", str(score) + ";  Your grade is", grade
