class MathDojo():
    def __init__(self):
        self.result = 0

    def add(self, *num):
        for x in range(len(num)):
            if isinstance(num[x], int):
                self.result += num[x]
            if isinstance(num[x], list) or isinstance(num[x], tuple):
                for i in num[x]:
                    self.result += i
        return self

    def subtract(self, *num):
        for x in range(len(num)):
            if isinstance(num[x], int):
                self.result -= num[x]
            if isinstance(num[x], list) or isinstance(num[x], tuple):
                for i in num[x]:
                    self.result -= i
        return self

print MathDojo().add([1], 3, 4).add([
    3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result