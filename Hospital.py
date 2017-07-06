import random
class Patient(object):
    def __init__(self, idnum, name, allergies):
        self.name = name
        self.idnum = str(random.randint(1000000, 9999999))
        self.allergies = allergies
        self.bednum = 'none'

        def display(self):
            print 'Patient: ' + str(self.name) + '-' + str(self.idnum) + ' Allergies: ' + str(self.allergies)
        return self

class Hospital(object):
    def __init__(self, name, beds = 5, patients = []):
        self.name = name
        self.beds = 5
        self.patients = []

    def add(self, patients):
        if self.beds >= len(self.patients):
            self.patients.append(patients)
            print 'patient admitted'
        else:
            print 'patient not admitted due to lack of available beds'
        return self

    def discharge(self, patients):
        self.patients.remove(patients[0])
        self.bednum = 'none'

    def view(self):
        for x in self.patients:
            print self.patients[x].name
            print self.patients[x].idnum
            print self.patients[x].bednum
            print self.patients

patient1 = Patient.name().idnum().allergies().bednum()
patient2 = Patient.name().idnum().allergies().bednum()
patient3 = Patient.name().idnum().allergies().bednum()
patient4 = Patient.name().idnum().allergies().bednum()
patient5 = Patient.name().idnum().allergies().bednum()
patient6 = Patient.name().idnum().allergies().bednum()

hospital = Hospital().add(patient1).add(patient2).add(patient3).add(patient4).add(patient5).view()
