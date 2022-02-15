from datetime import time

class Event:
    def __init__(self, startTime, endTime, venue):
        self.startTime = startTime
        self.endTime = endTime
        self.venue = venue

class Venue:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Address:
    def __init__(self, street, city, state, country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode

addr = Address('7th Avenue', 'NY City', 'NY', 'USA', '110000')
ven = Venue('Pen Plaza', addr)
evnt = Event(time(14, 30), time(15, 30), ven)

print('Event Start Time:', evnt.startTime, ', Event End Time:', evnt.endTime)
print('Venue:', evnt.venue.name)
print(f'Address: {evnt.venue.address.street}, {evnt.venue.address.city}, {evnt.venue.address.state}-{evnt.venue.address.zipcode}, {evnt.venue.address.country}')