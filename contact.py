class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
    def display_contact(self):
        print(f"Name:{self.name}\nPhone:{self.phone}\nEmail:{self.email}")