class Patient:

    def __init__(self):
        pass

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_ssn(self, ssn):
        self.ssn = ssn

    def get_ssn(self):
        return self.ssn

p = Patient()
p.set_id(1234)
p.set_name("John Doe")
p.set_ssn("123-45-6789")
print(p.get_id(), p.get_name(), p.get_ssn())