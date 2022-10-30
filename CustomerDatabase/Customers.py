
class Customers:

    def __init__(self, first, last, email, phone):
        self.first = first
        self.last = last 
        self.email = email
        self.phone = phone 

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Customers('{}','{}',{})".format(self.first, self.last, self.email, self.phone)
