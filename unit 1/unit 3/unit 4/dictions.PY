# dictionary is a collection type that store values that describe
# unique data.
# IT IS AN OBJECT!
# Its similar to class object but with less rules.
# there are no methpds on dictipnaries.

srProm= {
"name": "senior prom",
"date": "May 8th 2026",
"gradeLevel":"12th"
}

srFieldTrip={
    "name":"senior Field Trip",
    "date": "May 22nd, 2026",
    "gradeLevel": "12th",
    "timeLeaving":"6 AM"
}

graduation={
    "name":"graduation day"
    "date": "May 22nd, 2026",
    "grade": "12th"
}

# class is function that CRETAES OBJECTS- these objects need to follow the class
# rules
# dicionaries are natural objects
class event():
    def __init__(self, name):
        self.name= name,

events = [graduation, srFieldTrip, srProm]
print(events)
        