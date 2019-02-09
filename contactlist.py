contactList = []
class Contact:
    def __init__(self, _name, _phone, _email):
        self.name = _name
        self.phone = _phone
        self.email = _email
        contactList.append(self)
myContact = Contact('dylan', '3038271234', 'dylan@gmail.com')


        
