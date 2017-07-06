class Call(object):
    def __init__(self, idnum, name, number, time, reason):
        self.idnum = idnum
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    
        def display(self):
            print 'call: ' + str(self.idnum) + ', ' + str(self.name) + ', ' + str(self.number) + ', ' + str(self.time) + ', ' + str(self.reason)
        return self

class CallCenter():
    def __init__(self, calls):
        self.queue = queue
        self.calls = calls

    def add(self, calls):
        self.calls.append(calls)
        return self

    def remove(self, calls):
        self.calls.remove(calls[0])

    def info(self):
        for x in queue:
            print self.calls[x].name
            print self.calls[x].number
            print self.queue

call1 = Call.idnum().name().number().time().reason()
call2 = Call.idnum().name().number().time().reason()

callcenter = CallCenter().add(call1).add(call2).info()
